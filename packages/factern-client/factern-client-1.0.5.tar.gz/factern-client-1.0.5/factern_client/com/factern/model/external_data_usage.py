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


class ExternalDataUsage(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bytes_read': 'float',
        'bytes_written': 'float'
    }

    attribute_map = {
        'bytes_read': 'bytesRead',
        'bytes_written': 'bytesWritten'
    }

    def __init__(self, bytes_read=None, bytes_written=None):  # noqa: E501
        """ExternalDataUsage - a model defined in Swagger"""  # noqa: E501

        self._bytes_read = None
        self._bytes_written = None
        self.discriminator = None

        self.bytes_read = bytes_read
        self.bytes_written = bytes_written

    @property
    def bytes_read(self):
        """Gets the bytes_read of this ExternalDataUsage.  # noqa: E501


        :return: The bytes_read of this ExternalDataUsage.  # noqa: E501
        :rtype: float
        """
        return self._bytes_read

    @bytes_read.setter
    def bytes_read(self, bytes_read):
        """Sets the bytes_read of this ExternalDataUsage.


        :param bytes_read: The bytes_read of this ExternalDataUsage.  # noqa: E501
        :type: float
        """
        if bytes_read is None:
            raise ValueError("Invalid value for `bytes_read`, must not be `None`")  # noqa: E501

        self._bytes_read = bytes_read

    @property
    def bytes_written(self):
        """Gets the bytes_written of this ExternalDataUsage.  # noqa: E501


        :return: The bytes_written of this ExternalDataUsage.  # noqa: E501
        :rtype: float
        """
        return self._bytes_written

    @bytes_written.setter
    def bytes_written(self, bytes_written):
        """Sets the bytes_written of this ExternalDataUsage.


        :param bytes_written: The bytes_written of this ExternalDataUsage.  # noqa: E501
        :type: float
        """
        if bytes_written is None:
            raise ValueError("Invalid value for `bytes_written`, must not be `None`")  # noqa: E501

        self._bytes_written = bytes_written

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
        if not isinstance(other, ExternalDataUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
