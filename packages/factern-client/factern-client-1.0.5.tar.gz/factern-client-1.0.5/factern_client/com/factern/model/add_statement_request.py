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


class AddStatementRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'target_node_id': 'str',
        'action_qualifier_id': 'str',
        'action_id': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'target_node_id': 'targetNodeId',
        'action_qualifier_id': 'actionQualifierId',
        'action_id': 'actionId'
    }

    def __init__(self, include_summary=None, target_node_id=None, action_qualifier_id=None, action_id=None):  # noqa: E501
        """AddStatementRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._target_node_id = None
        self._action_qualifier_id = None
        self._action_id = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.target_node_id = target_node_id
        if action_qualifier_id is not None:
            self.action_qualifier_id = action_qualifier_id
        self.action_id = action_id

    @property
    def include_summary(self):
        """Gets the include_summary of this AddStatementRequest.  # noqa: E501


        :return: The include_summary of this AddStatementRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this AddStatementRequest.


        :param include_summary: The include_summary of this AddStatementRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def target_node_id(self):
        """Gets the target_node_id of this AddStatementRequest.  # noqa: E501


        :return: The target_node_id of this AddStatementRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_node_id

    @target_node_id.setter
    def target_node_id(self, target_node_id):
        """Sets the target_node_id of this AddStatementRequest.


        :param target_node_id: The target_node_id of this AddStatementRequest.  # noqa: E501
        :type: str
        """
        if target_node_id is None:
            raise ValueError("Invalid value for `target_node_id`, must not be `None`")  # noqa: E501

        self._target_node_id = target_node_id

    @property
    def action_qualifier_id(self):
        """Gets the action_qualifier_id of this AddStatementRequest.  # noqa: E501


        :return: The action_qualifier_id of this AddStatementRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_qualifier_id

    @action_qualifier_id.setter
    def action_qualifier_id(self, action_qualifier_id):
        """Sets the action_qualifier_id of this AddStatementRequest.


        :param action_qualifier_id: The action_qualifier_id of this AddStatementRequest.  # noqa: E501
        :type: str
        """

        self._action_qualifier_id = action_qualifier_id

    @property
    def action_id(self):
        """Gets the action_id of this AddStatementRequest.  # noqa: E501


        :return: The action_id of this AddStatementRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this AddStatementRequest.


        :param action_id: The action_id of this AddStatementRequest.  # noqa: E501
        :type: str
        """
        if action_id is None:
            raise ValueError("Invalid value for `action_id`, must not be `None`")  # noqa: E501

        self._action_id = action_id

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
        if not isinstance(other, AddStatementRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
