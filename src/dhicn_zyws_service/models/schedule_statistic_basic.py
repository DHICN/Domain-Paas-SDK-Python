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


class ScheduleStatisticBasic(object):
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
        'min': 'float',
        'max': 'float',
        'value': 'float'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'value': 'value'
    }

    def __init__(self, min=None, max=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleStatisticBasic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._min = None
        self._max = None
        self._value = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if value is not None:
            self.value = value

    @property
    def min(self):
        """Gets the min of this ScheduleStatisticBasic.  # noqa: E501


        :return: The min of this ScheduleStatisticBasic.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ScheduleStatisticBasic.


        :param min: The min of this ScheduleStatisticBasic.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this ScheduleStatisticBasic.  # noqa: E501


        :return: The max of this ScheduleStatisticBasic.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ScheduleStatisticBasic.


        :param max: The max of this ScheduleStatisticBasic.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def value(self):
        """Gets the value of this ScheduleStatisticBasic.  # noqa: E501


        :return: The value of this ScheduleStatisticBasic.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ScheduleStatisticBasic.


        :param value: The value of this ScheduleStatisticBasic.  # noqa: E501
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
        if not isinstance(other, ScheduleStatisticBasic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleStatisticBasic):
            return True

        return self.to_dict() != other.to_dict()
