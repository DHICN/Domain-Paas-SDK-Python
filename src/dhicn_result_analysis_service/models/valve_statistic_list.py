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


class ValveStatisticList(object):
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
        'model_feature_id': 'str',
        'valve_type': 'int',
        'state': 'int',
        'total_minutes': 'float'
    }

    attribute_map = {
        'asset_id': 'assetID',
        'asset_name': 'assetName',
        'model_feature_id': 'modelFeatureId',
        'valve_type': 'valveType',
        'state': 'state',
        'total_minutes': 'totalMinutes'
    }

    def __init__(self, asset_id=None, asset_name=None, model_feature_id=None, valve_type=None, state=None, total_minutes=None, local_vars_configuration=None):  # noqa: E501
        """ValveStatisticList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_id = None
        self._asset_name = None
        self._model_feature_id = None
        self._valve_type = None
        self._state = None
        self._total_minutes = None
        self.discriminator = None

        self.asset_id = asset_id
        self.asset_name = asset_name
        self.model_feature_id = model_feature_id
        if valve_type is not None:
            self.valve_type = valve_type
        if state is not None:
            self.state = state
        if total_minutes is not None:
            self.total_minutes = total_minutes

    @property
    def asset_id(self):
        """Gets the asset_id of this ValveStatisticList.  # noqa: E501

        阀门Id valve id  # noqa: E501

        :return: The asset_id of this ValveStatisticList.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ValveStatisticList.

        阀门Id valve id  # noqa: E501

        :param asset_id: The asset_id of this ValveStatisticList.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this ValveStatisticList.  # noqa: E501

        阀门名称 valve name  # noqa: E501

        :return: The asset_name of this ValveStatisticList.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this ValveStatisticList.

        阀门名称 valve name  # noqa: E501

        :param asset_name: The asset_name of this ValveStatisticList.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def model_feature_id(self):
        """Gets the model_feature_id of this ValveStatisticList.  # noqa: E501

        模型中阀门的ID modelfeature id  # noqa: E501

        :return: The model_feature_id of this ValveStatisticList.  # noqa: E501
        :rtype: str
        """
        return self._model_feature_id

    @model_feature_id.setter
    def model_feature_id(self, model_feature_id):
        """Sets the model_feature_id of this ValveStatisticList.

        模型中阀门的ID modelfeature id  # noqa: E501

        :param model_feature_id: The model_feature_id of this ValveStatisticList.  # noqa: E501
        :type: str
        """

        self._model_feature_id = model_feature_id

    @property
    def valve_type(self):
        """Gets the valve_type of this ValveStatisticList.  # noqa: E501

        阀门类型： valve type 0-WasteWater,1-RainWater  0-WasteWater  1-RainWater  # noqa: E501

        :return: The valve_type of this ValveStatisticList.  # noqa: E501
        :rtype: int
        """
        return self._valve_type

    @valve_type.setter
    def valve_type(self, valve_type):
        """Sets the valve_type of this ValveStatisticList.

        阀门类型： valve type 0-WasteWater,1-RainWater  0-WasteWater  1-RainWater  # noqa: E501

        :param valve_type: The valve_type of this ValveStatisticList.  # noqa: E501
        :type: int
        """

        self._valve_type = valve_type

    @property
    def state(self):
        """Gets the state of this ValveStatisticList.  # noqa: E501

        开关状态(0:关,1:开) switch status (0: off, 1: on)  # noqa: E501

        :return: The state of this ValveStatisticList.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ValveStatisticList.

        开关状态(0:关,1:开) switch status (0: off, 1: on)  # noqa: E501

        :param state: The state of this ValveStatisticList.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def total_minutes(self):
        """Gets the total_minutes of this ValveStatisticList.  # noqa: E501

        排河闸累计开启时间(min) total opening time (unit:minute)  # noqa: E501

        :return: The total_minutes of this ValveStatisticList.  # noqa: E501
        :rtype: float
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this ValveStatisticList.

        排河闸累计开启时间(min) total opening time (unit:minute)  # noqa: E501

        :param total_minutes: The total_minutes of this ValveStatisticList.  # noqa: E501
        :type: float
        """

        self._total_minutes = total_minutes

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
        if not isinstance(other, ValveStatisticList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValveStatisticList):
            return True

        return self.to_dict() != other.to_dict()
