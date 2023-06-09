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


class StatisticInfo(object):
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
        'statistic_type': 'int',
        'ts': 'TsPairs'
    }

    attribute_map = {
        'statistic_type': 'statisticType',
        'ts': 'ts'
    }

    def __init__(self, statistic_type=None, ts=None, local_vars_configuration=None):  # noqa: E501
        """StatisticInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._statistic_type = None
        self._ts = None
        self.discriminator = None

        if statistic_type is not None:
            self.statistic_type = statistic_type
        if ts is not None:
            self.ts = ts

    @property
    def statistic_type(self):
        """Gets the statistic_type of this StatisticInfo.  # noqa: E501

        0-PressureSafeRate(压力保障率) 1-PressureAvg(平均压力) 2-WaterDemandHourMax(最大小时供水量) 3-WQSafeRate(余氯保障率) 4-WaterDemand(用水量) 5-ForcastDemand(需水量) 6-PressureAccuracy(压力精度) 7-FlowAccuracy(流量精度)   # noqa: E501

        :return: The statistic_type of this StatisticInfo.  # noqa: E501
        :rtype: int
        """
        return self._statistic_type

    @statistic_type.setter
    def statistic_type(self, statistic_type):
        """Sets the statistic_type of this StatisticInfo.

        0-PressureSafeRate(压力保障率) 1-PressureAvg(平均压力) 2-WaterDemandHourMax(最大小时供水量) 3-WQSafeRate(余氯保障率) 4-WaterDemand(用水量) 5-ForcastDemand(需水量) 6-PressureAccuracy(压力精度) 7-FlowAccuracy(流量精度)   # noqa: E501

        :param statistic_type: The statistic_type of this StatisticInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and statistic_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `statistic_type` ({0}), must be one of {1}"  # noqa: E501
                .format(statistic_type, allowed_values)
            )

        self._statistic_type = statistic_type

    @property
    def ts(self):
        """Gets the ts of this StatisticInfo.  # noqa: E501


        :return: The ts of this StatisticInfo.  # noqa: E501
        :rtype: TsPairs
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this StatisticInfo.


        :param ts: The ts of this StatisticInfo.  # noqa: E501
        :type: TsPairs
        """

        self._ts = ts

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
        if not isinstance(other, StatisticInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticInfo):
            return True

        return self.to_dict() != other.to_dict()
