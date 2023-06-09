# coding: utf-8

"""
    wwtp-paas-main-bus-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wwtp_data_bus_service.configuration import Configuration


class ModelParam(object):
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
        'scenario_code': 'str',
        'para_code': 'str',
        'value': 'float',
        'unit': 'str',
        'description': 'str'
    }

    attribute_map = {
        'scenario_code': 'scenarioCode',
        'para_code': 'paraCode',
        'value': 'value',
        'unit': 'unit',
        'description': 'description'
    }

    def __init__(self, scenario_code=None, para_code=None, value=None, unit=None, description=None, local_vars_configuration=None):  # noqa: E501
        """ModelParam - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scenario_code = None
        self._para_code = None
        self._value = None
        self._unit = None
        self._description = None
        self.discriminator = None

        self.scenario_code = scenario_code
        self.para_code = para_code
        if value is not None:
            self.value = value
        self.unit = unit
        self.description = description

    @property
    def scenario_code(self):
        """Gets the scenario_code of this ModelParam.  # noqa: E501

        方案代码 scenario code  # noqa: E501

        :return: The scenario_code of this ModelParam.  # noqa: E501
        :rtype: str
        """
        return self._scenario_code

    @scenario_code.setter
    def scenario_code(self, scenario_code):
        """Sets the scenario_code of this ModelParam.

        方案代码 scenario code  # noqa: E501

        :param scenario_code: The scenario_code of this ModelParam.  # noqa: E501
        :type: str
        """

        self._scenario_code = scenario_code

    @property
    def para_code(self):
        """Gets the para_code of this ModelParam.  # noqa: E501

        参数代码 parameter code  # noqa: E501

        :return: The para_code of this ModelParam.  # noqa: E501
        :rtype: str
        """
        return self._para_code

    @para_code.setter
    def para_code(self, para_code):
        """Sets the para_code of this ModelParam.

        参数代码 parameter code  # noqa: E501

        :param para_code: The para_code of this ModelParam.  # noqa: E501
        :type: str
        """

        self._para_code = para_code

    @property
    def value(self):
        """Gets the value of this ModelParam.  # noqa: E501

        参数值 parameter value  # noqa: E501

        :return: The value of this ModelParam.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelParam.

        参数值 parameter value  # noqa: E501

        :param value: The value of this ModelParam.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this ModelParam.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this ModelParam.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ModelParam.

        单位 unit  # noqa: E501

        :param unit: The unit of this ModelParam.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def description(self):
        """Gets the description of this ModelParam.  # noqa: E501

        参数描述 parameter description  # noqa: E501

        :return: The description of this ModelParam.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelParam.

        参数描述 parameter description  # noqa: E501

        :param description: The description of this ModelParam.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, ModelParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelParam):
            return True

        return self.to_dict() != other.to_dict()
