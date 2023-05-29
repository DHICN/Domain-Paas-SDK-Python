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


class StorageData(object):
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
        'dt': 'str',
        'storage_volume': 'float',
        'storage_rate': 'float'
    }

    attribute_map = {
        'dt': 'dt',
        'storage_volume': 'storageVolume',
        'storage_rate': 'storageRate'
    }

    def __init__(self, dt=None, storage_volume=None, storage_rate=None, local_vars_configuration=None):  # noqa: E501
        """StorageData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dt = None
        self._storage_volume = None
        self._storage_rate = None
        self.discriminator = None

        self.dt = dt
        if storage_volume is not None:
            self.storage_volume = storage_volume
        if storage_rate is not None:
            self.storage_rate = storage_rate

    @property
    def dt(self):
        """Gets the dt of this StorageData.  # noqa: E501

        时间 time  # noqa: E501

        :return: The dt of this StorageData.  # noqa: E501
        :rtype: str
        """
        return self._dt

    @dt.setter
    def dt(self, dt):
        """Sets the dt of this StorageData.

        时间 time  # noqa: E501

        :param dt: The dt of this StorageData.  # noqa: E501
        :type: str
        """

        self._dt = dt

    @property
    def storage_volume(self):
        """Gets the storage_volume of this StorageData.  # noqa: E501

        调蓄管道储水量 water storage capacity of regulation and storage pipeline  # noqa: E501

        :return: The storage_volume of this StorageData.  # noqa: E501
        :rtype: float
        """
        return self._storage_volume

    @storage_volume.setter
    def storage_volume(self, storage_volume):
        """Sets the storage_volume of this StorageData.

        调蓄管道储水量 water storage capacity of regulation and storage pipeline  # noqa: E501

        :param storage_volume: The storage_volume of this StorageData.  # noqa: E501
        :type: float
        """

        self._storage_volume = storage_volume

    @property
    def storage_rate(self):
        """Gets the storage_rate of this StorageData.  # noqa: E501

        存储率 storage rate  # noqa: E501

        :return: The storage_rate of this StorageData.  # noqa: E501
        :rtype: float
        """
        return self._storage_rate

    @storage_rate.setter
    def storage_rate(self, storage_rate):
        """Sets the storage_rate of this StorageData.

        存储率 storage rate  # noqa: E501

        :param storage_rate: The storage_rate of this StorageData.  # noqa: E501
        :type: float
        """

        self._storage_rate = storage_rate

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
        if not isinstance(other, StorageData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageData):
            return True

        return self.to_dict() != other.to_dict()