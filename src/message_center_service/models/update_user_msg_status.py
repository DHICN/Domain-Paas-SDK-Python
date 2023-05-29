# coding: utf-8

"""
    message-center-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from message_center_service.configuration import Configuration


class UpdateUserMsgStatus(object):
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
        'receiver_user_id': 'str',
        'msg_type': 'str'
    }

    attribute_map = {
        'receiver_user_id': 'receiverUserId',
        'msg_type': 'msgType'
    }

    def __init__(self, receiver_user_id=None, msg_type=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUserMsgStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._receiver_user_id = None
        self._msg_type = None
        self.discriminator = None

        if receiver_user_id is not None:
            self.receiver_user_id = receiver_user_id
        self.msg_type = msg_type

    @property
    def receiver_user_id(self):
        """Gets the receiver_user_id of this UpdateUserMsgStatus.  # noqa: E501

        接收人ID  <br>receiver id  # noqa: E501

        :return: The receiver_user_id of this UpdateUserMsgStatus.  # noqa: E501
        :rtype: str
        """
        return self._receiver_user_id

    @receiver_user_id.setter
    def receiver_user_id(self, receiver_user_id):
        """Sets the receiver_user_id of this UpdateUserMsgStatus.

        接收人ID  <br>receiver id  # noqa: E501

        :param receiver_user_id: The receiver_user_id of this UpdateUserMsgStatus.  # noqa: E501
        :type: str
        """

        self._receiver_user_id = receiver_user_id

    @property
    def msg_type(self):
        """Gets the msg_type of this UpdateUserMsgStatus.  # noqa: E501

        消息类型  <br> message's type   # noqa: E501

        :return: The msg_type of this UpdateUserMsgStatus.  # noqa: E501
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        """Sets the msg_type of this UpdateUserMsgStatus.

        消息类型  <br> message's type   # noqa: E501

        :param msg_type: The msg_type of this UpdateUserMsgStatus.  # noqa: E501
        :type: str
        """

        self._msg_type = msg_type

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
        if not isinstance(other, UpdateUserMsgStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserMsgStatus):
            return True

        return self.to_dict() != other.to_dict()
