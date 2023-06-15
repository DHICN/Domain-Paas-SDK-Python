# coding: utf-8

"""
    digital-twin-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_digital_twin_service.configuration import Configuration


class DataTypeMappingItem(object):
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
        'model_component': 'str',
        'device_indicator_id': 'str',
        'model_data_type': 'str'
    }

    attribute_map = {
        'model_component': 'modelComponent',
        'device_indicator_id': 'deviceIndicatorId',
        'model_data_type': 'modelDataType'
    }

    def __init__(self, model_component=None, device_indicator_id=None, model_data_type=None, local_vars_configuration=None):  # noqa: E501
        """DataTypeMappingItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_component = None
        self._device_indicator_id = None
        self._model_data_type = None
        self.discriminator = None

        self.model_component = model_component
        if device_indicator_id is not None:
            self.device_indicator_id = device_indicator_id
        self.model_data_type = model_data_type

    @property
    def model_component(self):
        """Gets the model_component of this DataTypeMappingItem.  # noqa: E501

        模型水质项 model water quality component  # noqa: E501

        :return: The model_component of this DataTypeMappingItem.  # noqa: E501
        :rtype: str
        """
        return self._model_component

    @model_component.setter
    def model_component(self, model_component):
        """Sets the model_component of this DataTypeMappingItem.

        模型水质项 model water quality component  # noqa: E501

        :param model_component: The model_component of this DataTypeMappingItem.  # noqa: E501
        :type: str
        """

        self._model_component = model_component

    @property
    def device_indicator_id(self):
        """Gets the device_indicator_id of this DataTypeMappingItem.  # noqa: E501

        设备指标ID device indicator id  # noqa: E501

        :return: The device_indicator_id of this DataTypeMappingItem.  # noqa: E501
        :rtype: str
        """
        return self._device_indicator_id

    @device_indicator_id.setter
    def device_indicator_id(self, device_indicator_id):
        """Sets the device_indicator_id of this DataTypeMappingItem.

        设备指标ID device indicator id  # noqa: E501

        :param device_indicator_id: The device_indicator_id of this DataTypeMappingItem.  # noqa: E501
        :type: str
        """

        self._device_indicator_id = device_indicator_id

    @property
    def model_data_type(self):
        """Gets the model_data_type of this DataTypeMappingItem.  # noqa: E501

        模型数据类型 model data type  # noqa: E501

        :return: The model_data_type of this DataTypeMappingItem.  # noqa: E501
        :rtype: str
        """
        return self._model_data_type

    @model_data_type.setter
    def model_data_type(self, model_data_type):
        """Sets the model_data_type of this DataTypeMappingItem.

        模型数据类型 model data type  # noqa: E501

        :param model_data_type: The model_data_type of this DataTypeMappingItem.  # noqa: E501
        :type: str
        """

        self._model_data_type = model_data_type

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
        if not isinstance(other, DataTypeMappingItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataTypeMappingItem):
            return True

        return self.to_dict() != other.to_dict()