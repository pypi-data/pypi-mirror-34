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


class SettleAccountRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'token_payment': 'TokenPayment'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'token_payment': 'tokenPayment'
    }

    def __init__(self, include_summary=None, token_payment=None):  # noqa: E501
        """SettleAccountRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._token_payment = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.token_payment = token_payment

    @property
    def include_summary(self):
        """Gets the include_summary of this SettleAccountRequest.  # noqa: E501


        :return: The include_summary of this SettleAccountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this SettleAccountRequest.


        :param include_summary: The include_summary of this SettleAccountRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def token_payment(self):
        """Gets the token_payment of this SettleAccountRequest.  # noqa: E501


        :return: The token_payment of this SettleAccountRequest.  # noqa: E501
        :rtype: TokenPayment
        """
        return self._token_payment

    @token_payment.setter
    def token_payment(self, token_payment):
        """Sets the token_payment of this SettleAccountRequest.


        :param token_payment: The token_payment of this SettleAccountRequest.  # noqa: E501
        :type: TokenPayment
        """
        if token_payment is None:
            raise ValueError("Invalid value for `token_payment`, must not be `None`")  # noqa: E501

        self._token_payment = token_payment

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
        if not isinstance(other, SettleAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
