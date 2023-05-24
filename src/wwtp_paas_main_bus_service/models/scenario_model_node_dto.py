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


class ScenarioModelNodeDto(object):
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
        'outlet_model_node': 'str',
        'rem_model_node': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'outlet_model_node': 'outletModelNode',
        'rem_model_node': 'remModelNode',
        'unit': 'unit'
    }

    def __init__(self, outlet_model_node=None, rem_model_node=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """ScenarioModelNodeDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._outlet_model_node = None
        self._rem_model_node = None
        self._unit = None
        self.discriminator = None

        self.outlet_model_node = outlet_model_node
        self.rem_model_node = rem_model_node
        self.unit = unit

    @property
    def outlet_model_node(self):
        """Gets the outlet_model_node of this ScenarioModelNodeDto.  # noqa: E501

        出水模型节点  # noqa: E501

        :return: The outlet_model_node of this ScenarioModelNodeDto.  # noqa: E501
        :rtype: str
        """
        return self._outlet_model_node

    @outlet_model_node.setter
    def outlet_model_node(self, outlet_model_node):
        """Sets the outlet_model_node of this ScenarioModelNodeDto.

        出水模型节点  # noqa: E501

        :param outlet_model_node: The outlet_model_node of this ScenarioModelNodeDto.  # noqa: E501
        :type: str
        """

        self._outlet_model_node = outlet_model_node

    @property
    def rem_model_node(self):
        """Gets the rem_model_node of this ScenarioModelNodeDto.  # noqa: E501

        去除率节点  # noqa: E501

        :return: The rem_model_node of this ScenarioModelNodeDto.  # noqa: E501
        :rtype: str
        """
        return self._rem_model_node

    @rem_model_node.setter
    def rem_model_node(self, rem_model_node):
        """Sets the rem_model_node of this ScenarioModelNodeDto.

        去除率节点  # noqa: E501

        :param rem_model_node: The rem_model_node of this ScenarioModelNodeDto.  # noqa: E501
        :type: str
        """

        self._rem_model_node = rem_model_node

    @property
    def unit(self):
        """Gets the unit of this ScenarioModelNodeDto.  # noqa: E501

        方案模型Code的单位  # noqa: E501

        :return: The unit of this ScenarioModelNodeDto.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ScenarioModelNodeDto.

        方案模型Code的单位  # noqa: E501

        :param unit: The unit of this ScenarioModelNodeDto.  # noqa: E501
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
        if not isinstance(other, ScenarioModelNodeDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScenarioModelNodeDto):
            return True

        return self.to_dict() != other.to_dict()
