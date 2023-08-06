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


class Summary(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'facts': 'FactCount',
        'external_data_usage': 'ExternalDataUsage',
        'account': 'Account',
        'cost': 'Cost',
        'searches': 'Searches'
    }

    attribute_map = {
        'facts': 'facts',
        'external_data_usage': 'externalDataUsage',
        'account': 'account',
        'cost': 'cost',
        'searches': 'searches'
    }

    def __init__(self, facts=None, external_data_usage=None, account=None, cost=None, searches=None):  # noqa: E501
        """Summary - a model defined in Swagger"""  # noqa: E501

        self._facts = None
        self._external_data_usage = None
        self._account = None
        self._cost = None
        self._searches = None
        self.discriminator = None

        if facts is not None:
            self.facts = facts
        if external_data_usage is not None:
            self.external_data_usage = external_data_usage
        if account is not None:
            self.account = account
        if cost is not None:
            self.cost = cost
        if searches is not None:
            self.searches = searches

    @property
    def facts(self):
        """Gets the facts of this Summary.  # noqa: E501


        :return: The facts of this Summary.  # noqa: E501
        :rtype: FactCount
        """
        return self._facts

    @facts.setter
    def facts(self, facts):
        """Sets the facts of this Summary.


        :param facts: The facts of this Summary.  # noqa: E501
        :type: FactCount
        """

        self._facts = facts

    @property
    def external_data_usage(self):
        """Gets the external_data_usage of this Summary.  # noqa: E501


        :return: The external_data_usage of this Summary.  # noqa: E501
        :rtype: ExternalDataUsage
        """
        return self._external_data_usage

    @external_data_usage.setter
    def external_data_usage(self, external_data_usage):
        """Sets the external_data_usage of this Summary.


        :param external_data_usage: The external_data_usage of this Summary.  # noqa: E501
        :type: ExternalDataUsage
        """

        self._external_data_usage = external_data_usage

    @property
    def account(self):
        """Gets the account of this Summary.  # noqa: E501


        :return: The account of this Summary.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Summary.


        :param account: The account of this Summary.  # noqa: E501
        :type: Account
        """

        self._account = account

    @property
    def cost(self):
        """Gets the cost of this Summary.  # noqa: E501


        :return: The cost of this Summary.  # noqa: E501
        :rtype: Cost
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Summary.


        :param cost: The cost of this Summary.  # noqa: E501
        :type: Cost
        """

        self._cost = cost

    @property
    def searches(self):
        """Gets the searches of this Summary.  # noqa: E501


        :return: The searches of this Summary.  # noqa: E501
        :rtype: Searches
        """
        return self._searches

    @searches.setter
    def searches(self, searches):
        """Sets the searches of this Summary.


        :param searches: The searches of this Summary.  # noqa: E501
        :type: Searches
        """

        self._searches = searches

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
        if not isinstance(other, Summary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
