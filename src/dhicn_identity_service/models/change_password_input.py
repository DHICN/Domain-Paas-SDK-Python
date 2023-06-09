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

from dhicn_identity_service.configuration import Configuration


class ChangePasswordInput(object):
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
        'user_id': 'str',
        'current_password': 'str',
        'new_password': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'current_password': 'currentPassword',
        'new_password': 'newPassword'
    }

    def __init__(self, user_id=None, current_password=None, new_password=None, local_vars_configuration=None):  # noqa: E501
        """ChangePasswordInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._current_password = None
        self._new_password = None
        self.discriminator = None

        self.user_id = user_id
        self.current_password = current_password
        self.new_password = new_password

    @property
    def user_id(self):
        """Gets the user_id of this ChangePasswordInput.  # noqa: E501

        用户ID user id  # noqa: E501

        :return: The user_id of this ChangePasswordInput.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ChangePasswordInput.

        用户ID user id  # noqa: E501

        :param user_id: The user_id of this ChangePasswordInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def current_password(self):
        """Gets the current_password of this ChangePasswordInput.  # noqa: E501

        当前密码 current password  # noqa: E501

        :return: The current_password of this ChangePasswordInput.  # noqa: E501
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """Sets the current_password of this ChangePasswordInput.

        当前密码 current password  # noqa: E501

        :param current_password: The current_password of this ChangePasswordInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and current_password is None:  # noqa: E501
            raise ValueError("Invalid value for `current_password`, must not be `None`")  # noqa: E501

        self._current_password = current_password

    @property
    def new_password(self):
        """Gets the new_password of this ChangePasswordInput.  # noqa: E501

        新密码 new password  # noqa: E501

        :return: The new_password of this ChangePasswordInput.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ChangePasswordInput.

        新密码 new password  # noqa: E501

        :param new_password: The new_password of this ChangePasswordInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and new_password is None:  # noqa: E501
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501

        self._new_password = new_password

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
        if not isinstance(other, ChangePasswordInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangePasswordInput):
            return True

        return self.to_dict() != other.to_dict()
