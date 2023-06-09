# coding: utf-8

"""
    digital-twin-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_digital_twin_service.configuration import Configuration


class PrecisionModel(object):
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
        'is_floating': 'bool',
        'maximum_significant_digits': 'int',
        'scale': 'float',
        'precision_model_type': 'int'
    }

    attribute_map = {
        'is_floating': 'isFloating',
        'maximum_significant_digits': 'maximumSignificantDigits',
        'scale': 'scale',
        'precision_model_type': 'precisionModelType'
    }

    def __init__(self, is_floating=None, maximum_significant_digits=None, scale=None, precision_model_type=None, local_vars_configuration=None):  # noqa: E501
        """PrecisionModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_floating = None
        self._maximum_significant_digits = None
        self._scale = None
        self._precision_model_type = None
        self.discriminator = None

        if is_floating is not None:
            self.is_floating = is_floating
        if maximum_significant_digits is not None:
            self.maximum_significant_digits = maximum_significant_digits
        if scale is not None:
            self.scale = scale
        if precision_model_type is not None:
            self.precision_model_type = precision_model_type

    @property
    def is_floating(self):
        """Gets the is_floating of this PrecisionModel.  # noqa: E501


        :return: The is_floating of this PrecisionModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_floating

    @is_floating.setter
    def is_floating(self, is_floating):
        """Sets the is_floating of this PrecisionModel.


        :param is_floating: The is_floating of this PrecisionModel.  # noqa: E501
        :type: bool
        """

        self._is_floating = is_floating

    @property
    def maximum_significant_digits(self):
        """Gets the maximum_significant_digits of this PrecisionModel.  # noqa: E501


        :return: The maximum_significant_digits of this PrecisionModel.  # noqa: E501
        :rtype: int
        """
        return self._maximum_significant_digits

    @maximum_significant_digits.setter
    def maximum_significant_digits(self, maximum_significant_digits):
        """Sets the maximum_significant_digits of this PrecisionModel.


        :param maximum_significant_digits: The maximum_significant_digits of this PrecisionModel.  # noqa: E501
        :type: int
        """

        self._maximum_significant_digits = maximum_significant_digits

    @property
    def scale(self):
        """Gets the scale of this PrecisionModel.  # noqa: E501


        :return: The scale of this PrecisionModel.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this PrecisionModel.


        :param scale: The scale of this PrecisionModel.  # noqa: E501
        :type: float
        """

        self._scale = scale

    @property
    def precision_model_type(self):
        """Gets the precision_model_type of this PrecisionModel.  # noqa: E501

        0-Floating 1-FloatingSingle 2-Fixed   # noqa: E501

        :return: The precision_model_type of this PrecisionModel.  # noqa: E501
        :rtype: int
        """
        return self._precision_model_type

    @precision_model_type.setter
    def precision_model_type(self, precision_model_type):
        """Sets the precision_model_type of this PrecisionModel.

        0-Floating 1-FloatingSingle 2-Fixed   # noqa: E501

        :param precision_model_type: The precision_model_type of this PrecisionModel.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and precision_model_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `precision_model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(precision_model_type, allowed_values)
            )

        self._precision_model_type = precision_model_type

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
        if not isinstance(other, PrecisionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrecisionModel):
            return True

        return self.to_dict() != other.to_dict()
