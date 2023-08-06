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


class ResetLoginCredentialsRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        ResetLoginCredentialsRequest.swagger_types.update(get_parent().swagger_types)
        ResetLoginCredentialsRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'new_password': 'str',
        'node_id': 'str',
        'old_password': 'str'
    }

    attribute_map = {
        'new_password': 'newPassword',
        'node_id': 'nodeId',
        'old_password': 'oldPassword'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ResetLoginCredentialsRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("ResetLoginCredentialsRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._new_password = None
        self._node_id = None
        self._old_password = None


        if "new_password" not in kwargs:
            raise ValueError("ResetLoginCredentialsRequest missing required argument: new_password")
        self._new_password = kwargs["new_password"]

        if "node_id" not in kwargs:
            raise ValueError("ResetLoginCredentialsRequest missing required argument: node_id")
        self._node_id = kwargs["node_id"]

        if "old_password" not in kwargs:
            raise ValueError("ResetLoginCredentialsRequest missing required argument: old_password")
        self._old_password = kwargs["old_password"]


    @property
    def new_password(self):
        """Gets the new_password of this ResetLoginCredentialsRequest.  # noqa: E501


        :return: The new_password of this ResetLoginCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ResetLoginCredentialsRequest.


        :param new_password: The new_password of this ResetLoginCredentialsRequest.  # noqa: E501
        :type: str
        """
        if new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501

        self._new_password = new_password

    @property
    def node_id(self):
        """Gets the node_id of this ResetLoginCredentialsRequest.  # noqa: E501


        :return: The node_id of this ResetLoginCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ResetLoginCredentialsRequest.


        :param node_id: The node_id of this ResetLoginCredentialsRequest.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def old_password(self):
        """Gets the old_password of this ResetLoginCredentialsRequest.  # noqa: E501


        :return: The old_password of this ResetLoginCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this ResetLoginCredentialsRequest.


        :param old_password: The old_password of this ResetLoginCredentialsRequest.  # noqa: E501
        :type: str
        """
        if old_password is None:
            raise ValueError("Invalid value for `old_password`, must not be `None`")  # noqa: E501

        self._old_password = old_password

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
        if not isinstance(other, ResetLoginCredentialsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
