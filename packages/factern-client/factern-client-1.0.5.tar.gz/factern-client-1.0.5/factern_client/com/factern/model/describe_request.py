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


class DescribeRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'list_children': 'ListCriteria',
        'node_id': 'str',
        'generate_template': 'bool'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'list_children': 'listChildren',
        'node_id': 'nodeId',
        'generate_template': 'generateTemplate'
    }

    def __init__(self, include_summary=None, list_children=None, node_id=None, generate_template=None):  # noqa: E501
        """DescribeRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._list_children = None
        self._node_id = None
        self._generate_template = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if list_children is not None:
            self.list_children = list_children
        self.node_id = node_id
        if generate_template is not None:
            self.generate_template = generate_template

    @property
    def include_summary(self):
        """Gets the include_summary of this DescribeRequest.  # noqa: E501


        :return: The include_summary of this DescribeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this DescribeRequest.


        :param include_summary: The include_summary of this DescribeRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

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
