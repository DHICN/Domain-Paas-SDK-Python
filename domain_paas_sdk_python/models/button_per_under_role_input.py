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


class ButtonPerUnderRoleInput(object):
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
        'role_id': 'str',
        'menu_ids': 'list[str]'
    }

    attribute_map = {
        'role_id': 'roleId',
        'menu_ids': 'menuIds'
    }

    def __init__(self, role_id=None, menu_ids=None, local_vars_configuration=None):  # noqa: E501
        """ButtonPerUnderRoleInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._role_id = None
        self._menu_ids = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        self.menu_ids = menu_ids

    @property
    def role_id(self):
        """Gets the role_id of this ButtonPerUnderRoleInput.  # noqa: E501

        角色Id role id  # noqa: E501

        :return: The role_id of this ButtonPerUnderRoleInput.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this ButtonPerUnderRoleInput.

        角色Id role id  # noqa: E501

        :param role_id: The role_id of this ButtonPerUnderRoleInput.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def menu_ids(self):
        """Gets the menu_ids of this ButtonPerUnderRoleInput.  # noqa: E501

        选中的菜单Id列表 checked menu ids  # noqa: E501

        :return: The menu_ids of this ButtonPerUnderRoleInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._menu_ids

    @menu_ids.setter
    def menu_ids(self, menu_ids):
        """Sets the menu_ids of this ButtonPerUnderRoleInput.

        选中的菜单Id列表 checked menu ids  # noqa: E501

        :param menu_ids: The menu_ids of this ButtonPerUnderRoleInput.  # noqa: E501
        :type: list[str]
        """

        self._menu_ids = menu_ids

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
        if not isinstance(other, ButtonPerUnderRoleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ButtonPerUnderRoleInput):
            return True

        return self.to_dict() != other.to_dict()
