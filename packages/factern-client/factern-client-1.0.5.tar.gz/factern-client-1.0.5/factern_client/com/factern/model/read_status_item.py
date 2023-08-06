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


class ReadStatusItem(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'int',
        'read_item': 'ReadItem'
    }

    attribute_map = {
        'status': 'status',
        'read_item': 'readItem'
    }

    def __init__(self, status=None, read_item=None):  # noqa: E501
        """ReadStatusItem - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._read_item = None
        self.discriminator = None

        self.status = status
        self.read_item = read_item

    @property
    def status(self):
        """Gets the status of this ReadStatusItem.  # noqa: E501


        :return: The status of this ReadStatusItem.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReadStatusItem.


        :param status: The status of this ReadStatusItem.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def read_item(self):
        """Gets the read_item of this ReadStatusItem.  # noqa: E501


        :return: The read_item of this ReadStatusItem.  # noqa: E501
        :rtype: ReadItem
        """
        return self._read_item

    @read_item.setter
    def read_item(self, read_item):
        """Sets the read_item of this ReadStatusItem.


        :param read_item: The read_item of this ReadStatusItem.  # noqa: E501
        :type: ReadItem
        """
        if read_item is None:
            raise ValueError("Invalid value for `read_item`, must not be `None`")  # noqa: E501

        self._read_item = read_item

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
        if not isinstance(other, ReadStatusItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
