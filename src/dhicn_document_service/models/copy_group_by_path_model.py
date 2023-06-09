# coding: utf-8

"""
    document-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_document_service.configuration import Configuration


class CopyGroupByPathModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'parent_group_path': 'str',
        'copying_group': 'Group'
    }

    attribute_map = {
        'parent_group_path': 'parentGroupPath',
        'copying_group': 'copyingGroup'
    }

    def __init__(self, parent_group_path=None, copying_group=None, local_vars_configuration=None):  # noqa: E501
        """CopyGroupByPathModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parent_group_path = None
        self._copying_group = None
        self.discriminator = None

        self.parent_group_path = parent_group_path
        self.copying_group = copying_group

    @property
    def parent_group_path(self):
        """Gets the parent_group_path of this CopyGroupByPathModel.  # noqa: E501


        :return: The parent_group_path of this CopyGroupByPathModel.  # noqa: E501
        :rtype: str
        """
        return self._parent_group_path

    @parent_group_path.setter
    def parent_group_path(self, parent_group_path):
        """Sets the parent_group_path of this CopyGroupByPathModel.


        :param parent_group_path: The parent_group_path of this CopyGroupByPathModel.  # noqa: E501
        :type: str
        """

        self._parent_group_path = parent_group_path

    @property
    def copying_group(self):
        """Gets the copying_group of this CopyGroupByPathModel.  # noqa: E501


        :return: The copying_group of this CopyGroupByPathModel.  # noqa: E501
        :rtype: Group
        """
        return self._copying_group

    @copying_group.setter
    def copying_group(self, copying_group):
        """Sets the copying_group of this CopyGroupByPathModel.


        :param copying_group: The copying_group of this CopyGroupByPathModel.  # noqa: E501
        :type: Group
        """
        if self.local_vars_configuration.client_side_validation and copying_group is None:  # noqa: E501
            raise ValueError("Invalid value for `copying_group`, must not be `None`")  # noqa: E501

        self._copying_group = copying_group

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, CopyGroupByPathModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CopyGroupByPathModel):
            return True

        return self.to_dict() != other.to_dict()
