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


class CreateLoginResponse(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateLoginResponse.swagger_types.update(get_parent().swagger_types)
        CreateLoginResponse.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data_root_node': 'str',
        'status': 'str'
    }

    attribute_map = {
        'data_root_node': 'dataRootNode',
        'status': 'status'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateLoginResponse - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateLoginResponse got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._data_root_node = None
        self._status = None


        if "data_root_node" not in kwargs:
            raise ValueError("CreateLoginResponse missing required argument: data_root_node")
        self._data_root_node = kwargs["data_root_node"]

        if "status" not in kwargs:
            raise ValueError("CreateLoginResponse missing required argument: status")
        self._status = kwargs["status"]


    @property
    def data_root_node(self):
        """Gets the data_root_node of this CreateLoginResponse.  # noqa: E501


        :return: The data_root_node of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_root_node

    @data_root_node.setter
    def data_root_node(self, data_root_node):
        """Sets the data_root_node of this CreateLoginResponse.


        :param data_root_node: The data_root_node of this CreateLoginResponse.  # noqa: E501
        :type: str
        """
        if data_root_node is None:
            raise ValueError("Invalid value for `data_root_node`, must not be `None`")  # noqa: E501

        self._data_root_node = data_root_node

    @property
    def status(self):
        """Gets the status of this CreateLoginResponse.  # noqa: E501


        :return: The status of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateLoginResponse.


        :param status: The status of this CreateLoginResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PENDING_CONFIRMATION", "FAILED_TO_SEND_EMAIL"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, CreateLoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
