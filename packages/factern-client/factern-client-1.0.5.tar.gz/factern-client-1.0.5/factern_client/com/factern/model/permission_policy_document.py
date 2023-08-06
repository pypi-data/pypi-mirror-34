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


class PermissionPolicyDocument(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'grantee_id': 'str',
        'effect': 'PermissionEffect',
        'actions': 'list[PermissionAction]',
        'scope_id': 'str',
        'request_interface_id': 'str',
        'application_id': 'str'
    }

    attribute_map = {
        'grantee_id': 'granteeId',
        'effect': 'effect',
        'actions': 'actions',
        'scope_id': 'scopeId',
        'request_interface_id': 'requestInterfaceId',
        'application_id': 'applicationId'
    }

    def __init__(self, grantee_id=None, effect=None, actions=None, scope_id=None, request_interface_id=None, application_id=None):  # noqa: E501
        """PermissionPolicyDocument - a model defined in Swagger"""  # noqa: E501

        self._grantee_id = None
        self._effect = None
        self._actions = None
        self._scope_id = None
        self._request_interface_id = None
        self._application_id = None
        self.discriminator = None

        if grantee_id is not None:
            self.grantee_id = grantee_id
        if effect is not None:
            self.effect = effect
        self.actions = actions
        if scope_id is not None:
            self.scope_id = scope_id
        if request_interface_id is not None:
            self.request_interface_id = request_interface_id
        if application_id is not None:
            self.application_id = application_id

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
