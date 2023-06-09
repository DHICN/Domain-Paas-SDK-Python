# coding: utf-8

"""
    wwtp-paas-infrastructure-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wwtp_infrastructure_service.configuration import Configuration


class AssemblyConfigOutput(object):
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
        'sys_code_config': 'SysCodeConfigInputOutput',
        'online_point_config': 'OnlinePointConfigInputOutput',
        'model_node_config': 'ModelNodeConfigInputOutput',
        'mapping_config': 'MappingConfigInputOutput'
    }

    attribute_map = {
        'sys_code_config': 'sysCodeConfig',
        'online_point_config': 'onlinePointConfig',
        'model_node_config': 'modelNodeConfig',
        'mapping_config': 'mappingConfig'
    }

    def __init__(self, sys_code_config=None, online_point_config=None, model_node_config=None, mapping_config=None, local_vars_configuration=None):  # noqa: E501
        """AssemblyConfigOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sys_code_config = None
        self._online_point_config = None
        self._model_node_config = None
        self._mapping_config = None
        self.discriminator = None

        if sys_code_config is not None:
            self.sys_code_config = sys_code_config
        if online_point_config is not None:
            self.online_point_config = online_point_config
        if model_node_config is not None:
            self.model_node_config = model_node_config
        if mapping_config is not None:
            self.mapping_config = mapping_config

    @property
    def sys_code_config(self):
        """Gets the sys_code_config of this AssemblyConfigOutput.  # noqa: E501


        :return: The sys_code_config of this AssemblyConfigOutput.  # noqa: E501
        :rtype: SysCodeConfigInputOutput
        """
        return self._sys_code_config

    @sys_code_config.setter
    def sys_code_config(self, sys_code_config):
        """Sets the sys_code_config of this AssemblyConfigOutput.


        :param sys_code_config: The sys_code_config of this AssemblyConfigOutput.  # noqa: E501
        :type: SysCodeConfigInputOutput
        """

        self._sys_code_config = sys_code_config

    @property
    def online_point_config(self):
        """Gets the online_point_config of this AssemblyConfigOutput.  # noqa: E501


        :return: The online_point_config of this AssemblyConfigOutput.  # noqa: E501
        :rtype: OnlinePointConfigInputOutput
        """
        return self._online_point_config

    @online_point_config.setter
    def online_point_config(self, online_point_config):
        """Sets the online_point_config of this AssemblyConfigOutput.


        :param online_point_config: The online_point_config of this AssemblyConfigOutput.  # noqa: E501
        :type: OnlinePointConfigInputOutput
        """

        self._online_point_config = online_point_config

    @property
    def model_node_config(self):
        """Gets the model_node_config of this AssemblyConfigOutput.  # noqa: E501


        :return: The model_node_config of this AssemblyConfigOutput.  # noqa: E501
        :rtype: ModelNodeConfigInputOutput
        """
        return self._model_node_config

    @model_node_config.setter
    def model_node_config(self, model_node_config):
        """Sets the model_node_config of this AssemblyConfigOutput.


        :param model_node_config: The model_node_config of this AssemblyConfigOutput.  # noqa: E501
        :type: ModelNodeConfigInputOutput
        """

        self._model_node_config = model_node_config

    @property
    def mapping_config(self):
        """Gets the mapping_config of this AssemblyConfigOutput.  # noqa: E501


        :return: The mapping_config of this AssemblyConfigOutput.  # noqa: E501
        :rtype: MappingConfigInputOutput
        """
        return self._mapping_config

    @mapping_config.setter
    def mapping_config(self, mapping_config):
        """Sets the mapping_config of this AssemblyConfigOutput.


        :param mapping_config: The mapping_config of this AssemblyConfigOutput.  # noqa: E501
        :type: MappingConfigInputOutput
        """

        self._mapping_config = mapping_config

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
        if not isinstance(other, AssemblyConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssemblyConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
