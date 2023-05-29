# coding: utf-8

"""
    wd-domain-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wd_service_domain.configuration import Configuration


class CurrentOnlineData(object):
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
        'id': 'str',
        'current_time': 'datetime',
        'measure_data': 'float'
    }

    attribute_map = {
        'id': 'id',
        'current_time': 'currentTime',
        'measure_data': 'measureData'
    }

    def __init__(self, id=None, current_time=None, measure_data=None, local_vars_configuration=None):  # noqa: E501
        """CurrentOnlineData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._current_time = None
        self._measure_data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if current_time is not None:
            self.current_time = current_time
        if measure_data is not None:
            self.measure_data = measure_data

    @property
    def id(self):
        """Gets the id of this CurrentOnlineData.  # noqa: E501

        指标id  # noqa: E501

        :return: The id of this CurrentOnlineData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrentOnlineData.

        指标id  # noqa: E501

        :param id: The id of this CurrentOnlineData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def current_time(self):
        """Gets the current_time of this CurrentOnlineData.  # noqa: E501

        最新实测和模拟时间  # noqa: E501

        :return: The current_time of this CurrentOnlineData.  # noqa: E501
        :rtype: datetime
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """Sets the current_time of this CurrentOnlineData.

        最新实测和模拟时间  # noqa: E501

        :param current_time: The current_time of this CurrentOnlineData.  # noqa: E501
        :type: datetime
        """

        self._current_time = current_time

    @property
    def measure_data(self):
        """Gets the measure_data of this CurrentOnlineData.  # noqa: E501

        最新指标点位实测值  # noqa: E501

        :return: The measure_data of this CurrentOnlineData.  # noqa: E501
        :rtype: float
        """
        return self._measure_data

    @measure_data.setter
    def measure_data(self, measure_data):
        """Sets the measure_data of this CurrentOnlineData.

        最新指标点位实测值  # noqa: E501

        :param measure_data: The measure_data of this CurrentOnlineData.  # noqa: E501
        :type: float
        """

        self._measure_data = measure_data

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
        if not isinstance(other, CurrentOnlineData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentOnlineData):
            return True

        return self.to_dict() != other.to_dict()
