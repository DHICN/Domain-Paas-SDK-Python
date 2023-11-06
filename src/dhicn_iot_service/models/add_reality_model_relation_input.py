# coding: utf-8

"""
    IoT服务

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_iot_service.configuration import Configuration


class AddRealityModelRelationInput(object):
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
        'template_id': 'str',
        'model_point_id': 'str',
        'entity_id': 'str',
        'entity_type': 'str',
        'data_type_mapping': 'list[DataTypeMappingItem]'
    }

    attribute_map = {
        'template_id': 'templateId',
        'model_point_id': 'modelPointId',
        'entity_id': 'entityId',
        'entity_type': 'entityType',
        'data_type_mapping': 'dataTypeMapping'
    }

    def __init__(self, template_id=None, model_point_id=None, entity_id=None, entity_type=None, data_type_mapping=None, local_vars_configuration=None):  # noqa: E501
        """AddRealityModelRelationInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._template_id = None
        self._model_point_id = None
        self._entity_id = None
        self._entity_type = None
        self._data_type_mapping = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if model_point_id is not None:
            self.model_point_id = model_point_id
        if entity_id is not None:
            self.entity_id = entity_id
        self.entity_type = entity_type
        self.data_type_mapping = data_type_mapping

    @property
    def template_id(self):
        """Gets the template_id of this AddRealityModelRelationInput.  # noqa: E501

        模板方案ID template scenario id  # noqa: E501

        :return: The template_id of this AddRealityModelRelationInput.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this AddRealityModelRelationInput.

        模板方案ID template scenario id  # noqa: E501

        :param template_id: The template_id of this AddRealityModelRelationInput.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def model_point_id(self):
        """Gets the model_point_id of this AddRealityModelRelationInput.  # noqa: E501

        模型点位ID model point id  # noqa: E501

        :return: The model_point_id of this AddRealityModelRelationInput.  # noqa: E501
        :rtype: str
        """
        return self._model_point_id

    @model_point_id.setter
    def model_point_id(self, model_point_id):
        """Sets the model_point_id of this AddRealityModelRelationInput.

        模型点位ID model point id  # noqa: E501

        :param model_point_id: The model_point_id of this AddRealityModelRelationInput.  # noqa: E501
        :type: str
        """

        self._model_point_id = model_point_id

    @property
    def entity_id(self):
        """Gets the entity_id of this AddRealityModelRelationInput.  # noqa: E501

        资产/设备ID asset/device id  # noqa: E501

        :return: The entity_id of this AddRealityModelRelationInput.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this AddRealityModelRelationInput.

        资产/设备ID asset/device id  # noqa: E501

        :param entity_id: The entity_id of this AddRealityModelRelationInput.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this AddRealityModelRelationInput.  # noqa: E501

        实体类型，资产或设备 entity type, Asset or Device  # noqa: E501

        :return: The entity_type of this AddRealityModelRelationInput.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this AddRealityModelRelationInput.

        实体类型，资产或设备 entity type, Asset or Device  # noqa: E501

        :param entity_type: The entity_type of this AddRealityModelRelationInput.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def data_type_mapping(self):
        """Gets the data_type_mapping of this AddRealityModelRelationInput.  # noqa: E501

        模型点位数据类型与设备指标之间的映射关系 mapping relations of model point data type and device indicator  # noqa: E501

        :return: The data_type_mapping of this AddRealityModelRelationInput.  # noqa: E501
        :rtype: list[DataTypeMappingItem]
        """
        return self._data_type_mapping

    @data_type_mapping.setter
    def data_type_mapping(self, data_type_mapping):
        """Sets the data_type_mapping of this AddRealityModelRelationInput.

        模型点位数据类型与设备指标之间的映射关系 mapping relations of model point data type and device indicator  # noqa: E501

        :param data_type_mapping: The data_type_mapping of this AddRealityModelRelationInput.  # noqa: E501
        :type: list[DataTypeMappingItem]
        """

        self._data_type_mapping = data_type_mapping

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
        if not isinstance(other, AddRealityModelRelationInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddRealityModelRelationInput):
            return True

        return self.to_dict() != other.to_dict()
