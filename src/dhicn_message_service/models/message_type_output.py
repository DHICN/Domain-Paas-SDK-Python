# coding: utf-8

"""
    消息服务

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_message_service.configuration import Configuration


class MessageTypeOutput(object):
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
        'msg_type': 'str',
        'show_name': 'str',
        'order': 'int'
    }

    attribute_map = {
        'id': 'id',
        'msg_type': 'msgType',
        'show_name': 'showName',
        'order': 'order'
    }

    def __init__(self, id=None, msg_type=None, show_name=None, order=None, local_vars_configuration=None):  # noqa: E501
        """MessageTypeOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._msg_type = None
        self._show_name = None
        self._order = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.msg_type = msg_type
        self.show_name = show_name
        if order is not None:
            self.order = order

    @property
    def id(self):
        """Gets the id of this MessageTypeOutput.  # noqa: E501


        :return: The id of this MessageTypeOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessageTypeOutput.


        :param id: The id of this MessageTypeOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def msg_type(self):
        """Gets the msg_type of this MessageTypeOutput.  # noqa: E501

        消息类型  <br> message's type   # noqa: E501

        :return: The msg_type of this MessageTypeOutput.  # noqa: E501
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        """Sets the msg_type of this MessageTypeOutput.

        消息类型  <br> message's type   # noqa: E501

        :param msg_type: The msg_type of this MessageTypeOutput.  # noqa: E501
        :type: str
        """

        self._msg_type = msg_type

    @property
    def show_name(self):
        """Gets the show_name of this MessageTypeOutput.  # noqa: E501

        显示名  <br> display's name   # noqa: E501

        :return: The show_name of this MessageTypeOutput.  # noqa: E501
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        """Sets the show_name of this MessageTypeOutput.

        显示名  <br> display's name   # noqa: E501

        :param show_name: The show_name of this MessageTypeOutput.  # noqa: E501
        :type: str
        """

        self._show_name = show_name

    @property
    def order(self):
        """Gets the order of this MessageTypeOutput.  # noqa: E501

        排序 order number  # noqa: E501

        :return: The order of this MessageTypeOutput.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this MessageTypeOutput.

        排序 order number  # noqa: E501

        :param order: The order of this MessageTypeOutput.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if not isinstance(other, MessageTypeOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageTypeOutput):
            return True

        return self.to_dict() != other.to_dict()
