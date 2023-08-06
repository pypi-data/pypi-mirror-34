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


class CreateFieldRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateFieldRequest.swagger_types.update(get_parent().swagger_types)
        CreateFieldRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'branch': 'bool',
        'searchable': 'bool',
        'unique_by_parent': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'searchable': 'searchable',
        'unique_by_parent': 'uniqueByParent'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateFieldRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateFieldRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._branch = None
        self._searchable = None
        self._unique_by_parent = None


        if "branch" in kwargs:
            self.branch = kwargs["branch"]
        if "searchable" in kwargs:
            self.searchable = kwargs["searchable"]
        if "unique_by_parent" in kwargs:
            self.unique_by_parent = kwargs["unique_by_parent"]

    @property
    def branch(self):
        """Gets the branch of this CreateFieldRequest.  # noqa: E501


        :return: The branch of this CreateFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this CreateFieldRequest.


        :param branch: The branch of this CreateFieldRequest.  # noqa: E501
        :type: bool
        """

        self._branch = branch

    @property
    def searchable(self):
        """Gets the searchable of this CreateFieldRequest.  # noqa: E501


        :return: The searchable of this CreateFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this CreateFieldRequest.


        :param searchable: The searchable of this CreateFieldRequest.  # noqa: E501
        :type: bool
        """

        self._searchable = searchable

    @property
    def unique_by_parent(self):
        """Gets the unique_by_parent of this CreateFieldRequest.  # noqa: E501


        :return: The unique_by_parent of this CreateFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unique_by_parent

    @unique_by_parent.setter
    def unique_by_parent(self, unique_by_parent):
        """Sets the unique_by_parent of this CreateFieldRequest.


        :param unique_by_parent: The unique_by_parent of this CreateFieldRequest.  # noqa: E501
        :type: bool
        """

        self._unique_by_parent = unique_by_parent

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
        if not isinstance(other, CreateFieldRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
