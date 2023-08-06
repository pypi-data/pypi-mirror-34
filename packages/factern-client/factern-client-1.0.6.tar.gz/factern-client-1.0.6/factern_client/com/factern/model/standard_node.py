# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class StandardNode():


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
        'deleted': 'bool',
        'fact_type': 'str',
        'node_id': 'str',
        'parent_id': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'agent': 'agent',
        'batch_id': 'batchId',
        'deleted': 'deleted',
        'fact_type': 'factType',
        'node_id': 'nodeId',
        'parent_id': 'parentId',
        'timestamp': 'timestamp'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """StandardNode - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("StandardNode got unexpected argument '%s'" % k)

        self._agent = None
        self._batch_id = None
        self._deleted = None
        self._fact_type = None
        self._node_id = None
        self._parent_id = None
        self._timestamp = None


        if "agent" not in kwargs:
            raise ValueError("StandardNode missing required argument: agent")
        self._agent = kwargs["agent"]

        if "batch_id" not in kwargs:
            raise ValueError("StandardNode missing required argument: batch_id")
        self._batch_id = kwargs["batch_id"]

        if "deleted" in kwargs:
            self.deleted = kwargs["deleted"]
        if "fact_type" not in kwargs:
            raise ValueError("StandardNode missing required argument: fact_type")
        self._fact_type = kwargs["fact_type"]

        if "node_id" not in kwargs:
            raise ValueError("StandardNode missing required argument: node_id")
        self._node_id = kwargs["node_id"]

        if "parent_id" not in kwargs:
            raise ValueError("StandardNode missing required argument: parent_id")
        self._parent_id = kwargs["parent_id"]

        if "timestamp" not in kwargs:
            raise ValueError("StandardNode missing required argument: timestamp")
        self._timestamp = kwargs["timestamp"]


    @property
    def agent(self):
        """Gets the agent of this StandardNode.  # noqa: E501


        :return: The agent of this StandardNode.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this StandardNode.


        :param agent: The agent of this StandardNode.  # noqa: E501
        :type: Agent
        """
        if agent is None:
            raise ValueError("Invalid value for `agent`, must not be `None`")  # noqa: E501

        self._agent = agent

    @property
    def batch_id(self):
        """Gets the batch_id of this StandardNode.  # noqa: E501


        :return: The batch_id of this StandardNode.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this StandardNode.


        :param batch_id: The batch_id of this StandardNode.  # noqa: E501
        :type: str
        """
        if batch_id is None:
            raise ValueError("Invalid value for `batch_id`, must not be `None`")  # noqa: E501

        self._batch_id = batch_id

    @property
    def deleted(self):
        """Gets the deleted of this StandardNode.  # noqa: E501


        :return: The deleted of this StandardNode.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this StandardNode.


        :param deleted: The deleted of this StandardNode.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def fact_type(self):
        """Gets the fact_type of this StandardNode.  # noqa: E501


        :return: The fact_type of this StandardNode.  # noqa: E501
        :rtype: str
        """
        return self._fact_type

    @fact_type.setter
    def fact_type(self, fact_type):
        """Sets the fact_type of this StandardNode.


        :param fact_type: The fact_type of this StandardNode.  # noqa: E501
        :type: str
        """
        if fact_type is None:
            raise ValueError("Invalid value for `fact_type`, must not be `None`")  # noqa: E501

        self._fact_type = fact_type

    @property
    def node_id(self):
        """Gets the node_id of this StandardNode.  # noqa: E501


        :return: The node_id of this StandardNode.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this StandardNode.


        :param node_id: The node_id of this StandardNode.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def parent_id(self):
        """Gets the parent_id of this StandardNode.  # noqa: E501


        :return: The parent_id of this StandardNode.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this StandardNode.


        :param parent_id: The parent_id of this StandardNode.  # noqa: E501
        :type: str
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def timestamp(self):
        """Gets the timestamp of this StandardNode.  # noqa: E501


        :return: The timestamp of this StandardNode.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this StandardNode.


        :param timestamp: The timestamp of this StandardNode.  # noqa: E501
        :type: float
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, StandardNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
