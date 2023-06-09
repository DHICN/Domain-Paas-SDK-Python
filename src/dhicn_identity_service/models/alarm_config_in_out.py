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


class AlarmConfigInOut(object):
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
        'node_code': 'str',
        'indicator': 'str',
        'grade': 'int',
        'max_value': 'float',
        'min_value': 'float',
        'alarm_type': 'int',
        'node_type': 'int',
        'unit': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'node_code': 'nodeCode',
        'indicator': 'indicator',
        'grade': 'grade',
        'max_value': 'maxValue',
        'min_value': 'minValue',
        'alarm_type': 'alarmType',
        'node_type': 'nodeType',
        'unit': 'unit',
        'message': 'message'
    }

    def __init__(self, id=None, node_code=None, indicator=None, grade=None, max_value=None, min_value=None, alarm_type=None, node_type=None, unit=None, message=None, local_vars_configuration=None):  # noqa: E501
        """AlarmConfigInOut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._node_code = None
        self._indicator = None
        self._grade = None
        self._max_value = None
        self._min_value = None
        self._alarm_type = None
        self._node_type = None
        self._unit = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.node_code = node_code
        self.indicator = indicator
        if grade is not None:
            self.grade = grade
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if node_type is not None:
            self.node_type = node_type
        self.unit = unit
        self.message = message

    @property
    def id(self):
        """Gets the id of this AlarmConfigInOut.  # noqa: E501


        :return: The id of this AlarmConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlarmConfigInOut.


        :param id: The id of this AlarmConfigInOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def node_code(self):
        """Gets the node_code of this AlarmConfigInOut.  # noqa: E501

        节点编码 code  # noqa: E501

        :return: The node_code of this AlarmConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._node_code

    @node_code.setter
    def node_code(self, node_code):
        """Sets the node_code of this AlarmConfigInOut.

        节点编码 code  # noqa: E501

        :param node_code: The node_code of this AlarmConfigInOut.  # noqa: E501
        :type: str
        """

        self._node_code = node_code

    @property
    def indicator(self):
        """Gets the indicator of this AlarmConfigInOut.  # noqa: E501

        指标 indicator  # noqa: E501

        :return: The indicator of this AlarmConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this AlarmConfigInOut.

        指标 indicator  # noqa: E501

        :param indicator: The indicator of this AlarmConfigInOut.  # noqa: E501
        :type: str
        """

        self._indicator = indicator

    @property
    def grade(self):
        """Gets the grade of this AlarmConfigInOut.  # noqa: E501

        报警等级 alarm grade  # noqa: E501

        :return: The grade of this AlarmConfigInOut.  # noqa: E501
        :rtype: int
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        """Sets the grade of this AlarmConfigInOut.

        报警等级 alarm grade  # noqa: E501

        :param grade: The grade of this AlarmConfigInOut.  # noqa: E501
        :type: int
        """

        self._grade = grade

    @property
    def max_value(self):
        """Gets the max_value of this AlarmConfigInOut.  # noqa: E501

        最大值 maximum value  # noqa: E501

        :return: The max_value of this AlarmConfigInOut.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this AlarmConfigInOut.

        最大值 maximum value  # noqa: E501

        :param max_value: The max_value of this AlarmConfigInOut.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this AlarmConfigInOut.  # noqa: E501

        最小值 minimum value  # noqa: E501

        :return: The min_value of this AlarmConfigInOut.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this AlarmConfigInOut.

        最小值 minimum value  # noqa: E501

        :param min_value: The min_value of this AlarmConfigInOut.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def alarm_type(self):
        """Gets the alarm_type of this AlarmConfigInOut.  # noqa: E501

        警报类型 alarm type  # noqa: E501

        :return: The alarm_type of this AlarmConfigInOut.  # noqa: E501
        :rtype: int
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this AlarmConfigInOut.

        警报类型 alarm type  # noqa: E501

        :param alarm_type: The alarm_type of this AlarmConfigInOut.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and alarm_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `alarm_type` ({0}), must be one of {1}"  # noqa: E501
                .format(alarm_type, allowed_values)
            )

        self._alarm_type = alarm_type

    @property
    def node_type(self):
        """Gets the node_type of this AlarmConfigInOut.  # noqa: E501

        节点类型 node type  # noqa: E501

        :return: The node_type of this AlarmConfigInOut.  # noqa: E501
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this AlarmConfigInOut.

        节点类型 node type  # noqa: E501

        :param node_type: The node_type of this AlarmConfigInOut.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and node_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def unit(self):
        """Gets the unit of this AlarmConfigInOut.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this AlarmConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AlarmConfigInOut.

        单位 unit  # noqa: E501

        :param unit: The unit of this AlarmConfigInOut.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def message(self):
        """Gets the message of this AlarmConfigInOut.  # noqa: E501

        报警信息 alarm message  # noqa: E501

        :return: The message of this AlarmConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AlarmConfigInOut.

        报警信息 alarm message  # noqa: E501

        :param message: The message of this AlarmConfigInOut.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, AlarmConfigInOut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlarmConfigInOut):
            return True

        return self.to_dict() != other.to_dict()
