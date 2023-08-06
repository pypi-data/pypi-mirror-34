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


class CreateLoginResponse(object):

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
        'parent_id': 'str',
        'data_root_node': 'str',
        'status': 'str'
    }

    attribute_map = {
        'deleted': 'deleted',
        'timestamp': 'timestamp',
        'node_id': 'nodeId',
        'agent': 'agent',
        'summary': 'summary',
        'batch_id': 'batchId',
        'fact_type': 'factType',
        'parent_id': 'parentId',
        'data_root_node': 'dataRootNode',
        'status': 'status'
    }

    def __init__(self, deleted=None, timestamp=None, node_id=None, agent=None, summary=None, batch_id=None, fact_type=None, parent_id=None, data_root_node=None, status=None):  # noqa: E501
        """CreateLoginResponse - a model defined in Swagger"""  # noqa: E501

        self._deleted = None
        self._timestamp = None
        self._node_id = None
        self._agent = None
        self._summary = None
        self._batch_id = None
        self._fact_type = None
        self._parent_id = None
        self._data_root_node = None
        self._status = None
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
        self.data_root_node = data_root_node
        self.status = status

    @property
    def deleted(self):
        """Gets the deleted of this CreateLoginResponse.  # noqa: E501


        :return: The deleted of this CreateLoginResponse.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CreateLoginResponse.


        :param deleted: The deleted of this CreateLoginResponse.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateLoginResponse.  # noqa: E501


        :return: The timestamp of this CreateLoginResponse.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateLoginResponse.


        :param timestamp: The timestamp of this CreateLoginResponse.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

    @property
    def node_id(self):
        """Gets the node_id of this CreateLoginResponse.  # noqa: E501


        :return: The node_id of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this CreateLoginResponse.


        :param node_id: The node_id of this CreateLoginResponse.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def agent(self):
        """Gets the agent of this CreateLoginResponse.  # noqa: E501


        :return: The agent of this CreateLoginResponse.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this CreateLoginResponse.


        :param agent: The agent of this CreateLoginResponse.  # noqa: E501
        :type: Agent
        """

        self._agent = agent

    @property
    def summary(self):
        """Gets the summary of this CreateLoginResponse.  # noqa: E501


        :return: The summary of this CreateLoginResponse.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this CreateLoginResponse.


        :param summary: The summary of this CreateLoginResponse.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

    @property
    def batch_id(self):
        """Gets the batch_id of this CreateLoginResponse.  # noqa: E501


        :return: The batch_id of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this CreateLoginResponse.


        :param batch_id: The batch_id of this CreateLoginResponse.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def fact_type(self):
        """Gets the fact_type of this CreateLoginResponse.  # noqa: E501


        :return: The fact_type of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._fact_type

    @fact_type.setter
    def fact_type(self, fact_type):
        """Sets the fact_type of this CreateLoginResponse.


        :param fact_type: The fact_type of this CreateLoginResponse.  # noqa: E501
        :type: str
        """

        self._fact_type = fact_type

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateLoginResponse.  # noqa: E501


        :return: The parent_id of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateLoginResponse.


        :param parent_id: The parent_id of this CreateLoginResponse.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def data_root_node(self):
        """Gets the data_root_node of this CreateLoginResponse.  # noqa: E501


        :return: The data_root_node of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_root_node

    @data_root_node.setter
    def data_root_node(self, data_root_node):
        """Sets the data_root_node of this CreateLoginResponse.


        :param data_root_node: The data_root_node of this CreateLoginResponse.  # noqa: E501
        :type: str
        """
        if data_root_node is None:
            raise ValueError("Invalid value for `data_root_node`, must not be `None`")  # noqa: E501

        self._data_root_node = data_root_node

    @property
    def status(self):
        """Gets the status of this CreateLoginResponse.  # noqa: E501


        :return: The status of this CreateLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateLoginResponse.


        :param status: The status of this CreateLoginResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PENDING_CONFIRMATION", "FAILED_TO_SEND_EMAIL"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, CreateLoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
