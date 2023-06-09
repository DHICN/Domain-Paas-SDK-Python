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


class ModelResultPipeSewagePlantInstantStatisticOutput(object):
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
        'wq_statistic_infos': 'list[WqInstantStatisticInfo]'
    }

    attribute_map = {
        'asset_id': 'assetID',
        'asset_name': 'assetName',
        'wq_statistic_infos': 'wqStatisticInfos'
    }

    def __init__(self, asset_id=None, asset_name=None, wq_statistic_infos=None, local_vars_configuration=None):  # noqa: E501
        """ModelResultPipeSewagePlantInstantStatisticOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_id = None
        self._asset_name = None
        self._wq_statistic_infos = None
        self.discriminator = None

        self.asset_id = asset_id
        self.asset_name = asset_name
        self.wq_statistic_infos = wq_statistic_infos

    @property
    def asset_id(self):
        """Gets the asset_id of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501

        资产id asset id  # noqa: E501

        :return: The asset_id of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ModelResultPipeSewagePlantInstantStatisticOutput.

        资产id asset id  # noqa: E501

        :param asset_id: The asset_id of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501

        污水处理厂名称 asset name  # noqa: E501

        :return: The asset_name of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this ModelResultPipeSewagePlantInstantStatisticOutput.

        污水处理厂名称 asset name  # noqa: E501

        :param asset_name: The asset_name of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def wq_statistic_infos(self):
        """Gets the wq_statistic_infos of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501

        瞬时浓度列表 list of instantaneous concentrations  # noqa: E501

        :return: The wq_statistic_infos of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501
        :rtype: list[WqInstantStatisticInfo]
        """
        return self._wq_statistic_infos

    @wq_statistic_infos.setter
    def wq_statistic_infos(self, wq_statistic_infos):
        """Sets the wq_statistic_infos of this ModelResultPipeSewagePlantInstantStatisticOutput.

        瞬时浓度列表 list of instantaneous concentrations  # noqa: E501

        :param wq_statistic_infos: The wq_statistic_infos of this ModelResultPipeSewagePlantInstantStatisticOutput.  # noqa: E501
        :type: list[WqInstantStatisticInfo]
        """

        self._wq_statistic_infos = wq_statistic_infos

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
        if not isinstance(other, ModelResultPipeSewagePlantInstantStatisticOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelResultPipeSewagePlantInstantStatisticOutput):
            return True

        return self.to_dict() != other.to_dict()
