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

from wwtp_paas_main_bus_service.configuration import Configuration


class QueryIndicatorStatisticOutput(object):
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
        'code': 'str',
        'unit': 'str',
        'mean': 'float',
        'min': 'float',
        'max': 'float',
        'median': 'float',
        'upper_percent': 'float',
        'lower_percent': 'float'
    }

    attribute_map = {
        'code': 'code',
        'unit': 'unit',
        'mean': 'mean',
        'min': 'min',
        'max': 'max',
        'median': 'median',
        'upper_percent': 'upperPercent',
        'lower_percent': 'lowerPercent'
    }

    def __init__(self, code=None, unit=None, mean=None, min=None, max=None, median=None, upper_percent=None, lower_percent=None, local_vars_configuration=None):  # noqa: E501
        """QueryIndicatorStatisticOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._unit = None
        self._mean = None
        self._min = None
        self._max = None
        self._median = None
        self._upper_percent = None
        self._lower_percent = None
        self.discriminator = None

        self.code = code
        self.unit = unit
        if mean is not None:
            self.mean = mean
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if median is not None:
            self.median = median
        if upper_percent is not None:
            self.upper_percent = upper_percent
        if lower_percent is not None:
            self.lower_percent = lower_percent

    @property
    def code(self):
        """Gets the code of this QueryIndicatorStatisticOutput.  # noqa: E501

        指标代码 indicator code  # noqa: E501

        :return: The code of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this QueryIndicatorStatisticOutput.

        指标代码 indicator code  # noqa: E501

        :param code: The code of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def unit(self):
        """Gets the unit of this QueryIndicatorStatisticOutput.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this QueryIndicatorStatisticOutput.

        单位 unit  # noqa: E501

        :param unit: The unit of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def mean(self):
        """Gets the mean of this QueryIndicatorStatisticOutput.  # noqa: E501

        平均值 average value  # noqa: E501

        :return: The mean of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this QueryIndicatorStatisticOutput.

        平均值 average value  # noqa: E501

        :param mean: The mean of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: float
        """

        self._mean = mean

    @property
    def min(self):
        """Gets the min of this QueryIndicatorStatisticOutput.  # noqa: E501

        最小值 minimum value  # noqa: E501

        :return: The min of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this QueryIndicatorStatisticOutput.

        最小值 minimum value  # noqa: E501

        :param min: The min of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this QueryIndicatorStatisticOutput.  # noqa: E501

        最大值 maximum value  # noqa: E501

        :return: The max of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this QueryIndicatorStatisticOutput.

        最大值 maximum value  # noqa: E501

        :param max: The max of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def median(self):
        """Gets the median of this QueryIndicatorStatisticOutput.  # noqa: E501

        中位数 median value  # noqa: E501

        :return: The median of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this QueryIndicatorStatisticOutput.

        中位数 median value  # noqa: E501

        :param median: The median of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: float
        """

        self._median = median

    @property
    def upper_percent(self):
        """Gets the upper_percent of this QueryIndicatorStatisticOutput.  # noqa: E501

        上百分位 upper percentile  # noqa: E501

        :return: The upper_percent of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._upper_percent

    @upper_percent.setter
    def upper_percent(self, upper_percent):
        """Sets the upper_percent of this QueryIndicatorStatisticOutput.

        上百分位 upper percentile  # noqa: E501

        :param upper_percent: The upper_percent of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: float
        """

        self._upper_percent = upper_percent

    @property
    def lower_percent(self):
        """Gets the lower_percent of this QueryIndicatorStatisticOutput.  # noqa: E501

        下百分位 lower percentile  # noqa: E501

        :return: The lower_percent of this QueryIndicatorStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._lower_percent

    @lower_percent.setter
    def lower_percent(self, lower_percent):
        """Sets the lower_percent of this QueryIndicatorStatisticOutput.

        下百分位 lower percentile  # noqa: E501

        :param lower_percent: The lower_percent of this QueryIndicatorStatisticOutput.  # noqa: E501
        :type: float
        """

        self._lower_percent = lower_percent

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
        if not isinstance(other, QueryIndicatorStatisticOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryIndicatorStatisticOutput):
            return True

        return self.to_dict() != other.to_dict()
