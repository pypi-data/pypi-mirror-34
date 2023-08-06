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


class SearchAliasRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'name': 'name'
    }

    def __init__(self, include_summary=None, name=None):  # noqa: E501
        """SearchAliasRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._name = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.name = name

    @property
    def include_summary(self):
        """Gets the include_summary of this SearchAliasRequest.  # noqa: E501


        :return: The include_summary of this SearchAliasRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this SearchAliasRequest.


        :param include_summary: The include_summary of this SearchAliasRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def name(self):
        """Gets the name of this SearchAliasRequest.  # noqa: E501


        :return: The name of this SearchAliasRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchAliasRequest.


        :param name: The name of this SearchAliasRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, SearchAliasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
