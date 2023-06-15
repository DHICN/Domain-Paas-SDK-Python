# coding: utf-8

"""
    wwtp-paas-main-bus-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wwtp_data_bus_service.configuration import Configuration


class GetStatisticResultDto(object):
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
        'statistic_code': 'str',
        'time': 'datetime',
        'value': 'float'
    }

    attribute_map = {
        'statistic_code': 'statisticCode',
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, statistic_code=None, time=None, value=None, local_vars_configuration=None):  # noqa: E501
        """GetStatisticResultDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._statistic_code = None
        self._time = None
        self._value = None
        self.discriminator = None

        self.statistic_code = statistic_code
        if time is not None:
            self.time = time
        if value is not None:
            self.value = value

    @property
    def statistic_code(self):
        """Gets the statistic_code of this GetStatisticResultDto.  # noqa: E501

        统计码  # noqa: E501

        :return: The statistic_code of this GetStatisticResultDto.  # noqa: E501
        :rtype: str
        """
        return self._statistic_code

    @statistic_code.setter
    def statistic_code(self, statistic_code):
        """Sets the statistic_code of this GetStatisticResultDto.

        统计码  # noqa: E501

        :param statistic_code: The statistic_code of this GetStatisticResultDto.  # noqa: E501
        :type: str
        """

        self._statistic_code = statistic_code

    @property
    def time(self):
        """Gets the time of this GetStatisticResultDto.  # noqa: E501

        时间  # noqa: E501

        :return: The time of this GetStatisticResultDto.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this GetStatisticResultDto.

        时间  # noqa: E501

        :param time: The time of this GetStatisticResultDto.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def value(self):
        """Gets the value of this GetStatisticResultDto.  # noqa: E501

        值  # noqa: E501

        :return: The value of this GetStatisticResultDto.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetStatisticResultDto.

        值  # noqa: E501

        :param value: The value of this GetStatisticResultDto.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if not isinstance(other, GetStatisticResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetStatisticResultDto):
            return True

        return self.to_dict() != other.to_dict()
