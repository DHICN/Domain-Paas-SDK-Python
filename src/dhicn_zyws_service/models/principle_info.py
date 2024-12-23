# coding: utf-8

"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_zyws_service.configuration import Configuration


class PrincipleInfo(object):
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
        'factory_code': 'str',
        'factory_name': 'str',
        'item_code': 'str',
        'item_name': 'str',
        'sort': 'int',
        'value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'factory_code': 'factoryCode',
        'factory_name': 'factoryName',
        'item_code': 'itemCode',
        'item_name': 'itemName',
        'sort': 'sort',
        'value': 'value'
    }

    def __init__(self, id=None, factory_code=None, factory_name=None, item_code=None, item_name=None, sort=None, value=None, local_vars_configuration=None):  # noqa: E501
        """PrincipleInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._factory_code = None
        self._factory_name = None
        self._item_code = None
        self._item_name = None
        self._sort = None
        self._value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.factory_code = factory_code
        self.factory_name = factory_name
        self.item_code = item_code
        self.item_name = item_name
        if sort is not None:
            self.sort = sort
        if value is not None:
            self.value = value

    @property
    def id(self):
        """Gets the id of this PrincipleInfo.  # noqa: E501

        具体原则项Id  # noqa: E501

        :return: The id of this PrincipleInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrincipleInfo.

        具体原则项Id  # noqa: E501

        :param id: The id of this PrincipleInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def factory_code(self):
        """Gets the factory_code of this PrincipleInfo.  # noqa: E501

        厂区编码  # noqa: E501

        :return: The factory_code of this PrincipleInfo.  # noqa: E501
        :rtype: str
        """
        return self._factory_code

    @factory_code.setter
    def factory_code(self, factory_code):
        """Sets the factory_code of this PrincipleInfo.

        厂区编码  # noqa: E501

        :param factory_code: The factory_code of this PrincipleInfo.  # noqa: E501
        :type: str
        """

        self._factory_code = factory_code

    @property
    def factory_name(self):
        """Gets the factory_name of this PrincipleInfo.  # noqa: E501

        厂区名称  # noqa: E501

        :return: The factory_name of this PrincipleInfo.  # noqa: E501
        :rtype: str
        """
        return self._factory_name

    @factory_name.setter
    def factory_name(self, factory_name):
        """Sets the factory_name of this PrincipleInfo.

        厂区名称  # noqa: E501

        :param factory_name: The factory_name of this PrincipleInfo.  # noqa: E501
        :type: str
        """

        self._factory_name = factory_name

    @property
    def item_code(self):
        """Gets the item_code of this PrincipleInfo.  # noqa: E501

        厂区下的具体原则项编码  # noqa: E501

        :return: The item_code of this PrincipleInfo.  # noqa: E501
        :rtype: str
        """
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        """Sets the item_code of this PrincipleInfo.

        厂区下的具体原则项编码  # noqa: E501

        :param item_code: The item_code of this PrincipleInfo.  # noqa: E501
        :type: str
        """

        self._item_code = item_code

    @property
    def item_name(self):
        """Gets the item_name of this PrincipleInfo.  # noqa: E501

        厂区下的具体原则项名称  # noqa: E501

        :return: The item_name of this PrincipleInfo.  # noqa: E501
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this PrincipleInfo.

        厂区下的具体原则项名称  # noqa: E501

        :param item_name: The item_name of this PrincipleInfo.  # noqa: E501
        :type: str
        """

        self._item_name = item_name

    @property
    def sort(self):
        """Gets the sort of this PrincipleInfo.  # noqa: E501

        厂区下的具体原则项,排序号,越小越靠前  # noqa: E501

        :return: The sort of this PrincipleInfo.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this PrincipleInfo.

        厂区下的具体原则项,排序号,越小越靠前  # noqa: E501

        :param sort: The sort of this PrincipleInfo.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def value(self):
        """Gets the value of this PrincipleInfo.  # noqa: E501

        厂区下的具体原则项值  # noqa: E501

        :return: The value of this PrincipleInfo.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PrincipleInfo.

        厂区下的具体原则项值  # noqa: E501

        :param value: The value of this PrincipleInfo.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if not isinstance(other, PrincipleInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrincipleInfo):
            return True

        return self.to_dict() != other.to_dict()
