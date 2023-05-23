# coding: utf-8

"""
    identity-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from domain_paas_sdk_python.configuration import Configuration


class SelectItemNode(object):
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
        'node_type': 'int',
        'code': 'str',
        'name': 'str',
        'detailed_info': 'SelectItemNodeDetailInfo',
        'child_nodes': 'list[SelectItemNode]'
    }

    attribute_map = {
        'node_type': 'nodeType',
        'code': 'code',
        'name': 'name',
        'detailed_info': 'detailedInfo',
        'child_nodes': 'childNodes'
    }

    def __init__(self, node_type=None, code=None, name=None, detailed_info=None, child_nodes=None, local_vars_configuration=None):  # noqa: E501
        """SelectItemNode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._node_type = None
        self._code = None
        self._name = None
        self._detailed_info = None
        self._child_nodes = None
        self.discriminator = None

        if node_type is not None:
            self.node_type = node_type
        self.code = code
        self.name = name
        if detailed_info is not None:
            self.detailed_info = detailed_info
        self.child_nodes = child_nodes

    @property
    def node_type(self):
        """Gets the node_type of this SelectItemNode.  # noqa: E501

        选择节点的类型 select node type  # noqa: E501

        :return: The node_type of this SelectItemNode.  # noqa: E501
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this SelectItemNode.

        选择节点的类型 select node type  # noqa: E501

        :param node_type: The node_type of this SelectItemNode.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and node_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def code(self):
        """Gets the code of this SelectItemNode.  # noqa: E501

        代码 code  # noqa: E501

        :return: The code of this SelectItemNode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SelectItemNode.

        代码 code  # noqa: E501

        :param code: The code of this SelectItemNode.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this SelectItemNode.  # noqa: E501

        名称，用于显示 name for display  # noqa: E501

        :return: The name of this SelectItemNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SelectItemNode.

        名称，用于显示 name for display  # noqa: E501

        :param name: The name of this SelectItemNode.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def detailed_info(self):
        """Gets the detailed_info of this SelectItemNode.  # noqa: E501


        :return: The detailed_info of this SelectItemNode.  # noqa: E501
        :rtype: SelectItemNodeDetailInfo
        """
        return self._detailed_info

    @detailed_info.setter
    def detailed_info(self, detailed_info):
        """Sets the detailed_info of this SelectItemNode.


        :param detailed_info: The detailed_info of this SelectItemNode.  # noqa: E501
        :type: SelectItemNodeDetailInfo
        """

        self._detailed_info = detailed_info

    @property
    def child_nodes(self):
        """Gets the child_nodes of this SelectItemNode.  # noqa: E501

        子节点列表 sub node list  # noqa: E501

        :return: The child_nodes of this SelectItemNode.  # noqa: E501
        :rtype: list[SelectItemNode]
        """
        return self._child_nodes

    @child_nodes.setter
    def child_nodes(self, child_nodes):
        """Sets the child_nodes of this SelectItemNode.

        子节点列表 sub node list  # noqa: E501

        :param child_nodes: The child_nodes of this SelectItemNode.  # noqa: E501
        :type: list[SelectItemNode]
        """

        self._child_nodes = child_nodes

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
        if not isinstance(other, SelectItemNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SelectItemNode):
            return True

        return self.to_dict() != other.to_dict()
