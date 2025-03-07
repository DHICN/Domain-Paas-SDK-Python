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


class DamGateConfigurationInputOutput(object):
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
        'configuration_name': 'str',
        'storage_max': 'float',
        'dam_gate_configurations': 'list[DamGateConfiguration]',
        'weir_adjustment_parameter': 'list[WeirAdjustmentParameter]',
        'extended_parameter': 'dict(str, str)'
    }

    attribute_map = {
        'configuration_name': 'configurationName',
        'storage_max': 'storage_Max',
        'dam_gate_configurations': 'damGateConfigurations',
        'weir_adjustment_parameter': 'weirAdjustmentParameter',
        'extended_parameter': 'extendedParameter'
    }

    def __init__(self, configuration_name=None, storage_max=None, dam_gate_configurations=None, weir_adjustment_parameter=None, extended_parameter=None, local_vars_configuration=None):  # noqa: E501
        """DamGateConfigurationInputOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._configuration_name = None
        self._storage_max = None
        self._dam_gate_configurations = None
        self._weir_adjustment_parameter = None
        self._extended_parameter = None
        self.discriminator = None

        self.configuration_name = configuration_name
        if storage_max is not None:
            self.storage_max = storage_max
        self.dam_gate_configurations = dam_gate_configurations
        self.weir_adjustment_parameter = weir_adjustment_parameter
        self.extended_parameter = extended_parameter

    @property
    def configuration_name(self):
        """Gets the configuration_name of this DamGateConfigurationInputOutput.  # noqa: E501


        :return: The configuration_name of this DamGateConfigurationInputOutput.  # noqa: E501
        :rtype: str
        """
        return self._configuration_name

    @configuration_name.setter
    def configuration_name(self, configuration_name):
        """Sets the configuration_name of this DamGateConfigurationInputOutput.


        :param configuration_name: The configuration_name of this DamGateConfigurationInputOutput.  # noqa: E501
        :type: str
        """

        self._configuration_name = configuration_name

    @property
    def storage_max(self):
        """Gets the storage_max of this DamGateConfigurationInputOutput.  # noqa: E501

        调蓄池最大体积  # noqa: E501

        :return: The storage_max of this DamGateConfigurationInputOutput.  # noqa: E501
        :rtype: float
        """
        return self._storage_max

    @storage_max.setter
    def storage_max(self, storage_max):
        """Sets the storage_max of this DamGateConfigurationInputOutput.

        调蓄池最大体积  # noqa: E501

        :param storage_max: The storage_max of this DamGateConfigurationInputOutput.  # noqa: E501
        :type: float
        """

        self._storage_max = storage_max

    @property
    def dam_gate_configurations(self):
        """Gets the dam_gate_configurations of this DamGateConfigurationInputOutput.  # noqa: E501

        20个堰门的配置数据  # noqa: E501

        :return: The dam_gate_configurations of this DamGateConfigurationInputOutput.  # noqa: E501
        :rtype: list[DamGateConfiguration]
        """
        return self._dam_gate_configurations

    @dam_gate_configurations.setter
    def dam_gate_configurations(self, dam_gate_configurations):
        """Sets the dam_gate_configurations of this DamGateConfigurationInputOutput.

        20个堰门的配置数据  # noqa: E501

        :param dam_gate_configurations: The dam_gate_configurations of this DamGateConfigurationInputOutput.  # noqa: E501
        :type: list[DamGateConfiguration]
        """

        self._dam_gate_configurations = dam_gate_configurations

    @property
    def weir_adjustment_parameter(self):
        """Gets the weir_adjustment_parameter of this DamGateConfigurationInputOutput.  # noqa: E501

        1,3,4厂过堰调整参数  # noqa: E501

        :return: The weir_adjustment_parameter of this DamGateConfigurationInputOutput.  # noqa: E501
        :rtype: list[WeirAdjustmentParameter]
        """
        return self._weir_adjustment_parameter

    @weir_adjustment_parameter.setter
    def weir_adjustment_parameter(self, weir_adjustment_parameter):
        """Sets the weir_adjustment_parameter of this DamGateConfigurationInputOutput.

        1,3,4厂过堰调整参数  # noqa: E501

        :param weir_adjustment_parameter: The weir_adjustment_parameter of this DamGateConfigurationInputOutput.  # noqa: E501
        :type: list[WeirAdjustmentParameter]
        """

        self._weir_adjustment_parameter = weir_adjustment_parameter

    @property
    def extended_parameter(self):
        """Gets the extended_parameter of this DamGateConfigurationInputOutput.  # noqa: E501

        扩展算法参数  # noqa: E501

        :return: The extended_parameter of this DamGateConfigurationInputOutput.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extended_parameter

    @extended_parameter.setter
    def extended_parameter(self, extended_parameter):
        """Sets the extended_parameter of this DamGateConfigurationInputOutput.

        扩展算法参数  # noqa: E501

        :param extended_parameter: The extended_parameter of this DamGateConfigurationInputOutput.  # noqa: E501
        :type: dict(str, str)
        """

        self._extended_parameter = extended_parameter

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
        if not isinstance(other, DamGateConfigurationInputOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DamGateConfigurationInputOutput):
            return True

        return self.to_dict() != other.to_dict()
