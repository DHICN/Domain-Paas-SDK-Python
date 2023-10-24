# coding: utf-8

"""
    IoT服务

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_iot_service.configuration import Configuration


class SaveHistorySearchRecordInput(object):
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
        'name': 'str',
        'is_default': 'bool',
        'indicator': 'str',
        'is_search_simul': 'bool',
        'is_search_online': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_default': 'isDefault',
        'indicator': 'indicator',
        'is_search_simul': 'isSearchSimul',
        'is_search_online': 'isSearchOnline'
    }

    def __init__(self, name=None, is_default=None, indicator=None, is_search_simul=None, is_search_online=None, local_vars_configuration=None):  # noqa: E501
        """SaveHistorySearchRecordInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._is_default = None
        self._indicator = None
        self._is_search_simul = None
        self._is_search_online = None
        self.discriminator = None

        self.name = name
        if is_default is not None:
            self.is_default = is_default
        self.indicator = indicator
        if is_search_simul is not None:
            self.is_search_simul = is_search_simul
        if is_search_online is not None:
            self.is_search_online = is_search_online

    @property
    def name(self):
        """Gets the name of this SaveHistorySearchRecordInput.  # noqa: E501

        历史搜索条件记录  # noqa: E501

        :return: The name of this SaveHistorySearchRecordInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveHistorySearchRecordInput.

        历史搜索条件记录  # noqa: E501

        :param name: The name of this SaveHistorySearchRecordInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this SaveHistorySearchRecordInput.  # noqa: E501

        是否是默认展示点位  # noqa: E501

        :return: The is_default of this SaveHistorySearchRecordInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this SaveHistorySearchRecordInput.

        是否是默认展示点位  # noqa: E501

        :param is_default: The is_default of this SaveHistorySearchRecordInput.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def indicator(self):
        """Gets the indicator of this SaveHistorySearchRecordInput.  # noqa: E501

        指标编码  # noqa: E501

        :return: The indicator of this SaveHistorySearchRecordInput.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this SaveHistorySearchRecordInput.

        指标编码  # noqa: E501

        :param indicator: The indicator of this SaveHistorySearchRecordInput.  # noqa: E501
        :type: str
        """

        self._indicator = indicator

    @property
    def is_search_simul(self):
        """Gets the is_search_simul of this SaveHistorySearchRecordInput.  # noqa: E501

        是否需要查询模拟数据  # noqa: E501

        :return: The is_search_simul of this SaveHistorySearchRecordInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_search_simul

    @is_search_simul.setter
    def is_search_simul(self, is_search_simul):
        """Sets the is_search_simul of this SaveHistorySearchRecordInput.

        是否需要查询模拟数据  # noqa: E501

        :param is_search_simul: The is_search_simul of this SaveHistorySearchRecordInput.  # noqa: E501
        :type: bool
        """

        self._is_search_simul = is_search_simul

    @property
    def is_search_online(self):
        """Gets the is_search_online of this SaveHistorySearchRecordInput.  # noqa: E501

        是否需要查询在线数据  # noqa: E501

        :return: The is_search_online of this SaveHistorySearchRecordInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_search_online

    @is_search_online.setter
    def is_search_online(self, is_search_online):
        """Sets the is_search_online of this SaveHistorySearchRecordInput.

        是否需要查询在线数据  # noqa: E501

        :param is_search_online: The is_search_online of this SaveHistorySearchRecordInput.  # noqa: E501
        :type: bool
        """

        self._is_search_online = is_search_online

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
        if not isinstance(other, SaveHistorySearchRecordInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SaveHistorySearchRecordInput):
            return True

        return self.to_dict() != other.to_dict()
