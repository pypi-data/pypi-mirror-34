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


class ResetLoginResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'deleted': 'bool',
        'timestamp': 'float',
        'node_id': 'str',
        'agent': 'Agent',
        'summary': 'Summary',
        'batch_id': 'str',
        'fact_type': 'str',
        'parent_id': 'str'
    }

    attribute_map = {
        'deleted': 'deleted',
        'timestamp': 'timestamp',
        'node_id': 'nodeId',
        'agent': 'agent',
        'summary': 'summary',
        'batch_id': 'batchId',
        'fact_type': 'factType',
        'parent_id': 'parentId'
    }

    def __init__(self, deleted=None, timestamp=None, node_id=None, agent=None, summary=None, batch_id=None, fact_type=None, parent_id=None):  # noqa: E501
        """ResetLoginResponse - a model defined in Swagger"""  # noqa: E501

        self._deleted = None
        self._timestamp = None
        self._node_id = None
        self._agent = None
        self._summary = None
        self._batch_id = None
        self._fact_type = None
        self._parent_id = None
        self.discriminator = None

        if deleted is not None:
            self.deleted = deleted
        if timestamp is not None:
            self.timestamp = timestamp
        if node_id is not None:
            self.node_id = node_id
        if agent is not None:
            self.agent = agent
        if summary is not None:
            self.summary = summary
        if batch_id is not None:
            self.batch_id = batch_id
        if fact_type is not None:
            self.fact_type = fact_type
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def deleted(self):
        """Gets the deleted of this ResetLoginResponse.  # noqa: E501


        :return: The deleted of this ResetLoginResponse.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ResetLoginResponse.


        :param deleted: The deleted of this ResetLoginResponse.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def timestamp(self):
        """Gets the timestamp of this ResetLoginResponse.  # noqa: E501


        :return: The timestamp of this ResetLoginResponse.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ResetLoginResponse.


        :param timestamp: The timestamp of this ResetLoginResponse.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

    @property
    def node_id(self):
        """Gets the node_id of this ResetLoginResponse.  # noqa: E501


        :return: The node_id of this ResetLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ResetLoginResponse.


        :param node_id: The node_id of this ResetLoginResponse.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def agent(self):
        """Gets the agent of this ResetLoginResponse.  # noqa: E501


        :return: The agent of this ResetLoginResponse.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this ResetLoginResponse.


        :param agent: The agent of this ResetLoginResponse.  # noqa: E501
        :type: Agent
        """

        self._agent = agent

    @property
    def summary(self):
        """Gets the summary of this ResetLoginResponse.  # noqa: E501


        :return: The summary of this ResetLoginResponse.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ResetLoginResponse.


        :param summary: The summary of this ResetLoginResponse.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

    @property
    def batch_id(self):
        """Gets the batch_id of this ResetLoginResponse.  # noqa: E501


        :return: The batch_id of this ResetLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this ResetLoginResponse.


        :param batch_id: The batch_id of this ResetLoginResponse.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def fact_type(self):
        """Gets the fact_type of this ResetLoginResponse.  # noqa: E501


        :return: The fact_type of this ResetLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._fact_type

    @fact_type.setter
    def fact_type(self, fact_type):
        """Sets the fact_type of this ResetLoginResponse.


        :param fact_type: The fact_type of this ResetLoginResponse.  # noqa: E501
        :type: str
        """

        self._fact_type = fact_type

    @property
    def parent_id(self):
        """Gets the parent_id of this ResetLoginResponse.  # noqa: E501


        :return: The parent_id of this ResetLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ResetLoginResponse.


        :param parent_id: The parent_id of this ResetLoginResponse.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

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
        if not isinstance(other, ResetLoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
