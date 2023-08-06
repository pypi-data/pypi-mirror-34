# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "CreateNamedRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "CreateNamedRequest").lower()
        parent = importlib.import_module(parent_fname).CreateNamedRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class CreateFilterRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateFilterRequest.swagger_types.update(get_parent().swagger_types)
        CreateFilterRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'statements': 'list[FilterStatement]'
    }

    attribute_map = {
        'statements': 'statements'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateFilterRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateFilterRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._statements = None


        if "statements" not in kwargs:
            raise ValueError("CreateFilterRequest missing required argument: statements")
        self._statements = kwargs["statements"]


    @property
    def statements(self):
        """Gets the statements of this CreateFilterRequest.  # noqa: E501


        :return: The statements of this CreateFilterRequest.  # noqa: E501
        :rtype: list[FilterStatement]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """Sets the statements of this CreateFilterRequest.


        :param statements: The statements of this CreateFilterRequest.  # noqa: E501
        :type: list[FilterStatement]
        """
        if statements is None:
            raise ValueError("Invalid value for `statements`, must not be `None`")  # noqa: E501

        self._statements = statements

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
        if not isinstance(other, CreateFilterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
