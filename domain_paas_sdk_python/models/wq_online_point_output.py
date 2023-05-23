# coding: utf-8

"""
    identity-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from domain_paas_sdk_python.configuration import Configuration


class WqOnlinePointOutput(object):
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
        'location': 'str',
        'points': 'list[WqOnlinePoint]'
    }

    attribute_map = {
        'location': 'location',
        'points': 'points'
    }

    def __init__(self, location=None, points=None, local_vars_configuration=None):  # noqa: E501
        """WqOnlinePointOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location = None
        self._points = None
        self.discriminator = None

        self.location = location
        self.points = points

    @property
    def location(self):
        """Gets the location of this WqOnlinePointOutput.  # noqa: E501

        位置 location  # noqa: E501

        :return: The location of this WqOnlinePointOutput.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this WqOnlinePointOutput.

        位置 location  # noqa: E501

        :param location: The location of this WqOnlinePointOutput.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def points(self):
        """Gets the points of this WqOnlinePointOutput.  # noqa: E501

        进水点/工艺线，及其下的指标信息 inlet/product and corresponding indicators  # noqa: E501

        :return: The points of this WqOnlinePointOutput.  # noqa: E501
        :rtype: list[WqOnlinePoint]
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this WqOnlinePointOutput.

        进水点/工艺线，及其下的指标信息 inlet/product and corresponding indicators  # noqa: E501

        :param points: The points of this WqOnlinePointOutput.  # noqa: E501
        :type: list[WqOnlinePoint]
        """

        self._points = points

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
        if not isinstance(other, WqOnlinePointOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WqOnlinePointOutput):
            return True

        return self.to_dict() != other.to_dict()
