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


class GateInfo(object):
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
        'state': 'int',
        'open_num': 'float',
        'open_minutes': 'float'
    }

    attribute_map = {
        'asset_id': 'assetID',
        'asset_name': 'assetName',
        'state': 'state',
        'open_num': 'openNum',
        'open_minutes': 'openMinutes'
    }

    def __init__(self, asset_id=None, asset_name=None, state=None, open_num=None, open_minutes=None, local_vars_configuration=None):  # noqa: E501
        """GateInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_id = None
        self._asset_name = None
        self._state = None
        self._open_num = None
        self._open_minutes = None
        self.discriminator = None

        self.asset_id = asset_id
        self.asset_name = asset_name
        if state is not None:
            self.state = state
        if open_num is not None:
            self.open_num = open_num
        if open_minutes is not None:
            self.open_minutes = open_minutes

    @property
    def asset_id(self):
        """Gets the asset_id of this GateInfo.  # noqa: E501

        闸Id gate id  # noqa: E501

        :return: The asset_id of this GateInfo.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this GateInfo.

        闸Id gate id  # noqa: E501

        :param asset_id: The asset_id of this GateInfo.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def asset_name(self):
        """Gets the asset_name of this GateInfo.  # noqa: E501

        闸名称 gate name  # noqa: E501

        :return: The asset_name of this GateInfo.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this GateInfo.

        闸名称 gate name  # noqa: E501

        :param asset_name: The asset_name of this GateInfo.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def state(self):
        """Gets the state of this GateInfo.  # noqa: E501

        开关状态(0:关,1:开) switch status (0: off, 1: on)  # noqa: E501

        :return: The state of this GateInfo.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GateInfo.

        开关状态(0:关,1:开) switch status (0: off, 1: on)  # noqa: E501

        :param state: The state of this GateInfo.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def open_num(self):
        """Gets the open_num of this GateInfo.  # noqa: E501

        开启次数 Opening times  # noqa: E501

        :return: The open_num of this GateInfo.  # noqa: E501
        :rtype: float
        """
        return self._open_num

    @open_num.setter
    def open_num(self, open_num):
        """Sets the open_num of this GateInfo.

        开启次数 Opening times  # noqa: E501

        :param open_num: The open_num of this GateInfo.  # noqa: E501
        :type: float
        """

        self._open_num = open_num

    @property
    def open_minutes(self):
        """Gets the open_minutes of this GateInfo.  # noqa: E501

        开启时长，以分钟为单位 opening duration (unit:minute)  # noqa: E501

        :return: The open_minutes of this GateInfo.  # noqa: E501
        :rtype: float
        """
        return self._open_minutes

    @open_minutes.setter
    def open_minutes(self, open_minutes):
        """Sets the open_minutes of this GateInfo.

        开启时长，以分钟为单位 opening duration (unit:minute)  # noqa: E501

        :param open_minutes: The open_minutes of this GateInfo.  # noqa: E501
        :type: float
        """

        self._open_minutes = open_minutes

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
        if not isinstance(other, GateInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GateInfo):
            return True

        return self.to_dict() != other.to_dict()
