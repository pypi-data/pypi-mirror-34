#
# Template source downloaded from:
# https://github.com/swagger-api/swagger-codegen/tree/master/modules/swagger-codegen/src/main/resources/python
#
# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six


class SearchEntityRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'term': 'str',
        'max_results': 'float',
        'restrict_to': 'str',
        'operator': 'str',
        'query': 'object',
        'next_token': 'str',
        'field_id': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'term': 'term',
        'max_results': 'maxResults',
        'restrict_to': 'restrictTo',
        'operator': 'operator',
        'query': 'query',
        'next_token': 'nextToken',
        'field_id': 'fieldId'
    }

    def __init__(self, include_summary=None, term=None, max_results=None, restrict_to=None, operator=None, query=None, next_token=None, field_id=None):  # noqa: E501
        """SearchEntityRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._term = None
        self._max_results = None
        self._restrict_to = None
        self._operator = None
        self._query = None
        self._next_token = None
        self._field_id = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if term is not None:
            self.term = term
        if max_results is not None:
            self.max_results = max_results
        if restrict_to is not None:
            self.restrict_to = restrict_to
        if operator is not None:
            self.operator = operator
        if query is not None:
            self.query = query
        if next_token is not None:
            self.next_token = next_token
        if field_id is not None:
            self.field_id = field_id

    @property
    def include_summary(self):
        """Gets the include_summary of this SearchEntityRequest.  # noqa: E501


        :return: The include_summary of this SearchEntityRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this SearchEntityRequest.


        :param include_summary: The include_summary of this SearchEntityRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

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
