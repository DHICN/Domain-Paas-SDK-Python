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

from dhicn_identity_service.configuration import Configuration


class WqStatisticOutput(object):
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
        'bio_chemical_tank': 'str',
        'data': 'list[StatisticData]'
    }

    attribute_map = {
        'bio_chemical_tank': 'bioChemicalTank',
        'data': 'data'
    }

    def __init__(self, bio_chemical_tank=None, data=None, local_vars_configuration=None):  # noqa: E501
        """WqStatisticOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bio_chemical_tank = None
        self._data = None
        self.discriminator = None

        self.bio_chemical_tank = bio_chemical_tank
        self.data = data

    @property
    def bio_chemical_tank(self):
        """Gets the bio_chemical_tank of this WqStatisticOutput.  # noqa: E501

        生化池名称 biochemical pool name  # noqa: E501

        :return: The bio_chemical_tank of this WqStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._bio_chemical_tank

    @bio_chemical_tank.setter
    def bio_chemical_tank(self, bio_chemical_tank):
        """Sets the bio_chemical_tank of this WqStatisticOutput.

        生化池名称 biochemical pool name  # noqa: E501

        :param bio_chemical_tank: The bio_chemical_tank of this WqStatisticOutput.  # noqa: E501
        :type: str
        """

        self._bio_chemical_tank = bio_chemical_tank

    @property
    def data(self):
        """Gets the data of this WqStatisticOutput.  # noqa: E501

        统计数据 statistic data  # noqa: E501

        :return: The data of this WqStatisticOutput.  # noqa: E501
        :rtype: list[StatisticData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WqStatisticOutput.

        统计数据 statistic data  # noqa: E501

        :param data: The data of this WqStatisticOutput.  # noqa: E501
        :type: list[StatisticData]
        """

        self._data = data

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
        if not isinstance(other, WqStatisticOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WqStatisticOutput):
            return True

        return self.to_dict() != other.to_dict()
