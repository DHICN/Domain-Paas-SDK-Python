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


class DeleteDevicesInput(object):
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
        'device_ids': 'list[str]'
    }

    attribute_map = {
        'device_ids': 'deviceIds'
    }

    def __init__(self, device_ids=None, local_vars_configuration=None):  # noqa: E501
        """DeleteDevicesInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_ids = None
        self.discriminator = None

        self.device_ids = device_ids

    @property
    def device_ids(self):
        """Gets the device_ids of this DeleteDevicesInput.  # noqa: E501

        设备Id列表 device ids  # noqa: E501

        :return: The device_ids of this DeleteDevicesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this DeleteDevicesInput.

        设备Id列表 device ids  # noqa: E501

        :param device_ids: The device_ids of this DeleteDevicesInput.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and device_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `device_ids`, must not be `None`")  # noqa: E501

        self._device_ids = device_ids

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
        if not isinstance(other, DeleteDevicesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteDevicesInput):
            return True

        return self.to_dict() != other.to_dict()
