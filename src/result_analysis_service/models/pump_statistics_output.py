# coding: utf-8

"""
    result-analysis-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from result_analysis_service.configuration import Configuration


class PumpStatisticsOutput(object):
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
        'pump_id': 'str',
        'acc_discharge': 'float',
        'acc_open_time': 'float'
    }

    attribute_map = {
        'pump_id': 'pumpID',
        'acc_discharge': 'accDischarge',
        'acc_open_time': 'accOpenTime'
    }

    def __init__(self, pump_id=None, acc_discharge=None, acc_open_time=None, local_vars_configuration=None):  # noqa: E501
        """PumpStatisticsOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pump_id = None
        self._acc_discharge = None
        self._acc_open_time = None
        self.discriminator = None

        self.pump_id = pump_id
        if acc_discharge is not None:
            self.acc_discharge = acc_discharge
        if acc_open_time is not None:
            self.acc_open_time = acc_open_time

    @property
    def pump_id(self):
        """Gets the pump_id of this PumpStatisticsOutput.  # noqa: E501

        泵站ID pump id  # noqa: E501

        :return: The pump_id of this PumpStatisticsOutput.  # noqa: E501
        :rtype: str
        """
        return self._pump_id

    @pump_id.setter
    def pump_id(self, pump_id):
        """Sets the pump_id of this PumpStatisticsOutput.

        泵站ID pump id  # noqa: E501

        :param pump_id: The pump_id of this PumpStatisticsOutput.  # noqa: E501
        :type: str
        """

        self._pump_id = pump_id

    @property
    def acc_discharge(self):
        """Gets the acc_discharge of this PumpStatisticsOutput.  # noqa: E501

        累计流量（单位：m3） accumulated discharge (unit: m3)  # noqa: E501

        :return: The acc_discharge of this PumpStatisticsOutput.  # noqa: E501
        :rtype: float
        """
        return self._acc_discharge

    @acc_discharge.setter
    def acc_discharge(self, acc_discharge):
        """Sets the acc_discharge of this PumpStatisticsOutput.

        累计流量（单位：m3） accumulated discharge (unit: m3)  # noqa: E501

        :param acc_discharge: The acc_discharge of this PumpStatisticsOutput.  # noqa: E501
        :type: float
        """

        self._acc_discharge = acc_discharge

    @property
    def acc_open_time(self):
        """Gets the acc_open_time of this PumpStatisticsOutput.  # noqa: E501

        累计开启时长（单位：分钟） accumulated open time(unit: minute)  # noqa: E501

        :return: The acc_open_time of this PumpStatisticsOutput.  # noqa: E501
        :rtype: float
        """
        return self._acc_open_time

    @acc_open_time.setter
    def acc_open_time(self, acc_open_time):
        """Sets the acc_open_time of this PumpStatisticsOutput.

        累计开启时长（单位：分钟） accumulated open time(unit: minute)  # noqa: E501

        :param acc_open_time: The acc_open_time of this PumpStatisticsOutput.  # noqa: E501
        :type: float
        """

        self._acc_open_time = acc_open_time

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
        if not isinstance(other, PumpStatisticsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PumpStatisticsOutput):
            return True

        return self.to_dict() != other.to_dict()
