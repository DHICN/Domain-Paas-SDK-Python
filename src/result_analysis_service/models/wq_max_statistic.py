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


class WqMaxStatistic(object):
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
        'wq_item': 'str',
        'wq_item_max_value': 'float',
        'is_exceed': 'int',
        'max_model_feature_id': 'str'
    }

    attribute_map = {
        'wq_item': 'wqItem',
        'wq_item_max_value': 'wqItemMaxValue',
        'is_exceed': 'isExceed',
        'max_model_feature_id': 'maxModelFeatureId'
    }

    def __init__(self, wq_item=None, wq_item_max_value=None, is_exceed=None, max_model_feature_id=None, local_vars_configuration=None):  # noqa: E501
        """WqMaxStatistic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wq_item = None
        self._wq_item_max_value = None
        self._is_exceed = None
        self._max_model_feature_id = None
        self.discriminator = None

        self.wq_item = wq_item
        if wq_item_max_value is not None:
            self.wq_item_max_value = wq_item_max_value
        if is_exceed is not None:
            self.is_exceed = is_exceed
        self.max_model_feature_id = max_model_feature_id

    @property
    def wq_item(self):
        """Gets the wq_item of this WqMaxStatistic.  # noqa: E501

        水质项 water quality item  # noqa: E501

        :return: The wq_item of this WqMaxStatistic.  # noqa: E501
        :rtype: str
        """
        return self._wq_item

    @wq_item.setter
    def wq_item(self, wq_item):
        """Sets the wq_item of this WqMaxStatistic.

        水质项 water quality item  # noqa: E501

        :param wq_item: The wq_item of this WqMaxStatistic.  # noqa: E501
        :type: str
        """

        self._wq_item = wq_item

    @property
    def wq_item_max_value(self):
        """Gets the wq_item_max_value of this WqMaxStatistic.  # noqa: E501

        最大值 max value  # noqa: E501

        :return: The wq_item_max_value of this WqMaxStatistic.  # noqa: E501
        :rtype: float
        """
        return self._wq_item_max_value

    @wq_item_max_value.setter
    def wq_item_max_value(self, wq_item_max_value):
        """Sets the wq_item_max_value of this WqMaxStatistic.

        最大值 max value  # noqa: E501

        :param wq_item_max_value: The wq_item_max_value of this WqMaxStatistic.  # noqa: E501
        :type: float
        """

        self._wq_item_max_value = wq_item_max_value

    @property
    def is_exceed(self):
        """Gets the is_exceed of this WqMaxStatistic.  # noqa: E501

        是否超标 is exceed  # noqa: E501

        :return: The is_exceed of this WqMaxStatistic.  # noqa: E501
        :rtype: int
        """
        return self._is_exceed

    @is_exceed.setter
    def is_exceed(self, is_exceed):
        """Sets the is_exceed of this WqMaxStatistic.

        是否超标 is exceed  # noqa: E501

        :param is_exceed: The is_exceed of this WqMaxStatistic.  # noqa: E501
        :type: int
        """

        self._is_exceed = is_exceed

    @property
    def max_model_feature_id(self):
        """Gets the max_model_feature_id of this WqMaxStatistic.  # noqa: E501

        最大浓度位置 Maximum concentration modelfeature id  # noqa: E501

        :return: The max_model_feature_id of this WqMaxStatistic.  # noqa: E501
        :rtype: str
        """
        return self._max_model_feature_id

    @max_model_feature_id.setter
    def max_model_feature_id(self, max_model_feature_id):
        """Sets the max_model_feature_id of this WqMaxStatistic.

        最大浓度位置 Maximum concentration modelfeature id  # noqa: E501

        :param max_model_feature_id: The max_model_feature_id of this WqMaxStatistic.  # noqa: E501
        :type: str
        """

        self._max_model_feature_id = max_model_feature_id

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
        if not isinstance(other, WqMaxStatistic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WqMaxStatistic):
            return True

        return self.to_dict() != other.to_dict()
