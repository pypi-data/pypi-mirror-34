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


class CreatePriceRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreatePriceRequest.swagger_types.update(get_parent().swagger_types)
        CreatePriceRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'policy': 'PermissionPolicyDocument',
        'price_details': 'PriceDetails',
        'target_node_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'policy': 'policy',
        'price_details': 'priceDetails',
        'target_node_id': 'targetNodeId',
        'type': 'type'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreatePriceRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreatePriceRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._policy = None
        self._price_details = None
        self._target_node_id = None
        self._type = None


        if "policy" not in kwargs:
            raise ValueError("CreatePriceRequest missing required argument: policy")
        self._policy = kwargs["policy"]

        if "price_details" not in kwargs:
            raise ValueError("CreatePriceRequest missing required argument: price_details")
        self._price_details = kwargs["price_details"]

        if "target_node_id" not in kwargs:
            raise ValueError("CreatePriceRequest missing required argument: target_node_id")
        self._target_node_id = kwargs["target_node_id"]

        if "type" not in kwargs:
            raise ValueError("CreatePriceRequest missing required argument: type")
        self._type = kwargs["type"]


    @property
    def policy(self):
        """Gets the policy of this CreatePriceRequest.  # noqa: E501


        :return: The policy of this CreatePriceRequest.  # noqa: E501
        :rtype: PermissionPolicyDocument
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this CreatePriceRequest.


        :param policy: The policy of this CreatePriceRequest.  # noqa: E501
        :type: PermissionPolicyDocument
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def price_details(self):
        """Gets the price_details of this CreatePriceRequest.  # noqa: E501


        :return: The price_details of this CreatePriceRequest.  # noqa: E501
        :rtype: PriceDetails
        """
        return self._price_details

    @price_details.setter
    def price_details(self, price_details):
        """Sets the price_details of this CreatePriceRequest.


        :param price_details: The price_details of this CreatePriceRequest.  # noqa: E501
        :type: PriceDetails
        """
        if price_details is None:
            raise ValueError("Invalid value for `price_details`, must not be `None`")  # noqa: E501

        self._price_details = price_details

    @property
    def target_node_id(self):
        """Gets the target_node_id of this CreatePriceRequest.  # noqa: E501


        :return: The target_node_id of this CreatePriceRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_node_id

    @target_node_id.setter
    def target_node_id(self, target_node_id):
        """Sets the target_node_id of this CreatePriceRequest.


        :param target_node_id: The target_node_id of this CreatePriceRequest.  # noqa: E501
        :type: str
        """
        if target_node_id is None:
            raise ValueError("Invalid value for `target_node_id`, must not be `None`")  # noqa: E501

        self._target_node_id = target_node_id

    @property
    def type(self):
        """Gets the type of this CreatePriceRequest.  # noqa: E501


        :return: The type of this CreatePriceRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePriceRequest.


        :param type: The type of this CreatePriceRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Fixed"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, CreatePriceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
