# coding: utf-8

"""
    scenario-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from scenario_manager_service.configuration import Configuration


class Group(object):
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
        'name': 'str',
        'parent_id': 'str',
        'group_type': 'int',
        'item_ref': 'str',
        'group_family': 'str',
        'group_level': 'str',
        'item_id': 'str',
        'version': 'str',
        'tenant_id': 'str',
        'parent': 'Group',
        'path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent_id': 'parentId',
        'group_type': 'groupType',
        'item_ref': 'itemRef',
        'group_family': 'groupFamily',
        'group_level': 'groupLevel',
        'item_id': 'itemId',
        'version': 'version',
        'tenant_id': 'tenantId',
        'parent': 'parent',
        'path': 'path'
    }

    def __init__(self, id=None, name=None, parent_id=None, group_type=None, item_ref=None, group_family=None, group_level=None, item_id=None, version=None, tenant_id=None, parent=None, path=None, local_vars_configuration=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._parent_id = None
        self._group_type = None
        self._item_ref = None
        self._group_family = None
        self._group_level = None
        self._item_id = None
        self._version = None
        self._tenant_id = None
        self._parent = None
        self._path = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.parent_id = parent_id
        if group_type is not None:
            self.group_type = group_type
        self.item_ref = item_ref
        self.group_family = group_family
        self.group_level = group_level
        if item_id is not None:
            self.item_id = item_id
        if version is not None:
            self.version = version
        self.tenant_id = tenant_id
        if parent is not None:
            self.parent = parent
        self.path = path

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501


        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.


        :param name: The name of this Group.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[^\\/:*?<>"|]+$', name)):  # noqa: E501
            raise ValueError(r'Invalid value for `name`, must be a follow pattern or equal to `/^[^\\/:*?<>"|]+$/`')  # noqa: E501

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this Group.  # noqa: E501


        :return: The parent_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Group.


        :param parent_id: The parent_id of this Group.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parent_id is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def group_type(self):
        """Gets the group_type of this Group.  # noqa: E501


        :return: The group_type of this Group.  # noqa: E501
        :rtype: int
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this Group.


        :param group_type: The group_type of this Group.  # noqa: E501
        :type: int
        """

        self._group_type = group_type

    @property
    def item_ref(self):
        """Gets the item_ref of this Group.  # noqa: E501


        :return: The item_ref of this Group.  # noqa: E501
        :rtype: str
        """
        return self._item_ref

    @item_ref.setter
    def item_ref(self, item_ref):
        """Sets the item_ref of this Group.


        :param item_ref: The item_ref of this Group.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                item_ref is not None and len(item_ref) > 100):
            raise ValueError("Invalid value for `item_ref`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                item_ref is not None and len(item_ref) < 0):
            raise ValueError("Invalid value for `item_ref`, length must be greater than or equal to `0`")  # noqa: E501

        self._item_ref = item_ref

    @property
    def group_family(self):
        """Gets the group_family of this Group.  # noqa: E501


        :return: The group_family of this Group.  # noqa: E501
        :rtype: str
        """
        return self._group_family

    @group_family.setter
    def group_family(self, group_family):
        """Sets the group_family of this Group.


        :param group_family: The group_family of this Group.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_family is None:  # noqa: E501
            raise ValueError("Invalid value for `group_family`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                group_family is not None and len(group_family) > 100):
            raise ValueError("Invalid value for `group_family`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                group_family is not None and len(group_family) < 0):
            raise ValueError("Invalid value for `group_family`, length must be greater than or equal to `0`")  # noqa: E501

        self._group_family = group_family

    @property
    def group_level(self):
        """Gets the group_level of this Group.  # noqa: E501


        :return: The group_level of this Group.  # noqa: E501
        :rtype: str
        """
        return self._group_level

    @group_level.setter
    def group_level(self, group_level):
        """Sets the group_level of this Group.


        :param group_level: The group_level of this Group.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_level is None:  # noqa: E501
            raise ValueError("Invalid value for `group_level`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                group_level is not None and len(group_level) > 1000):
            raise ValueError("Invalid value for `group_level`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                group_level is not None and len(group_level) < 0):
            raise ValueError("Invalid value for `group_level`, length must be greater than or equal to `0`")  # noqa: E501

        self._group_level = group_level

    @property
    def item_id(self):
        """Gets the item_id of this Group.  # noqa: E501


        :return: The item_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this Group.


        :param item_id: The item_id of this Group.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def version(self):
        """Gets the version of this Group.  # noqa: E501


        :return: The version of this Group.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Group.


        :param version: The version of this Group.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Group.  # noqa: E501


        :return: The tenant_id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Group.


        :param tenant_id: The tenant_id of this Group.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def parent(self):
        """Gets the parent of this Group.  # noqa: E501


        :return: The parent of this Group.  # noqa: E501
        :rtype: Group
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Group.


        :param parent: The parent of this Group.  # noqa: E501
        :type: Group
        """

        self._parent = parent

    @property
    def path(self):
        """Gets the path of this Group.  # noqa: E501


        :return: The path of this Group.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Group.


        :param path: The path of this Group.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if not isinstance(other, Group):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Group):
            return True

        return self.to_dict() != other.to_dict()
