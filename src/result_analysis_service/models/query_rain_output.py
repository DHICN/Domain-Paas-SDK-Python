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


class QueryRainOutput(object):
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
        'rain_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'measure_rainfall': 'float',
        'forecast_rainfall': 'float',
        'status': 'RainfallStatusEnum',
        'scenarios': 'list[str]'
    }

    attribute_map = {
        'rain_id': 'rainId',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'measure_rainfall': 'measureRainfall',
        'forecast_rainfall': 'forecastRainfall',
        'status': 'status',
        'scenarios': 'scenarios'
    }

    def __init__(self, rain_id=None, start_time=None, end_time=None, measure_rainfall=None, forecast_rainfall=None, status=None, scenarios=None, local_vars_configuration=None):  # noqa: E501
        """QueryRainOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rain_id = None
        self._start_time = None
        self._end_time = None
        self._measure_rainfall = None
        self._forecast_rainfall = None
        self._status = None
        self._scenarios = None
        self.discriminator = None

        if rain_id is not None:
            self.rain_id = rain_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if measure_rainfall is not None:
            self.measure_rainfall = measure_rainfall
        if forecast_rainfall is not None:
            self.forecast_rainfall = forecast_rainfall
        if status is not None:
            self.status = status
        self.scenarios = scenarios

    @property
    def rain_id(self):
        """Gets the rain_id of this QueryRainOutput.  # noqa: E501

        降雨记录的ID rain id  # noqa: E501

        :return: The rain_id of this QueryRainOutput.  # noqa: E501
        :rtype: str
        """
        return self._rain_id

    @rain_id.setter
    def rain_id(self, rain_id):
        """Sets the rain_id of this QueryRainOutput.

        降雨记录的ID rain id  # noqa: E501

        :param rain_id: The rain_id of this QueryRainOutput.  # noqa: E501
        :type: str
        """

        self._rain_id = rain_id

    @property
    def start_time(self):
        """Gets the start_time of this QueryRainOutput.  # noqa: E501

        降雨记录的开始时间 rainfall start time  # noqa: E501

        :return: The start_time of this QueryRainOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryRainOutput.

        降雨记录的开始时间 rainfall start time  # noqa: E501

        :param start_time: The start_time of this QueryRainOutput.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryRainOutput.  # noqa: E501

        降雨记录的结束时间 rainfall end time  # noqa: E501

        :return: The end_time of this QueryRainOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryRainOutput.

        降雨记录的结束时间 rainfall end time  # noqa: E501

        :param end_time: The end_time of this QueryRainOutput.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def measure_rainfall(self):
        """Gets the measure_rainfall of this QueryRainOutput.  # noqa: E501

        实测总降雨量 measured total rainfall  # noqa: E501

        :return: The measure_rainfall of this QueryRainOutput.  # noqa: E501
        :rtype: float
        """
        return self._measure_rainfall

    @measure_rainfall.setter
    def measure_rainfall(self, measure_rainfall):
        """Sets the measure_rainfall of this QueryRainOutput.

        实测总降雨量 measured total rainfall  # noqa: E501

        :param measure_rainfall: The measure_rainfall of this QueryRainOutput.  # noqa: E501
        :type: float
        """

        self._measure_rainfall = measure_rainfall

    @property
    def forecast_rainfall(self):
        """Gets the forecast_rainfall of this QueryRainOutput.  # noqa: E501

        预报总降雨量 forecast total rainfall  # noqa: E501

        :return: The forecast_rainfall of this QueryRainOutput.  # noqa: E501
        :rtype: float
        """
        return self._forecast_rainfall

    @forecast_rainfall.setter
    def forecast_rainfall(self, forecast_rainfall):
        """Sets the forecast_rainfall of this QueryRainOutput.

        预报总降雨量 forecast total rainfall  # noqa: E501

        :param forecast_rainfall: The forecast_rainfall of this QueryRainOutput.  # noqa: E501
        :type: float
        """

        self._forecast_rainfall = forecast_rainfall

    @property
    def status(self):
        """Gets the status of this QueryRainOutput.  # noqa: E501


        :return: The status of this QueryRainOutput.  # noqa: E501
        :rtype: RainfallStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryRainOutput.


        :param status: The status of this QueryRainOutput.  # noqa: E501
        :type: RainfallStatusEnum
        """

        self._status = status

    @property
    def scenarios(self):
        """Gets the scenarios of this QueryRainOutput.  # noqa: E501

        与降雨记录关联的方案ID列表 scenarios associated with this rainfall  # noqa: E501

        :return: The scenarios of this QueryRainOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._scenarios

    @scenarios.setter
    def scenarios(self, scenarios):
        """Sets the scenarios of this QueryRainOutput.

        与降雨记录关联的方案ID列表 scenarios associated with this rainfall  # noqa: E501

        :param scenarios: The scenarios of this QueryRainOutput.  # noqa: E501
        :type: list[str]
        """

        self._scenarios = scenarios

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
        if not isinstance(other, QueryRainOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryRainOutput):
            return True

        return self.to_dict() != other.to_dict()