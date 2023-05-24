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


class PercentagesDto(object):
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
        'region_name': 'str',
        'rec_probability': 'str',
        'value': 'float'
    }

    attribute_map = {
        'region_name': 'regionName',
        'rec_probability': 'recProbability',
        'value': 'value'
    }

    def __init__(self, region_name=None, rec_probability=None, value=None, local_vars_configuration=None):  # noqa: E501
        """PercentagesDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._region_name = None
        self._rec_probability = None
        self._value = None
        self.discriminator = None

        self.region_name = region_name
        self.rec_probability = rec_probability
        if value is not None:
            self.value = value

    @property
    def region_name(self):
        """Gets the region_name of this PercentagesDto.  # noqa: E501

        精度区间名称，如:80-100(优秀)  precision region name  # noqa: E501

        :return: The region_name of this PercentagesDto.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this PercentagesDto.

        精度区间名称，如:80-100(优秀)  precision region name  # noqa: E501

        :param region_name: The region_name of this PercentagesDto.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def rec_probability(self):
        """Gets the rec_probability of this PercentagesDto.  # noqa: E501

        推荐占比，如:>70 precision region recommended proportion  # noqa: E501

        :return: The rec_probability of this PercentagesDto.  # noqa: E501
        :rtype: str
        """
        return self._rec_probability

    @rec_probability.setter
    def rec_probability(self, rec_probability):
        """Sets the rec_probability of this PercentagesDto.

        推荐占比，如:>70 precision region recommended proportion  # noqa: E501

        :param rec_probability: The rec_probability of this PercentagesDto.  # noqa: E501
        :type: str
        """

        self._rec_probability = rec_probability

    @property
    def value(self):
        """Gets the value of this PercentagesDto.  # noqa: E501

        精度百分比区间占比 precision region proportion  # noqa: E501

        :return: The value of this PercentagesDto.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PercentagesDto.

        精度百分比区间占比 precision region proportion  # noqa: E501

        :param value: The value of this PercentagesDto.  # noqa: E501
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
        if not isinstance(other, PercentagesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PercentagesDto):
            return True

        return self.to_dict() != other.to_dict()
