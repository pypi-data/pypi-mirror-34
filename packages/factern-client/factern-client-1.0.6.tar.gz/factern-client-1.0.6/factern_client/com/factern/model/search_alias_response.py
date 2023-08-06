# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class SearchAliasResponse():


    @staticmethod
    def compute_parent_updates():
        pass

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'exists': 'bool',
        'summary': 'Summary'
    }

    attribute_map = {
        'exists': 'exists',
        'summary': 'summary'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SearchAliasResponse - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("SearchAliasResponse got unexpected argument '%s'" % k)

        self._exists = None
        self._summary = None


        if "exists" not in kwargs:
            raise ValueError("SearchAliasResponse missing required argument: exists")
        self._exists = kwargs["exists"]

        if "summary" in kwargs:
            self.summary = kwargs["summary"]

    @property
    def exists(self):
        """Gets the exists of this SearchAliasResponse.  # noqa: E501


        :return: The exists of this SearchAliasResponse.  # noqa: E501
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        """Sets the exists of this SearchAliasResponse.


        :param exists: The exists of this SearchAliasResponse.  # noqa: E501
        :type: bool
        """
        if exists is None:
            raise ValueError("Invalid value for `exists`, must not be `None`")  # noqa: E501

        self._exists = exists

    @property
    def summary(self):
        """Gets the summary of this SearchAliasResponse.  # noqa: E501


        :return: The summary of this SearchAliasResponse.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this SearchAliasResponse.


        :param summary: The summary of this SearchAliasResponse.  # noqa: E501
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
        if not isinstance(other, SearchAliasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
