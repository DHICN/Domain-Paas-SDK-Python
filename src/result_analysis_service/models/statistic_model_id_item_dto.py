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


class StatisticModelIdItemDto(object):
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
        'max_value': 'float',
        'min_value': 'float',
        'avg_value': 'float'
    }

    attribute_map = {
        'max_value': 'maxValue',
        'min_value': 'minValue',
        'avg_value': 'avgValue'
    }

    def __init__(self, max_value=None, min_value=None, avg_value=None, local_vars_configuration=None):  # noqa: E501
        """StatisticModelIdItemDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_value = None
        self._min_value = None
        self._avg_value = None
        self.discriminator = None

        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if avg_value is not None:
            self.avg_value = avg_value

    @property
    def max_value(self):
        """Gets the max_value of this StatisticModelIdItemDto.  # noqa: E501


        :return: The max_value of this StatisticModelIdItemDto.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this StatisticModelIdItemDto.


        :param max_value: The max_value of this StatisticModelIdItemDto.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this StatisticModelIdItemDto.  # noqa: E501


        :return: The min_value of this StatisticModelIdItemDto.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this StatisticModelIdItemDto.


        :param min_value: The min_value of this StatisticModelIdItemDto.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def avg_value(self):
        """Gets the avg_value of this StatisticModelIdItemDto.  # noqa: E501


        :return: The avg_value of this StatisticModelIdItemDto.  # noqa: E501
        :rtype: float
        """
        return self._avg_value

    @avg_value.setter
    def avg_value(self, avg_value):
        """Sets the avg_value of this StatisticModelIdItemDto.


        :param avg_value: The avg_value of this StatisticModelIdItemDto.  # noqa: E501
        :type: float
        """

        self._avg_value = avg_value

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
        if not isinstance(other, StatisticModelIdItemDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticModelIdItemDto):
            return True

        return self.to_dict() != other.to_dict()
