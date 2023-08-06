# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "BaseResponse"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "BaseResponse").lower()
        parent = importlib.import_module(parent_fname).BaseResponse
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class CreateLabelListResponse(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateLabelListResponse.swagger_types.update(get_parent().swagger_types)
        CreateLabelListResponse.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'members': 'list[LabelListMember]',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'members': 'members',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateLabelListResponse - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateLabelListResponse got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._description = None
        self._members = None
        self._name = None


        if "description" in kwargs:
            self.description = kwargs["description"]
        if "members" not in kwargs:
            raise ValueError("CreateLabelListResponse missing required argument: members")
        self._members = kwargs["members"]

        if "name" not in kwargs:
            raise ValueError("CreateLabelListResponse missing required argument: name")
        self._name = kwargs["name"]


    @property
    def description(self):
        """Gets the description of this CreateLabelListResponse.  # noqa: E501


        :return: The description of this CreateLabelListResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLabelListResponse.


        :param description: The description of this CreateLabelListResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def members(self):
        """Gets the members of this CreateLabelListResponse.  # noqa: E501


        :return: The members of this CreateLabelListResponse.  # noqa: E501
        :rtype: list[LabelListMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this CreateLabelListResponse.


        :param members: The members of this CreateLabelListResponse.  # noqa: E501
        :type: list[LabelListMember]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

    @property
    def name(self):
        """Gets the name of this CreateLabelListResponse.  # noqa: E501


        :return: The name of this CreateLabelListResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLabelListResponse.


        :param name: The name of this CreateLabelListResponse.  # noqa: E501
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
        if not isinstance(other, CreateLabelListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
