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


class PumpBaseConfiguration(object):
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
        'config': 'FactoryConfig'
    }

    attribute_map = {
        'name': 'name',
        'config': 'config'
    }

    def __init__(self, name=None, config=None, local_vars_configuration=None):  # noqa: E501
        """PumpBaseConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._config = None
        self.discriminator = None

        self.name = name
        if config is not None:
            self.config = config

    @property
    def name(self):
        """Gets the name of this PumpBaseConfiguration.  # noqa: E501


        :return: The name of this PumpBaseConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PumpBaseConfiguration.


        :param name: The name of this PumpBaseConfiguration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def config(self):
        """Gets the config of this PumpBaseConfiguration.  # noqa: E501


        :return: The config of this PumpBaseConfiguration.  # noqa: E501
        :rtype: FactoryConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this PumpBaseConfiguration.


        :param config: The config of this PumpBaseConfiguration.  # noqa: E501
        :type: FactoryConfig
        """

        self._config = config

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
        if not isinstance(other, PumpBaseConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PumpBaseConfiguration):
            return True

        return self.to_dict() != other.to_dict()
