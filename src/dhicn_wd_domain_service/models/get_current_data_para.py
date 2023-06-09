# coding: utf-8

"""
    wd-domain-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wd_domain_service.configuration import Configuration


class GetCurrentDataPara(object):
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
        'device_indicator_paras': 'list[DeviceIndicatorPara]',
        'real_sync_frequency': 'int'
    }

    attribute_map = {
        'device_indicator_paras': 'deviceIndicatorParas',
        'real_sync_frequency': 'realSyncFrequency'
    }

    def __init__(self, device_indicator_paras=None, real_sync_frequency=None, local_vars_configuration=None):  # noqa: E501
        """GetCurrentDataPara - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_indicator_paras = None
        self._real_sync_frequency = None
        self.discriminator = None

        self.device_indicator_paras = device_indicator_paras
        if real_sync_frequency is not None:
            self.real_sync_frequency = real_sync_frequency

    @property
    def device_indicator_paras(self):
        """Gets the device_indicator_paras of this GetCurrentDataPara.  # noqa: E501

        设备查询参数  # noqa: E501

        :return: The device_indicator_paras of this GetCurrentDataPara.  # noqa: E501
        :rtype: list[DeviceIndicatorPara]
        """
        return self._device_indicator_paras

    @device_indicator_paras.setter
    def device_indicator_paras(self, device_indicator_paras):
        """Sets the device_indicator_paras of this GetCurrentDataPara.

        设备查询参数  # noqa: E501

        :param device_indicator_paras: The device_indicator_paras of this GetCurrentDataPara.  # noqa: E501
        :type: list[DeviceIndicatorPara]
        """

        self._device_indicator_paras = device_indicator_paras

    @property
    def real_sync_frequency(self):
        """Gets the real_sync_frequency of this GetCurrentDataPara.  # noqa: E501

        实测数据同步频率  # noqa: E501

        :return: The real_sync_frequency of this GetCurrentDataPara.  # noqa: E501
        :rtype: int
        """
        return self._real_sync_frequency

    @real_sync_frequency.setter
    def real_sync_frequency(self, real_sync_frequency):
        """Sets the real_sync_frequency of this GetCurrentDataPara.

        实测数据同步频率  # noqa: E501

        :param real_sync_frequency: The real_sync_frequency of this GetCurrentDataPara.  # noqa: E501
        :type: int
        """

        self._real_sync_frequency = real_sync_frequency

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
        if not isinstance(other, GetCurrentDataPara):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCurrentDataPara):
            return True

        return self.to_dict() != other.to_dict()
