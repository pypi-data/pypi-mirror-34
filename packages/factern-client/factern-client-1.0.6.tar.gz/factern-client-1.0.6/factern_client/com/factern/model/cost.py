# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class Cost():


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
        'gas': 'GasCost',
        'total': 'float'
    }

    attribute_map = {
        'gas': 'gas',
        'total': 'total'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Cost - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("Cost got unexpected argument '%s'" % k)

        self._gas = None
        self._total = None


        if "gas" in kwargs:
            self.gas = kwargs["gas"]
        if "total" not in kwargs:
            raise ValueError("Cost missing required argument: total")
        self._total = kwargs["total"]


    @property
    def gas(self):
        """Gets the gas of this Cost.  # noqa: E501


        :return: The gas of this Cost.  # noqa: E501
        :rtype: GasCost
        """
        return self._gas

    @gas.setter
    def gas(self, gas):
        """Sets the gas of this Cost.


        :param gas: The gas of this Cost.  # noqa: E501
        :type: GasCost
        """

        self._gas = gas

    @property
    def total(self):
        """Gets the total of this Cost.  # noqa: E501


        :return: The total of this Cost.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Cost.


        :param total: The total of this Cost.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, Cost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
