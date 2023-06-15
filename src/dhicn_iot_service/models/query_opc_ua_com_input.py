# coding: utf-8

"""
    iot-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_iot_service.configuration import Configuration


class QueryOpcUaComInput(object):
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
        'indicator_id': 'str',
        'node_name': 'str',
        'node': 'str'
    }

    attribute_map = {
        'indicator_id': 'indicatorId',
        'node_name': 'nodeName',
        'node': 'node'
    }

    def __init__(self, indicator_id=None, node_name=None, node=None, local_vars_configuration=None):  # noqa: E501
        """QueryOpcUaComInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._indicator_id = None
        self._node_name = None
        self._node = None
        self.discriminator = None

        self.indicator_id = indicator_id
        self.node_name = node_name
        self.node = node

    @property
    def indicator_id(self):
        """Gets the indicator_id of this QueryOpcUaComInput.  # noqa: E501

        设备指标Id，对应着设备-指标 device indicator id  # noqa: E501

        :return: The indicator_id of this QueryOpcUaComInput.  # noqa: E501
        :rtype: str
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this QueryOpcUaComInput.

        设备指标Id，对应着设备-指标 device indicator id  # noqa: E501

        :param indicator_id: The indicator_id of this QueryOpcUaComInput.  # noqa: E501
        :type: str
        """

        self._indicator_id = indicator_id

    @property
    def node_name(self):
        """Gets the node_name of this QueryOpcUaComInput.  # noqa: E501

        节点名称，如:主线静压式液位 node name  # noqa: E501

        :return: The node_name of this QueryOpcUaComInput.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this QueryOpcUaComInput.

        节点名称，如:主线静压式液位 node name  # noqa: E501

        :param node_name: The node_name of this QueryOpcUaComInput.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def node(self):
        """Gets the node of this QueryOpcUaComInput.  # noqa: E501

        节点检测项 node detection item  # noqa: E501

        :return: The node of this QueryOpcUaComInput.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this QueryOpcUaComInput.

        节点检测项 node detection item  # noqa: E501

        :param node: The node of this QueryOpcUaComInput.  # noqa: E501
        :type: str
        """

        self._node = node

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
        if not isinstance(other, QueryOpcUaComInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryOpcUaComInput):
            return True

        return self.to_dict() != other.to_dict()