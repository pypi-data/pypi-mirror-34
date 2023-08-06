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


class ReplaceFieldRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'storage_interface_id': 'str',
        'data': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'storage_interface_id': 'storageInterfaceId',
        'data': 'data',
        'node_id': 'nodeId'
    }

    def __init__(self, include_summary=None, storage_interface_id=None, data=None, node_id=None):  # noqa: E501
        """ReplaceFieldRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._storage_interface_id = None
        self._data = None
        self._node_id = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if storage_interface_id is not None:
            self.storage_interface_id = storage_interface_id
        self.data = data
        self.node_id = node_id

    @property
    def include_summary(self):
        """Gets the include_summary of this ReplaceFieldRequest.  # noqa: E501


        :return: The include_summary of this ReplaceFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this ReplaceFieldRequest.


        :param include_summary: The include_summary of this ReplaceFieldRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def storage_interface_id(self):
        """Gets the storage_interface_id of this ReplaceFieldRequest.  # noqa: E501


        :return: The storage_interface_id of this ReplaceFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_interface_id

    @storage_interface_id.setter
    def storage_interface_id(self, storage_interface_id):
        """Sets the storage_interface_id of this ReplaceFieldRequest.


        :param storage_interface_id: The storage_interface_id of this ReplaceFieldRequest.  # noqa: E501
        :type: str
        """

        self._storage_interface_id = storage_interface_id

    @property
    def data(self):
        """Gets the data of this ReplaceFieldRequest.  # noqa: E501


        :return: The data of this ReplaceFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ReplaceFieldRequest.


        :param data: The data of this ReplaceFieldRequest.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def node_id(self):
        """Gets the node_id of this ReplaceFieldRequest.  # noqa: E501


        :return: The node_id of this ReplaceFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ReplaceFieldRequest.


        :param node_id: The node_id of this ReplaceFieldRequest.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

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
        if not isinstance(other, ReplaceFieldRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
