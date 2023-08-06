from typing import Any, Dict

from mindfoundry.optaas.client.configuration import Configuration
from mindfoundry.optaas.client.utils import _pprint


class Result:
    """The result obtained by taking a :class:`.Configuration` and running it through your scoring function.

    Must contain **either** a `score` value **or** an `error`.

    Args:
        configuration (Configuration): The Configuration used to obtain this Result.
        score (float): The score obtained.
        error (Any): Any data related to an error encountered while calculating the score.
        variance (float >=0, optional, defaults to 0): Variance associated with the score.
        user_defined_data (Any, optional): Any other data you wish to store as part of this Result.

    Raises:
        :class:`.ValueError` if invalid data is provided (e.g. both score and error are provided, or neither).
    """

    def __init__(self, configuration: Configuration, score: float = None, error: str = None,
                 variance: float = None, user_defined_data: Any = None) -> None:
        if (score is None) == (error is None):
            raise ValueError("Results must specify either a score or an error, not both.")

        if score is None and variance is not None:
            raise ValueError("Cannot specify variance without score.")

        self.configuration = configuration
        self.score = score
        self.error = error
        self.variance = variance
        self.user_defined_data = user_defined_data

    def to_json(self) -> Dict[str, Any]:
        json = self.to_json_without_configuration()
        json['configuration'] = self.configuration.id
        return json

    def to_json_without_configuration(self) -> Dict[str, Any]:
        json: Dict[str, Any] = {'score': self.score} if self.error is None else {'error': self.error}
        if self.variance is not None:
            json['variance'] = self.variance
        if self.user_defined_data is not None:
            json['userDefined'] = self.user_defined_data
        return json


class StoredResult:
    """A Result that has been stored in OPTaaS.

    Attributes:
        json (Dict): The full Result object as stored in OPTaaS in JSON format.
        id (int): Unique id for the Result.
        configuration (str): Unique id for the :class:`.Configuration` used to obtain the Result.
        score (float): Score obtained by using the :class:`.Configuration`.
        variance (float): Variance associated with the score.
        error (Any): Any data related to an error encountered when trying to use the :class:`.Configuration`.
        user_defined_data (Any): Any other data provided when storing the Result.
    """

    def __init__(self, json: Dict) -> None:
        self.json = json
        self.id = json['id']  # pylint: disable=invalid-name
        self.configuration = json['configuration']
        self.score = json.get('score')
        self.variance = json.get('variance')
        self.error = json.get('error')
        self.user_defined_data = json.get('userDefined')

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__dict__ == other.__dict__

    def __repr__(self):
        return _pprint(self, 'id', 'score', 'configuration', 'user_defined_data')
