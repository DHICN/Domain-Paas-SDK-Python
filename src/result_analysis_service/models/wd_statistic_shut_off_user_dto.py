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


class WdStatisticShutOffUserDto(object):
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
        'time': 'datetime',
        'user_infos': 'list[UserInfo]'
    }

    attribute_map = {
        'time': 'time',
        'user_infos': 'userInfos'
    }

    def __init__(self, time=None, user_infos=None, local_vars_configuration=None):  # noqa: E501
        """WdStatisticShutOffUserDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._user_infos = None
        self.discriminator = None

        if time is not None:
            self.time = time
        self.user_infos = user_infos

    @property
    def time(self):
        """Gets the time of this WdStatisticShutOffUserDto.  # noqa: E501


        :return: The time of this WdStatisticShutOffUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this WdStatisticShutOffUserDto.


        :param time: The time of this WdStatisticShutOffUserDto.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def user_infos(self):
        """Gets the user_infos of this WdStatisticShutOffUserDto.  # noqa: E501


        :return: The user_infos of this WdStatisticShutOffUserDto.  # noqa: E501
        :rtype: list[UserInfo]
        """
        return self._user_infos

    @user_infos.setter
    def user_infos(self, user_infos):
        """Sets the user_infos of this WdStatisticShutOffUserDto.


        :param user_infos: The user_infos of this WdStatisticShutOffUserDto.  # noqa: E501
        :type: list[UserInfo]
        """

        self._user_infos = user_infos

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
        if not isinstance(other, WdStatisticShutOffUserDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WdStatisticShutOffUserDto):
            return True

        return self.to_dict() != other.to_dict()
