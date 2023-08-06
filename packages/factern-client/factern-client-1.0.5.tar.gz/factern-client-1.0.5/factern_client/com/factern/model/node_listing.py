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


class NodeListing(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'nodes': 'list[StandardNode]',
        'next_token': 'str',
        'total_results': 'float'
    }

    attribute_map = {
        'nodes': 'nodes',
        'next_token': 'nextToken',
        'total_results': 'totalResults'
    }

    def __init__(self, nodes=None, next_token=None, total_results=None):  # noqa: E501
        """NodeListing - a model defined in Swagger"""  # noqa: E501

        self._nodes = None
        self._next_token = None
        self._total_results = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if next_token is not None:
            self.next_token = next_token
        if total_results is not None:
            self.total_results = total_results

    @property
    def nodes(self):
        """Gets the nodes of this NodeListing.  # noqa: E501


        :return: The nodes of this NodeListing.  # noqa: E501
        :rtype: list[StandardNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this NodeListing.


        :param nodes: The nodes of this NodeListing.  # noqa: E501
        :type: list[StandardNode]
        """

        self._nodes = nodes

    @property
    def next_token(self):
        """Gets the next_token of this NodeListing.  # noqa: E501


        :return: The next_token of this NodeListing.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this NodeListing.


        :param next_token: The next_token of this NodeListing.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def total_results(self):
        """Gets the total_results of this NodeListing.  # noqa: E501


        :return: The total_results of this NodeListing.  # noqa: E501
        :rtype: float
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this NodeListing.


        :param total_results: The total_results of this NodeListing.  # noqa: E501
        :type: float
        """

        self._total_results = total_results

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
        if not isinstance(other, NodeListing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
