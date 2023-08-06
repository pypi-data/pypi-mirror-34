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


class Searches(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'searches': 'float',
        'reindexing_calls': 'float',
        'hits': 'float',
        'reindexed_nodes': 'float'
    }

    attribute_map = {
        'searches': 'searches',
        'reindexing_calls': 'reindexingCalls',
        'hits': 'hits',
        'reindexed_nodes': 'reindexedNodes'
    }

    def __init__(self, searches=None, reindexing_calls=None, hits=None, reindexed_nodes=None):  # noqa: E501
        """Searches - a model defined in Swagger"""  # noqa: E501

        self._searches = None
        self._reindexing_calls = None
        self._hits = None
        self._reindexed_nodes = None
        self.discriminator = None

        self.searches = searches
        self.reindexing_calls = reindexing_calls
        self.hits = hits
        self.reindexed_nodes = reindexed_nodes

    @property
    def searches(self):
        """Gets the searches of this Searches.  # noqa: E501


        :return: The searches of this Searches.  # noqa: E501
        :rtype: float
        """
        return self._searches

    @searches.setter
    def searches(self, searches):
        """Sets the searches of this Searches.


        :param searches: The searches of this Searches.  # noqa: E501
        :type: float
        """
        if searches is None:
            raise ValueError("Invalid value for `searches`, must not be `None`")  # noqa: E501

        self._searches = searches

    @property
    def reindexing_calls(self):
        """Gets the reindexing_calls of this Searches.  # noqa: E501


        :return: The reindexing_calls of this Searches.  # noqa: E501
        :rtype: float
        """
        return self._reindexing_calls

    @reindexing_calls.setter
    def reindexing_calls(self, reindexing_calls):
        """Sets the reindexing_calls of this Searches.


        :param reindexing_calls: The reindexing_calls of this Searches.  # noqa: E501
        :type: float
        """
        if reindexing_calls is None:
            raise ValueError("Invalid value for `reindexing_calls`, must not be `None`")  # noqa: E501

        self._reindexing_calls = reindexing_calls

    @property
    def hits(self):
        """Gets the hits of this Searches.  # noqa: E501


        :return: The hits of this Searches.  # noqa: E501
        :rtype: float
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this Searches.


        :param hits: The hits of this Searches.  # noqa: E501
        :type: float
        """
        if hits is None:
            raise ValueError("Invalid value for `hits`, must not be `None`")  # noqa: E501

        self._hits = hits

    @property
    def reindexed_nodes(self):
        """Gets the reindexed_nodes of this Searches.  # noqa: E501


        :return: The reindexed_nodes of this Searches.  # noqa: E501
        :rtype: float
        """
        return self._reindexed_nodes

    @reindexed_nodes.setter
    def reindexed_nodes(self, reindexed_nodes):
        """Sets the reindexed_nodes of this Searches.


        :param reindexed_nodes: The reindexed_nodes of this Searches.  # noqa: E501
        :type: float
        """
        if reindexed_nodes is None:
            raise ValueError("Invalid value for `reindexed_nodes`, must not be `None`")  # noqa: E501

        self._reindexed_nodes = reindexed_nodes

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
        if not isinstance(other, Searches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
