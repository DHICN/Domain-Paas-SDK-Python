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


class OpcUaPubSubPara(object):
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
        'id': 'str',
        'opc_flag': 'str',
        'sub_key': 'str',
        'node': 'str',
        'notify_pattern': 'str',
        'remarks': 'str',
        'notify_details': 'NotifyParams'
    }

    attribute_map = {
        'id': 'id',
        'opc_flag': 'opcFlag',
        'sub_key': 'subKey',
        'node': 'node',
        'notify_pattern': 'notifyPattern',
        'remarks': 'remarks',
        'notify_details': 'notifyDetails'
    }

    def __init__(self, id=None, opc_flag=None, sub_key=None, node=None, notify_pattern=None, remarks=None, notify_details=None, local_vars_configuration=None):  # noqa: E501
        """OpcUaPubSubPara - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._opc_flag = None
        self._sub_key = None
        self._node = None
        self._notify_pattern = None
        self._remarks = None
        self._notify_details = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.opc_flag = opc_flag
        self.sub_key = sub_key
        self.node = node
        self.notify_pattern = notify_pattern
        self.remarks = remarks
        if notify_details is not None:
            self.notify_details = notify_details

    @property
    def id(self):
        """Gets the id of this OpcUaPubSubPara.  # noqa: E501

        Id Id  # noqa: E501

        :return: The id of this OpcUaPubSubPara.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OpcUaPubSubPara.

        Id Id  # noqa: E501

        :param id: The id of this OpcUaPubSubPara.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def opc_flag(self):
        """Gets the opc_flag of this OpcUaPubSubPara.  # noqa: E501

        标识,OpcUaConfig表的OpcFlag mark,OpcFlag of OpcUaConfig table  # noqa: E501

        :return: The opc_flag of this OpcUaPubSubPara.  # noqa: E501
        :rtype: str
        """
        return self._opc_flag

    @opc_flag.setter
    def opc_flag(self, opc_flag):
        """Sets the opc_flag of this OpcUaPubSubPara.

        标识,OpcUaConfig表的OpcFlag mark,OpcFlag of OpcUaConfig table  # noqa: E501

        :param opc_flag: The opc_flag of this OpcUaPubSubPara.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and opc_flag is None:  # noqa: E501
            raise ValueError("Invalid value for `opc_flag`, must not be `None`")  # noqa: E501

        self._opc_flag = opc_flag

    @property
    def sub_key(self):
        """Gets the sub_key of this OpcUaPubSubPara.  # noqa: E501

        订阅回调标识Key subscription callback ID Key  # noqa: E501

        :return: The sub_key of this OpcUaPubSubPara.  # noqa: E501
        :rtype: str
        """
        return self._sub_key

    @sub_key.setter
    def sub_key(self, sub_key):
        """Sets the sub_key of this OpcUaPubSubPara.

        订阅回调标识Key subscription callback ID Key  # noqa: E501

        :param sub_key: The sub_key of this OpcUaPubSubPara.  # noqa: E501
        :type: str
        """

        self._sub_key = sub_key

    @property
    def node(self):
        """Gets the node of this OpcUaPubSubPara.  # noqa: E501

        要订阅的节点名 node name to subscribe to  # noqa: E501

        :return: The node of this OpcUaPubSubPara.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this OpcUaPubSubPara.

        要订阅的节点名 node name to subscribe to  # noqa: E501

        :param node: The node of this OpcUaPubSubPara.  # noqa: E501
        :type: str
        """

        self._node = node

    @property
    def notify_pattern(self):
        """Gets the notify_pattern of this OpcUaPubSubPara.  # noqa: E501

        通知模式：kafka,notify,rabitmq notification mode: kafka,notify,rabitmq, etc.  # noqa: E501

        :return: The notify_pattern of this OpcUaPubSubPara.  # noqa: E501
        :rtype: str
        """
        return self._notify_pattern

    @notify_pattern.setter
    def notify_pattern(self, notify_pattern):
        """Sets the notify_pattern of this OpcUaPubSubPara.

        通知模式：kafka,notify,rabitmq notification mode: kafka,notify,rabitmq, etc.  # noqa: E501

        :param notify_pattern: The notify_pattern of this OpcUaPubSubPara.  # noqa: E501
        :type: str
        """

        self._notify_pattern = notify_pattern

    @property
    def remarks(self):
        """Gets the remarks of this OpcUaPubSubPara.  # noqa: E501

        备注 remarks  # noqa: E501

        :return: The remarks of this OpcUaPubSubPara.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this OpcUaPubSubPara.

        备注 remarks  # noqa: E501

        :param remarks: The remarks of this OpcUaPubSubPara.  # noqa: E501
        :type: str
        """

        self._remarks = remarks

    @property
    def notify_details(self):
        """Gets the notify_details of this OpcUaPubSubPara.  # noqa: E501


        :return: The notify_details of this OpcUaPubSubPara.  # noqa: E501
        :rtype: NotifyParams
        """
        return self._notify_details

    @notify_details.setter
    def notify_details(self, notify_details):
        """Sets the notify_details of this OpcUaPubSubPara.


        :param notify_details: The notify_details of this OpcUaPubSubPara.  # noqa: E501
        :type: NotifyParams
        """

        self._notify_details = notify_details

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
        if not isinstance(other, OpcUaPubSubPara):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpcUaPubSubPara):
            return True

        return self.to_dict() != other.to_dict()
