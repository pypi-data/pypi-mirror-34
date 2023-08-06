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


class CreateInterfaceRequest(object):

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
        'description': 'str',
        'name': 'str',
        'delete_data': 'ApiEndpoint',
        'get_data': 'ApiEndpoint',
        'add_data': 'ApiEndpoint'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'parent_id': 'parentId',
        'description': 'description',
        'name': 'name',
        'delete_data': 'deleteData',
        'get_data': 'getData',
        'add_data': 'addData'
    }

    def __init__(self, include_summary=None, parent_id=None, description=None, name=None, delete_data=None, get_data=None, add_data=None):  # noqa: E501
        """CreateInterfaceRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._parent_id = None
        self._description = None
        self._name = None
        self._delete_data = None
        self._get_data = None
        self._add_data = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if parent_id is not None:
            self.parent_id = parent_id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if delete_data is not None:
            self.delete_data = delete_data
        if get_data is not None:
            self.get_data = get_data
        if add_data is not None:
            self.add_data = add_data

    @property
    def include_summary(self):
        """Gets the include_summary of this CreateInterfaceRequest.  # noqa: E501


        :return: The include_summary of this CreateInterfaceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreateInterfaceRequest.


        :param include_summary: The include_summary of this CreateInterfaceRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateInterfaceRequest.  # noqa: E501


        :return: The parent_id of this CreateInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateInterfaceRequest.


        :param parent_id: The parent_id of this CreateInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this CreateInterfaceRequest.  # noqa: E501


        :return: The description of this CreateInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInterfaceRequest.


        :param description: The description of this CreateInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateInterfaceRequest.  # noqa: E501


        :return: The name of this CreateInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInterfaceRequest.


        :param name: The name of this CreateInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def delete_data(self):
        """Gets the delete_data of this CreateInterfaceRequest.  # noqa: E501


        :return: The delete_data of this CreateInterfaceRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._delete_data

    @delete_data.setter
    def delete_data(self, delete_data):
        """Sets the delete_data of this CreateInterfaceRequest.


        :param delete_data: The delete_data of this CreateInterfaceRequest.  # noqa: E501
        :type: ApiEndpoint
        """

        self._delete_data = delete_data

    @property
    def get_data(self):
        """Gets the get_data of this CreateInterfaceRequest.  # noqa: E501


        :return: The get_data of this CreateInterfaceRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._get_data

    @get_data.setter
    def get_data(self, get_data):
        """Sets the get_data of this CreateInterfaceRequest.


        :param get_data: The get_data of this CreateInterfaceRequest.  # noqa: E501
        :type: ApiEndpoint
        """

        self._get_data = get_data

    @property
    def add_data(self):
        """Gets the add_data of this CreateInterfaceRequest.  # noqa: E501


        :return: The add_data of this CreateInterfaceRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._add_data

    @add_data.setter
    def add_data(self, add_data):
        """Sets the add_data of this CreateInterfaceRequest.


        :param add_data: The add_data of this CreateInterfaceRequest.  # noqa: E501
        :type: ApiEndpoint
        """

        self._add_data = add_data

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
        if not isinstance(other, CreateInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
