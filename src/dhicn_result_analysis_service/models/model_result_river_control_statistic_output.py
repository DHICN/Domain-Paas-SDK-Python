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


class ModelResultRiverControlStatisticOutput(object):
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
        'node_type': 'str',
        'data_item': 'int',
        'value': 'float'
    }

    attribute_map = {
        'asset_name': 'assetName',
        'node_type': 'nodeType',
        'data_item': 'dataItem',
        'value': 'value'
    }

    def __init__(self, asset_name=None, node_type=None, data_item=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ModelResultRiverControlStatisticOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_name = None
        self._node_type = None
        self._data_item = None
        self._value = None
        self.discriminator = None

        self.asset_name = asset_name
        self.node_type = node_type
        if data_item is not None:
            self.data_item = data_item
        if value is not None:
            self.value = value

    @property
    def asset_name(self):
        """Gets the asset_name of this ModelResultRiverControlStatisticOutput.  # noqa: E501

        坝/闸/泵名称 control name  # noqa: E501

        :return: The asset_name of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this ModelResultRiverControlStatisticOutput.

        坝/闸/泵名称 control name  # noqa: E501

        :param asset_name: The asset_name of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def node_type(self):
        """Gets the node_type of this ModelResultRiverControlStatisticOutput.  # noqa: E501

        类型：pump 泵，dam 坝，gate闸 type:pump,dam,gate  # noqa: E501

        :return: The node_type of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ModelResultRiverControlStatisticOutput.

        类型：pump 泵，dam 坝，gate闸 type:pump,dam,gate  # noqa: E501

        :param node_type: The node_type of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :type: str
        """

        self._node_type = node_type

    @property
    def data_item(self):
        """Gets the data_item of this ModelResultRiverControlStatisticOutput.  # noqa: E501

        最高（低）控制水位/开停次数 开启时长/补水时长 补水总量  data type (maximum (low) control water level/number of starts and stops/Start duration/water make-up duration/Total water make-up)  # noqa: E501

        :return: The data_item of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :rtype: int
        """
        return self._data_item

    @data_item.setter
    def data_item(self, data_item):
        """Sets the data_item of this ModelResultRiverControlStatisticOutput.

        最高（低）控制水位/开停次数 开启时长/补水时长 补水总量  data type (maximum (low) control water level/number of starts and stops/Start duration/water make-up duration/Total water make-up)  # noqa: E501

        :param data_item: The data_item of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :type: int
        """

        self._data_item = data_item

    @property
    def value(self):
        """Gets the value of this ModelResultRiverControlStatisticOutput.  # noqa: E501

        结果值 value  # noqa: E501

        :return: The value of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelResultRiverControlStatisticOutput.

        结果值 value  # noqa: E501

        :param value: The value of this ModelResultRiverControlStatisticOutput.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if not isinstance(other, ModelResultRiverControlStatisticOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelResultRiverControlStatisticOutput):
            return True

        return self.to_dict() != other.to_dict()