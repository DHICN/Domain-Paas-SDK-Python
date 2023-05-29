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


class AddMsgTypeTempLocalInput(object):
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
        'msg_type': 'str',
        'language': 'str',
        'msg_template': 'MsgTemplateObj'
    }

    attribute_map = {
        'msg_type': 'msgType',
        'language': 'language',
        'msg_template': 'msgTemplate'
    }

    def __init__(self, msg_type=None, language=None, msg_template=None, local_vars_configuration=None):  # noqa: E501
        """AddMsgTypeTempLocalInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._msg_type = None
        self._language = None
        self._msg_template = None
        self.discriminator = None

        self.msg_type = msg_type
        self.language = language
        self.msg_template = msg_template

    @property
    def msg_type(self):
        """Gets the msg_type of this AddMsgTypeTempLocalInput.  # noqa: E501

        消息类型  <br> message's type   # noqa: E501

        :return: The msg_type of this AddMsgTypeTempLocalInput.  # noqa: E501
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        """Sets the msg_type of this AddMsgTypeTempLocalInput.

        消息类型  <br> message's type   # noqa: E501

        :param msg_type: The msg_type of this AddMsgTypeTempLocalInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and msg_type is None:  # noqa: E501
            raise ValueError("Invalid value for `msg_type`, must not be `None`")  # noqa: E501

        self._msg_type = msg_type

    @property
    def language(self):
        """Gets the language of this AddMsgTypeTempLocalInput.  # noqa: E501

        模板语言  <br> tempalte's language   # noqa: E501

        :return: The language of this AddMsgTypeTempLocalInput.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AddMsgTypeTempLocalInput.

        模板语言  <br> tempalte's language   # noqa: E501

        :param language: The language of this AddMsgTypeTempLocalInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def msg_template(self):
        """Gets the msg_template of this AddMsgTypeTempLocalInput.  # noqa: E501


        :return: The msg_template of this AddMsgTypeTempLocalInput.  # noqa: E501
        :rtype: MsgTemplateObj
        """
        return self._msg_template

    @msg_template.setter
    def msg_template(self, msg_template):
        """Sets the msg_template of this AddMsgTypeTempLocalInput.


        :param msg_template: The msg_template of this AddMsgTypeTempLocalInput.  # noqa: E501
        :type: MsgTemplateObj
        """
        if self.local_vars_configuration.client_side_validation and msg_template is None:  # noqa: E501
            raise ValueError("Invalid value for `msg_template`, must not be `None`")  # noqa: E501

        self._msg_template = msg_template

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
        if not isinstance(other, AddMsgTypeTempLocalInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddMsgTypeTempLocalInput):
            return True

        return self.to_dict() != other.to_dict()
