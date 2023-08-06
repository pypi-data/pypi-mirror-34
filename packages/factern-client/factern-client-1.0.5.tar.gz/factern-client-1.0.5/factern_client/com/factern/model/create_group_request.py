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


class CreateGroupRequest(object):

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
        'member_ids': 'list[str]',
        'member_fact_type': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'parent_id': 'parentId',
        'description': 'description',
        'name': 'name',
        'member_ids': 'memberIds',
        'member_fact_type': 'memberFactType'
    }

    def __init__(self, include_summary=None, parent_id=None, description=None, name=None, member_ids=None, member_fact_type=None):  # noqa: E501
        """CreateGroupRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._parent_id = None
        self._description = None
        self._name = None
        self._member_ids = None
        self._member_fact_type = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if parent_id is not None:
            self.parent_id = parent_id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        self.member_ids = member_ids
        if member_fact_type is not None:
            self.member_fact_type = member_fact_type

    @property
    def include_summary(self):
        """Gets the include_summary of this CreateGroupRequest.  # noqa: E501


        :return: The include_summary of this CreateGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreateGroupRequest.


        :param include_summary: The include_summary of this CreateGroupRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateGroupRequest.  # noqa: E501


        :return: The parent_id of this CreateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateGroupRequest.


        :param parent_id: The parent_id of this CreateGroupRequest.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this CreateGroupRequest.  # noqa: E501


        :return: The description of this CreateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateGroupRequest.


        :param description: The description of this CreateGroupRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateGroupRequest.  # noqa: E501


        :return: The name of this CreateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGroupRequest.


        :param name: The name of this CreateGroupRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def member_ids(self):
        """Gets the member_ids of this CreateGroupRequest.  # noqa: E501


        :return: The member_ids of this CreateGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_ids

    @member_ids.setter
    def member_ids(self, member_ids):
        """Sets the member_ids of this CreateGroupRequest.


        :param member_ids: The member_ids of this CreateGroupRequest.  # noqa: E501
        :type: list[str]
        """
        if member_ids is None:
            raise ValueError("Invalid value for `member_ids`, must not be `None`")  # noqa: E501

        self._member_ids = member_ids

    @property
    def member_fact_type(self):
        """Gets the member_fact_type of this CreateGroupRequest.  # noqa: E501


        :return: The member_fact_type of this CreateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._member_fact_type

    @member_fact_type.setter
    def member_fact_type(self, member_fact_type):
        """Sets the member_fact_type of this CreateGroupRequest.


        :param member_fact_type: The member_fact_type of this CreateGroupRequest.  # noqa: E501
        :type: str
        """

        self._member_fact_type = member_fact_type

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
        if not isinstance(other, CreateGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
