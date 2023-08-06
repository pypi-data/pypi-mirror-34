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


class FactCount(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'read': 'float',
        'written': 'float'
    }

    attribute_map = {
        'read': 'read',
        'written': 'written'
    }

    def __init__(self, read=None, written=None):  # noqa: E501
        """FactCount - a model defined in Swagger"""  # noqa: E501

        self._read = None
        self._written = None
        self.discriminator = None

        self.read = read
        self.written = written

    @property
    def read(self):
        """Gets the read of this FactCount.  # noqa: E501


        :return: The read of this FactCount.  # noqa: E501
        :rtype: float
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this FactCount.


        :param read: The read of this FactCount.  # noqa: E501
        :type: float
        """
        if read is None:
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

    @property
    def written(self):
        """Gets the written of this FactCount.  # noqa: E501


        :return: The written of this FactCount.  # noqa: E501
        :rtype: float
        """
        return self._written

    @written.setter
    def written(self, written):
        """Sets the written of this FactCount.


        :param written: The written of this FactCount.  # noqa: E501
        :type: float
        """
        if written is None:
            raise ValueError("Invalid value for `written`, must not be `None`")  # noqa: E501

        self._written = written

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
        if not isinstance(other, FactCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
