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


class MenuPerTree(object):
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
        'label': 'str',
        'is_check': 'bool',
        'menu_router': 'str',
        'regular': 'str',
        'api_regular': 'str',
        'children': 'list[MenuPerTree]'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'is_check': 'isCheck',
        'menu_router': 'menuRouter',
        'regular': 'regular',
        'api_regular': 'apiRegular',
        'children': 'children'
    }

    def __init__(self, id=None, label=None, is_check=None, menu_router=None, regular=None, api_regular=None, children=None, local_vars_configuration=None):  # noqa: E501
        """MenuPerTree - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._label = None
        self._is_check = None
        self._menu_router = None
        self._regular = None
        self._api_regular = None
        self._children = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.label = label
        if is_check is not None:
            self.is_check = is_check
        self.menu_router = menu_router
        self.regular = regular
        self.api_regular = api_regular
        self.children = children

    @property
    def id(self):
        """Gets the id of this MenuPerTree.  # noqa: E501

        菜单Id menu id  # noqa: E501

        :return: The id of this MenuPerTree.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MenuPerTree.

        菜单Id menu id  # noqa: E501

        :param id: The id of this MenuPerTree.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this MenuPerTree.  # noqa: E501

        菜单名称 menu label  # noqa: E501

        :return: The label of this MenuPerTree.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MenuPerTree.

        菜单名称 menu label  # noqa: E501

        :param label: The label of this MenuPerTree.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def is_check(self):
        """Gets the is_check of this MenuPerTree.  # noqa: E501

        是否选中状态 if it is checked  # noqa: E501

        :return: The is_check of this MenuPerTree.  # noqa: E501
        :rtype: bool
        """
        return self._is_check

    @is_check.setter
    def is_check(self, is_check):
        """Sets the is_check of this MenuPerTree.

        是否选中状态 if it is checked  # noqa: E501

        :param is_check: The is_check of this MenuPerTree.  # noqa: E501
        :type: bool
        """

        self._is_check = is_check

    @property
    def menu_router(self):
        """Gets the menu_router of this MenuPerTree.  # noqa: E501

        菜单路由  # noqa: E501

        :return: The menu_router of this MenuPerTree.  # noqa: E501
        :rtype: str
        """
        return self._menu_router

    @menu_router.setter
    def menu_router(self, menu_router):
        """Sets the menu_router of this MenuPerTree.

        菜单路由  # noqa: E501

        :param menu_router: The menu_router of this MenuPerTree.  # noqa: E501
        :type: str
        """

        self._menu_router = menu_router

    @property
    def regular(self):
        """Gets the regular of this MenuPerTree.  # noqa: E501

        按钮路由  # noqa: E501

        :return: The regular of this MenuPerTree.  # noqa: E501
        :rtype: str
        """
        return self._regular

    @regular.setter
    def regular(self, regular):
        """Sets the regular of this MenuPerTree.

        按钮路由  # noqa: E501

        :param regular: The regular of this MenuPerTree.  # noqa: E501
        :type: str
        """

        self._regular = regular

    @property
    def api_regular(self):
        """Gets the api_regular of this MenuPerTree.  # noqa: E501

        后端API权限规则  # noqa: E501

        :return: The api_regular of this MenuPerTree.  # noqa: E501
        :rtype: str
        """
        return self._api_regular

    @api_regular.setter
    def api_regular(self, api_regular):
        """Sets the api_regular of this MenuPerTree.

        后端API权限规则  # noqa: E501

        :param api_regular: The api_regular of this MenuPerTree.  # noqa: E501
        :type: str
        """

        self._api_regular = api_regular

    @property
    def children(self):
        """Gets the children of this MenuPerTree.  # noqa: E501

        子菜单 sub menus  # noqa: E501

        :return: The children of this MenuPerTree.  # noqa: E501
        :rtype: list[MenuPerTree]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this MenuPerTree.

        子菜单 sub menus  # noqa: E501

        :param children: The children of this MenuPerTree.  # noqa: E501
        :type: list[MenuPerTree]
        """

        self._children = children

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
        if not isinstance(other, MenuPerTree):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MenuPerTree):
            return True

        return self.to_dict() != other.to_dict()
