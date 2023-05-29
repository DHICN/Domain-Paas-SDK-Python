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

from wd_service_domain.configuration import Configuration


class SaveAlarmConfigByTypeInput(object):
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
        'alarm_data_type': 'int',
        'alarm_policy': 'int',
        'max': 'float',
        'min': 'float',
        'threshold': 'float'
    }

    attribute_map = {
        'alarm_data_type': 'alarmDataType',
        'alarm_policy': 'alarmPolicy',
        'max': 'max',
        'min': 'min',
        'threshold': 'threshold'
    }

    def __init__(self, alarm_data_type=None, alarm_policy=None, max=None, min=None, threshold=None, local_vars_configuration=None):  # noqa: E501
        """SaveAlarmConfigByTypeInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alarm_data_type = None
        self._alarm_policy = None
        self._max = None
        self._min = None
        self._threshold = None
        self.discriminator = None

        self.alarm_data_type = alarm_data_type
        if alarm_policy is not None:
            self.alarm_policy = alarm_policy
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if threshold is not None:
            self.threshold = threshold

    @property
    def alarm_data_type(self):
        """Gets the alarm_data_type of this SaveAlarmConfigByTypeInput.  # noqa: E501

        0-Pressure(压力) 1-Flow(流量) 2-Velocity(流速) 3-NodeWaterQuality(节点水质) 4-PipeWaterQuality(管线水质) 5-Waterlevel(水位)   # noqa: E501

        :return: The alarm_data_type of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :rtype: int
        """
        return self._alarm_data_type

    @alarm_data_type.setter
    def alarm_data_type(self, alarm_data_type):
        """Sets the alarm_data_type of this SaveAlarmConfigByTypeInput.

        0-Pressure(压力) 1-Flow(流量) 2-Velocity(流速) 3-NodeWaterQuality(节点水质) 4-PipeWaterQuality(管线水质) 5-Waterlevel(水位)   # noqa: E501

        :param alarm_data_type: The alarm_data_type of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and alarm_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alarm_data_type`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1, 2, 3, 4, 5]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and alarm_data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `alarm_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(alarm_data_type, allowed_values)
            )

        self._alarm_data_type = alarm_data_type

    @property
    def alarm_policy(self):
        """Gets the alarm_policy of this SaveAlarmConfigByTypeInput.  # noqa: E501

        报警策略（0阈值、1范围值报警）  # noqa: E501

        :return: The alarm_policy of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :rtype: int
        """
        return self._alarm_policy

    @alarm_policy.setter
    def alarm_policy(self, alarm_policy):
        """Sets the alarm_policy of this SaveAlarmConfigByTypeInput.

        报警策略（0阈值、1范围值报警）  # noqa: E501

        :param alarm_policy: The alarm_policy of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :type: int
        """

        self._alarm_policy = alarm_policy

    @property
    def max(self):
        """Gets the max of this SaveAlarmConfigByTypeInput.  # noqa: E501

        最大值  # noqa: E501

        :return: The max of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this SaveAlarmConfigByTypeInput.

        最大值  # noqa: E501

        :param max: The max of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this SaveAlarmConfigByTypeInput.  # noqa: E501

        最小值  # noqa: E501

        :return: The min of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this SaveAlarmConfigByTypeInput.

        最小值  # noqa: E501

        :param min: The min of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def threshold(self):
        """Gets the threshold of this SaveAlarmConfigByTypeInput.  # noqa: E501

        差值阈值（实测-模拟）  # noqa: E501

        :return: The threshold of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this SaveAlarmConfigByTypeInput.

        差值阈值（实测-模拟）  # noqa: E501

        :param threshold: The threshold of this SaveAlarmConfigByTypeInput.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

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
        if not isinstance(other, SaveAlarmConfigByTypeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SaveAlarmConfigByTypeInput):
            return True

        return self.to_dict() != other.to_dict()
