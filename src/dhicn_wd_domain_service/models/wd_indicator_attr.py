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

from dhicn_wd_domain_service.configuration import Configuration


class WdIndicatorAttr(object):
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
        'indicator': 'str',
        'min_clean': 'float',
        'max_clean': 'float',
        'accuracy_check': 'bool'
    }

    attribute_map = {
        'indicator': 'indicator',
        'min_clean': 'minClean',
        'max_clean': 'maxClean',
        'accuracy_check': 'accuracyCheck'
    }

    def __init__(self, indicator=None, min_clean=None, max_clean=None, accuracy_check=None, local_vars_configuration=None):  # noqa: E501
        """WdIndicatorAttr - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._indicator = None
        self._min_clean = None
        self._max_clean = None
        self._accuracy_check = None
        self.discriminator = None

        self.indicator = indicator
        if min_clean is not None:
            self.min_clean = min_clean
        if max_clean is not None:
            self.max_clean = max_clean
        if accuracy_check is not None:
            self.accuracy_check = accuracy_check

    @property
    def indicator(self):
        """Gets the indicator of this WdIndicatorAttr.  # noqa: E501

        指标  # noqa: E501

        :return: The indicator of this WdIndicatorAttr.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this WdIndicatorAttr.

        指标  # noqa: E501

        :param indicator: The indicator of this WdIndicatorAttr.  # noqa: E501
        :type: str
        """

        self._indicator = indicator

    @property
    def min_clean(self):
        """Gets the min_clean of this WdIndicatorAttr.  # noqa: E501

        触发数据清洗的最小值  # noqa: E501

        :return: The min_clean of this WdIndicatorAttr.  # noqa: E501
        :rtype: float
        """
        return self._min_clean

    @min_clean.setter
    def min_clean(self, min_clean):
        """Sets the min_clean of this WdIndicatorAttr.

        触发数据清洗的最小值  # noqa: E501

        :param min_clean: The min_clean of this WdIndicatorAttr.  # noqa: E501
        :type: float
        """

        self._min_clean = min_clean

    @property
    def max_clean(self):
        """Gets the max_clean of this WdIndicatorAttr.  # noqa: E501

        触发数据清洗的最大值  # noqa: E501

        :return: The max_clean of this WdIndicatorAttr.  # noqa: E501
        :rtype: float
        """
        return self._max_clean

    @max_clean.setter
    def max_clean(self, max_clean):
        """Sets the max_clean of this WdIndicatorAttr.

        触发数据清洗的最大值  # noqa: E501

        :param max_clean: The max_clean of this WdIndicatorAttr.  # noqa: E501
        :type: float
        """

        self._max_clean = max_clean

    @property
    def accuracy_check(self):
        """Gets the accuracy_check of this WdIndicatorAttr.  # noqa: E501

        是否参与精度计算  # noqa: E501

        :return: The accuracy_check of this WdIndicatorAttr.  # noqa: E501
        :rtype: bool
        """
        return self._accuracy_check

    @accuracy_check.setter
    def accuracy_check(self, accuracy_check):
        """Sets the accuracy_check of this WdIndicatorAttr.

        是否参与精度计算  # noqa: E501

        :param accuracy_check: The accuracy_check of this WdIndicatorAttr.  # noqa: E501
        :type: bool
        """

        self._accuracy_check = accuracy_check

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
        if not isinstance(other, WdIndicatorAttr):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WdIndicatorAttr):
            return True

        return self.to_dict() != other.to_dict()