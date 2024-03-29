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


class GetMultiDeviceIndicatorOutput(object):
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
        'device_id': 'str',
        'indicators': 'list[DeviceIndicatorOutput]'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'indicators': 'indicators'
    }

    def __init__(self, device_id=None, indicators=None, local_vars_configuration=None):  # noqa: E501
        """GetMultiDeviceIndicatorOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._indicators = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        self.indicators = indicators

    @property
    def device_id(self):
        """Gets the device_id of this GetMultiDeviceIndicatorOutput.  # noqa: E501


        :return: The device_id of this GetMultiDeviceIndicatorOutput.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this GetMultiDeviceIndicatorOutput.


        :param device_id: The device_id of this GetMultiDeviceIndicatorOutput.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def indicators(self):
        """Gets the indicators of this GetMultiDeviceIndicatorOutput.  # noqa: E501


        :return: The indicators of this GetMultiDeviceIndicatorOutput.  # noqa: E501
        :rtype: list[DeviceIndicatorOutput]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this GetMultiDeviceIndicatorOutput.


        :param indicators: The indicators of this GetMultiDeviceIndicatorOutput.  # noqa: E501
        :type: list[DeviceIndicatorOutput]
        """

        self._indicators = indicators

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
        if not isinstance(other, GetMultiDeviceIndicatorOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetMultiDeviceIndicatorOutput):
            return True

        return self.to_dict() != other.to_dict()
