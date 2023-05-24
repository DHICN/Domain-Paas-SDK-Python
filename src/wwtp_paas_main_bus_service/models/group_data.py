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


class GroupData(object):
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
        'board_name': 'str',
        'board_value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'board_name': 'boardName',
        'board_value': 'boardValue',
        'unit': 'unit'
    }

    def __init__(self, board_name=None, board_value=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """GroupData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._board_name = None
        self._board_value = None
        self._unit = None
        self.discriminator = None

        self.board_name = board_name
        self.board_value = board_value
        self.unit = unit

    @property
    def board_name(self):
        """Gets the board_name of this GroupData.  # noqa: E501

        看板项名称 statistic item name  # noqa: E501

        :return: The board_name of this GroupData.  # noqa: E501
        :rtype: str
        """
        return self._board_name

    @board_name.setter
    def board_name(self, board_name):
        """Sets the board_name of this GroupData.

        看板项名称 statistic item name  # noqa: E501

        :param board_name: The board_name of this GroupData.  # noqa: E501
        :type: str
        """

        self._board_name = board_name

    @property
    def board_value(self):
        """Gets the board_value of this GroupData.  # noqa: E501

        看板项数值 statistic item value  # noqa: E501

        :return: The board_value of this GroupData.  # noqa: E501
        :rtype: float
        """
        return self._board_value

    @board_value.setter
    def board_value(self, board_value):
        """Sets the board_value of this GroupData.

        看板项数值 statistic item value  # noqa: E501

        :param board_value: The board_value of this GroupData.  # noqa: E501
        :type: float
        """

        self._board_value = board_value

    @property
    def unit(self):
        """Gets the unit of this GroupData.  # noqa: E501

        看板项单位 statistic item unit  # noqa: E501

        :return: The unit of this GroupData.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GroupData.

        看板项单位 statistic item unit  # noqa: E501

        :param unit: The unit of this GroupData.  # noqa: E501
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
        if not isinstance(other, GroupData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupData):
            return True

        return self.to_dict() != other.to_dict()
