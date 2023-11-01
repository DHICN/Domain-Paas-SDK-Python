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

from openapi_client.configuration import Configuration


class LatestTimeSeriesOutput(object):
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
        't': 'str',
        'v': 'str'
    }

    attribute_map = {
        'indicator': 'indicator',
        't': 't',
        'v': 'v'
    }

    def __init__(self, indicator=None, t=None, v=None, local_vars_configuration=None):  # noqa: E501
        """LatestTimeSeriesOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._indicator = None
        self._t = None
        self._v = None
        self.discriminator = None

        self.indicator = indicator
        self.t = t
        self.v = v

    @property
    def indicator(self):
        """Gets the indicator of this LatestTimeSeriesOutput.  # noqa: E501


        :return: The indicator of this LatestTimeSeriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this LatestTimeSeriesOutput.


        :param indicator: The indicator of this LatestTimeSeriesOutput.  # noqa: E501
        :type: str
        """

        self._indicator = indicator

    @property
    def t(self):
        """Gets the t of this LatestTimeSeriesOutput.  # noqa: E501


        :return: The t of this LatestTimeSeriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this LatestTimeSeriesOutput.


        :param t: The t of this LatestTimeSeriesOutput.  # noqa: E501
        :type: str
        """

        self._t = t

    @property
    def v(self):
        """Gets the v of this LatestTimeSeriesOutput.  # noqa: E501


        :return: The v of this LatestTimeSeriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this LatestTimeSeriesOutput.


        :param v: The v of this LatestTimeSeriesOutput.  # noqa: E501
        :type: str
        """

        self._v = v

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
        if not isinstance(other, LatestTimeSeriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LatestTimeSeriesOutput):
            return True

        return self.to_dict() != other.to_dict()
