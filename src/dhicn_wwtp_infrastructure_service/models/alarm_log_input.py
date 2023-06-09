# coding: utf-8

"""
    wwtp-paas-infrastructure-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wwtp_infrastructure_service.configuration import Configuration


class AlarmLogInput(object):
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
        'start_time': 'datetime',
        'end_time': 'datetime',
        'alarm_types': 'list[int]',
        'is_national_standard': 'bool'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'alarm_types': 'alarmTypes',
        'is_national_standard': 'isNationalStandard'
    }

    def __init__(self, start_time=None, end_time=None, alarm_types=None, is_national_standard=None, local_vars_configuration=None):  # noqa: E501
        """AlarmLogInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_time = None
        self._end_time = None
        self._alarm_types = None
        self._is_national_standard = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.alarm_types = alarm_types
        self.is_national_standard = is_national_standard

    @property
    def start_time(self):
        """Gets the start_time of this AlarmLogInput.  # noqa: E501

        开始时间 start time  # noqa: E501

        :return: The start_time of this AlarmLogInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AlarmLogInput.

        开始时间 start time  # noqa: E501

        :param start_time: The start_time of this AlarmLogInput.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AlarmLogInput.  # noqa: E501

        结束时间 end time  # noqa: E501

        :return: The end_time of this AlarmLogInput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AlarmLogInput.

        结束时间 end time  # noqa: E501

        :param end_time: The end_time of this AlarmLogInput.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def alarm_types(self):
        """Gets the alarm_types of this AlarmLogInput.  # noqa: E501

        消息类型 alarm type  # noqa: E501

        :return: The alarm_types of this AlarmLogInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._alarm_types

    @alarm_types.setter
    def alarm_types(self, alarm_types):
        """Sets the alarm_types of this AlarmLogInput.

        消息类型 alarm type  # noqa: E501

        :param alarm_types: The alarm_types of this AlarmLogInput.  # noqa: E501
        :type: list[int]
        """
        allowed_values = [None,0, 1, 2]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(alarm_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `alarm_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(alarm_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._alarm_types = alarm_types

    @property
    def is_national_standard(self):
        """Gets the is_national_standard of this AlarmLogInput.  # noqa: E501

        是否获取国标 true indicates grade=1, and false indicates grade!=1  # noqa: E501

        :return: The is_national_standard of this AlarmLogInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_national_standard

    @is_national_standard.setter
    def is_national_standard(self, is_national_standard):
        """Sets the is_national_standard of this AlarmLogInput.

        是否获取国标 true indicates grade=1, and false indicates grade!=1  # noqa: E501

        :param is_national_standard: The is_national_standard of this AlarmLogInput.  # noqa: E501
        :type: bool
        """

        self._is_national_standard = is_national_standard

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
        if not isinstance(other, AlarmLogInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlarmLogInput):
            return True

        return self.to_dict() != other.to_dict()
