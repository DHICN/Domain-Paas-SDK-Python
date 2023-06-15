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


class QueryTemplateListOutput(object):
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
        'id': 'str',
        'file_name': 'str',
        'enable': 'bool',
        'remark': 'str',
        'version': 'int',
        'library_type': 'str',
        'business_type': 'str',
        'model_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'fileName',
        'enable': 'enable',
        'remark': 'remark',
        'version': 'version',
        'library_type': 'libraryType',
        'business_type': 'businessType',
        'model_type': 'modelType'
    }

    def __init__(self, id=None, file_name=None, enable=None, remark=None, version=None, library_type=None, business_type=None, model_type=None, local_vars_configuration=None):  # noqa: E501
        """QueryTemplateListOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._file_name = None
        self._enable = None
        self._remark = None
        self._version = None
        self._library_type = None
        self._business_type = None
        self._model_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.file_name = file_name
        if enable is not None:
            self.enable = enable
        self.remark = remark
        if version is not None:
            self.version = version
        self.library_type = library_type
        self.business_type = business_type
        self.model_type = model_type

    @property
    def id(self):
        """Gets the id of this QueryTemplateListOutput.  # noqa: E501

        模板文件ID template file Id  # noqa: E501

        :return: The id of this QueryTemplateListOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryTemplateListOutput.

        模板文件ID template file Id  # noqa: E501

        :param id: The id of this QueryTemplateListOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def file_name(self):
        """Gets the file_name of this QueryTemplateListOutput.  # noqa: E501

        模板文件名称 template file name  # noqa: E501

        :return: The file_name of this QueryTemplateListOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this QueryTemplateListOutput.

        模板文件名称 template file name  # noqa: E501

        :param file_name: The file_name of this QueryTemplateListOutput.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def enable(self):
        """Gets the enable of this QueryTemplateListOutput.  # noqa: E501

        是否可用于创建模板方案 if it can be used to create template scenario  # noqa: E501

        :return: The enable of this QueryTemplateListOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this QueryTemplateListOutput.

        是否可用于创建模板方案 if it can be used to create template scenario  # noqa: E501

        :param enable: The enable of this QueryTemplateListOutput.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def remark(self):
        """Gets the remark of this QueryTemplateListOutput.  # noqa: E501

        模板文件备注 template file remark  # noqa: E501

        :return: The remark of this QueryTemplateListOutput.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this QueryTemplateListOutput.

        模板文件备注 template file remark  # noqa: E501

        :param remark: The remark of this QueryTemplateListOutput.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def version(self):
        """Gets the version of this QueryTemplateListOutput.  # noqa: E501

        模板文件版本 template file version  # noqa: E501

        :return: The version of this QueryTemplateListOutput.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this QueryTemplateListOutput.

        模板文件版本 template file version  # noqa: E501

        :param version: The version of this QueryTemplateListOutput.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def library_type(self):
        """Gets the library_type of this QueryTemplateListOutput.  # noqa: E501

        库类型  # noqa: E501

        :return: The library_type of this QueryTemplateListOutput.  # noqa: E501
        :rtype: str
        """
        return self._library_type

    @library_type.setter
    def library_type(self, library_type):
        """Sets the library_type of this QueryTemplateListOutput.

        库类型  # noqa: E501

        :param library_type: The library_type of this QueryTemplateListOutput.  # noqa: E501
        :type: str
        """

        self._library_type = library_type

    @property
    def business_type(self):
        """Gets the business_type of this QueryTemplateListOutput.  # noqa: E501

        业务类型  # noqa: E501

        :return: The business_type of this QueryTemplateListOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this QueryTemplateListOutput.

        业务类型  # noqa: E501

        :param business_type: The business_type of this QueryTemplateListOutput.  # noqa: E501
        :type: str
        """

        self._business_type = business_type

    @property
    def model_type(self):
        """Gets the model_type of this QueryTemplateListOutput.  # noqa: E501

        模型类型  # noqa: E501

        :return: The model_type of this QueryTemplateListOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this QueryTemplateListOutput.

        模型类型  # noqa: E501

        :param model_type: The model_type of this QueryTemplateListOutput.  # noqa: E501
        :type: str
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
        if not isinstance(other, QueryTemplateListOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryTemplateListOutput):
            return True

        return self.to_dict() != other.to_dict()