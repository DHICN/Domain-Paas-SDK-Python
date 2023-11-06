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

from dhicn_iot_service.configuration import Configuration


class QueryOpcUaPubSubInput(object):
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
        'opc_flag': 'str',
        'sub_key': 'str',
        'node': 'str',
        'notify_pattern': 'str'
    }

    attribute_map = {
        'opc_flag': 'opcFlag',
        'sub_key': 'subKey',
        'node': 'node',
        'notify_pattern': 'notifyPattern'
    }

    def __init__(self, opc_flag=None, sub_key=None, node=None, notify_pattern=None, local_vars_configuration=None):  # noqa: E501
        """QueryOpcUaPubSubInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opc_flag = None
        self._sub_key = None
        self._node = None
        self._notify_pattern = None
        self.discriminator = None

        self.opc_flag = opc_flag
        self.sub_key = sub_key
        self.node = node
        self.notify_pattern = notify_pattern

    @property
    def opc_flag(self):
        """Gets the opc_flag of this QueryOpcUaPubSubInput.  # noqa: E501

        标识,OpcUaConfig表的OpcFlag mark,OpcFlag of OpcUaConfig table  # noqa: E501

        :return: The opc_flag of this QueryOpcUaPubSubInput.  # noqa: E501
        :rtype: str
        """
        return self._opc_flag

    @opc_flag.setter
    def opc_flag(self, opc_flag):
        """Sets the opc_flag of this QueryOpcUaPubSubInput.

        标识,OpcUaConfig表的OpcFlag mark,OpcFlag of OpcUaConfig table  # noqa: E501

        :param opc_flag: The opc_flag of this QueryOpcUaPubSubInput.  # noqa: E501
        :type: str
        """

        self._opc_flag = opc_flag

    @property
    def sub_key(self):
        """Gets the sub_key of this QueryOpcUaPubSubInput.  # noqa: E501

        订阅回调标识Key subscription callback ID Key  # noqa: E501

        :return: The sub_key of this QueryOpcUaPubSubInput.  # noqa: E501
        :rtype: str
        """
        return self._sub_key

    @sub_key.setter
    def sub_key(self, sub_key):
        """Sets the sub_key of this QueryOpcUaPubSubInput.

        订阅回调标识Key subscription callback ID Key  # noqa: E501

        :param sub_key: The sub_key of this QueryOpcUaPubSubInput.  # noqa: E501
        :type: str
        """

        self._sub_key = sub_key

    @property
    def node(self):
        """Gets the node of this QueryOpcUaPubSubInput.  # noqa: E501

        要订阅的节点名 node name to subscribe to  # noqa: E501

        :return: The node of this QueryOpcUaPubSubInput.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this QueryOpcUaPubSubInput.

        要订阅的节点名 node name to subscribe to  # noqa: E501

        :param node: The node of this QueryOpcUaPubSubInput.  # noqa: E501
        :type: str
        """

        self._node = node

    @property
    def notify_pattern(self):
        """Gets the notify_pattern of this QueryOpcUaPubSubInput.  # noqa: E501

        通知模式：kafka,notify,rabitmq notification mode: kafka,notify,rabitmq, etc.  # noqa: E501

        :return: The notify_pattern of this QueryOpcUaPubSubInput.  # noqa: E501
        :rtype: str
        """
        return self._notify_pattern

    @notify_pattern.setter
    def notify_pattern(self, notify_pattern):
        """Sets the notify_pattern of this QueryOpcUaPubSubInput.

        通知模式：kafka,notify,rabitmq notification mode: kafka,notify,rabitmq, etc.  # noqa: E501

        :param notify_pattern: The notify_pattern of this QueryOpcUaPubSubInput.  # noqa: E501
        :type: str
        """

        self._notify_pattern = notify_pattern

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
        if not isinstance(other, QueryOpcUaPubSubInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryOpcUaPubSubInput):
            return True

        return self.to_dict() != other.to_dict()
