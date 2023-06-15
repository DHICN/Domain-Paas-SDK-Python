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

from dhicn_result_analysis_service.configuration import Configuration


class ModelResultPipePumpVolumeStatisticOutput(object):
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
        'asset_name': 'str',
        'pump_ts': 'list[PumpVolume]'
    }

    attribute_map = {
        'asset_name': 'assetName',
        'pump_ts': 'pumpTS'
    }

    def __init__(self, asset_name=None, pump_ts=None, local_vars_configuration=None):  # noqa: E501
        """ModelResultPipePumpVolumeStatisticOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_name = None
        self._pump_ts = None
        self.discriminator = None

        self.asset_name = asset_name
        self.pump_ts = pump_ts

    @property
    def asset_name(self):
        """Gets the asset_name of this ModelResultPipePumpVolumeStatisticOutput.  # noqa: E501

        资产名称 asset name  # noqa: E501

        :return: The asset_name of this ModelResultPipePumpVolumeStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this ModelResultPipePumpVolumeStatisticOutput.

        资产名称 asset name  # noqa: E501

        :param asset_name: The asset_name of this ModelResultPipePumpVolumeStatisticOutput.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def pump_ts(self):
        """Gets the pump_ts of this ModelResultPipePumpVolumeStatisticOutput.  # noqa: E501

        调蓄泵站信息 information of regulation and storage pump  # noqa: E501

        :return: The pump_ts of this ModelResultPipePumpVolumeStatisticOutput.  # noqa: E501
        :rtype: list[PumpVolume]
        """
        return self._pump_ts

    @pump_ts.setter
    def pump_ts(self, pump_ts):
        """Sets the pump_ts of this ModelResultPipePumpVolumeStatisticOutput.

        调蓄泵站信息 information of regulation and storage pump  # noqa: E501

        :param pump_ts: The pump_ts of this ModelResultPipePumpVolumeStatisticOutput.  # noqa: E501
        :type: list[PumpVolume]
        """

        self._pump_ts = pump_ts

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
        if not isinstance(other, ModelResultPipePumpVolumeStatisticOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelResultPipePumpVolumeStatisticOutput):
            return True

        return self.to_dict() != other.to_dict()