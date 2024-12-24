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


class TimeSpan(object):
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
        'ticks': 'int',
        'days': 'int',
        'hours': 'int',
        'milliseconds': 'int',
        'microseconds': 'int',
        'nanoseconds': 'int',
        'minutes': 'int',
        'seconds': 'int',
        'total_days': 'float',
        'total_hours': 'float',
        'total_milliseconds': 'float',
        'total_microseconds': 'float',
        'total_nanoseconds': 'float',
        'total_minutes': 'float',
        'total_seconds': 'float'
    }

    attribute_map = {
        'ticks': 'ticks',
        'days': 'days',
        'hours': 'hours',
        'milliseconds': 'milliseconds',
        'microseconds': 'microseconds',
        'nanoseconds': 'nanoseconds',
        'minutes': 'minutes',
        'seconds': 'seconds',
        'total_days': 'totalDays',
        'total_hours': 'totalHours',
        'total_milliseconds': 'totalMilliseconds',
        'total_microseconds': 'totalMicroseconds',
        'total_nanoseconds': 'totalNanoseconds',
        'total_minutes': 'totalMinutes',
        'total_seconds': 'totalSeconds'
    }

    def __init__(self, ticks=None, days=None, hours=None, milliseconds=None, microseconds=None, nanoseconds=None, minutes=None, seconds=None, total_days=None, total_hours=None, total_milliseconds=None, total_microseconds=None, total_nanoseconds=None, total_minutes=None, total_seconds=None, local_vars_configuration=None):  # noqa: E501
        """TimeSpan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ticks = None
        self._days = None
        self._hours = None
        self._milliseconds = None
        self._microseconds = None
        self._nanoseconds = None
        self._minutes = None
        self._seconds = None
        self._total_days = None
        self._total_hours = None
        self._total_milliseconds = None
        self._total_microseconds = None
        self._total_nanoseconds = None
        self._total_minutes = None
        self._total_seconds = None
        self.discriminator = None

        if ticks is not None:
            self.ticks = ticks
        if days is not None:
            self.days = days
        if hours is not None:
            self.hours = hours
        if milliseconds is not None:
            self.milliseconds = milliseconds
        if microseconds is not None:
            self.microseconds = microseconds
        if nanoseconds is not None:
            self.nanoseconds = nanoseconds
        if minutes is not None:
            self.minutes = minutes
        if seconds is not None:
            self.seconds = seconds
        if total_days is not None:
            self.total_days = total_days
        if total_hours is not None:
            self.total_hours = total_hours
        if total_milliseconds is not None:
            self.total_milliseconds = total_milliseconds
        if total_microseconds is not None:
            self.total_microseconds = total_microseconds
        if total_nanoseconds is not None:
            self.total_nanoseconds = total_nanoseconds
        if total_minutes is not None:
            self.total_minutes = total_minutes
        if total_seconds is not None:
            self.total_seconds = total_seconds

    @property
    def ticks(self):
        """Gets the ticks of this TimeSpan.  # noqa: E501


        :return: The ticks of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._ticks

    @ticks.setter
    def ticks(self, ticks):
        """Sets the ticks of this TimeSpan.


        :param ticks: The ticks of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._ticks = ticks

    @property
    def days(self):
        """Gets the days of this TimeSpan.  # noqa: E501


        :return: The days of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this TimeSpan.


        :param days: The days of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._days = days

    @property
    def hours(self):
        """Gets the hours of this TimeSpan.  # noqa: E501


        :return: The hours of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this TimeSpan.


        :param hours: The hours of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._hours = hours

    @property
    def milliseconds(self):
        """Gets the milliseconds of this TimeSpan.  # noqa: E501


        :return: The milliseconds of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._milliseconds

    @milliseconds.setter
    def milliseconds(self, milliseconds):
        """Sets the milliseconds of this TimeSpan.


        :param milliseconds: The milliseconds of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._milliseconds = milliseconds

    @property
    def microseconds(self):
        """Gets the microseconds of this TimeSpan.  # noqa: E501


        :return: The microseconds of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._microseconds

    @microseconds.setter
    def microseconds(self, microseconds):
        """Sets the microseconds of this TimeSpan.


        :param microseconds: The microseconds of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._microseconds = microseconds

    @property
    def nanoseconds(self):
        """Gets the nanoseconds of this TimeSpan.  # noqa: E501


        :return: The nanoseconds of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._nanoseconds

    @nanoseconds.setter
    def nanoseconds(self, nanoseconds):
        """Sets the nanoseconds of this TimeSpan.


        :param nanoseconds: The nanoseconds of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._nanoseconds = nanoseconds

    @property
    def minutes(self):
        """Gets the minutes of this TimeSpan.  # noqa: E501


        :return: The minutes of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this TimeSpan.


        :param minutes: The minutes of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._minutes = minutes

    @property
    def seconds(self):
        """Gets the seconds of this TimeSpan.  # noqa: E501


        :return: The seconds of this TimeSpan.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this TimeSpan.


        :param seconds: The seconds of this TimeSpan.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

    @property
    def total_days(self):
        """Gets the total_days of this TimeSpan.  # noqa: E501


        :return: The total_days of this TimeSpan.  # noqa: E501
        :rtype: float
        """
        return self._total_days

    @total_days.setter
    def total_days(self, total_days):
        """Sets the total_days of this TimeSpan.


        :param total_days: The total_days of this TimeSpan.  # noqa: E501
        :type: float
        """

        self._total_days = total_days

    @property
    def total_hours(self):
        """Gets the total_hours of this TimeSpan.  # noqa: E501


        :return: The total_hours of this TimeSpan.  # noqa: E501
        :rtype: float
        """
        return self._total_hours

    @total_hours.setter
    def total_hours(self, total_hours):
        """Sets the total_hours of this TimeSpan.


        :param total_hours: The total_hours of this TimeSpan.  # noqa: E501
        :type: float
        """

        self._total_hours = total_hours

    @property
    def total_milliseconds(self):
        """Gets the total_milliseconds of this TimeSpan.  # noqa: E501


        :return: The total_milliseconds of this TimeSpan.  # noqa: E501
        :rtype: float
        """
        return self._total_milliseconds

    @total_milliseconds.setter
    def total_milliseconds(self, total_milliseconds):
        """Sets the total_milliseconds of this TimeSpan.


        :param total_milliseconds: The total_milliseconds of this TimeSpan.  # noqa: E501
        :type: float
        """

        self._total_milliseconds = total_milliseconds

    @property
    def total_microseconds(self):
        """Gets the total_microseconds of this TimeSpan.  # noqa: E501


        :return: The total_microseconds of this TimeSpan.  # noqa: E501
        :rtype: float
        """
        return self._total_microseconds

    @total_microseconds.setter
    def total_microseconds(self, total_microseconds):
        """Sets the total_microseconds of this TimeSpan.


        :param total_microseconds: The total_microseconds of this TimeSpan.  # noqa: E501
        :type: float
        """

        self._total_microseconds = total_microseconds

    @property
    def total_nanoseconds(self):
        """Gets the total_nanoseconds of this TimeSpan.  # noqa: E501


        :return: The total_nanoseconds of this TimeSpan.  # noqa: E501
        :rtype: float
        """
        return self._total_nanoseconds

    @total_nanoseconds.setter
    def total_nanoseconds(self, total_nanoseconds):
        """Sets the total_nanoseconds of this TimeSpan.


        :param total_nanoseconds: The total_nanoseconds of this TimeSpan.  # noqa: E501
        :type: float
        """

        self._total_nanoseconds = total_nanoseconds

    @property
    def total_minutes(self):
        """Gets the total_minutes of this TimeSpan.  # noqa: E501


        :return: The total_minutes of this TimeSpan.  # noqa: E501
        :rtype: float
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this TimeSpan.


        :param total_minutes: The total_minutes of this TimeSpan.  # noqa: E501
        :type: float
        """

        self._total_minutes = total_minutes

    @property
    def total_seconds(self):
        """Gets the total_seconds of this TimeSpan.  # noqa: E501


        :return: The total_seconds of this TimeSpan.  # noqa: E501
        :rtype: float
        """
        return self._total_seconds

    @total_seconds.setter
    def total_seconds(self, total_seconds):
        """Sets the total_seconds of this TimeSpan.


        :param total_seconds: The total_seconds of this TimeSpan.  # noqa: E501
        :type: float
        """

        self._total_seconds = total_seconds

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
        if not isinstance(other, TimeSpan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeSpan):
            return True

        return self.to_dict() != other.to_dict()
