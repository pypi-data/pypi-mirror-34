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


class CreateFieldRequest(object):

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
        'unique_by_parent': 'bool',
        'searchable': 'bool',
        'branch': 'bool'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'parent_id': 'parentId',
        'description': 'description',
        'name': 'name',
        'unique_by_parent': 'uniqueByParent',
        'searchable': 'searchable',
        'branch': 'branch'
    }

    def __init__(self, include_summary=None, parent_id=None, description=None, name=None, unique_by_parent=None, searchable=None, branch=None):  # noqa: E501
        """CreateFieldRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._parent_id = None
        self._description = None
        self._name = None
        self._unique_by_parent = None
        self._searchable = None
        self._branch = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if parent_id is not None:
            self.parent_id = parent_id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        self.unique_by_parent = unique_by_parent
        self.searchable = searchable
        self.branch = branch

    @property
    def include_summary(self):
        """Gets the include_summary of this CreateFieldRequest.  # noqa: E501


        :return: The include_summary of this CreateFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreateFieldRequest.


        :param include_summary: The include_summary of this CreateFieldRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateFieldRequest.  # noqa: E501


        :return: The parent_id of this CreateFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateFieldRequest.


        :param parent_id: The parent_id of this CreateFieldRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this CreateFieldRequest.  # noqa: E501


        :return: The description of this CreateFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateFieldRequest.


        :param description: The description of this CreateFieldRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateFieldRequest.  # noqa: E501


        :return: The name of this CreateFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFieldRequest.


        :param name: The name of this CreateFieldRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unique_by_parent(self):
        """Gets the unique_by_parent of this CreateFieldRequest.  # noqa: E501


        :return: The unique_by_parent of this CreateFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unique_by_parent

    @unique_by_parent.setter
    def unique_by_parent(self, unique_by_parent):
        """Sets the unique_by_parent of this CreateFieldRequest.


        :param unique_by_parent: The unique_by_parent of this CreateFieldRequest.  # noqa: E501
        :type: bool
        """
        if unique_by_parent is None:
            raise ValueError("Invalid value for `unique_by_parent`, must not be `None`")  # noqa: E501

        self._unique_by_parent = unique_by_parent

    @property
    def searchable(self):
        """Gets the searchable of this CreateFieldRequest.  # noqa: E501


        :return: The searchable of this CreateFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this CreateFieldRequest.


        :param searchable: The searchable of this CreateFieldRequest.  # noqa: E501
        :type: bool
        """
        if searchable is None:
            raise ValueError("Invalid value for `searchable`, must not be `None`")  # noqa: E501

        self._searchable = searchable

    @property
    def branch(self):
        """Gets the branch of this CreateFieldRequest.  # noqa: E501


        :return: The branch of this CreateFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this CreateFieldRequest.


        :param branch: The branch of this CreateFieldRequest.  # noqa: E501
        :type: bool
        """
        if branch is None:
            raise ValueError("Invalid value for `branch`, must not be `None`")  # noqa: E501

        self._branch = branch

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
        if not isinstance(other, CreateFieldRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
