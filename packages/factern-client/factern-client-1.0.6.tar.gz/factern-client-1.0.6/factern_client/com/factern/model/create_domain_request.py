# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "CreateNamedRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "CreateNamedRequest").lower()
        parent = importlib.import_module(parent_fname).CreateNamedRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class CreateDomainRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateDomainRequest.swagger_types.update(get_parent().swagger_types)
        CreateDomainRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'add_fact': 'ApiEndpoint',
        'get_fact': 'ApiEndpoint',
        'query_facts': 'ApiEndpoint'
    }

    attribute_map = {
        'add_fact': 'addFact',
        'get_fact': 'getFact',
        'query_facts': 'queryFacts'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateDomainRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateDomainRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._add_fact = None
        self._get_fact = None
        self._query_facts = None


        if "add_fact" not in kwargs:
            raise ValueError("CreateDomainRequest missing required argument: add_fact")
        self._add_fact = kwargs["add_fact"]

        if "get_fact" not in kwargs:
            raise ValueError("CreateDomainRequest missing required argument: get_fact")
        self._get_fact = kwargs["get_fact"]

        if "query_facts" in kwargs:
            self.query_facts = kwargs["query_facts"]

    @property
    def add_fact(self):
        """Gets the add_fact of this CreateDomainRequest.  # noqa: E501


        :return: The add_fact of this CreateDomainRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._add_fact

    @add_fact.setter
    def add_fact(self, add_fact):
        """Sets the add_fact of this CreateDomainRequest.


        :param add_fact: The add_fact of this CreateDomainRequest.  # noqa: E501
        :type: ApiEndpoint
        """
        if add_fact is None:
            raise ValueError("Invalid value for `add_fact`, must not be `None`")  # noqa: E501

        self._add_fact = add_fact

    @property
    def get_fact(self):
        """Gets the get_fact of this CreateDomainRequest.  # noqa: E501


        :return: The get_fact of this CreateDomainRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._get_fact

    @get_fact.setter
    def get_fact(self, get_fact):
        """Sets the get_fact of this CreateDomainRequest.


        :param get_fact: The get_fact of this CreateDomainRequest.  # noqa: E501
        :type: ApiEndpoint
        """
        if get_fact is None:
            raise ValueError("Invalid value for `get_fact`, must not be `None`")  # noqa: E501

        self._get_fact = get_fact

    @property
    def query_facts(self):
        """Gets the query_facts of this CreateDomainRequest.  # noqa: E501


        :return: The query_facts of this CreateDomainRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._query_facts

    @query_facts.setter
    def query_facts(self, query_facts):
        """Sets the query_facts of this CreateDomainRequest.


        :param query_facts: The query_facts of this CreateDomainRequest.  # noqa: E501
        :type: ApiEndpoint
        """

        self._query_facts = query_facts

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
        if not isinstance(other, CreateDomainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
