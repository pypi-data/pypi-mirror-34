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


class LabelList(object):

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
        'batch_id': 'str',
        'fact_type': 'str',
        'parent_id': 'str',
        'description': 'str',
        'members': 'list[LabelListMember]',
        'name': 'str'
    }

    attribute_map = {
        'deleted': 'deleted',
        'timestamp': 'timestamp',
        'node_id': 'nodeId',
        'agent': 'agent',
        'batch_id': 'batchId',
        'fact_type': 'factType',
        'parent_id': 'parentId',
        'description': 'description',
        'members': 'members',
        'name': 'name'
    }

    def __init__(self, deleted=None, timestamp=None, node_id=None, agent=None, batch_id=None, fact_type=None, parent_id=None, description=None, members=None, name=None):  # noqa: E501
        """LabelList - a model defined in Swagger"""  # noqa: E501

        self._deleted = None
        self._timestamp = None
        self._node_id = None
        self._agent = None
        self._batch_id = None
        self._fact_type = None
        self._parent_id = None
        self._description = None
        self._members = None
        self._name = None
        self.discriminator = None

        if deleted is not None:
            self.deleted = deleted
        self.timestamp = timestamp
        self.node_id = node_id
        self.agent = agent
        self.batch_id = batch_id
        self.fact_type = fact_type
        self.parent_id = parent_id
        if description is not None:
            self.description = description
        self.members = members
        self.name = name

    @property
    def deleted(self):
        """Gets the deleted of this LabelList.  # noqa: E501


        :return: The deleted of this LabelList.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this LabelList.


        :param deleted: The deleted of this LabelList.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def timestamp(self):
        """Gets the timestamp of this LabelList.  # noqa: E501


        :return: The timestamp of this LabelList.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this LabelList.


        :param timestamp: The timestamp of this LabelList.  # noqa: E501
        :type: float
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def node_id(self):
        """Gets the node_id of this LabelList.  # noqa: E501


        :return: The node_id of this LabelList.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this LabelList.


        :param node_id: The node_id of this LabelList.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def agent(self):
        """Gets the agent of this LabelList.  # noqa: E501


        :return: The agent of this LabelList.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this LabelList.


        :param agent: The agent of this LabelList.  # noqa: E501
        :type: Agent
        """
        if agent is None:
            raise ValueError("Invalid value for `agent`, must not be `None`")  # noqa: E501

        self._agent = agent

    @property
    def batch_id(self):
        """Gets the batch_id of this LabelList.  # noqa: E501


        :return: The batch_id of this LabelList.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this LabelList.


        :param batch_id: The batch_id of this LabelList.  # noqa: E501
        :type: str
        """
        if batch_id is None:
            raise ValueError("Invalid value for `batch_id`, must not be `None`")  # noqa: E501

        self._batch_id = batch_id

    @property
    def fact_type(self):
        """Gets the fact_type of this LabelList.  # noqa: E501


        :return: The fact_type of this LabelList.  # noqa: E501
        :rtype: str
        """
        return self._fact_type

    @fact_type.setter
    def fact_type(self, fact_type):
        """Sets the fact_type of this LabelList.


        :param fact_type: The fact_type of this LabelList.  # noqa: E501
        :type: str
        """
        if fact_type is None:
            raise ValueError("Invalid value for `fact_type`, must not be `None`")  # noqa: E501

        self._fact_type = fact_type

    @property
    def parent_id(self):
        """Gets the parent_id of this LabelList.  # noqa: E501


        :return: The parent_id of this LabelList.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this LabelList.


        :param parent_id: The parent_id of this LabelList.  # noqa: E501
        :type: str
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this LabelList.  # noqa: E501


        :return: The description of this LabelList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LabelList.


        :param description: The description of this LabelList.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def members(self):
        """Gets the members of this LabelList.  # noqa: E501


        :return: The members of this LabelList.  # noqa: E501
        :rtype: list[LabelListMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this LabelList.


        :param members: The members of this LabelList.  # noqa: E501
        :type: list[LabelListMember]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

    @property
    def name(self):
        """Gets the name of this LabelList.  # noqa: E501


        :return: The name of this LabelList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelList.


        :param name: The name of this LabelList.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, LabelList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
