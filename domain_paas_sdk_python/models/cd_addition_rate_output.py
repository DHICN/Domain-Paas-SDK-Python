# coding: utf-8

"""
    identity-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from domain_paas_sdk_python.configuration import Configuration


class CdAdditionRateOutput(object):
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
        'code': 'str',
        'cal_value': 'list[TsPair1]',
        'value': 'list[TsPair1]',
        'unit': 'str'
    }

    attribute_map = {
        'code': 'code',
        'cal_value': 'calValue',
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, code=None, cal_value=None, value=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """CdAdditionRateOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._cal_value = None
        self._value = None
        self._unit = None
        self.discriminator = None

        self.code = code
        self.cal_value = cal_value
        self.value = value
        self.unit = unit

    @property
    def code(self):
        """Gets the code of this CdAdditionRateOutput.  # noqa: E501

        药剂代码 dosage code  # noqa: E501

        :return: The code of this CdAdditionRateOutput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CdAdditionRateOutput.

        药剂代码 dosage code  # noqa: E501

        :param code: The code of this CdAdditionRateOutput.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def cal_value(self):
        """Gets the cal_value of this CdAdditionRateOutput.  # noqa: E501

        计算值 calculated value  # noqa: E501

        :return: The cal_value of this CdAdditionRateOutput.  # noqa: E501
        :rtype: list[TsPair1]
        """
        return self._cal_value

    @cal_value.setter
    def cal_value(self, cal_value):
        """Sets the cal_value of this CdAdditionRateOutput.

        计算值 calculated value  # noqa: E501

        :param cal_value: The cal_value of this CdAdditionRateOutput.  # noqa: E501
        :type: list[TsPair1]
        """

        self._cal_value = cal_value

    @property
    def value(self):
        """Gets the value of this CdAdditionRateOutput.  # noqa: E501

        实际值 actual value  # noqa: E501

        :return: The value of this CdAdditionRateOutput.  # noqa: E501
        :rtype: list[TsPair1]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CdAdditionRateOutput.

        实际值 actual value  # noqa: E501

        :param value: The value of this CdAdditionRateOutput.  # noqa: E501
        :type: list[TsPair1]
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this CdAdditionRateOutput.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this CdAdditionRateOutput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this CdAdditionRateOutput.

        单位 unit  # noqa: E501

        :param unit: The unit of this CdAdditionRateOutput.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, CdAdditionRateOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CdAdditionRateOutput):
            return True

        return self.to_dict() != other.to_dict()
