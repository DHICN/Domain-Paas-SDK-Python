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

from wwtp_paas_main_bus_service.configuration import Configuration


class OutletTnOutput(object):
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
        'inlet_value': 'list[TsPair1]',
        'out_let_value': 'list[TsPair1]',
        'unit': 'str'
    }

    attribute_map = {
        'code': 'code',
        'inlet_value': 'inletValue',
        'out_let_value': 'outLetValue',
        'unit': 'unit'
    }

    def __init__(self, code=None, inlet_value=None, out_let_value=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """OutletTnOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._inlet_value = None
        self._out_let_value = None
        self._unit = None
        self.discriminator = None

        self.code = code
        self.inlet_value = inlet_value
        self.out_let_value = out_let_value
        self.unit = unit

    @property
    def code(self):
        """Gets the code of this OutletTnOutput.  # noqa: E501

        指标代码 indicator code  # noqa: E501

        :return: The code of this OutletTnOutput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OutletTnOutput.

        指标代码 indicator code  # noqa: E501

        :param code: The code of this OutletTnOutput.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def inlet_value(self):
        """Gets the inlet_value of this OutletTnOutput.  # noqa: E501

        实际出水水质数据 actual effluent water quality data  # noqa: E501

        :return: The inlet_value of this OutletTnOutput.  # noqa: E501
        :rtype: list[TsPair1]
        """
        return self._inlet_value

    @inlet_value.setter
    def inlet_value(self, inlet_value):
        """Sets the inlet_value of this OutletTnOutput.

        实际出水水质数据 actual effluent water quality data  # noqa: E501

        :param inlet_value: The inlet_value of this OutletTnOutput.  # noqa: E501
        :type: list[TsPair1]
        """

        self._inlet_value = inlet_value

    @property
    def out_let_value(self):
        """Gets the out_let_value of this OutletTnOutput.  # noqa: E501

        模拟出水水质数据 simulated effluent water quality data  # noqa: E501

        :return: The out_let_value of this OutletTnOutput.  # noqa: E501
        :rtype: list[TsPair1]
        """
        return self._out_let_value

    @out_let_value.setter
    def out_let_value(self, out_let_value):
        """Sets the out_let_value of this OutletTnOutput.

        模拟出水水质数据 simulated effluent water quality data  # noqa: E501

        :param out_let_value: The out_let_value of this OutletTnOutput.  # noqa: E501
        :type: list[TsPair1]
        """

        self._out_let_value = out_let_value

    @property
    def unit(self):
        """Gets the unit of this OutletTnOutput.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this OutletTnOutput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this OutletTnOutput.

        单位 unit  # noqa: E501

        :param unit: The unit of this OutletTnOutput.  # noqa: E501
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
        if not isinstance(other, OutletTnOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutletTnOutput):
            return True

        return self.to_dict() != other.to_dict()
