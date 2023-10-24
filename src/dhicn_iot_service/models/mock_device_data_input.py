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


class MockDeviceDataInput(object):
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
        'tenant_id': 'str',
        'devices': 'list[MockDeviceInfoInput]'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'devices': 'devices'
    }

    def __init__(self, tenant_id=None, devices=None, local_vars_configuration=None):  # noqa: E501
        """MockDeviceDataInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tenant_id = None
        self._devices = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.devices = devices

    @property
    def tenant_id(self):
        """Gets the tenant_id of this MockDeviceDataInput.  # noqa: E501

        租户Id  # noqa: E501

        :return: The tenant_id of this MockDeviceDataInput.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this MockDeviceDataInput.

        租户Id  # noqa: E501

        :param tenant_id: The tenant_id of this MockDeviceDataInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def devices(self):
        """Gets the devices of this MockDeviceDataInput.  # noqa: E501

        设备信息  # noqa: E501

        :return: The devices of this MockDeviceDataInput.  # noqa: E501
        :rtype: list[MockDeviceInfoInput]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this MockDeviceDataInput.

        设备信息  # noqa: E501

        :param devices: The devices of this MockDeviceDataInput.  # noqa: E501
        :type: list[MockDeviceInfoInput]
        """
        if self.local_vars_configuration.client_side_validation and devices is None:  # noqa: E501
            raise ValueError("Invalid value for `devices`, must not be `None`")  # noqa: E501

        self._devices = devices

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
        if not isinstance(other, MockDeviceDataInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MockDeviceDataInput):
            return True

        return self.to_dict() != other.to_dict()
