# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class DeletedItem():


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
        'children': 'list[DeletedStatusItem]',
        'deleted_node_id': 'str',
        'field_id': 'str',
        'node_id': 'str',
        'nodes': 'list[DeletedItem]'
    }

    attribute_map = {
        'children': 'children',
        'deleted_node_id': 'deletedNodeId',
        'field_id': 'fieldId',
        'node_id': 'nodeId',
        'nodes': 'nodes'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DeletedItem - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("DeletedItem got unexpected argument '%s'" % k)

        self._children = None
        self._deleted_node_id = None
        self._field_id = None
        self._node_id = None
        self._nodes = None


        if "children" in kwargs:
            self.children = kwargs["children"]
        if "deleted_node_id" in kwargs:
            self.deleted_node_id = kwargs["deleted_node_id"]
        if "field_id" not in kwargs:
            raise ValueError("DeletedItem missing required argument: field_id")
        self._field_id = kwargs["field_id"]

        if "node_id" in kwargs:
            self.node_id = kwargs["node_id"]
        if "nodes" in kwargs:
            self.nodes = kwargs["nodes"]

    @property
    def children(self):
        """Gets the children of this DeletedItem.  # noqa: E501


        :return: The children of this DeletedItem.  # noqa: E501
        :rtype: list[DeletedStatusItem]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this DeletedItem.


        :param children: The children of this DeletedItem.  # noqa: E501
        :type: list[DeletedStatusItem]
        """

        self._children = children

    @property
    def deleted_node_id(self):
        """Gets the deleted_node_id of this DeletedItem.  # noqa: E501


        :return: The deleted_node_id of this DeletedItem.  # noqa: E501
        :rtype: str
        """
        return self._deleted_node_id

    @deleted_node_id.setter
    def deleted_node_id(self, deleted_node_id):
        """Sets the deleted_node_id of this DeletedItem.


        :param deleted_node_id: The deleted_node_id of this DeletedItem.  # noqa: E501
        :type: str
        """

        self._deleted_node_id = deleted_node_id

    @property
    def field_id(self):
        """Gets the field_id of this DeletedItem.  # noqa: E501


        :return: The field_id of this DeletedItem.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this DeletedItem.


        :param field_id: The field_id of this DeletedItem.  # noqa: E501
        :type: str
        """
        if field_id is None:
            raise ValueError("Invalid value for `field_id`, must not be `None`")  # noqa: E501

        self._field_id = field_id

    @property
    def node_id(self):
        """Gets the node_id of this DeletedItem.  # noqa: E501


        :return: The node_id of this DeletedItem.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DeletedItem.


        :param node_id: The node_id of this DeletedItem.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def nodes(self):
        """Gets the nodes of this DeletedItem.  # noqa: E501


        :return: The nodes of this DeletedItem.  # noqa: E501
        :rtype: list[DeletedItem]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this DeletedItem.


        :param nodes: The nodes of this DeletedItem.  # noqa: E501
        :type: list[DeletedItem]
        """

        self._nodes = nodes

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
        if not isinstance(other, DeletedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
