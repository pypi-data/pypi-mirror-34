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


class EntityListResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'nodes': 'list[Entity]',
        'next_token': 'str',
        'total_results': 'float',
        'summary': 'Summary'
    }

    attribute_map = {
        'nodes': 'nodes',
        'next_token': 'nextToken',
        'total_results': 'totalResults',
        'summary': 'summary'
    }

    def __init__(self, nodes=None, next_token=None, total_results=None, summary=None):  # noqa: E501
        """EntityListResponse - a model defined in Swagger"""  # noqa: E501

        self._nodes = None
        self._next_token = None
        self._total_results = None
        self._summary = None
        self.discriminator = None

        self.nodes = nodes
        if next_token is not None:
            self.next_token = next_token
        if total_results is not None:
            self.total_results = total_results
        if summary is not None:
            self.summary = summary

    @property
    def nodes(self):
        """Gets the nodes of this EntityListResponse.  # noqa: E501


        :return: The nodes of this EntityListResponse.  # noqa: E501
        :rtype: list[Entity]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this EntityListResponse.


        :param nodes: The nodes of this EntityListResponse.  # noqa: E501
        :type: list[Entity]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def next_token(self):
        """Gets the next_token of this EntityListResponse.  # noqa: E501


        :return: The next_token of this EntityListResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this EntityListResponse.


        :param next_token: The next_token of this EntityListResponse.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def total_results(self):
        """Gets the total_results of this EntityListResponse.  # noqa: E501


        :return: The total_results of this EntityListResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this EntityListResponse.


        :param total_results: The total_results of this EntityListResponse.  # noqa: E501
        :type: float
        """

        self._total_results = total_results

    @property
    def summary(self):
        """Gets the summary of this EntityListResponse.  # noqa: E501


        :return: The summary of this EntityListResponse.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this EntityListResponse.


        :param summary: The summary of this EntityListResponse.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

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
        if not isinstance(other, EntityListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
