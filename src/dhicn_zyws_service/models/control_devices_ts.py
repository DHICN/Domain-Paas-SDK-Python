# coding: utf-8

"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_zyws_service.configuration import Configuration


class ControlDevicesTs(object):
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
        'indicator': 'str',
        'actual_weir_height_ts_pairs': 'TsPairs',
        'suggest_weir_height_ts_pairs': 'TsPairs',
        'control_ts_pairs': 'TsPairs',
        'data_issued_ts_pairs': 'TsPairs'
    }

    attribute_map = {
        'indicator': 'indicator',
        'actual_weir_height_ts_pairs': 'actualWeirHeightTsPairs',
        'suggest_weir_height_ts_pairs': 'suggestWeirHeightTsPairs',
        'control_ts_pairs': 'controlTsPairs',
        'data_issued_ts_pairs': 'dataIssuedTsPairs'
    }

    def __init__(self, indicator=None, actual_weir_height_ts_pairs=None, suggest_weir_height_ts_pairs=None, control_ts_pairs=None, data_issued_ts_pairs=None, local_vars_configuration=None):  # noqa: E501
        """ControlDevicesTs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._indicator = None
        self._actual_weir_height_ts_pairs = None
        self._suggest_weir_height_ts_pairs = None
        self._control_ts_pairs = None
        self._data_issued_ts_pairs = None
        self.discriminator = None

        self.indicator = indicator
        if actual_weir_height_ts_pairs is not None:
            self.actual_weir_height_ts_pairs = actual_weir_height_ts_pairs
        if suggest_weir_height_ts_pairs is not None:
            self.suggest_weir_height_ts_pairs = suggest_weir_height_ts_pairs
        if control_ts_pairs is not None:
            self.control_ts_pairs = control_ts_pairs
        if data_issued_ts_pairs is not None:
            self.data_issued_ts_pairs = data_issued_ts_pairs

    @property
    def indicator(self):
        """Gets the indicator of this ControlDevicesTs.  # noqa: E501


        :return: The indicator of this ControlDevicesTs.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this ControlDevicesTs.


        :param indicator: The indicator of this ControlDevicesTs.  # noqa: E501
        :type: str
        """

        self._indicator = indicator

    @property
    def actual_weir_height_ts_pairs(self):
        """Gets the actual_weir_height_ts_pairs of this ControlDevicesTs.  # noqa: E501


        :return: The actual_weir_height_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :rtype: TsPairs
        """
        return self._actual_weir_height_ts_pairs

    @actual_weir_height_ts_pairs.setter
    def actual_weir_height_ts_pairs(self, actual_weir_height_ts_pairs):
        """Sets the actual_weir_height_ts_pairs of this ControlDevicesTs.


        :param actual_weir_height_ts_pairs: The actual_weir_height_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :type: TsPairs
        """

        self._actual_weir_height_ts_pairs = actual_weir_height_ts_pairs

    @property
    def suggest_weir_height_ts_pairs(self):
        """Gets the suggest_weir_height_ts_pairs of this ControlDevicesTs.  # noqa: E501


        :return: The suggest_weir_height_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :rtype: TsPairs
        """
        return self._suggest_weir_height_ts_pairs

    @suggest_weir_height_ts_pairs.setter
    def suggest_weir_height_ts_pairs(self, suggest_weir_height_ts_pairs):
        """Sets the suggest_weir_height_ts_pairs of this ControlDevicesTs.


        :param suggest_weir_height_ts_pairs: The suggest_weir_height_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :type: TsPairs
        """

        self._suggest_weir_height_ts_pairs = suggest_weir_height_ts_pairs

    @property
    def control_ts_pairs(self):
        """Gets the control_ts_pairs of this ControlDevicesTs.  # noqa: E501


        :return: The control_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :rtype: TsPairs
        """
        return self._control_ts_pairs

    @control_ts_pairs.setter
    def control_ts_pairs(self, control_ts_pairs):
        """Sets the control_ts_pairs of this ControlDevicesTs.


        :param control_ts_pairs: The control_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :type: TsPairs
        """

        self._control_ts_pairs = control_ts_pairs

    @property
    def data_issued_ts_pairs(self):
        """Gets the data_issued_ts_pairs of this ControlDevicesTs.  # noqa: E501


        :return: The data_issued_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :rtype: TsPairs
        """
        return self._data_issued_ts_pairs

    @data_issued_ts_pairs.setter
    def data_issued_ts_pairs(self, data_issued_ts_pairs):
        """Sets the data_issued_ts_pairs of this ControlDevicesTs.


        :param data_issued_ts_pairs: The data_issued_ts_pairs of this ControlDevicesTs.  # noqa: E501
        :type: TsPairs
        """

        self._data_issued_ts_pairs = data_issued_ts_pairs

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
        if not isinstance(other, ControlDevicesTs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlDevicesTs):
            return True

        return self.to_dict() != other.to_dict()
