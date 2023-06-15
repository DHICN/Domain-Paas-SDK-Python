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


class LegendItemDto(object):
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
        'model_type': 'str',
        'result_type': 'str',
        'type_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'model_type': 'modelType',
        'result_type': 'resultType',
        'type_name': 'typeName',
        'description': 'description'
    }

    def __init__(self, model_type=None, result_type=None, type_name=None, description=None, local_vars_configuration=None):  # noqa: E501
        """LegendItemDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_type = None
        self._result_type = None
        self._type_name = None
        self._description = None
        self.discriminator = None

        self.model_type = model_type
        self.result_type = result_type
        self.type_name = type_name
        self.description = description

    @property
    def model_type(self):
        """Gets the model_type of this LegendItemDto.  # noqa: E501

        模型类型 model type  # noqa: E501

        :return: The model_type of this LegendItemDto.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this LegendItemDto.

        模型类型 model type  # noqa: E501

        :param model_type: The model_type of this LegendItemDto.  # noqa: E501
        :type: str
        """

        self._model_type = model_type

    @property
    def result_type(self):
        """Gets the result_type of this LegendItemDto.  # noqa: E501

        结果类型 result type  # noqa: E501

        :return: The result_type of this LegendItemDto.  # noqa: E501
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this LegendItemDto.

        结果类型 result type  # noqa: E501

        :param result_type: The result_type of this LegendItemDto.  # noqa: E501
        :type: str
        """

        self._result_type = result_type

    @property
    def type_name(self):
        """Gets the type_name of this LegendItemDto.  # noqa: E501

        数据类型 data type name  # noqa: E501

        :return: The type_name of this LegendItemDto.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this LegendItemDto.

        数据类型 data type name  # noqa: E501

        :param type_name: The type_name of this LegendItemDto.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    @property
    def description(self):
        """Gets the description of this LegendItemDto.  # noqa: E501

        描述 description  # noqa: E501

        :return: The description of this LegendItemDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LegendItemDto.

        描述 description  # noqa: E501

        :param description: The description of this LegendItemDto.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, LegendItemDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LegendItemDto):
            return True

        return self.to_dict() != other.to_dict()
