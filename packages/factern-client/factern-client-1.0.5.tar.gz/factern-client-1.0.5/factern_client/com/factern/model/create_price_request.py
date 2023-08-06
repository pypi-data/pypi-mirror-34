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


class CreatePriceRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'policy': 'PermissionPolicyDocument',
        'target_node_id': 'str',
        'price_details': 'PriceDetails',
        'type': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'policy': 'policy',
        'target_node_id': 'targetNodeId',
        'price_details': 'priceDetails',
        'type': 'type'
    }

    def __init__(self, include_summary=None, policy=None, target_node_id=None, price_details=None, type=None):  # noqa: E501
        """CreatePriceRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._policy = None
        self._target_node_id = None
        self._price_details = None
        self._type = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.policy = policy
        self.target_node_id = target_node_id
        self.price_details = price_details
        self.type = type

    @property
    def include_summary(self):
        """Gets the include_summary of this CreatePriceRequest.  # noqa: E501


        :return: The include_summary of this CreatePriceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreatePriceRequest.


        :param include_summary: The include_summary of this CreatePriceRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

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
