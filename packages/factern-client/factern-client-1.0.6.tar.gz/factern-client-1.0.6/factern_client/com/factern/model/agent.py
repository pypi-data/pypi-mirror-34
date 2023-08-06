# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class Agent():


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
        'application': 'str',
        'login': 'str',
        'representing': 'str'
    }

    attribute_map = {
        'application': 'application',
        'login': 'login',
        'representing': 'representing'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Agent - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("Agent got unexpected argument '%s'" % k)

        self._application = None
        self._login = None
        self._representing = None


        if "application" not in kwargs:
            raise ValueError("Agent missing required argument: application")
        self._application = kwargs["application"]

        if "login" not in kwargs:
            raise ValueError("Agent missing required argument: login")
        self._login = kwargs["login"]

        if "representing" not in kwargs:
            raise ValueError("Agent missing required argument: representing")
        self._representing = kwargs["representing"]


    @property
    def application(self):
        """Gets the application of this Agent.  # noqa: E501


        :return: The application of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this Agent.


        :param application: The application of this Agent.  # noqa: E501
        :type: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def login(self):
        """Gets the login of this Agent.  # noqa: E501


        :return: The login of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this Agent.


        :param login: The login of this Agent.  # noqa: E501
        :type: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    @property
    def representing(self):
        """Gets the representing of this Agent.  # noqa: E501


        :return: The representing of this Agent.  # noqa: E501
        :rtype: str
        """
        return self._representing

    @representing.setter
    def representing(self, representing):
        """Sets the representing of this Agent.


        :param representing: The representing of this Agent.  # noqa: E501
        :type: str
        """
        if representing is None:
            raise ValueError("Invalid value for `representing`, must not be `None`")  # noqa: E501

        self._representing = representing

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
        if not isinstance(other, Agent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
