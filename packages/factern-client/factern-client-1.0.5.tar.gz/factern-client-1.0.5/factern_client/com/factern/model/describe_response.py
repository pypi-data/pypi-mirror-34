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


class DescribeResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'node': 'StandardNode',
        'summary': 'Summary',
        'children': 'NodeListing',
        'member_ids': 'list[object]'
    }

    attribute_map = {
        'node': 'node',
        'summary': 'summary',
        'children': 'children',
        'member_ids': 'memberIds'
    }

    def __init__(self, node=None, summary=None, children=None, member_ids=None):  # noqa: E501
        """DescribeResponse - a model defined in Swagger"""  # noqa: E501

        self._node = None
        self._summary = None
        self._children = None
        self._member_ids = None
        self.discriminator = None

        self.node = node
        if summary is not None:
            self.summary = summary
        if children is not None:
            self.children = children
        if member_ids is not None:
            self.member_ids = member_ids

    @property
    def node(self):
        """Gets the node of this DescribeResponse.  # noqa: E501


        :return: The node of this DescribeResponse.  # noqa: E501
        :rtype: StandardNode
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this DescribeResponse.


        :param node: The node of this DescribeResponse.  # noqa: E501
        :type: StandardNode
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def summary(self):
        """Gets the summary of this DescribeResponse.  # noqa: E501


        :return: The summary of this DescribeResponse.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this DescribeResponse.


        :param summary: The summary of this DescribeResponse.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

    @property
    def children(self):
        """Gets the children of this DescribeResponse.  # noqa: E501


        :return: The children of this DescribeResponse.  # noqa: E501
        :rtype: NodeListing
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this DescribeResponse.


        :param children: The children of this DescribeResponse.  # noqa: E501
        :type: NodeListing
        """

        self._children = children

    @property
    def member_ids(self):
        """Gets the member_ids of this DescribeResponse.  # noqa: E501


        :return: The member_ids of this DescribeResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._member_ids

    @member_ids.setter
    def member_ids(self, member_ids):
        """Sets the member_ids of this DescribeResponse.


        :param member_ids: The member_ids of this DescribeResponse.  # noqa: E501
        :type: list[object]
        """

        self._member_ids = member_ids

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
        if not isinstance(other, DescribeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
