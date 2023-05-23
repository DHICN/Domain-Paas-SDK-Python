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


class TenantAdminDto(object):
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
        'tenant_admin_user_id': 'str',
        'tenant_admin_user_name': 'str'
    }

    attribute_map = {
        'tenant_admin_user_id': 'tenantAdminUserId',
        'tenant_admin_user_name': 'tenantAdminUserName'
    }

    def __init__(self, tenant_admin_user_id=None, tenant_admin_user_name=None, local_vars_configuration=None):  # noqa: E501
        """TenantAdminDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tenant_admin_user_id = None
        self._tenant_admin_user_name = None
        self.discriminator = None

        if tenant_admin_user_id is not None:
            self.tenant_admin_user_id = tenant_admin_user_id
        self.tenant_admin_user_name = tenant_admin_user_name

    @property
    def tenant_admin_user_id(self):
        """Gets the tenant_admin_user_id of this TenantAdminDto.  # noqa: E501

        租户管理员账户ID tenant administrator id  # noqa: E501

        :return: The tenant_admin_user_id of this TenantAdminDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_admin_user_id

    @tenant_admin_user_id.setter
    def tenant_admin_user_id(self, tenant_admin_user_id):
        """Sets the tenant_admin_user_id of this TenantAdminDto.

        租户管理员账户ID tenant administrator id  # noqa: E501

        :param tenant_admin_user_id: The tenant_admin_user_id of this TenantAdminDto.  # noqa: E501
        :type: str
        """

        self._tenant_admin_user_id = tenant_admin_user_id

    @property
    def tenant_admin_user_name(self):
        """Gets the tenant_admin_user_name of this TenantAdminDto.  # noqa: E501

        租户管理员账户名称 tenant administrator name  # noqa: E501

        :return: The tenant_admin_user_name of this TenantAdminDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_admin_user_name

    @tenant_admin_user_name.setter
    def tenant_admin_user_name(self, tenant_admin_user_name):
        """Sets the tenant_admin_user_name of this TenantAdminDto.

        租户管理员账户名称 tenant administrator name  # noqa: E501

        :param tenant_admin_user_name: The tenant_admin_user_name of this TenantAdminDto.  # noqa: E501
        :type: str
        """

        self._tenant_admin_user_name = tenant_admin_user_name

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
        if not isinstance(other, TenantAdminDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantAdminDto):
            return True

        return self.to_dict() != other.to_dict()
