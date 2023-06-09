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


class UpdateRoleInput(object):
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
        'name': 'str',
        'remarks': 'str',
        'is_default': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remarks': 'remarks',
        'is_default': 'isDefault',
        'id': 'id'
    }

    def __init__(self, name=None, remarks=None, is_default=None, id=None, local_vars_configuration=None):  # noqa: E501
        """UpdateRoleInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._remarks = None
        self._is_default = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.remarks = remarks
        if is_default is not None:
            self.is_default = is_default
        self.id = id

    @property
    def name(self):
        """Gets the name of this UpdateRoleInput.  # noqa: E501

        角色名称 role name  # noqa: E501

        :return: The name of this UpdateRoleInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRoleInput.

        角色名称 role name  # noqa: E501

        :param name: The name of this UpdateRoleInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def remarks(self):
        """Gets the remarks of this UpdateRoleInput.  # noqa: E501

        角色备注 role remark  # noqa: E501

        :return: The remarks of this UpdateRoleInput.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this UpdateRoleInput.

        角色备注 role remark  # noqa: E501

        :param remarks: The remarks of this UpdateRoleInput.  # noqa: E501
        :type: str
        """

        self._remarks = remarks

    @property
    def is_default(self):
        """Gets the is_default of this UpdateRoleInput.  # noqa: E501

        是否默认角色 if it is the default role  # noqa: E501

        :return: The is_default of this UpdateRoleInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this UpdateRoleInput.

        是否默认角色 if it is the default role  # noqa: E501

        :param is_default: The is_default of this UpdateRoleInput.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def id(self):
        """Gets the id of this UpdateRoleInput.  # noqa: E501

        角色ID role id  # noqa: E501

        :return: The id of this UpdateRoleInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateRoleInput.

        角色ID role id  # noqa: E501

        :param id: The id of this UpdateRoleInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, UpdateRoleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateRoleInput):
            return True

        return self.to_dict() != other.to_dict()
