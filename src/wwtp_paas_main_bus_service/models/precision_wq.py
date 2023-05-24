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


class PrecisionWq(object):
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
        'display_msg': 'str',
        'max_value': 'float',
        'min_value': 'float',
        'average_value': 'float',
        'deviation_value': 'float',
        'ts_data': 'list[TsPair1]'
    }

    attribute_map = {
        'code': 'code',
        'display_msg': 'displayMsg',
        'max_value': 'maxValue',
        'min_value': 'minValue',
        'average_value': 'averageValue',
        'deviation_value': 'deviationValue',
        'ts_data': 'tsData'
    }

    def __init__(self, code=None, display_msg=None, max_value=None, min_value=None, average_value=None, deviation_value=None, ts_data=None, local_vars_configuration=None):  # noqa: E501
        """PrecisionWq - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._display_msg = None
        self._max_value = None
        self._min_value = None
        self._average_value = None
        self._deviation_value = None
        self._ts_data = None
        self.discriminator = None

        self.code = code
        self.display_msg = display_msg
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if average_value is not None:
            self.average_value = average_value
        if deviation_value is not None:
            self.deviation_value = deviation_value
        self.ts_data = ts_data

    @property
    def code(self):
        """Gets the code of this PrecisionWq.  # noqa: E501

        指标 indicator code  # noqa: E501

        :return: The code of this PrecisionWq.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PrecisionWq.

        指标 indicator code  # noqa: E501

        :param code: The code of this PrecisionWq.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def display_msg(self):
        """Gets the display_msg of this PrecisionWq.  # noqa: E501

        展示信息 display message  # noqa: E501

        :return: The display_msg of this PrecisionWq.  # noqa: E501
        :rtype: str
        """
        return self._display_msg

    @display_msg.setter
    def display_msg(self, display_msg):
        """Sets the display_msg of this PrecisionWq.

        展示信息 display message  # noqa: E501

        :param display_msg: The display_msg of this PrecisionWq.  # noqa: E501
        :type: str
        """

        self._display_msg = display_msg

    @property
    def max_value(self):
        """Gets the max_value of this PrecisionWq.  # noqa: E501

        最大值 maximum value  # noqa: E501

        :return: The max_value of this PrecisionWq.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this PrecisionWq.

        最大值 maximum value  # noqa: E501

        :param max_value: The max_value of this PrecisionWq.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this PrecisionWq.  # noqa: E501

        最小值 minimum value  # noqa: E501

        :return: The min_value of this PrecisionWq.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this PrecisionWq.

        最小值 minimum value  # noqa: E501

        :param min_value: The min_value of this PrecisionWq.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def average_value(self):
        """Gets the average_value of this PrecisionWq.  # noqa: E501

        平均值 average value  # noqa: E501

        :return: The average_value of this PrecisionWq.  # noqa: E501
        :rtype: float
        """
        return self._average_value

    @average_value.setter
    def average_value(self, average_value):
        """Sets the average_value of this PrecisionWq.

        平均值 average value  # noqa: E501

        :param average_value: The average_value of this PrecisionWq.  # noqa: E501
        :type: float
        """

        self._average_value = average_value

    @property
    def deviation_value(self):
        """Gets the deviation_value of this PrecisionWq.  # noqa: E501

        差值 difference value  # noqa: E501

        :return: The deviation_value of this PrecisionWq.  # noqa: E501
        :rtype: float
        """
        return self._deviation_value

    @deviation_value.setter
    def deviation_value(self, deviation_value):
        """Sets the deviation_value of this PrecisionWq.

        差值 difference value  # noqa: E501

        :param deviation_value: The deviation_value of this PrecisionWq.  # noqa: E501
        :type: float
        """

        self._deviation_value = deviation_value

    @property
    def ts_data(self):
        """Gets the ts_data of this PrecisionWq.  # noqa: E501

        时间序列值 time-series data  # noqa: E501

        :return: The ts_data of this PrecisionWq.  # noqa: E501
        :rtype: list[TsPair1]
        """
        return self._ts_data

    @ts_data.setter
    def ts_data(self, ts_data):
        """Sets the ts_data of this PrecisionWq.

        时间序列值 time-series data  # noqa: E501

        :param ts_data: The ts_data of this PrecisionWq.  # noqa: E501
        :type: list[TsPair1]
        """

        self._ts_data = ts_data

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
        if not isinstance(other, PrecisionWq):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrecisionWq):
            return True

        return self.to_dict() != other.to_dict()
