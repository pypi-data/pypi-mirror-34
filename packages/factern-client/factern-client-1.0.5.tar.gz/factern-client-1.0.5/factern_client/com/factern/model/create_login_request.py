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


class CreateLoginRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'password': 'str',
        'domain_id': 'str',
        'email': 'str',
        'workflow': 'str',
        'redirect_uri': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'password': 'password',
        'domain_id': 'domainId',
        'email': 'email',
        'workflow': 'workflow',
        'redirect_uri': 'redirectUri'
    }

    def __init__(self, include_summary=None, password=None, domain_id=None, email=None, workflow=None, redirect_uri=None):  # noqa: E501
        """CreateLoginRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._password = None
        self._domain_id = None
        self._email = None
        self._workflow = None
        self._redirect_uri = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if password is not None:
            self.password = password
        if domain_id is not None:
            self.domain_id = domain_id
        self.email = email
        self.workflow = workflow
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri

    @property
    def include_summary(self):
        """Gets the include_summary of this CreateLoginRequest.  # noqa: E501


        :return: The include_summary of this CreateLoginRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreateLoginRequest.


        :param include_summary: The include_summary of this CreateLoginRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def password(self):
        """Gets the password of this CreateLoginRequest.  # noqa: E501


        :return: The password of this CreateLoginRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateLoginRequest.


        :param password: The password of this CreateLoginRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateLoginRequest.  # noqa: E501


        :return: The domain_id of this CreateLoginRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateLoginRequest.


        :param domain_id: The domain_id of this CreateLoginRequest.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def email(self):
        """Gets the email of this CreateLoginRequest.  # noqa: E501


        :return: The email of this CreateLoginRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateLoginRequest.


        :param email: The email of this CreateLoginRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def workflow(self):
        """Gets the workflow of this CreateLoginRequest.  # noqa: E501


        :return: The workflow of this CreateLoginRequest.  # noqa: E501
        :rtype: str
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this CreateLoginRequest.


        :param workflow: The workflow of this CreateLoginRequest.  # noqa: E501
        :type: str
        """
        if workflow is None:
            raise ValueError("Invalid value for `workflow`, must not be `None`")  # noqa: E501

        self._workflow = workflow

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this CreateLoginRequest.  # noqa: E501


        :return: The redirect_uri of this CreateLoginRequest.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this CreateLoginRequest.


        :param redirect_uri: The redirect_uri of this CreateLoginRequest.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

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
        if not isinstance(other, CreateLoginRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
