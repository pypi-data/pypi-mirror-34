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


class CreateScopeRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateScopeRequest.swagger_types.update(get_parent().swagger_types)
        CreateScopeRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'filter_ids': 'list[str]',
        'template_ids': 'list[str]'
    }

    attribute_map = {
        'filter_ids': 'filterIds',
        'template_ids': 'templateIds'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateScopeRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateScopeRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._filter_ids = None
        self._template_ids = None


        if "filter_ids" not in kwargs:
            raise ValueError("CreateScopeRequest missing required argument: filter_ids")
        self._filter_ids = kwargs["filter_ids"]

        if "template_ids" not in kwargs:
            raise ValueError("CreateScopeRequest missing required argument: template_ids")
        self._template_ids = kwargs["template_ids"]


    @property
    def filter_ids(self):
        """Gets the filter_ids of this CreateScopeRequest.  # noqa: E501


        :return: The filter_ids of this CreateScopeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter_ids

    @filter_ids.setter
    def filter_ids(self, filter_ids):
        """Sets the filter_ids of this CreateScopeRequest.


        :param filter_ids: The filter_ids of this CreateScopeRequest.  # noqa: E501
        :type: list[str]
        """
        if filter_ids is None:
            raise ValueError("Invalid value for `filter_ids`, must not be `None`")  # noqa: E501

        self._filter_ids = filter_ids

    @property
    def template_ids(self):
        """Gets the template_ids of this CreateScopeRequest.  # noqa: E501


        :return: The template_ids of this CreateScopeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        """Sets the template_ids of this CreateScopeRequest.


        :param template_ids: The template_ids of this CreateScopeRequest.  # noqa: E501
        :type: list[str]
        """
        if template_ids is None:
            raise ValueError("Invalid value for `template_ids`, must not be `None`")  # noqa: E501

        self._template_ids = template_ids

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
        if not isinstance(other, CreateScopeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
