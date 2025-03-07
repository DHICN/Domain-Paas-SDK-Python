# coding: utf-8

"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_zyws_service.configuration import Configuration


class ControlDeviceTsDetails(object):
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
        'create_time': 'datetime',
        'device_code': 'str',
        'is_intelligence': 'bool',
        'value': 'float',
        'indicator': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'device_code': 'deviceCode',
        'is_intelligence': 'isIntelligence',
        'value': 'value',
        'indicator': 'indicator'
    }

    def __init__(self, create_time=None, device_code=None, is_intelligence=None, value=None, indicator=None, local_vars_configuration=None):  # noqa: E501
        """ControlDeviceTsDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._create_time = None
        self._device_code = None
        self._is_intelligence = None
        self._value = None
        self._indicator = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        self.device_code = device_code
        if is_intelligence is not None:
            self.is_intelligence = is_intelligence
        if value is not None:
            self.value = value
        self.indicator = indicator

    @property
    def create_time(self):
        """Gets the create_time of this ControlDeviceTsDetails.  # noqa: E501


        :return: The create_time of this ControlDeviceTsDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ControlDeviceTsDetails.


        :param create_time: The create_time of this ControlDeviceTsDetails.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def device_code(self):
        """Gets the device_code of this ControlDeviceTsDetails.  # noqa: E501


        :return: The device_code of this ControlDeviceTsDetails.  # noqa: E501
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        """Sets the device_code of this ControlDeviceTsDetails.


        :param device_code: The device_code of this ControlDeviceTsDetails.  # noqa: E501
        :type: str
        """

        self._device_code = device_code

    @property
    def is_intelligence(self):
        """Gets the is_intelligence of this ControlDeviceTsDetails.  # noqa: E501


        :return: The is_intelligence of this ControlDeviceTsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_intelligence

    @is_intelligence.setter
    def is_intelligence(self, is_intelligence):
        """Sets the is_intelligence of this ControlDeviceTsDetails.


        :param is_intelligence: The is_intelligence of this ControlDeviceTsDetails.  # noqa: E501
        :type: bool
        """

        self._is_intelligence = is_intelligence

    @property
    def value(self):
        """Gets the value of this ControlDeviceTsDetails.  # noqa: E501


        :return: The value of this ControlDeviceTsDetails.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ControlDeviceTsDetails.


        :param value: The value of this ControlDeviceTsDetails.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def indicator(self):
        """Gets the indicator of this ControlDeviceTsDetails.  # noqa: E501


        :return: The indicator of this ControlDeviceTsDetails.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this ControlDeviceTsDetails.


        :param indicator: The indicator of this ControlDeviceTsDetails.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, ControlDeviceTsDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlDeviceTsDetails):
            return True

        return self.to_dict() != other.to_dict()
