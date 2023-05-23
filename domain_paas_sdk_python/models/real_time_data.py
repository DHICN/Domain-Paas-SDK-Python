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


class RealTimeData(object):
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
        'name': 'str',
        'latest_value': 'float',
        'description': 'str',
        'ts_datas': 'list[TsData]'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'latest_value': 'latestValue',
        'description': 'description',
        'ts_datas': 'tsDatas'
    }

    def __init__(self, code=None, name=None, latest_value=None, description=None, ts_datas=None, local_vars_configuration=None):  # noqa: E501
        """RealTimeData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._name = None
        self._latest_value = None
        self._description = None
        self._ts_datas = None
        self.discriminator = None

        self.code = code
        self.name = name
        if latest_value is not None:
            self.latest_value = latest_value
        self.description = description
        self.ts_datas = ts_datas

    @property
    def code(self):
        """Gets the code of this RealTimeData.  # noqa: E501

        毒性指标 toxicity indicator  # noqa: E501

        :return: The code of this RealTimeData.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RealTimeData.

        毒性指标 toxicity indicator  # noqa: E501

        :param code: The code of this RealTimeData.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this RealTimeData.  # noqa: E501

        指标名称 indicator name  # noqa: E501

        :return: The name of this RealTimeData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RealTimeData.

        指标名称 indicator name  # noqa: E501

        :param name: The name of this RealTimeData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def latest_value(self):
        """Gets the latest_value of this RealTimeData.  # noqa: E501

        最新值 latest value  # noqa: E501

        :return: The latest_value of this RealTimeData.  # noqa: E501
        :rtype: float
        """
        return self._latest_value

    @latest_value.setter
    def latest_value(self, latest_value):
        """Sets the latest_value of this RealTimeData.

        最新值 latest value  # noqa: E501

        :param latest_value: The latest_value of this RealTimeData.  # noqa: E501
        :type: float
        """

        self._latest_value = latest_value

    @property
    def description(self):
        """Gets the description of this RealTimeData.  # noqa: E501

        毒性描述 toxicity description  # noqa: E501

        :return: The description of this RealTimeData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RealTimeData.

        毒性描述 toxicity description  # noqa: E501

        :param description: The description of this RealTimeData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ts_datas(self):
        """Gets the ts_datas of this RealTimeData.  # noqa: E501

        时间序列数据 time-series data  # noqa: E501

        :return: The ts_datas of this RealTimeData.  # noqa: E501
        :rtype: list[TsData]
        """
        return self._ts_datas

    @ts_datas.setter
    def ts_datas(self, ts_datas):
        """Sets the ts_datas of this RealTimeData.

        时间序列数据 time-series data  # noqa: E501

        :param ts_datas: The ts_datas of this RealTimeData.  # noqa: E501
        :type: list[TsData]
        """

        self._ts_datas = ts_datas

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
        if not isinstance(other, RealTimeData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RealTimeData):
            return True

        return self.to_dict() != other.to_dict()
