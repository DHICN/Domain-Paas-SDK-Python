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


class ModelResultRiverPumpTotalStatisticOutput(object):
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
        'asset_id': 'str',
        'asset_name': 'str',
        'total_minutes': 'float',
        'total_volume': 'float'
    }

    attribute_map = {
        'asset_id': 'assetID',
        'asset_name': 'assetName',
        'total_minutes': 'totalMinutes',
        'total_volume': 'totalVolume'
    }

    def __init__(self, asset_id=None, asset_name=None, total_minutes=None, total_volume=None, local_vars_configuration=None):  # noqa: E501
        """ModelResultRiverPumpTotalStatisticOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_id = None
        self._asset_name = None
        self._total_minutes = None
        self._total_volume = None
        self.discriminator = None

        self.asset_id = asset_id
        self.asset_name = asset_name
        if total_minutes is not None:
            self.total_minutes = total_minutes
        if total_volume is not None:
            self.total_volume = total_volume

    @property
    def asset_id(self):
        """Gets the asset_id of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501

        泵id pump id  # noqa: E501

        :return: The asset_id of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ModelResultRiverPumpTotalStatisticOutput.

        泵id pump id  # noqa: E501

        :param asset_id: The asset_id of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501

        泵站名称 pump name  # noqa: E501

        :return: The asset_name of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this ModelResultRiverPumpTotalStatisticOutput.

        泵站名称 pump name  # noqa: E501

        :param asset_name: The asset_name of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def total_minutes(self):
        """Gets the total_minutes of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501

        总补水时长，以分钟为单位 total water make-up time(unit:minute)  # noqa: E501

        :return: The total_minutes of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this ModelResultRiverPumpTotalStatisticOutput.

        总补水时长，以分钟为单位 total water make-up time(unit:minute)  # noqa: E501

        :param total_minutes: The total_minutes of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :type: float
        """

        self._total_minutes = total_minutes

    @property
    def total_volume(self):
        """Gets the total_volume of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501

        总补水量 total make-up water  # noqa: E501

        :return: The total_volume of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._total_volume

    @total_volume.setter
    def total_volume(self, total_volume):
        """Sets the total_volume of this ModelResultRiverPumpTotalStatisticOutput.

        总补水量 total make-up water  # noqa: E501

        :param total_volume: The total_volume of this ModelResultRiverPumpTotalStatisticOutput.  # noqa: E501
        :type: float
        """

        self._total_volume = total_volume

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
        if not isinstance(other, ModelResultRiverPumpTotalStatisticOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelResultRiverPumpTotalStatisticOutput):
            return True

        return self.to_dict() != other.to_dict()
