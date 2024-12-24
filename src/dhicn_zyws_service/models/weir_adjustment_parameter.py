# coding: utf-8

"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_zyws_service.configuration import Configuration


class WeirAdjustmentParameter(object):
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
        'device_code': 'str',
        'weir_adjustment_factor': 'float',
        'weir_adjustment_height': 'float',
        'weir_adjustment_opening': 'float',
        'adjust_minimum_amount': 'float',
        'minimum_opening': 'float',
        'maximum_opening': 'float',
        'sort': 'int'
    }

    attribute_map = {
        'device_code': 'deviceCode',
        'weir_adjustment_factor': 'weirAdjustmentFactor',
        'weir_adjustment_height': 'weirAdjustmentHeight',
        'weir_adjustment_opening': 'weirAdjustmentOpening',
        'adjust_minimum_amount': 'adjustMinimumAmount',
        'minimum_opening': 'minimumOpening',
        'maximum_opening': 'maximumOpening',
        'sort': 'sort'
    }

    def __init__(self, device_code=None, weir_adjustment_factor=None, weir_adjustment_height=None, weir_adjustment_opening=None, adjust_minimum_amount=None, minimum_opening=None, maximum_opening=None, sort=None, local_vars_configuration=None):  # noqa: E501
        """WeirAdjustmentParameter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_code = None
        self._weir_adjustment_factor = None
        self._weir_adjustment_height = None
        self._weir_adjustment_opening = None
        self._adjust_minimum_amount = None
        self._minimum_opening = None
        self._maximum_opening = None
        self._sort = None
        self.discriminator = None

        self.device_code = device_code
        if weir_adjustment_factor is not None:
            self.weir_adjustment_factor = weir_adjustment_factor
        if weir_adjustment_height is not None:
            self.weir_adjustment_height = weir_adjustment_height
        if weir_adjustment_opening is not None:
            self.weir_adjustment_opening = weir_adjustment_opening
        if adjust_minimum_amount is not None:
            self.adjust_minimum_amount = adjust_minimum_amount
        if minimum_opening is not None:
            self.minimum_opening = minimum_opening
        if maximum_opening is not None:
            self.maximum_opening = maximum_opening
        if sort is not None:
            self.sort = sort

    @property
    def device_code(self):
        """Gets the device_code of this WeirAdjustmentParameter.  # noqa: E501


        :return: The device_code of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        """Sets the device_code of this WeirAdjustmentParameter.


        :param device_code: The device_code of this WeirAdjustmentParameter.  # noqa: E501
        :type: str
        """

        self._device_code = device_code

    @property
    def weir_adjustment_factor(self):
        """Gets the weir_adjustment_factor of this WeirAdjustmentParameter.  # noqa: E501

        堰调整系数  # noqa: E501

        :return: The weir_adjustment_factor of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: float
        """
        return self._weir_adjustment_factor

    @weir_adjustment_factor.setter
    def weir_adjustment_factor(self, weir_adjustment_factor):
        """Sets the weir_adjustment_factor of this WeirAdjustmentParameter.

        堰调整系数  # noqa: E501

        :param weir_adjustment_factor: The weir_adjustment_factor of this WeirAdjustmentParameter.  # noqa: E501
        :type: float
        """

        self._weir_adjustment_factor = weir_adjustment_factor

    @property
    def weir_adjustment_height(self):
        """Gets the weir_adjustment_height of this WeirAdjustmentParameter.  # noqa: E501

        单位变化堰调整开度  # noqa: E501

        :return: The weir_adjustment_height of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: float
        """
        return self._weir_adjustment_height

    @weir_adjustment_height.setter
    def weir_adjustment_height(self, weir_adjustment_height):
        """Sets the weir_adjustment_height of this WeirAdjustmentParameter.

        单位变化堰调整开度  # noqa: E501

        :param weir_adjustment_height: The weir_adjustment_height of this WeirAdjustmentParameter.  # noqa: E501
        :type: float
        """

        self._weir_adjustment_height = weir_adjustment_height

    @property
    def weir_adjustment_opening(self):
        """Gets the weir_adjustment_opening of this WeirAdjustmentParameter.  # noqa: E501

        单位变化堰调整开度  # noqa: E501

        :return: The weir_adjustment_opening of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: float
        """
        return self._weir_adjustment_opening

    @weir_adjustment_opening.setter
    def weir_adjustment_opening(self, weir_adjustment_opening):
        """Sets the weir_adjustment_opening of this WeirAdjustmentParameter.

        单位变化堰调整开度  # noqa: E501

        :param weir_adjustment_opening: The weir_adjustment_opening of this WeirAdjustmentParameter.  # noqa: E501
        :type: float
        """

        self._weir_adjustment_opening = weir_adjustment_opening

    @property
    def adjust_minimum_amount(self):
        """Gets the adjust_minimum_amount of this WeirAdjustmentParameter.  # noqa: E501

        调节最小量  # noqa: E501

        :return: The adjust_minimum_amount of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: float
        """
        return self._adjust_minimum_amount

    @adjust_minimum_amount.setter
    def adjust_minimum_amount(self, adjust_minimum_amount):
        """Sets the adjust_minimum_amount of this WeirAdjustmentParameter.

        调节最小量  # noqa: E501

        :param adjust_minimum_amount: The adjust_minimum_amount of this WeirAdjustmentParameter.  # noqa: E501
        :type: float
        """

        self._adjust_minimum_amount = adjust_minimum_amount

    @property
    def minimum_opening(self):
        """Gets the minimum_opening of this WeirAdjustmentParameter.  # noqa: E501

        最小开度  # noqa: E501

        :return: The minimum_opening of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: float
        """
        return self._minimum_opening

    @minimum_opening.setter
    def minimum_opening(self, minimum_opening):
        """Sets the minimum_opening of this WeirAdjustmentParameter.

        最小开度  # noqa: E501

        :param minimum_opening: The minimum_opening of this WeirAdjustmentParameter.  # noqa: E501
        :type: float
        """

        self._minimum_opening = minimum_opening

    @property
    def maximum_opening(self):
        """Gets the maximum_opening of this WeirAdjustmentParameter.  # noqa: E501

        最大开度  # noqa: E501

        :return: The maximum_opening of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: float
        """
        return self._maximum_opening

    @maximum_opening.setter
    def maximum_opening(self, maximum_opening):
        """Sets the maximum_opening of this WeirAdjustmentParameter.

        最大开度  # noqa: E501

        :param maximum_opening: The maximum_opening of this WeirAdjustmentParameter.  # noqa: E501
        :type: float
        """

        self._maximum_opening = maximum_opening

    @property
    def sort(self):
        """Gets the sort of this WeirAdjustmentParameter.  # noqa: E501


        :return: The sort of this WeirAdjustmentParameter.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this WeirAdjustmentParameter.


        :param sort: The sort of this WeirAdjustmentParameter.  # noqa: E501
        :type: int
        """

        self._sort = sort

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
        if not isinstance(other, WeirAdjustmentParameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WeirAdjustmentParameter):
            return True

        return self.to_dict() != other.to_dict()