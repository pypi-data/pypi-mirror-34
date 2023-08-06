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


class WriteRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        WriteRequest.swagger_types.update(get_parent().swagger_types)
        WriteRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_storage_id': 'str',
        'document': 'list[object]',
        'node_id': 'str',
        'source_node_id': 'str',
        'template': 'list[object]',
        'template_id': 'str',
        'transform': 'list[TransformElement]',
        'values': 'list[object]'
    }

    attribute_map = {
        'default_storage_id': 'defaultStorageId',
        'document': 'document',
        'node_id': 'nodeId',
        'source_node_id': 'sourceNodeId',
        'template': 'template',
        'template_id': 'templateId',
        'transform': 'transform',
        'values': 'values'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """WriteRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("WriteRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._default_storage_id = None
        self._document = None
        self._node_id = None
        self._source_node_id = None
        self._template = None
        self._template_id = None
        self._transform = None
        self._values = None


        if "default_storage_id" in kwargs:
            self.default_storage_id = kwargs["default_storage_id"]
        if "document" in kwargs:
            self.document = kwargs["document"]
        if "node_id" not in kwargs:
            raise ValueError("WriteRequest missing required argument: node_id")
        self._node_id = kwargs["node_id"]

        if "source_node_id" in kwargs:
            self.source_node_id = kwargs["source_node_id"]
        if "template" in kwargs:
            self.template = kwargs["template"]
        if "template_id" in kwargs:
            self.template_id = kwargs["template_id"]
        if "transform" in kwargs:
            self.transform = kwargs["transform"]
        if "values" in kwargs:
            self.values = kwargs["values"]

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
