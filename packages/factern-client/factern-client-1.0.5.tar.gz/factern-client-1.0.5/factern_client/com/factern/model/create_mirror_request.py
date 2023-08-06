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


class CreateMirrorRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'destination_node_id': 'str',
        'source_node_id': 'str',
        'template_id': 'str'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'destination_node_id': 'destinationNodeId',
        'source_node_id': 'sourceNodeId',
        'template_id': 'templateId'
    }

    def __init__(self, include_summary=None, destination_node_id=None, source_node_id=None, template_id=None):  # noqa: E501
        """CreateMirrorRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._destination_node_id = None
        self._source_node_id = None
        self._template_id = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        self.destination_node_id = destination_node_id
        self.source_node_id = source_node_id
        self.template_id = template_id

    @property
    def include_summary(self):
        """Gets the include_summary of this CreateMirrorRequest.  # noqa: E501


        :return: The include_summary of this CreateMirrorRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this CreateMirrorRequest.


        :param include_summary: The include_summary of this CreateMirrorRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def destination_node_id(self):
        """Gets the destination_node_id of this CreateMirrorRequest.  # noqa: E501


        :return: The destination_node_id of this CreateMirrorRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_node_id

    @destination_node_id.setter
    def destination_node_id(self, destination_node_id):
        """Sets the destination_node_id of this CreateMirrorRequest.


        :param destination_node_id: The destination_node_id of this CreateMirrorRequest.  # noqa: E501
        :type: str
        """
        if destination_node_id is None:
            raise ValueError("Invalid value for `destination_node_id`, must not be `None`")  # noqa: E501

        self._destination_node_id = destination_node_id

    @property
    def source_node_id(self):
        """Gets the source_node_id of this CreateMirrorRequest.  # noqa: E501


        :return: The source_node_id of this CreateMirrorRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        """Sets the source_node_id of this CreateMirrorRequest.


        :param source_node_id: The source_node_id of this CreateMirrorRequest.  # noqa: E501
        :type: str
        """
        if source_node_id is None:
            raise ValueError("Invalid value for `source_node_id`, must not be `None`")  # noqa: E501

        self._source_node_id = source_node_id

    @property
    def template_id(self):
        """Gets the template_id of this CreateMirrorRequest.  # noqa: E501


        :return: The template_id of this CreateMirrorRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateMirrorRequest.


        :param template_id: The template_id of this CreateMirrorRequest.  # noqa: E501
        :type: str
        """
        if template_id is None:
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

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
        if not isinstance(other, CreateMirrorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
