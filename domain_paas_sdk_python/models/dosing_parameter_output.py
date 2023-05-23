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


class DosingParameterOutput(object):
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
        'sys_code': 'str',
        'value': 'float',
        'unit': 'str',
        'order_by': 'int',
        'is_edit_manual': 'bool',
        'is_edit_smart': 'bool',
        'name': 'str',
        'code': 'str',
        'product_line': 'str',
        'category': 'int'
    }

    attribute_map = {
        'id': 'id',
        'sys_code': 'sysCode',
        'value': 'value',
        'unit': 'unit',
        'order_by': 'orderBy',
        'is_edit_manual': 'isEditManual',
        'is_edit_smart': 'isEditSmart',
        'name': 'name',
        'code': 'code',
        'product_line': 'productLine',
        'category': 'category'
    }

    def __init__(self, id=None, sys_code=None, value=None, unit=None, order_by=None, is_edit_manual=None, is_edit_smart=None, name=None, code=None, product_line=None, category=None, local_vars_configuration=None):  # noqa: E501
        """DosingParameterOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._sys_code = None
        self._value = None
        self._unit = None
        self._order_by = None
        self._is_edit_manual = None
        self._is_edit_smart = None
        self._name = None
        self._code = None
        self._product_line = None
        self._category = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.sys_code = sys_code
        if value is not None:
            self.value = value
        self.unit = unit
        if order_by is not None:
            self.order_by = order_by
        self.is_edit_manual = is_edit_manual
        self.is_edit_smart = is_edit_smart
        self.name = name
        self.code = code
        self.product_line = product_line
        if category is not None:
            self.category = category

    @property
    def id(self):
        """Gets the id of this DosingParameterOutput.  # noqa: E501


        :return: The id of this DosingParameterOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DosingParameterOutput.


        :param id: The id of this DosingParameterOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sys_code(self):
        """Gets the sys_code of this DosingParameterOutput.  # noqa: E501

        系统代码 corresponding system code  # noqa: E501

        :return: The sys_code of this DosingParameterOutput.  # noqa: E501
        :rtype: str
        """
        return self._sys_code

    @sys_code.setter
    def sys_code(self, sys_code):
        """Sets the sys_code of this DosingParameterOutput.

        系统代码 corresponding system code  # noqa: E501

        :param sys_code: The sys_code of this DosingParameterOutput.  # noqa: E501
        :type: str
        """

        self._sys_code = sys_code

    @property
    def value(self):
        """Gets the value of this DosingParameterOutput.  # noqa: E501

        值 value  # noqa: E501

        :return: The value of this DosingParameterOutput.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DosingParameterOutput.

        值 value  # noqa: E501

        :param value: The value of this DosingParameterOutput.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this DosingParameterOutput.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this DosingParameterOutput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DosingParameterOutput.

        单位 unit  # noqa: E501

        :param unit: The unit of this DosingParameterOutput.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def order_by(self):
        """Gets the order_by of this DosingParameterOutput.  # noqa: E501

        序号 display index  # noqa: E501

        :return: The order_by of this DosingParameterOutput.  # noqa: E501
        :rtype: int
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this DosingParameterOutput.

        序号 display index  # noqa: E501

        :param order_by: The order_by of this DosingParameterOutput.  # noqa: E501
        :type: int
        """

        self._order_by = order_by

    @property
    def is_edit_manual(self):
        """Gets the is_edit_manual of this DosingParameterOutput.  # noqa: E501

        是否为手动加药参数 if support manual dosage  # noqa: E501

        :return: The is_edit_manual of this DosingParameterOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_edit_manual

    @is_edit_manual.setter
    def is_edit_manual(self, is_edit_manual):
        """Sets the is_edit_manual of this DosingParameterOutput.

        是否为手动加药参数 if support manual dosage  # noqa: E501

        :param is_edit_manual: The is_edit_manual of this DosingParameterOutput.  # noqa: E501
        :type: bool
        """

        self._is_edit_manual = is_edit_manual

    @property
    def is_edit_smart(self):
        """Gets the is_edit_smart of this DosingParameterOutput.  # noqa: E501

        是否为智能加药参数 if support smart dosage  # noqa: E501

        :return: The is_edit_smart of this DosingParameterOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_edit_smart

    @is_edit_smart.setter
    def is_edit_smart(self, is_edit_smart):
        """Sets the is_edit_smart of this DosingParameterOutput.

        是否为智能加药参数 if support smart dosage  # noqa: E501

        :param is_edit_smart: The is_edit_smart of this DosingParameterOutput.  # noqa: E501
        :type: bool
        """

        self._is_edit_smart = is_edit_smart

    @property
    def name(self):
        """Gets the name of this DosingParameterOutput.  # noqa: E501

        参数名称 parameter name  # noqa: E501

        :return: The name of this DosingParameterOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DosingParameterOutput.

        参数名称 parameter name  # noqa: E501

        :param name: The name of this DosingParameterOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this DosingParameterOutput.  # noqa: E501

        参数编码 parameter code  # noqa: E501

        :return: The code of this DosingParameterOutput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DosingParameterOutput.

        参数编码 parameter code  # noqa: E501

        :param code: The code of this DosingParameterOutput.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def product_line(self):
        """Gets the product_line of this DosingParameterOutput.  # noqa: E501

        生产线 product line code  # noqa: E501

        :return: The product_line of this DosingParameterOutput.  # noqa: E501
        :rtype: str
        """
        return self._product_line

    @product_line.setter
    def product_line(self, product_line):
        """Sets the product_line of this DosingParameterOutput.

        生产线 product line code  # noqa: E501

        :param product_line: The product_line of this DosingParameterOutput.  # noqa: E501
        :type: str
        """

        self._product_line = product_line

    @property
    def category(self):
        """Gets the category of this DosingParameterOutput.  # noqa: E501

        药剂投加类别  # noqa: E501

        :return: The category of this DosingParameterOutput.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this DosingParameterOutput.

        药剂投加类别  # noqa: E501

        :param category: The category of this DosingParameterOutput.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and category not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

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
        if not isinstance(other, DosingParameterOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DosingParameterOutput):
            return True

        return self.to_dict() != other.to_dict()
