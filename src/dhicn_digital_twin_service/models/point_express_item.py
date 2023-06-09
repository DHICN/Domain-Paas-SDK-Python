# coding: utf-8

"""
    digital-twin-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_digital_twin_service.configuration import Configuration


class PointExpressItem(object):
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
        'point_parameter_dic': 'dict(str, str)',
        'expression': 'str'
    }

    attribute_map = {
        'point_parameter_dic': 'pointParameterDic',
        'expression': 'expression'
    }

    def __init__(self, point_parameter_dic=None, expression=None, local_vars_configuration=None):  # noqa: E501
        """PointExpressItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._point_parameter_dic = None
        self._expression = None
        self.discriminator = None

        self.point_parameter_dic = point_parameter_dic
        self.expression = expression

    @property
    def point_parameter_dic(self):
        """Gets the point_parameter_dic of this PointExpressItem.  # noqa: E501

        点位与表达式中参数对应关系的列表 point and parameter mapping relations list  # noqa: E501

        :return: The point_parameter_dic of this PointExpressItem.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._point_parameter_dic

    @point_parameter_dic.setter
    def point_parameter_dic(self, point_parameter_dic):
        """Sets the point_parameter_dic of this PointExpressItem.

        点位与表达式中参数对应关系的列表 point and parameter mapping relations list  # noqa: E501

        :param point_parameter_dic: The point_parameter_dic of this PointExpressItem.  # noqa: E501
        :type: dict(str, str)
        """

        self._point_parameter_dic = point_parameter_dic

    @property
    def expression(self):
        """Gets the expression of this PointExpressItem.  # noqa: E501

        表达式 expression  # noqa: E501

        :return: The expression of this PointExpressItem.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this PointExpressItem.

        表达式 expression  # noqa: E501

        :param expression: The expression of this PointExpressItem.  # noqa: E501
        :type: str
        """

        self._expression = expression

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
        if not isinstance(other, PointExpressItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PointExpressItem):
            return True

        return self.to_dict() != other.to_dict()
