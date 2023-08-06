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


class CreateBidRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateBidRequest.swagger_types.update(get_parent().swagger_types)
        CreateBidRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'price_id': 'str'
    }

    attribute_map = {
        'price_id': 'priceId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateBidRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateBidRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._price_id = None


        if "price_id" not in kwargs:
            raise ValueError("CreateBidRequest missing required argument: price_id")
        self._price_id = kwargs["price_id"]


    @property
    def price_id(self):
        """Gets the price_id of this CreateBidRequest.  # noqa: E501


        :return: The price_id of this CreateBidRequest.  # noqa: E501
        :rtype: str
        """
        return self._price_id

    @price_id.setter
    def price_id(self, price_id):
        """Sets the price_id of this CreateBidRequest.


        :param price_id: The price_id of this CreateBidRequest.  # noqa: E501
        :type: str
        """
        if price_id is None:
            raise ValueError("Invalid value for `price_id`, must not be `None`")  # noqa: E501

        self._price_id = price_id

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
        if not isinstance(other, CreateBidRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
