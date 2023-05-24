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


class EntireProcessWqOut(object):
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
        'unit': 'str',
        'ts_data': 'list[EntireProcessTs]'
    }

    attribute_map = {
        'code': 'code',
        'unit': 'unit',
        'ts_data': 'tsData'
    }

    def __init__(self, code=None, unit=None, ts_data=None, local_vars_configuration=None):  # noqa: E501
        """EntireProcessWqOut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._unit = None
        self._ts_data = None
        self.discriminator = None

        self.code = code
        self.unit = unit
        self.ts_data = ts_data

    @property
    def code(self):
        """Gets the code of this EntireProcessWqOut.  # noqa: E501

        指标 indicator code  # noqa: E501

        :return: The code of this EntireProcessWqOut.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EntireProcessWqOut.

        指标 indicator code  # noqa: E501

        :param code: The code of this EntireProcessWqOut.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def unit(self):
        """Gets the unit of this EntireProcessWqOut.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this EntireProcessWqOut.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this EntireProcessWqOut.

        单位 unit  # noqa: E501

        :param unit: The unit of this EntireProcessWqOut.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def ts_data(self):
        """Gets the ts_data of this EntireProcessWqOut.  # noqa: E501

        全流程水质时间序列 entire process time-series data  # noqa: E501

        :return: The ts_data of this EntireProcessWqOut.  # noqa: E501
        :rtype: list[EntireProcessTs]
        """
        return self._ts_data

    @ts_data.setter
    def ts_data(self, ts_data):
        """Sets the ts_data of this EntireProcessWqOut.

        全流程水质时间序列 entire process time-series data  # noqa: E501

        :param ts_data: The ts_data of this EntireProcessWqOut.  # noqa: E501
        :type: list[EntireProcessTs]
        """

        self._ts_data = ts_data

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
        if not isinstance(other, EntireProcessWqOut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntireProcessWqOut):
            return True

        return self.to_dict() != other.to_dict()
