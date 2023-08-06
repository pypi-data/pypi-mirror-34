# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "BaseRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "BaseRequest").lower()
        parent = importlib.import_module(parent_fname).BaseRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class CreateLoginRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateLoginRequest.swagger_types.update(get_parent().swagger_types)
        CreateLoginRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain_id': 'str',
        'email': 'str',
        'password': 'str',
        'redirect_uri': 'str',
        'workflow': 'str'
    }

    attribute_map = {
        'domain_id': 'domainId',
        'email': 'email',
        'password': 'password',
        'redirect_uri': 'redirectUri',
        'workflow': 'workflow'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateLoginRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateLoginRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._domain_id = None
        self._email = None
        self._password = None
        self._redirect_uri = None
        self._workflow = None


        if "domain_id" in kwargs:
            self.domain_id = kwargs["domain_id"]
        if "email" not in kwargs:
            raise ValueError("CreateLoginRequest missing required argument: email")
        self._email = kwargs["email"]

        if "password" in kwargs:
            self.password = kwargs["password"]
        if "redirect_uri" in kwargs:
            self.redirect_uri = kwargs["redirect_uri"]
        if "workflow" not in kwargs:
            raise ValueError("CreateLoginRequest missing required argument: workflow")
        self._workflow = kwargs["workflow"]


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
