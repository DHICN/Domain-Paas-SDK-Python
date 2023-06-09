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


class AddingDocumentModel(object):
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
        'doc': 'Document',
        'parent_group_id': 'str',
        'file_id': 'str'
    }

    attribute_map = {
        'doc': 'doc',
        'parent_group_id': 'parentGroupId',
        'file_id': 'fileId'
    }

    def __init__(self, doc=None, parent_group_id=None, file_id=None, local_vars_configuration=None):  # noqa: E501
        """AddingDocumentModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._doc = None
        self._parent_group_id = None
        self._file_id = None
        self.discriminator = None

        self.doc = doc
        self.parent_group_id = parent_group_id
        self.file_id = file_id

    @property
    def doc(self):
        """Gets the doc of this AddingDocumentModel.  # noqa: E501


        :return: The doc of this AddingDocumentModel.  # noqa: E501
        :rtype: Document
        """
        return self._doc

    @doc.setter
    def doc(self, doc):
        """Sets the doc of this AddingDocumentModel.


        :param doc: The doc of this AddingDocumentModel.  # noqa: E501
        :type: Document
        """
        if self.local_vars_configuration.client_side_validation and doc is None:  # noqa: E501
            raise ValueError("Invalid value for `doc`, must not be `None`")  # noqa: E501

        self._doc = doc

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this AddingDocumentModel.  # noqa: E501


        :return: The parent_group_id of this AddingDocumentModel.  # noqa: E501
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this AddingDocumentModel.


        :param parent_group_id: The parent_group_id of this AddingDocumentModel.  # noqa: E501
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def file_id(self):
        """Gets the file_id of this AddingDocumentModel.  # noqa: E501


        :return: The file_id of this AddingDocumentModel.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this AddingDocumentModel.


        :param file_id: The file_id of this AddingDocumentModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_id is None:  # noqa: E501
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

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
        if not isinstance(other, AddingDocumentModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddingDocumentModel):
            return True

        return self.to_dict() != other.to_dict()
