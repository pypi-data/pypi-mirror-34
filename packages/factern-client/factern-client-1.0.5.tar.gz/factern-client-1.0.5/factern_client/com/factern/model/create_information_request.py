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


class CreateInformationRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'parent_id': 'str',
        'field_id': 'str',
        'data': 'str',
        'storage_id': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'parent_id': 'parentId',
        'field_id': 'fieldId',
        'data': 'data',
        'storage_id': 'storageId'
    }

    def __init__(self, include_summary=None, parent_id=None, field_id=None, data=None, storage_id=None):  # noqa: E501
        """CreateInformationRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._parent_id = None
        self._field_id = None
        self._data = None
        self._storage_id = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if parent_id is not None:
            self.parent_id = parent_id
        self.field_id = field_id
        self.data = data
        if storage_id is not None:
            self.storage_id = storage_id

    @property
    def include_summary(self):
        """Gets the include_summary of this CreateInformationRequest.  # noqa: E501


        :return: The include_summary of this CreateInformationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreateInformationRequest.


        :param include_summary: The include_summary of this CreateInformationRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateInformationRequest.  # noqa: E501


        :return: The parent_id of this CreateInformationRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateInformationRequest.


        :param parent_id: The parent_id of this CreateInformationRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def field_id(self):
        """Gets the field_id of this CreateInformationRequest.  # noqa: E501


        :return: The field_id of this CreateInformationRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this CreateInformationRequest.


        :param field_id: The field_id of this CreateInformationRequest.  # noqa: E501
        :type: str
        """
        if field_id is None:
            raise ValueError("Invalid value for `field_id`, must not be `None`")  # noqa: E501

        self._field_id = field_id

    @property
    def data(self):
        """Gets the data of this CreateInformationRequest.  # noqa: E501


        :return: The data of this CreateInformationRequest.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateInformationRequest.


        :param data: The data of this CreateInformationRequest.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def storage_id(self):
        """Gets the storage_id of this CreateInformationRequest.  # noqa: E501


        :return: The storage_id of this CreateInformationRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this CreateInformationRequest.


        :param storage_id: The storage_id of this CreateInformationRequest.  # noqa: E501
        :type: str
        """

        self._storage_id = storage_id

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
        if not isinstance(other, CreateInformationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
