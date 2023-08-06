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


class TransformElement(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'operation': 'str',
        'spec': 'object'
    }

    attribute_map = {
        'operation': 'operation',
        'spec': 'spec'
    }

    def __init__(self, operation=None, spec=None):  # noqa: E501
        """TransformElement - a model defined in Swagger"""  # noqa: E501

        self._operation = None
        self._spec = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if spec is not None:
            self.spec = spec

    @property
    def operation(self):
        """Gets the operation of this TransformElement.  # noqa: E501


        :return: The operation of this TransformElement.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this TransformElement.


        :param operation: The operation of this TransformElement.  # noqa: E501
        :type: str
        """
        allowed_values = ["shift", "default", "remove", "sort", "cardinality"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def spec(self):
        """Gets the spec of this TransformElement.  # noqa: E501


        :return: The spec of this TransformElement.  # noqa: E501
        :rtype: object
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this TransformElement.


        :param spec: The spec of this TransformElement.  # noqa: E501
        :type: object
        """

        self._spec = spec

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
        if not isinstance(other, TransformElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
