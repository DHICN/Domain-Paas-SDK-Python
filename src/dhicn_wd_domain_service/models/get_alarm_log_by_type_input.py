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


class GetAlarmLogByTypeInput(object):
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
        'alarm_data_type': 'list[int]'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'alarm_data_type': 'alarmDataType'
    }

    def __init__(self, start_time=None, end_time=None, alarm_data_type=None, local_vars_configuration=None):  # noqa: E501
        """GetAlarmLogByTypeInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_time = None
        self._end_time = None
        self._alarm_data_type = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.alarm_data_type = alarm_data_type

    @property
    def start_time(self):
        """Gets the start_time of this GetAlarmLogByTypeInput.  # noqa: E501

        开始时间  # noqa: E501

        :return: The start_time of this GetAlarmLogByTypeInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GetAlarmLogByTypeInput.

        开始时间  # noqa: E501

        :param start_time: The start_time of this GetAlarmLogByTypeInput.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this GetAlarmLogByTypeInput.  # noqa: E501

        结束时间  # noqa: E501

        :return: The end_time of this GetAlarmLogByTypeInput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GetAlarmLogByTypeInput.

        结束时间  # noqa: E501

        :param end_time: The end_time of this GetAlarmLogByTypeInput.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def alarm_data_type(self):
        """Gets the alarm_data_type of this GetAlarmLogByTypeInput.  # noqa: E501

        报警数据类型  # noqa: E501

        :return: The alarm_data_type of this GetAlarmLogByTypeInput.  # noqa: E501
        :rtype: list[int]
        """
        return self._alarm_data_type

    @alarm_data_type.setter
    def alarm_data_type(self, alarm_data_type):
        """Sets the alarm_data_type of this GetAlarmLogByTypeInput.

        报警数据类型  # noqa: E501

        :param alarm_data_type: The alarm_data_type of this GetAlarmLogByTypeInput.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and alarm_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alarm_data_type`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1, 2, 3, 4, 5]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(alarm_data_type).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `alarm_data_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(alarm_data_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._alarm_data_type = alarm_data_type

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
        if not isinstance(other, GetAlarmLogByTypeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAlarmLogByTypeInput):
            return True

        return self.to_dict() != other.to_dict()
