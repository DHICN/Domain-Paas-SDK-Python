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


class DataBoardFullOut(object):
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
        'data_group': 'str',
        'data': 'list[GroupData]'
    }

    attribute_map = {
        'data_group': 'dataGroup',
        'data': 'data'
    }

    def __init__(self, data_group=None, data=None, local_vars_configuration=None):  # noqa: E501
        """DataBoardFullOut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_group = None
        self._data = None
        self.discriminator = None

        self.data_group = data_group
        self.data = data

    @property
    def data_group(self):
        """Gets the data_group of this DataBoardFullOut.  # noqa: E501

        数据看板分组 statistic data group  # noqa: E501

        :return: The data_group of this DataBoardFullOut.  # noqa: E501
        :rtype: str
        """
        return self._data_group

    @data_group.setter
    def data_group(self, data_group):
        """Sets the data_group of this DataBoardFullOut.

        数据看板分组 statistic data group  # noqa: E501

        :param data_group: The data_group of this DataBoardFullOut.  # noqa: E501
        :type: str
        """

        self._data_group = data_group

    @property
    def data(self):
        """Gets the data of this DataBoardFullOut.  # noqa: E501

        分组下的数据 statistic data  # noqa: E501

        :return: The data of this DataBoardFullOut.  # noqa: E501
        :rtype: list[GroupData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DataBoardFullOut.

        分组下的数据 statistic data  # noqa: E501

        :param data: The data of this DataBoardFullOut.  # noqa: E501
        :type: list[GroupData]
        """

        self._data = data

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
        if not isinstance(other, DataBoardFullOut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataBoardFullOut):
            return True

        return self.to_dict() != other.to_dict()
