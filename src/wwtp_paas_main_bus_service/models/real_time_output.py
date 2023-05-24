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


class RealTimeOutput(object):
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
        'location': 'str',
        'inlet': 'str',
        'inlet_name': 'str',
        'datas': 'list[RealTimeData]'
    }

    attribute_map = {
        'location': 'location',
        'inlet': 'inlet',
        'inlet_name': 'inletName',
        'datas': 'datas'
    }

    def __init__(self, location=None, inlet=None, inlet_name=None, datas=None, local_vars_configuration=None):  # noqa: E501
        """RealTimeOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location = None
        self._inlet = None
        self._inlet_name = None
        self._datas = None
        self.discriminator = None

        self.location = location
        self.inlet = inlet
        self.inlet_name = inlet_name
        self.datas = datas

    @property
    def location(self):
        """Gets the location of this RealTimeOutput.  # noqa: E501

        毒性仪位置 toxicity meter location  # noqa: E501

        :return: The location of this RealTimeOutput.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this RealTimeOutput.

        毒性仪位置 toxicity meter location  # noqa: E501

        :param location: The location of this RealTimeOutput.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def inlet(self):
        """Gets the inlet of this RealTimeOutput.  # noqa: E501

        所处的进水点 inlet  # noqa: E501

        :return: The inlet of this RealTimeOutput.  # noqa: E501
        :rtype: str
        """
        return self._inlet

    @inlet.setter
    def inlet(self, inlet):
        """Sets the inlet of this RealTimeOutput.

        所处的进水点 inlet  # noqa: E501

        :param inlet: The inlet of this RealTimeOutput.  # noqa: E501
        :type: str
        """

        self._inlet = inlet

    @property
    def inlet_name(self):
        """Gets the inlet_name of this RealTimeOutput.  # noqa: E501


        :return: The inlet_name of this RealTimeOutput.  # noqa: E501
        :rtype: str
        """
        return self._inlet_name

    @inlet_name.setter
    def inlet_name(self, inlet_name):
        """Sets the inlet_name of this RealTimeOutput.


        :param inlet_name: The inlet_name of this RealTimeOutput.  # noqa: E501
        :type: str
        """

        self._inlet_name = inlet_name

    @property
    def datas(self):
        """Gets the datas of this RealTimeOutput.  # noqa: E501

        具体数据 detailed data  # noqa: E501

        :return: The datas of this RealTimeOutput.  # noqa: E501
        :rtype: list[RealTimeData]
        """
        return self._datas

    @datas.setter
    def datas(self, datas):
        """Sets the datas of this RealTimeOutput.

        具体数据 detailed data  # noqa: E501

        :param datas: The datas of this RealTimeOutput.  # noqa: E501
        :type: list[RealTimeData]
        """

        self._datas = datas

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
        if not isinstance(other, RealTimeOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RealTimeOutput):
            return True

        return self.to_dict() != other.to_dict()
