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


class WriteNodeInput(object):
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
        'node': 'str',
        'node_value': 'str',
        'data_type': 'int'
    }

    attribute_map = {
        'opc_flag': 'opcFlag',
        'node': 'node',
        'node_value': 'nodeValue',
        'data_type': 'dataType'
    }

    def __init__(self, opc_flag=None, node=None, node_value=None, data_type=None, local_vars_configuration=None):  # noqa: E501
        """WriteNodeInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opc_flag = None
        self._node = None
        self._node_value = None
        self._data_type = None
        self.discriminator = None

        self.opc_flag = opc_flag
        self.node = node
        self.node_value = node_value
        self.data_type = data_type

    @property
    def opc_flag(self):
        """Gets the opc_flag of this WriteNodeInput.  # noqa: E501

        opc server 标识 mark  # noqa: E501

        :return: The opc_flag of this WriteNodeInput.  # noqa: E501
        :rtype: str
        """
        return self._opc_flag

    @opc_flag.setter
    def opc_flag(self, opc_flag):
        """Sets the opc_flag of this WriteNodeInput.

        opc server 标识 mark  # noqa: E501

        :param opc_flag: The opc_flag of this WriteNodeInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and opc_flag is None:  # noqa: E501
            raise ValueError("Invalid value for `opc_flag`, must not be `None`")  # noqa: E501

        self._opc_flag = opc_flag

    @property
    def node(self):
        """Gets the node of this WriteNodeInput.  # noqa: E501

        节点 node  # noqa: E501

        :return: The node of this WriteNodeInput.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this WriteNodeInput.

        节点 node  # noqa: E501

        :param node: The node of this WriteNodeInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and node is None:  # noqa: E501
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def node_value(self):
        """Gets the node_value of this WriteNodeInput.  # noqa: E501

        节点值 node value  # noqa: E501

        :return: The node_value of this WriteNodeInput.  # noqa: E501
        :rtype: str
        """
        return self._node_value

    @node_value.setter
    def node_value(self, node_value):
        """Sets the node_value of this WriteNodeInput.

        节点值 node value  # noqa: E501

        :param node_value: The node_value of this WriteNodeInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and node_value is None:  # noqa: E501
            raise ValueError("Invalid value for `node_value`, must not be `None`")  # noqa: E501

        self._node_value = node_value

    @property
    def data_type(self):
        """Gets the data_type of this WriteNodeInput.  # noqa: E501

        0-BoolValue 1-DateTimeValue 2-DblValue 3-LongValue 4-StrValue 5-FloatValue 6-UInt32Value 7-UInt16Value 8-Int32Value 9-Int16Value   # noqa: E501

        :return: The data_type of this WriteNodeInput.  # noqa: E501
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this WriteNodeInput.

        0-BoolValue 1-DateTimeValue 2-DblValue 3-LongValue 4-StrValue 5-FloatValue 6-UInt32Value 7-UInt16Value 8-Int32Value 9-Int16Value   # noqa: E501

        :param data_type: The data_type of this WriteNodeInput.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

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
        if not isinstance(other, WriteNodeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WriteNodeInput):
            return True

        return self.to_dict() != other.to_dict()
