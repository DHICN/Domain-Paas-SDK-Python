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

from iot_service.configuration import Configuration


class InitOpcUaConfigInput(object):
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
        'opc_server_ip': 'str',
        'opc_server_port': 'str',
        'user_name': 'str',
        'password': 'str',
        'remarks': 'str'
    }

    attribute_map = {
        'opc_flag': 'opcFlag',
        'opc_server_ip': 'opcServerIp',
        'opc_server_port': 'opcServerPort',
        'user_name': 'userName',
        'password': 'password',
        'remarks': 'remarks'
    }

    def __init__(self, opc_flag=None, opc_server_ip=None, opc_server_port=None, user_name=None, password=None, remarks=None, local_vars_configuration=None):  # noqa: E501
        """InitOpcUaConfigInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._opc_flag = None
        self._opc_server_ip = None
        self._opc_server_port = None
        self._user_name = None
        self._password = None
        self._remarks = None
        self.discriminator = None

        self.opc_flag = opc_flag
        self.opc_server_ip = opc_server_ip
        self.opc_server_port = opc_server_port
        self.user_name = user_name
        self.password = password
        self.remarks = remarks

    @property
    def opc_flag(self):
        """Gets the opc_flag of this InitOpcUaConfigInput.  # noqa: E501

        标识 mark  # noqa: E501

        :return: The opc_flag of this InitOpcUaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._opc_flag

    @opc_flag.setter
    def opc_flag(self, opc_flag):
        """Sets the opc_flag of this InitOpcUaConfigInput.

        标识 mark  # noqa: E501

        :param opc_flag: The opc_flag of this InitOpcUaConfigInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and opc_flag is None:  # noqa: E501
            raise ValueError("Invalid value for `opc_flag`, must not be `None`")  # noqa: E501

        self._opc_flag = opc_flag

    @property
    def opc_server_ip(self):
        """Gets the opc_server_ip of this InitOpcUaConfigInput.  # noqa: E501

        Ip Ip  # noqa: E501

        :return: The opc_server_ip of this InitOpcUaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._opc_server_ip

    @opc_server_ip.setter
    def opc_server_ip(self, opc_server_ip):
        """Sets the opc_server_ip of this InitOpcUaConfigInput.

        Ip Ip  # noqa: E501

        :param opc_server_ip: The opc_server_ip of this InitOpcUaConfigInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and opc_server_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `opc_server_ip`, must not be `None`")  # noqa: E501

        self._opc_server_ip = opc_server_ip

    @property
    def opc_server_port(self):
        """Gets the opc_server_port of this InitOpcUaConfigInput.  # noqa: E501

        端口 port  # noqa: E501

        :return: The opc_server_port of this InitOpcUaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._opc_server_port

    @opc_server_port.setter
    def opc_server_port(self, opc_server_port):
        """Sets the opc_server_port of this InitOpcUaConfigInput.

        端口 port  # noqa: E501

        :param opc_server_port: The opc_server_port of this InitOpcUaConfigInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and opc_server_port is None:  # noqa: E501
            raise ValueError("Invalid value for `opc_server_port`, must not be `None`")  # noqa: E501

        self._opc_server_port = opc_server_port

    @property
    def user_name(self):
        """Gets the user_name of this InitOpcUaConfigInput.  # noqa: E501

        用户名 user name  # noqa: E501

        :return: The user_name of this InitOpcUaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this InitOpcUaConfigInput.

        用户名 user name  # noqa: E501

        :param user_name: The user_name of this InitOpcUaConfigInput.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this InitOpcUaConfigInput.  # noqa: E501

        密码 password  # noqa: E501

        :return: The password of this InitOpcUaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InitOpcUaConfigInput.

        密码 password  # noqa: E501

        :param password: The password of this InitOpcUaConfigInput.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def remarks(self):
        """Gets the remarks of this InitOpcUaConfigInput.  # noqa: E501

        备注 remarks  # noqa: E501

        :return: The remarks of this InitOpcUaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this InitOpcUaConfigInput.

        备注 remarks  # noqa: E501

        :param remarks: The remarks of this InitOpcUaConfigInput.  # noqa: E501
        :type: str
        """

        self._remarks = remarks

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
        if not isinstance(other, InitOpcUaConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InitOpcUaConfigInput):
            return True

        return self.to_dict() != other.to_dict()