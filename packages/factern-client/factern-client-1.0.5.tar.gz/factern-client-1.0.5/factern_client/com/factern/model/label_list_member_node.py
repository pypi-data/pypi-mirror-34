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


class LabelListMemberNode(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'label_list_id': 'str'
    }

    attribute_map = {
        'label_list_id': 'labelListId'
    }

    def __init__(self, label_list_id=None):  # noqa: E501
        """LabelListMemberNode - a model defined in Swagger"""  # noqa: E501

        self._label_list_id = None
        self.discriminator = None

        self.label_list_id = label_list_id

    @property
    def label_list_id(self):
        """Gets the label_list_id of this LabelListMemberNode.  # noqa: E501


        :return: The label_list_id of this LabelListMemberNode.  # noqa: E501
        :rtype: str
        """
        return self._label_list_id

    @label_list_id.setter
    def label_list_id(self, label_list_id):
        """Sets the label_list_id of this LabelListMemberNode.


        :param label_list_id: The label_list_id of this LabelListMemberNode.  # noqa: E501
        :type: str
        """
        if label_list_id is None:
            raise ValueError("Invalid value for `label_list_id`, must not be `None`")  # noqa: E501

        self._label_list_id = label_list_id

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
        if not isinstance(other, LabelListMemberNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
