from typing import Any, Tuple, List, Dict, Callable, Union

from mindfoundry.optaas.client.configuration import Configuration
from mindfoundry.optaas.client.result import StoredResult, Result
from mindfoundry.optaas.client.session import OPTaaSSession
from mindfoundry.optaas.client.utils import _pprint


class Task:
    """Allows you to access Task attributes and perform all Task-related functions.

    Attributes:
        json (Dict): The full JSON representation of this Task in OPTaaS.
        id (str): Unique id for the Task.
        title (str): Name/description as provided when the Task was created.
        parameters (List[Dict]): JSON representation of the :class:`Parameters <.Parameter>` defined for this Task.
        constraints (List[str]): List of OPTaaS string representations of the :class:`Constraints <.Constraint>` defined for this Task.
        status (str): Current status of the Task, e.g. 'running' or 'done'
        number_of_iterations (int): Number of :class:`Results <.Result>` provided for this Task so far.
        user_defined_data (Any): Any other data as provided when the Task was created.
    """

    def __init__(self, json: dict, session: OPTaaSSession) -> None:
        self.json = json
        self.id = json['id']  # pylint: disable=invalid-name
        self.parameters = json['parameters']
        self.constraints = json['constraints']
        self._update_attributes(json)

        self._session = session
        self._task_url = json['_links']['self']['href']
        self._configurations_url = json['_links']['configurations']['href']
        self._results_url = json['_links']['results']['href']
        self._complete_url = json['_links']['complete']['href']
        self._resume_url = json['_links']['resume']['href']

    def _update_attributes(self, json: dict):
        self.title = json['title']
        self.status = json['status']
        self.number_of_iterations = json['numberOfIterations']
        self.user_defined_data = json.get('userDefined')

    def run(self, scoring_function: Callable[..., Union[float, Tuple[float, float]]], max_iterations: int,
            score_threshold: float = None) -> Tuple[StoredResult, Configuration]:
        """Run this task, using the provided scoring function to calculate the score for each configuration.

        Args:
            scoring_function (Callable[..., Union[float, Tuple[float, float]]]):
                Function that takes configuration values as arguments, e.g. if you have parameters x and y, your
                function would be `def get_score(x, y)`.
                The function must return either a single float (the score), or a tuple of floats (score, variance).
            max_iterations (int):
                Max number of iterations to run, i.e. number of results to record before stopping.
            score_threshold (float, optional, defaults to target_score if defined):
                Stop running the task when the score is equal to or better than this value.

        Returns:
            A Tuple of the best recorded :class:`.Result` and the corresponding :class:`.Configuration`.

        Raises:
            :class:`.OPTaaSError` if the server is unavailable.
        """
        print(f'Running task "{self.title}" for {max_iterations} iterations')

        reached_threshold = self._reached_threshold_if_defined(score_threshold)

        print()
        configuration = self.generate_configurations(1)[0]

        for i in range(max_iterations):
            scoring_result = scoring_function(**configuration.values)

            if isinstance(scoring_result, tuple):
                score, variance = scoring_result
                print(f'Iteration: {i}    Score: {score}    Variance: {variance}')
            else:
                score = scoring_result
                variance = None  # type: ignore
                print(f'Iteration: {i}    Score: {score}')

            print(f'Configuration: {configuration.values}')
            print()

            configuration = self.record_result(configuration=configuration, score=score, variance=variance)
            if reached_threshold(score):
                break

        self.complete()
        print('Task Completed')
        print()

        self.refresh()
        return self.get_best_result_and_configuration()

    def _reached_threshold_if_defined(self, score_threshold: float = None) -> Callable[[float], bool]:
        if score_threshold is None:
            target_score = self.json.get('targetScore')

            if target_score is None:
                print('(no score threshold set)')
                return lambda score: False

            print(f'(or until target score {target_score} is reached)')
            return self._reached_threshold(target_score)

        print(f'(or until score is {score_threshold} or better)')
        return self._reached_threshold(score_threshold)

    def _reached_threshold(self, threshold: float) -> Callable[[float], bool]:
        from mindfoundry.optaas.client.client import Goal
        if Goal[self.json['goal']] == Goal.min:
            return lambda score: score <= threshold
        return lambda score: score >= threshold

    def refresh(self):
        """Make a GET request to OPTaaS to retrieve the latest Task data and update this object accordingly."""
        response = self._session.get(self._task_url)
        self._update_attributes(response.body)

    def delete(self):
        """Delete this Task (cannot be undone)."""
        self._session.delete(self._task_url)

    def generate_configurations(self, quantity: int = 1) -> List[Configuration]:
        """Make a POST request to OPTaaS to generate a set of new :class:`Configurations <.Configuration>` for this Task.

        Args:
            quantity (int, optional, default 1): The number of configurations to generate (minimum 1).

        Returns:
            A list of the newly created :class:`Configurations <.Configuration>`.

        Raises:
            :class:`.OPTaaSError` if the server is unavailable or the quantity is invalid.
        """
        response = self._session.post(self._configurations_url + f'?quantity={quantity}', {})
        return [Configuration(json) for json in response.body['configurations']]

    def add_user_defined_configuration(self, values: Dict, score: float = None, variance: float = None,
                                       user_defined_data: Any = None) -> Configuration:
        """Make a POST request to OPTaaS to store a new user-provided :class:`.Configuration` using the values provided.

        Also optionally store a :class:`.Result` for this Configuration using the provided `score`.

        This is useful for giving OPTaaS a "warm start" by providing some examples of good/bad Configurations.

        Args:
            values (Dict): Values assigned to each :class:`.Parameter`. See :attr:`.Configuration.values`.
            score (float, optional): Score obtained when using this Configuration.
            variance (float >=0, optional, defaults to 0): Variance associated with the score.
            user_defined_data (Any, optional, ignored if `score` is not provided): Any other data to store in the Result.

        Returns:
            The newly created :class:`.Configuration`

        Raises:
            :class:`.OPTaaSError` if the values are otherwise invalid or the server is unavailable.
        """
        body: Dict = {'values': values}
        if score is not None:
            result = Result(configuration=_MockConfiguration(), score=score, variance=variance,
                            user_defined_data=user_defined_data)
            body['results'] = [result.to_json_without_configuration()]

        response = self._session.post(self._configurations_url, body)
        return Configuration(response.body['configurations'][0])

    def record_result(self, configuration: Configuration, score: float = None, error: str = None,
                      variance: float = None, user_defined_data: Any = None) -> Configuration:
        """Make a POST request to OPTaaS to record a :class:`.Result` for the given :class:`.Configuration`.

        Must specify **either** `score` **or** `error`.

        After the Result is recorded, OPTaaS will automatically generate the next Configuration for you to try.

        Args:
            configuration (Configuration): The Configuration used to obtain this Result.
            score (float): The score obtained.
            error (Any): Any data related to an error encountered while calculating the score.
            variance (float >=0, optional, defaults to 0): Variance associated with the score.
            user_defined_data (Any, optional): Any other data you wish to store as part of this Result.

        Returns:
            The next :class:`.Configuration` generated by OPTaaS.

        Raises:
            :class:`.OPTaaSError` if the data provided is invalid or the server is unavailable.
            :class:`.ValueError` if both score and error are provided, or neither.
        """
        result = Result(configuration=configuration, score=score, error=error, variance=variance,
                        user_defined_data=user_defined_data)
        response = self._session.post(configuration.results_url, result.to_json_without_configuration())
        return Configuration(response.body['nextConfiguration'])

    def record_results(self, results: List[Result]) -> List[Configuration]:
        """Make a POST request to OPTaaS to store a batch of :class:`Results <.Result>` and get the next batch of :class:`Configurations <.Configuration>`.

        Args:
            results (List[Result]): List of Results to record. Must be non-empty.

        Returns:
            A list of the same length as `results`, containing the next :class:`Configurations <.Configuration>` for you to try.

        Raises:
            :class:`.OPTaaSError` if the data provided is invalid or the server is unavailable.
            :class:`.ValueError` if the result list is empty.
        """
        if not results:
            raise ValueError("Result list must be non-empty.")

        body = {'results': [result.to_json() for result in results]}
        response = self._session.post(self._results_url, body)
        return [Configuration(json) for json in response.body['nextConfigurations']]

    def get_configurations(self, limit: int = None) -> List[Configuration]:
        """Make a GET request to OPTaaS to retrieve a list of :class:`Configurations <.Configuration>` for this Task.

        Args:
            limit (int, optional, minimum 1): Upper bound on the number of Configurations that will be returned.

        Returns:
            The list of :class:`Configurations <.Configuration>`.

        Raises:
            :class:`.OPTaaSError` if the limit is invalid or the server is unavailable.
        """
        url = self._configurations_url
        if limit is not None:
            url += f'?limit={limit}'
        response = self._session.get(url)
        return [Configuration(json) for json in response.body['configurations']]

    def get_configuration(self, configuration_id: str) -> Configuration:
        """Make a GET request to OPTaaS to retrieve a specific :class:`.Configuration` by id.

        Args:
            configuration_id (str): Unique id for the Configuration.

        Returns:
            The retrieved :class:`.Configuration`.

        Raises:
            :class:`.OPTaaSError` if the configuration_id is invalid or the server is unavailable.
        """
        url = f'{self._configurations_url}/{configuration_id}'
        response = self._session.get(url)
        return Configuration(response.body)

    def get_results(self, limit: int = None, best_first: bool = False) -> List[StoredResult]:
        """Make a GET request to OPTaaS to retrieve a list of :class:`Results <.StoredResult>` for this Task.

        Args:
            limit (int, optional, minimum 1): Upper bound on the number of Results that will be returned.
            best_first (bool, optional, default False):
                If True, Results will appear in score order, with the best score first.
                If False, Results will appear in the order they were created.

        Returns:
            The list of :class:`Results <.StoredResult>`.

        Raises:
            :class:`.OPTaaSError` if the limit is invalid or the server is unavailable.
        """
        url = self._results_url
        if limit is not None and best_first:
            url += f'?limit={limit}&order=bestFirst'
        elif best_first:
            url += '?order=bestFirst'
        elif limit is not None:
            url += f'?limit={limit}'
        response = self._session.get(url)
        return [StoredResult(json) for json in response.body['results']]

    def get_result(self, result_id: int) -> StoredResult:
        """Make a GET request to OPTaaS to retrieve a specific :class:`.StoredResult` by id.

        Args:
            result_id (str): Unique id for the Result.

        Returns:
            The retrieved :class:`.StoredResult`.

        Raises:
            :class:`.OPTaaSError` if the result_id is invalid or the server is unavailable.
        """
        url = f'{self._results_url}/{result_id}'
        response = self._session.get(url)
        return StoredResult(response.body)

    def get_best_result_and_configuration(self) -> Tuple[StoredResult, Configuration]:
        """Make GET requests to OPTaaS to retrieve the Result with the best score and the Configuration used to obtain it.

        Returns:
            A Tuple of the best :class:`.StoredResult` and best :class:`.Configuration`.

        Raises:
            :class:`.OPTaaSError` if the server is unavailable.
            :class:`.ValueError` if no results have been posted for this task.
        """
        results = self.get_results(best_first=True, limit=1)
        if results:
            best_result = results[0]
            best_configuration = self.get_configuration(best_result.configuration)
            return best_result, best_configuration
        raise ValueError('No results available for this task yet')

    def complete(self):
        """Make a PUT request to OPTaaS to complete the task (no further configurations or results can be created)"""
        self._session.put(self._complete_url, {})

    def resume(self):
        """Make a PUT request to OPTaaS to resume a completed task"""
        self._session.put(self._resume_url, {})

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__dict__ == other.__dict__

    def __repr__(self):
        return _pprint(self, 'id', 'title', 'user_defined_data', 'parameters', 'constraints')


class _MockConfiguration(Configuration):
    """Used only internally, to post a result for a user-defined configuration."""

    def __init__(self):  # pylint: disable=super-init-not-called
        pass
