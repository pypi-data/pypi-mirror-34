# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class ListCriteria():


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
        'action_id': 'str',
        'fact_type': 'str',
        'field_id': 'str',
        'include_deleted': 'bool',
        'label_list_id': 'str',
        'label_list_name': 'str',
        'max_results': 'float',
        'next_token': 'str',
        'starting_from_timestamp': 'float',
        'type_name': 'str'
    }

    attribute_map = {
        'action_id': 'actionId',
        'fact_type': 'factType',
        'field_id': 'fieldId',
        'include_deleted': 'includeDeleted',
        'label_list_id': 'labelListId',
        'label_list_name': 'labelListName',
        'max_results': 'maxResults',
        'next_token': 'nextToken',
        'starting_from_timestamp': 'startingFromTimestamp',
        'type_name': 'typeName'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ListCriteria - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("ListCriteria got unexpected argument '%s'" % k)

        self._action_id = None
        self._fact_type = None
        self._field_id = None
        self._include_deleted = None
        self._label_list_id = None
        self._label_list_name = None
        self._max_results = None
        self._next_token = None
        self._starting_from_timestamp = None
        self._type_name = None


        if "action_id" in kwargs:
            self.action_id = kwargs["action_id"]
        if "fact_type" in kwargs:
            self.fact_type = kwargs["fact_type"]
        if "field_id" in kwargs:
            self.field_id = kwargs["field_id"]
        if "include_deleted" in kwargs:
            self.include_deleted = kwargs["include_deleted"]
        if "label_list_id" in kwargs:
            self.label_list_id = kwargs["label_list_id"]
        if "label_list_name" in kwargs:
            self.label_list_name = kwargs["label_list_name"]
        if "max_results" in kwargs:
            self.max_results = kwargs["max_results"]
        if "next_token" in kwargs:
            self.next_token = kwargs["next_token"]
        if "starting_from_timestamp" in kwargs:
            self.starting_from_timestamp = kwargs["starting_from_timestamp"]
        if "type_name" in kwargs:
            self.type_name = kwargs["type_name"]

    @property
    def action_id(self):
        """Gets the action_id of this ListCriteria.  # noqa: E501


        :return: The action_id of this ListCriteria.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ListCriteria.


        :param action_id: The action_id of this ListCriteria.  # noqa: E501
        :type: str
        """

        self._action_id = action_id

    @property
    def fact_type(self):
        """Gets the fact_type of this ListCriteria.  # noqa: E501


        :return: The fact_type of this ListCriteria.  # noqa: E501
        :rtype: str
        """
        return self._fact_type

    @fact_type.setter
    def fact_type(self, fact_type):
        """Sets the fact_type of this ListCriteria.


        :param fact_type: The fact_type of this ListCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["Entity", "Login", "Application", "Field", "Information", "Permission", "Watch", "WatchEvent", "Group", "Interface", "LabelList", "Label", "Template", "Scope"]  # noqa: E501
        if fact_type not in allowed_values:
            raise ValueError(
                "Invalid value for `fact_type` ({0}), must be one of {1}"  # noqa: E501
                .format(fact_type, allowed_values)
            )

        self._fact_type = fact_type

    @property
    def field_id(self):
        """Gets the field_id of this ListCriteria.  # noqa: E501


        :return: The field_id of this ListCriteria.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this ListCriteria.


        :param field_id: The field_id of this ListCriteria.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def include_deleted(self):
        """Gets the include_deleted of this ListCriteria.  # noqa: E501


        :return: The include_deleted of this ListCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._include_deleted

    @include_deleted.setter
    def include_deleted(self, include_deleted):
        """Sets the include_deleted of this ListCriteria.


        :param include_deleted: The include_deleted of this ListCriteria.  # noqa: E501
        :type: bool
        """

        self._include_deleted = include_deleted

    @property
    def label_list_id(self):
        """Gets the label_list_id of this ListCriteria.  # noqa: E501


        :return: The label_list_id of this ListCriteria.  # noqa: E501
        :rtype: str
        """
        return self._label_list_id

    @label_list_id.setter
    def label_list_id(self, label_list_id):
        """Sets the label_list_id of this ListCriteria.


        :param label_list_id: The label_list_id of this ListCriteria.  # noqa: E501
        :type: str
        """

        self._label_list_id = label_list_id

    @property
    def label_list_name(self):
        """Gets the label_list_name of this ListCriteria.  # noqa: E501


        :return: The label_list_name of this ListCriteria.  # noqa: E501
        :rtype: str
        """
        return self._label_list_name

    @label_list_name.setter
    def label_list_name(self, label_list_name):
        """Sets the label_list_name of this ListCriteria.


        :param label_list_name: The label_list_name of this ListCriteria.  # noqa: E501
        :type: str
        """

        self._label_list_name = label_list_name

    @property
    def max_results(self):
        """Gets the max_results of this ListCriteria.  # noqa: E501


        :return: The max_results of this ListCriteria.  # noqa: E501
        :rtype: float
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ListCriteria.


        :param max_results: The max_results of this ListCriteria.  # noqa: E501
        :type: float
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this ListCriteria.  # noqa: E501


        :return: The next_token of this ListCriteria.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this ListCriteria.


        :param next_token: The next_token of this ListCriteria.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def starting_from_timestamp(self):
        """Gets the starting_from_timestamp of this ListCriteria.  # noqa: E501


        :return: The starting_from_timestamp of this ListCriteria.  # noqa: E501
        :rtype: float
        """
        return self._starting_from_timestamp

    @starting_from_timestamp.setter
    def starting_from_timestamp(self, starting_from_timestamp):
        """Sets the starting_from_timestamp of this ListCriteria.


        :param starting_from_timestamp: The starting_from_timestamp of this ListCriteria.  # noqa: E501
        :type: float
        """

        self._starting_from_timestamp = starting_from_timestamp

    @property
    def type_name(self):
        """Gets the type_name of this ListCriteria.  # noqa: E501


        :return: The type_name of this ListCriteria.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this ListCriteria.


        :param type_name: The type_name of this ListCriteria.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

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
        if not isinstance(other, ListCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
