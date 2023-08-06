# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class TokenPayment():


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
        'publickey': 'str',
        'signature': 'str',
        'value': 'str'
    }

    attribute_map = {
        'publickey': 'publickey',
        'signature': 'signature',
        'value': 'value'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """TokenPayment - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("TokenPayment got unexpected argument '%s'" % k)

        self._publickey = None
        self._signature = None
        self._value = None


        if "publickey" not in kwargs:
            raise ValueError("TokenPayment missing required argument: publickey")
        self._publickey = kwargs["publickey"]

        if "signature" not in kwargs:
            raise ValueError("TokenPayment missing required argument: signature")
        self._signature = kwargs["signature"]

        if "value" not in kwargs:
            raise ValueError("TokenPayment missing required argument: value")
        self._value = kwargs["value"]


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
