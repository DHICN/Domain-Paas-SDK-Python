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


class ControlOrificeHeightOutput(object):
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
        'factory_name': 'str',
        'control_orifice_height_ts': 'ResultTimeSeries'
    }

    attribute_map = {
        'factory_name': 'factoryName',
        'control_orifice_height_ts': 'controlOrificeHeightTS'
    }

    def __init__(self, factory_name=None, control_orifice_height_ts=None, local_vars_configuration=None):  # noqa: E501
        """ControlOrificeHeightOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._factory_name = None
        self._control_orifice_height_ts = None
        self.discriminator = None

        self.factory_name = factory_name
        if control_orifice_height_ts is not None:
            self.control_orifice_height_ts = control_orifice_height_ts

    @property
    def factory_name(self):
        """Gets the factory_name of this ControlOrificeHeightOutput.  # noqa: E501

        厂区名称  # noqa: E501

        :return: The factory_name of this ControlOrificeHeightOutput.  # noqa: E501
        :rtype: str
        """
        return self._factory_name

    @factory_name.setter
    def factory_name(self, factory_name):
        """Sets the factory_name of this ControlOrificeHeightOutput.

        厂区名称  # noqa: E501

        :param factory_name: The factory_name of this ControlOrificeHeightOutput.  # noqa: E501
        :type: str
        """

        self._factory_name = factory_name

    @property
    def control_orifice_height_ts(self):
        """Gets the control_orifice_height_ts of this ControlOrificeHeightOutput.  # noqa: E501


        :return: The control_orifice_height_ts of this ControlOrificeHeightOutput.  # noqa: E501
        :rtype: ResultTimeSeries
        """
        return self._control_orifice_height_ts

    @control_orifice_height_ts.setter
    def control_orifice_height_ts(self, control_orifice_height_ts):
        """Sets the control_orifice_height_ts of this ControlOrificeHeightOutput.


        :param control_orifice_height_ts: The control_orifice_height_ts of this ControlOrificeHeightOutput.  # noqa: E501
        :type: ResultTimeSeries
        """

        self._control_orifice_height_ts = control_orifice_height_ts

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
        if not isinstance(other, ControlOrificeHeightOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlOrificeHeightOutput):
            return True

        return self.to_dict() != other.to_dict()
