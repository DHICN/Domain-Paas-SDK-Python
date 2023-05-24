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


class SimResultsOutupt(object):
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
        'out_waters_unit': 'str',
        'out_waters': 'list[TsPair1]'
    }

    attribute_map = {
        'code': 'code',
        'out_waters_unit': 'outWatersUnit',
        'out_waters': 'outWaters'
    }

    def __init__(self, code=None, out_waters_unit=None, out_waters=None, local_vars_configuration=None):  # noqa: E501
        """SimResultsOutupt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._out_waters_unit = None
        self._out_waters = None
        self.discriminator = None

        self.code = code
        self.out_waters_unit = out_waters_unit
        self.out_waters = out_waters

    @property
    def code(self):
        """Gets the code of this SimResultsOutupt.  # noqa: E501

        指标代码 indicator code  # noqa: E501

        :return: The code of this SimResultsOutupt.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SimResultsOutupt.

        指标代码 indicator code  # noqa: E501

        :param code: The code of this SimResultsOutupt.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def out_waters_unit(self):
        """Gets the out_waters_unit of this SimResultsOutupt.  # noqa: E501

        指标单位 indicator unit  # noqa: E501

        :return: The out_waters_unit of this SimResultsOutupt.  # noqa: E501
        :rtype: str
        """
        return self._out_waters_unit

    @out_waters_unit.setter
    def out_waters_unit(self, out_waters_unit):
        """Sets the out_waters_unit of this SimResultsOutupt.

        指标单位 indicator unit  # noqa: E501

        :param out_waters_unit: The out_waters_unit of this SimResultsOutupt.  # noqa: E501
        :type: str
        """

        self._out_waters_unit = out_waters_unit

    @property
    def out_waters(self):
        """Gets the out_waters of this SimResultsOutupt.  # noqa: E501

        时间序列数据 time-series data  # noqa: E501

        :return: The out_waters of this SimResultsOutupt.  # noqa: E501
        :rtype: list[TsPair1]
        """
        return self._out_waters

    @out_waters.setter
    def out_waters(self, out_waters):
        """Sets the out_waters of this SimResultsOutupt.

        时间序列数据 time-series data  # noqa: E501

        :param out_waters: The out_waters of this SimResultsOutupt.  # noqa: E501
        :type: list[TsPair1]
        """

        self._out_waters = out_waters

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
        if not isinstance(other, SimResultsOutupt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimResultsOutupt):
            return True

        return self.to_dict() != other.to_dict()
