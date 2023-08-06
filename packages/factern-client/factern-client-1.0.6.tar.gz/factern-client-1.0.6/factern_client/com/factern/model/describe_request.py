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


class DescribeRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        DescribeRequest.swagger_types.update(get_parent().swagger_types)
        DescribeRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'generate_template': 'bool',
        'list_children': 'ListCriteria',
        'node_id': 'str'
    }

    attribute_map = {
        'generate_template': 'generateTemplate',
        'list_children': 'listChildren',
        'node_id': 'nodeId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DescribeRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("DescribeRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._generate_template = None
        self._list_children = None
        self._node_id = None


        if "generate_template" in kwargs:
            self.generate_template = kwargs["generate_template"]
        if "list_children" in kwargs:
            self.list_children = kwargs["list_children"]
        if "node_id" not in kwargs:
            raise ValueError("DescribeRequest missing required argument: node_id")
        self._node_id = kwargs["node_id"]


    @property
    def generate_template(self):
        """Gets the generate_template of this DescribeRequest.  # noqa: E501


        :return: The generate_template of this DescribeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._generate_template

    @generate_template.setter
    def generate_template(self, generate_template):
        """Sets the generate_template of this DescribeRequest.


        :param generate_template: The generate_template of this DescribeRequest.  # noqa: E501
        :type: bool
        """

        self._generate_template = generate_template

    @property
    def list_children(self):
        """Gets the list_children of this DescribeRequest.  # noqa: E501


        :return: The list_children of this DescribeRequest.  # noqa: E501
        :rtype: ListCriteria
        """
        return self._list_children

    @list_children.setter
    def list_children(self, list_children):
        """Sets the list_children of this DescribeRequest.


        :param list_children: The list_children of this DescribeRequest.  # noqa: E501
        :type: ListCriteria
        """

        self._list_children = list_children

    @property
    def node_id(self):
        """Gets the node_id of this DescribeRequest.  # noqa: E501


        :return: The node_id of this DescribeRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DescribeRequest.


        :param node_id: The node_id of this DescribeRequest.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

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
        if not isinstance(other, DescribeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
