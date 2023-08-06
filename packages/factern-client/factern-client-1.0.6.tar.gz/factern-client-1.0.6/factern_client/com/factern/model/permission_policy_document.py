# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class PermissionPolicyDocument():


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
        'actions': 'list[PermissionAction]',
        'application_id': 'str',
        'effect': 'PermissionEffect',
        'grantee_id': 'str',
        'request_interface_id': 'str',
        'scope_id': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'application_id': 'applicationId',
        'effect': 'effect',
        'grantee_id': 'granteeId',
        'request_interface_id': 'requestInterfaceId',
        'scope_id': 'scopeId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """PermissionPolicyDocument - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("PermissionPolicyDocument got unexpected argument '%s'" % k)

        self._actions = None
        self._application_id = None
        self._effect = None
        self._grantee_id = None
        self._request_interface_id = None
        self._scope_id = None


        if "actions" not in kwargs:
            raise ValueError("PermissionPolicyDocument missing required argument: actions")
        self._actions = kwargs["actions"]

        if "application_id" in kwargs:
            self.application_id = kwargs["application_id"]
        if "effect" in kwargs:
            self.effect = kwargs["effect"]
        if "grantee_id" in kwargs:
            self.grantee_id = kwargs["grantee_id"]
        if "request_interface_id" in kwargs:
            self.request_interface_id = kwargs["request_interface_id"]
        if "scope_id" in kwargs:
            self.scope_id = kwargs["scope_id"]

    @property
    def actions(self):
        """Gets the actions of this PermissionPolicyDocument.  # noqa: E501


        :return: The actions of this PermissionPolicyDocument.  # noqa: E501
        :rtype: list[PermissionAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this PermissionPolicyDocument.


        :param actions: The actions of this PermissionPolicyDocument.  # noqa: E501
        :type: list[PermissionAction]
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

    @property
    def application_id(self):
        """Gets the application_id of this PermissionPolicyDocument.  # noqa: E501


        :return: The application_id of this PermissionPolicyDocument.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this PermissionPolicyDocument.


        :param application_id: The application_id of this PermissionPolicyDocument.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def effect(self):
        """Gets the effect of this PermissionPolicyDocument.  # noqa: E501


        :return: The effect of this PermissionPolicyDocument.  # noqa: E501
        :rtype: PermissionEffect
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this PermissionPolicyDocument.


        :param effect: The effect of this PermissionPolicyDocument.  # noqa: E501
        :type: PermissionEffect
        """

        self._effect = effect

    @property
    def grantee_id(self):
        """Gets the grantee_id of this PermissionPolicyDocument.  # noqa: E501


        :return: The grantee_id of this PermissionPolicyDocument.  # noqa: E501
        :rtype: str
        """
        return self._grantee_id

    @grantee_id.setter
    def grantee_id(self, grantee_id):
        """Sets the grantee_id of this PermissionPolicyDocument.


        :param grantee_id: The grantee_id of this PermissionPolicyDocument.  # noqa: E501
        :type: str
        """

        self._grantee_id = grantee_id

    @property
    def request_interface_id(self):
        """Gets the request_interface_id of this PermissionPolicyDocument.  # noqa: E501


        :return: The request_interface_id of this PermissionPolicyDocument.  # noqa: E501
        :rtype: str
        """
        return self._request_interface_id

    @request_interface_id.setter
    def request_interface_id(self, request_interface_id):
        """Sets the request_interface_id of this PermissionPolicyDocument.


        :param request_interface_id: The request_interface_id of this PermissionPolicyDocument.  # noqa: E501
        :type: str
        """

        self._request_interface_id = request_interface_id

    @property
    def scope_id(self):
        """Gets the scope_id of this PermissionPolicyDocument.  # noqa: E501


        :return: The scope_id of this PermissionPolicyDocument.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this PermissionPolicyDocument.


        :param scope_id: The scope_id of this PermissionPolicyDocument.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

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
        if not isinstance(other, PermissionPolicyDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
