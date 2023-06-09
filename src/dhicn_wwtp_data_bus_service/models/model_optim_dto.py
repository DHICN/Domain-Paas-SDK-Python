# coding: utf-8

"""
    wwtp-paas-main-bus-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wwtp_data_bus_service.configuration import Configuration


class ModelOptimDto(object):
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
        'control_items': 'list[ControlItem]',
        'precision_w_qs': 'list[PrecisionWq]'
    }

    attribute_map = {
        'control_items': 'controlItems',
        'precision_w_qs': 'precisionWQs'
    }

    def __init__(self, control_items=None, precision_w_qs=None, local_vars_configuration=None):  # noqa: E501
        """ModelOptimDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._control_items = None
        self._precision_w_qs = None
        self.discriminator = None

        self.control_items = control_items
        self.precision_w_qs = precision_w_qs

    @property
    def control_items(self):
        """Gets the control_items of this ModelOptimDto.  # noqa: E501

        控制项数据 control item data  # noqa: E501

        :return: The control_items of this ModelOptimDto.  # noqa: E501
        :rtype: list[ControlItem]
        """
        return self._control_items

    @control_items.setter
    def control_items(self, control_items):
        """Sets the control_items of this ModelOptimDto.

        控制项数据 control item data  # noqa: E501

        :param control_items: The control_items of this ModelOptimDto.  # noqa: E501
        :type: list[ControlItem]
        """

        self._control_items = control_items

    @property
    def precision_w_qs(self):
        """Gets the precision_w_qs of this ModelOptimDto.  # noqa: E501

        预测出水水质 effluent water quality data  # noqa: E501

        :return: The precision_w_qs of this ModelOptimDto.  # noqa: E501
        :rtype: list[PrecisionWq]
        """
        return self._precision_w_qs

    @precision_w_qs.setter
    def precision_w_qs(self, precision_w_qs):
        """Sets the precision_w_qs of this ModelOptimDto.

        预测出水水质 effluent water quality data  # noqa: E501

        :param precision_w_qs: The precision_w_qs of this ModelOptimDto.  # noqa: E501
        :type: list[PrecisionWq]
        """

        self._precision_w_qs = precision_w_qs

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
        if not isinstance(other, ModelOptimDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelOptimDto):
            return True

        return self.to_dict() != other.to_dict()
