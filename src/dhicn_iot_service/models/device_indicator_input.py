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

from openapi_client.configuration import Configuration


class DeviceIndicatorInput(object):
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
        'device_code': 'str',
        'indicator': 'str'
    }

    attribute_map = {
        'device_code': 'deviceCode',
        'indicator': 'indicator'
    }

    def __init__(self, device_code=None, indicator=None, local_vars_configuration=None):  # noqa: E501
        """DeviceIndicatorInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_code = None
        self._indicator = None
        self.discriminator = None

        self.device_code = device_code
        self.indicator = indicator

    @property
    def device_code(self):
        """Gets the device_code of this DeviceIndicatorInput.  # noqa: E501

        设备编码,若当前项目下Indicator有重复,设备编码必传  # noqa: E501

        :return: The device_code of this DeviceIndicatorInput.  # noqa: E501
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        """Sets the device_code of this DeviceIndicatorInput.

        设备编码,若当前项目下Indicator有重复,设备编码必传  # noqa: E501

        :param device_code: The device_code of this DeviceIndicatorInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_code is None:  # noqa: E501
            raise ValueError("Invalid value for `device_code`, must not be `None`")  # noqa: E501

        self._device_code = device_code

    @property
    def indicator(self):
        """Gets the indicator of this DeviceIndicatorInput.  # noqa: E501

        指标 indicator  # noqa: E501

        :return: The indicator of this DeviceIndicatorInput.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this DeviceIndicatorInput.

        指标 indicator  # noqa: E501

        :param indicator: The indicator of this DeviceIndicatorInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and indicator is None:  # noqa: E501
            raise ValueError("Invalid value for `indicator`, must not be `None`")  # noqa: E501

        self._indicator = indicator

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
        if not isinstance(other, DeviceIndicatorInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceIndicatorInput):
            return True

        return self.to_dict() != other.to_dict()
