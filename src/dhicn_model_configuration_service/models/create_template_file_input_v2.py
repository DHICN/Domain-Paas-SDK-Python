# coding: utf-8

"""
    model-configuration-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_model_configuration_service.configuration import Configuration


class CreateTemplateFileInputV2(object):
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
        'mupp_name': 'str',
        'file_id': 'str',
        'system_id': 'str',
        'library_type': 'LibraryTypeEnum',
        'business_type': 'BusinessTypeEnum',
        'model_type': 'ModelTypeEnum'
    }

    attribute_map = {
        'mupp_name': 'muppName',
        'file_id': 'fileId',
        'system_id': 'systemId',
        'library_type': 'libraryType',
        'business_type': 'businessType',
        'model_type': 'modelType'
    }

    def __init__(self, mupp_name=None, file_id=None, system_id=None, library_type=None, business_type=None, model_type=None, local_vars_configuration=None):  # noqa: E501
        """CreateTemplateFileInputV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mupp_name = None
        self._file_id = None
        self._system_id = None
        self._library_type = None
        self._business_type = None
        self._model_type = None
        self.discriminator = None

        self.mupp_name = mupp_name
        if file_id is not None:
            self.file_id = file_id
        self.system_id = system_id
        if library_type is not None:
            self.library_type = library_type
        if business_type is not None:
            self.business_type = business_type
        if model_type is not None:
            self.model_type = model_type

    @property
    def mupp_name(self):
        """Gets the mupp_name of this CreateTemplateFileInputV2.  # noqa: E501

        模型文件名称 model file name without path  # noqa: E501

        :return: The mupp_name of this CreateTemplateFileInputV2.  # noqa: E501
        :rtype: str
        """
        return self._mupp_name

    @mupp_name.setter
    def mupp_name(self, mupp_name):
        """Sets the mupp_name of this CreateTemplateFileInputV2.

        模型文件名称 model file name without path  # noqa: E501

        :param mupp_name: The mupp_name of this CreateTemplateFileInputV2.  # noqa: E501
        :type: str
        """

        self._mupp_name = mupp_name

    @property
    def file_id(self):
        """Gets the file_id of this CreateTemplateFileInputV2.  # noqa: E501

        上传的文件的ID upload file id  # noqa: E501

        :return: The file_id of this CreateTemplateFileInputV2.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this CreateTemplateFileInputV2.

        上传的文件的ID upload file id  # noqa: E501

        :param file_id: The file_id of this CreateTemplateFileInputV2.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def system_id(self):
        """Gets the system_id of this CreateTemplateFileInputV2.  # noqa: E501

        系统ID system id  # noqa: E501

        :return: The system_id of this CreateTemplateFileInputV2.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this CreateTemplateFileInputV2.

        系统ID system id  # noqa: E501

        :param system_id: The system_id of this CreateTemplateFileInputV2.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def library_type(self):
        """Gets the library_type of this CreateTemplateFileInputV2.  # noqa: E501


        :return: The library_type of this CreateTemplateFileInputV2.  # noqa: E501
        :rtype: LibraryTypeEnum
        """
        return self._library_type

    @library_type.setter
    def library_type(self, library_type):
        """Sets the library_type of this CreateTemplateFileInputV2.


        :param library_type: The library_type of this CreateTemplateFileInputV2.  # noqa: E501
        :type: LibraryTypeEnum
        """

        self._library_type = library_type

    @property
    def business_type(self):
        """Gets the business_type of this CreateTemplateFileInputV2.  # noqa: E501


        :return: The business_type of this CreateTemplateFileInputV2.  # noqa: E501
        :rtype: BusinessTypeEnum
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this CreateTemplateFileInputV2.


        :param business_type: The business_type of this CreateTemplateFileInputV2.  # noqa: E501
        :type: BusinessTypeEnum
        """

        self._business_type = business_type

    @property
    def model_type(self):
        """Gets the model_type of this CreateTemplateFileInputV2.  # noqa: E501


        :return: The model_type of this CreateTemplateFileInputV2.  # noqa: E501
        :rtype: ModelTypeEnum
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this CreateTemplateFileInputV2.


        :param model_type: The model_type of this CreateTemplateFileInputV2.  # noqa: E501
        :type: ModelTypeEnum
        """

        self._model_type = model_type

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
        if not isinstance(other, CreateTemplateFileInputV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTemplateFileInputV2):
            return True

        return self.to_dict() != other.to_dict()
