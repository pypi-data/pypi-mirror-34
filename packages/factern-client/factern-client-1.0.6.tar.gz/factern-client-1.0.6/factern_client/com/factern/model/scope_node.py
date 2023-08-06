# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class ScopeNode():


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
        'description': 'str',
        'member_ids': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'member_ids': 'memberIds',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ScopeNode - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("ScopeNode got unexpected argument '%s'" % k)

        self._description = None
        self._member_ids = None
        self._name = None


        if "description" in kwargs:
            self.description = kwargs["description"]
        if "member_ids" not in kwargs:
            raise ValueError("ScopeNode missing required argument: member_ids")
        self._member_ids = kwargs["member_ids"]

        if "name" not in kwargs:
            raise ValueError("ScopeNode missing required argument: name")
        self._name = kwargs["name"]


    @property
    def description(self):
        """Gets the description of this ScopeNode.  # noqa: E501


        :return: The description of this ScopeNode.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScopeNode.


        :param description: The description of this ScopeNode.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def member_ids(self):
        """Gets the member_ids of this ScopeNode.  # noqa: E501


        :return: The member_ids of this ScopeNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_ids

    @member_ids.setter
    def member_ids(self, member_ids):
        """Sets the member_ids of this ScopeNode.


        :param member_ids: The member_ids of this ScopeNode.  # noqa: E501
        :type: list[str]
        """
        if member_ids is None:
            raise ValueError("Invalid value for `member_ids`, must not be `None`")  # noqa: E501

        self._member_ids = member_ids

    @property
    def name(self):
        """Gets the name of this ScopeNode.  # noqa: E501


        :return: The name of this ScopeNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScopeNode.


        :param name: The name of this ScopeNode.  # noqa: E501
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
        if not isinstance(other, ScopeNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
