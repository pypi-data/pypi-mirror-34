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


class TokenPayment(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'publickey': 'str',
        'value': 'str',
        'signature': 'str'
    }

    attribute_map = {
        'publickey': 'publickey',
        'value': 'value',
        'signature': 'signature'
    }

    def __init__(self, publickey=None, value=None, signature=None):  # noqa: E501
        """TokenPayment - a model defined in Swagger"""  # noqa: E501

        self._publickey = None
        self._value = None
        self._signature = None
        self.discriminator = None

        self.publickey = publickey
        self.value = value
        self.signature = signature

    @property
    def publickey(self):
        """Gets the publickey of this TokenPayment.  # noqa: E501


        :return: The publickey of this TokenPayment.  # noqa: E501
        :rtype: str
        """
        return self._publickey

    @publickey.setter
    def publickey(self, publickey):
        """Sets the publickey of this TokenPayment.


        :param publickey: The publickey of this TokenPayment.  # noqa: E501
        :type: str
        """
        if publickey is None:
            raise ValueError("Invalid value for `publickey`, must not be `None`")  # noqa: E501

        self._publickey = publickey

    @property
    def value(self):
        """Gets the value of this TokenPayment.  # noqa: E501


        :return: The value of this TokenPayment.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TokenPayment.


        :param value: The value of this TokenPayment.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def signature(self):
        """Gets the signature of this TokenPayment.  # noqa: E501


        :return: The signature of this TokenPayment.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this TokenPayment.


        :param signature: The signature of this TokenPayment.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

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
        if not isinstance(other, TokenPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
