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


class QueryControlParamCompareOutput(object):
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
        'para_code': 'str',
        'description': 'str',
        'unit': 'str',
        'scenarios': 'list[Scenario]'
    }

    attribute_map = {
        'para_code': 'paraCode',
        'description': 'description',
        'unit': 'unit',
        'scenarios': 'scenarios'
    }

    def __init__(self, para_code=None, description=None, unit=None, scenarios=None, local_vars_configuration=None):  # noqa: E501
        """QueryControlParamCompareOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._para_code = None
        self._description = None
        self._unit = None
        self._scenarios = None
        self.discriminator = None

        self.para_code = para_code
        self.description = description
        self.unit = unit
        self.scenarios = scenarios

    @property
    def para_code(self):
        """Gets the para_code of this QueryControlParamCompareOutput.  # noqa: E501

        参数代码 parameter code  # noqa: E501

        :return: The para_code of this QueryControlParamCompareOutput.  # noqa: E501
        :rtype: str
        """
        return self._para_code

    @para_code.setter
    def para_code(self, para_code):
        """Sets the para_code of this QueryControlParamCompareOutput.

        参数代码 parameter code  # noqa: E501

        :param para_code: The para_code of this QueryControlParamCompareOutput.  # noqa: E501
        :type: str
        """

        self._para_code = para_code

    @property
    def description(self):
        """Gets the description of this QueryControlParamCompareOutput.  # noqa: E501

        参数描述 parameter description  # noqa: E501

        :return: The description of this QueryControlParamCompareOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryControlParamCompareOutput.

        参数描述 parameter description  # noqa: E501

        :param description: The description of this QueryControlParamCompareOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unit(self):
        """Gets the unit of this QueryControlParamCompareOutput.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this QueryControlParamCompareOutput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this QueryControlParamCompareOutput.

        单位 unit  # noqa: E501

        :param unit: The unit of this QueryControlParamCompareOutput.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def scenarios(self):
        """Gets the scenarios of this QueryControlParamCompareOutput.  # noqa: E501

        方案对比结果 scenario comparision result  # noqa: E501

        :return: The scenarios of this QueryControlParamCompareOutput.  # noqa: E501
        :rtype: list[Scenario]
        """
        return self._scenarios

    @scenarios.setter
    def scenarios(self, scenarios):
        """Sets the scenarios of this QueryControlParamCompareOutput.

        方案对比结果 scenario comparision result  # noqa: E501

        :param scenarios: The scenarios of this QueryControlParamCompareOutput.  # noqa: E501
        :type: list[Scenario]
        """

        self._scenarios = scenarios

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
        if not isinstance(other, QueryControlParamCompareOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryControlParamCompareOutput):
            return True

        return self.to_dict() != other.to_dict()
