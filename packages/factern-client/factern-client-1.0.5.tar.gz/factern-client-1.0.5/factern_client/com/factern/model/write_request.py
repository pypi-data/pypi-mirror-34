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


class WriteRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_summary': 'bool',
        'source_node_id': 'str',
        'node_id': 'str',
        'transform': 'list[TransformElement]',
        'default_storage_id': 'str',
        'values': 'list[object]',
        'template': 'list[object]',
        'template_id': 'str',
        'document': 'list[object]'
    }

    attribute_map = {
        'include_summary': 'includeSummary',
        'source_node_id': 'sourceNodeId',
        'node_id': 'nodeId',
        'transform': 'transform',
        'default_storage_id': 'defaultStorageId',
        'values': 'values',
        'template': 'template',
        'template_id': 'templateId',
        'document': 'document'
    }

    def __init__(self, include_summary=None, source_node_id=None, node_id=None, transform=None, default_storage_id=None, values=None, template=None, template_id=None, document=None):  # noqa: E501
        """WriteRequest - a model defined in Swagger"""  # noqa: E501

        self._include_summary = None
        self._source_node_id = None
        self._node_id = None
        self._transform = None
        self._default_storage_id = None
        self._values = None
        self._template = None
        self._template_id = None
        self._document = None
        self.discriminator = None

        if include_summary is not None:
            self.include_summary = include_summary
        if source_node_id is not None:
            self.source_node_id = source_node_id
        self.node_id = node_id
        if transform is not None:
            self.transform = transform
        if default_storage_id is not None:
            self.default_storage_id = default_storage_id
        if values is not None:
            self.values = values
        if template is not None:
            self.template = template
        if template_id is not None:
            self.template_id = template_id
        if document is not None:
            self.document = document

    @property
    def include_summary(self):
        """Gets the include_summary of this WriteRequest.  # noqa: E501


        :return: The include_summary of this WriteRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_summary

    @include_summary.setter
    def include_summary(self, include_summary):
        """Sets the include_summary of this WriteRequest.


        :param include_summary: The include_summary of this WriteRequest.  # noqa: E501
        :type: bool
        """

        self._include_summary = include_summary

    @property
    def source_node_id(self):
        """Gets the source_node_id of this WriteRequest.  # noqa: E501


        :return: The source_node_id of this WriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        """Sets the source_node_id of this WriteRequest.


        :param source_node_id: The source_node_id of this WriteRequest.  # noqa: E501
        :type: str
        """

        self._source_node_id = source_node_id

    @property
    def node_id(self):
        """Gets the node_id of this WriteRequest.  # noqa: E501


        :return: The node_id of this WriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this WriteRequest.


        :param node_id: The node_id of this WriteRequest.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def transform(self):
        """Gets the transform of this WriteRequest.  # noqa: E501


        :return: The transform of this WriteRequest.  # noqa: E501
        :rtype: list[TransformElement]
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this WriteRequest.


        :param transform: The transform of this WriteRequest.  # noqa: E501
        :type: list[TransformElement]
        """

        self._transform = transform

    @property
    def default_storage_id(self):
        """Gets the default_storage_id of this WriteRequest.  # noqa: E501


        :return: The default_storage_id of this WriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._default_storage_id

    @default_storage_id.setter
    def default_storage_id(self, default_storage_id):
        """Sets the default_storage_id of this WriteRequest.


        :param default_storage_id: The default_storage_id of this WriteRequest.  # noqa: E501
        :type: str
        """

        self._default_storage_id = default_storage_id

    @property
    def values(self):
        """Gets the values of this WriteRequest.  # noqa: E501


        :return: The values of this WriteRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this WriteRequest.


        :param values: The values of this WriteRequest.  # noqa: E501
        :type: list[object]
        """

        self._values = values

    @property
    def template(self):
        """Gets the template of this WriteRequest.  # noqa: E501


        :return: The template of this WriteRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this WriteRequest.


        :param template: The template of this WriteRequest.  # noqa: E501
        :type: list[object]
        """

        self._template = template

    @property
    def template_id(self):
        """Gets the template_id of this WriteRequest.  # noqa: E501


        :return: The template_id of this WriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this WriteRequest.


        :param template_id: The template_id of this WriteRequest.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def document(self):
        """Gets the document of this WriteRequest.  # noqa: E501


        :return: The document of this WriteRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this WriteRequest.


        :param document: The document of this WriteRequest.  # noqa: E501
        :type: list[object]
        """

        self._document = document

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
        if not isinstance(other, WriteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
