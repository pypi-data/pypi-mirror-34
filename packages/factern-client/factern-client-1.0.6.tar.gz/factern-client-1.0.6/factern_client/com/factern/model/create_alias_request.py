# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "BaseRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "BaseRequest").lower()
        parent = importlib.import_module(parent_fname).BaseRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class CreateAliasRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateAliasRequest.swagger_types.update(get_parent().swagger_types)
        CreateAliasRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'local': 'bool',
        'name': 'str',
        'target_node_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'local': 'local',
        'name': 'name',
        'target_node_id': 'targetNodeId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateAliasRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateAliasRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._description = None
        self._local = None
        self._name = None
        self._target_node_id = None


        if "description" in kwargs:
            self.description = kwargs["description"]
        if "local" in kwargs:
            self.local = kwargs["local"]
        if "name" not in kwargs:
            raise ValueError("CreateAliasRequest missing required argument: name")
        self._name = kwargs["name"]

        if "target_node_id" not in kwargs:
            raise ValueError("CreateAliasRequest missing required argument: target_node_id")
        self._target_node_id = kwargs["target_node_id"]


    @property
    def description(self):
        """Gets the description of this CreateAliasRequest.  # noqa: E501


        :return: The description of this CreateAliasRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAliasRequest.


        :param description: The description of this CreateAliasRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def local(self):
        """Gets the local of this CreateAliasRequest.  # noqa: E501


        :return: The local of this CreateAliasRequest.  # noqa: E501
        :rtype: bool
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this CreateAliasRequest.


        :param local: The local of this CreateAliasRequest.  # noqa: E501
        :type: bool
        """

        self._local = local

    @property
    def name(self):
        """Gets the name of this CreateAliasRequest.  # noqa: E501


        :return: The name of this CreateAliasRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAliasRequest.


        :param name: The name of this CreateAliasRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target_node_id(self):
        """Gets the target_node_id of this CreateAliasRequest.  # noqa: E501


        :return: The target_node_id of this CreateAliasRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_node_id

    @target_node_id.setter
    def target_node_id(self, target_node_id):
        """Sets the target_node_id of this CreateAliasRequest.


        :param target_node_id: The target_node_id of this CreateAliasRequest.  # noqa: E501
        :type: str
        """
        if target_node_id is None:
            raise ValueError("Invalid value for `target_node_id`, must not be `None`")  # noqa: E501

        self._target_node_id = target_node_id

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
        if not isinstance(other, CreateAliasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
