# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "BaseRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "BaseRequest").lower()
        parent = importlib.import_module(parent_fname).BaseRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class SearchEntityRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        SearchEntityRequest.swagger_types.update(get_parent().swagger_types)
        SearchEntityRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field_id': 'str',
        'max_results': 'float',
        'next_token': 'str',
        'operator': 'str',
        'query': 'object',
        'restrict_to': 'str',
        'term': 'str'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'max_results': 'maxResults',
        'next_token': 'nextToken',
        'operator': 'operator',
        'query': 'query',
        'restrict_to': 'restrictTo',
        'term': 'term'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SearchEntityRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("SearchEntityRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._field_id = None
        self._max_results = None
        self._next_token = None
        self._operator = None
        self._query = None
        self._restrict_to = None
        self._term = None


        if "field_id" in kwargs:
            self.field_id = kwargs["field_id"]
        if "max_results" in kwargs:
            self.max_results = kwargs["max_results"]
        if "next_token" in kwargs:
            self.next_token = kwargs["next_token"]
        if "operator" in kwargs:
            self.operator = kwargs["operator"]
        if "query" in kwargs:
            self.query = kwargs["query"]
        if "restrict_to" in kwargs:
            self.restrict_to = kwargs["restrict_to"]
        if "term" in kwargs:
            self.term = kwargs["term"]

    @property
    def field_id(self):
        """Gets the field_id of this SearchEntityRequest.  # noqa: E501


        :return: The field_id of this SearchEntityRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this SearchEntityRequest.


        :param field_id: The field_id of this SearchEntityRequest.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def max_results(self):
        """Gets the max_results of this SearchEntityRequest.  # noqa: E501


        :return: The max_results of this SearchEntityRequest.  # noqa: E501
        :rtype: float
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this SearchEntityRequest.


        :param max_results: The max_results of this SearchEntityRequest.  # noqa: E501
        :type: float
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this SearchEntityRequest.  # noqa: E501


        :return: The next_token of this SearchEntityRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this SearchEntityRequest.


        :param next_token: The next_token of this SearchEntityRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def operator(self):
        """Gets the operator of this SearchEntityRequest.  # noqa: E501


        :return: The operator of this SearchEntityRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SearchEntityRequest.


        :param operator: The operator of this SearchEntityRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["equals", "startsWith", "contains", "elasticsearch"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def query(self):
        """Gets the query of this SearchEntityRequest.  # noqa: E501


        :return: The query of this SearchEntityRequest.  # noqa: E501
        :rtype: object
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchEntityRequest.


        :param query: The query of this SearchEntityRequest.  # noqa: E501
        :type: object
        """

        self._query = query

    @property
    def restrict_to(self):
        """Gets the restrict_to of this SearchEntityRequest.  # noqa: E501


        :return: The restrict_to of this SearchEntityRequest.  # noqa: E501
        :rtype: str
        """
        return self._restrict_to

    @restrict_to.setter
    def restrict_to(self, restrict_to):
        """Sets the restrict_to of this SearchEntityRequest.


        :param restrict_to: The restrict_to of this SearchEntityRequest.  # noqa: E501
        :type: str
        """

        self._restrict_to = restrict_to

    @property
    def term(self):
        """Gets the term of this SearchEntityRequest.  # noqa: E501


        :return: The term of this SearchEntityRequest.  # noqa: E501
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this SearchEntityRequest.


        :param term: The term of this SearchEntityRequest.  # noqa: E501
        :type: str
        """

        self._term = term

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchEntityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
