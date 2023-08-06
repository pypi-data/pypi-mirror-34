# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class GasCost():


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
        'consumed': 'float',
        'price': 'float'
    }

    attribute_map = {
        'consumed': 'consumed',
        'price': 'price'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GasCost - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("GasCost got unexpected argument '%s'" % k)

        self._consumed = None
        self._price = None


        if "consumed" not in kwargs:
            raise ValueError("GasCost missing required argument: consumed")
        self._consumed = kwargs["consumed"]

        if "price" not in kwargs:
            raise ValueError("GasCost missing required argument: price")
        self._price = kwargs["price"]


    @property
    def consumed(self):
        """Gets the consumed of this GasCost.  # noqa: E501


        :return: The consumed of this GasCost.  # noqa: E501
        :rtype: float
        """
        return self._consumed

    @consumed.setter
    def consumed(self, consumed):
        """Sets the consumed of this GasCost.


        :param consumed: The consumed of this GasCost.  # noqa: E501
        :type: float
        """
        if consumed is None:
            raise ValueError("Invalid value for `consumed`, must not be `None`")  # noqa: E501

        self._consumed = consumed

    @property
    def price(self):
        """Gets the price of this GasCost.  # noqa: E501


        :return: The price of this GasCost.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this GasCost.


        :param price: The price of this GasCost.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

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
        if not isinstance(other, GasCost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
