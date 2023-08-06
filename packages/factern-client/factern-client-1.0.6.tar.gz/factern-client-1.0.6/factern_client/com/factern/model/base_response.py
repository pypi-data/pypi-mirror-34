# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class BaseResponse():


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
        'agent': 'Agent',
        'batch_id': 'str',
        'fact_type': 'str',
        'node_id': 'str',
        'parent_id': 'str',
        'summary': 'Summary',
        'timestamp': 'float'
    }

    attribute_map = {
        'agent': 'agent',
        'batch_id': 'batchId',
        'fact_type': 'factType',
        'node_id': 'nodeId',
        'parent_id': 'parentId',
        'summary': 'summary',
        'timestamp': 'timestamp'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BaseResponse - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("BaseResponse got unexpected argument '%s'" % k)

        self._agent = None
        self._batch_id = None
        self._fact_type = None
        self._node_id = None
        self._parent_id = None
        self._summary = None
        self._timestamp = None


        if "agent" in kwargs:
            self.agent = kwargs["agent"]
        if "batch_id" in kwargs:
            self.batch_id = kwargs["batch_id"]
        if "fact_type" in kwargs:
            self.fact_type = kwargs["fact_type"]
        if "node_id" in kwargs:
            self.node_id = kwargs["node_id"]
        if "parent_id" in kwargs:
            self.parent_id = kwargs["parent_id"]
        if "summary" in kwargs:
            self.summary = kwargs["summary"]
        if "timestamp" in kwargs:
            self.timestamp = kwargs["timestamp"]

    @property
    def agent(self):
        """Gets the agent of this BaseResponse.  # noqa: E501


        :return: The agent of this BaseResponse.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this BaseResponse.


        :param agent: The agent of this BaseResponse.  # noqa: E501
        :type: Agent
        """

        self._agent = agent

    @property
    def batch_id(self):
        """Gets the batch_id of this BaseResponse.  # noqa: E501


        :return: The batch_id of this BaseResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this BaseResponse.


        :param batch_id: The batch_id of this BaseResponse.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def fact_type(self):
        """Gets the fact_type of this BaseResponse.  # noqa: E501


        :return: The fact_type of this BaseResponse.  # noqa: E501
        :rtype: str
        """
        return self._fact_type

    @fact_type.setter
    def fact_type(self, fact_type):
        """Sets the fact_type of this BaseResponse.


        :param fact_type: The fact_type of this BaseResponse.  # noqa: E501
        :type: str
        """

        self._fact_type = fact_type

    @property
    def node_id(self):
        """Gets the node_id of this BaseResponse.  # noqa: E501


        :return: The node_id of this BaseResponse.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BaseResponse.


        :param node_id: The node_id of this BaseResponse.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BaseResponse.  # noqa: E501


        :return: The parent_id of this BaseResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BaseResponse.


        :param parent_id: The parent_id of this BaseResponse.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def summary(self):
        """Gets the summary of this BaseResponse.  # noqa: E501


        :return: The summary of this BaseResponse.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this BaseResponse.


        :param summary: The summary of this BaseResponse.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

    @property
    def timestamp(self):
        """Gets the timestamp of this BaseResponse.  # noqa: E501


        :return: The timestamp of this BaseResponse.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BaseResponse.


        :param timestamp: The timestamp of this BaseResponse.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

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
        if not isinstance(other, BaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
