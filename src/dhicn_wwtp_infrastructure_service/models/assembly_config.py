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


class AssemblyConfig(object):
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
        'sys_input_output_code_configs': 'list[SysCodeConfigInputOutput]',
        'mapping_dic': 'dict(str, object)',
        'online_point_dic': 'dict(str, object)',
        'model_nodes_dic': 'dict(str, object)'
    }

    attribute_map = {
        'sys_input_output_code_configs': 'sysInputOutputCodeConfigs',
        'mapping_dic': 'mappingDic',
        'online_point_dic': 'onlinePointDic',
        'model_nodes_dic': 'modelNodesDic'
    }

    def __init__(self, sys_input_output_code_configs=None, mapping_dic=None, online_point_dic=None, model_nodes_dic=None, local_vars_configuration=None):  # noqa: E501
        """AssemblyConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sys_input_output_code_configs = None
        self._mapping_dic = None
        self._online_point_dic = None
        self._model_nodes_dic = None
        self.discriminator = None

        self.sys_input_output_code_configs = sys_input_output_code_configs
        self.mapping_dic = mapping_dic
        self.online_point_dic = online_point_dic
        self.model_nodes_dic = model_nodes_dic

    @property
    def sys_input_output_code_configs(self):
        """Gets the sys_input_output_code_configs of this AssemblyConfig.  # noqa: E501


        :return: The sys_input_output_code_configs of this AssemblyConfig.  # noqa: E501
        :rtype: list[SysCodeConfigInputOutput]
        """
        return self._sys_input_output_code_configs

    @sys_input_output_code_configs.setter
    def sys_input_output_code_configs(self, sys_input_output_code_configs):
        """Sets the sys_input_output_code_configs of this AssemblyConfig.


        :param sys_input_output_code_configs: The sys_input_output_code_configs of this AssemblyConfig.  # noqa: E501
        :type: list[SysCodeConfigInputOutput]
        """

        self._sys_input_output_code_configs = sys_input_output_code_configs

    @property
    def mapping_dic(self):
        """Gets the mapping_dic of this AssemblyConfig.  # noqa: E501


        :return: The mapping_dic of this AssemblyConfig.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._mapping_dic

    @mapping_dic.setter
    def mapping_dic(self, mapping_dic):
        """Sets the mapping_dic of this AssemblyConfig.


        :param mapping_dic: The mapping_dic of this AssemblyConfig.  # noqa: E501
        :type: dict(str, object)
        """

        self._mapping_dic = mapping_dic

    @property
    def online_point_dic(self):
        """Gets the online_point_dic of this AssemblyConfig.  # noqa: E501


        :return: The online_point_dic of this AssemblyConfig.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._online_point_dic

    @online_point_dic.setter
    def online_point_dic(self, online_point_dic):
        """Sets the online_point_dic of this AssemblyConfig.


        :param online_point_dic: The online_point_dic of this AssemblyConfig.  # noqa: E501
        :type: dict(str, object)
        """

        self._online_point_dic = online_point_dic

    @property
    def model_nodes_dic(self):
        """Gets the model_nodes_dic of this AssemblyConfig.  # noqa: E501


        :return: The model_nodes_dic of this AssemblyConfig.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._model_nodes_dic

    @model_nodes_dic.setter
    def model_nodes_dic(self, model_nodes_dic):
        """Sets the model_nodes_dic of this AssemblyConfig.


        :param model_nodes_dic: The model_nodes_dic of this AssemblyConfig.  # noqa: E501
        :type: dict(str, object)
        """

        self._model_nodes_dic = model_nodes_dic

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
        if not isinstance(other, AssemblyConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssemblyConfig):
            return True

        return self.to_dict() != other.to_dict()