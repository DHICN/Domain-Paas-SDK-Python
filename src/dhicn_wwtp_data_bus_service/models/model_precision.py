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


class ModelPrecision(object):
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
        'code': 'str',
        'unit': 'str',
        'evaluation': 'str',
        'level_code': 'str',
        'percentages_distri': 'list[PercentagesDto]'
    }

    attribute_map = {
        'code': 'code',
        'unit': 'unit',
        'evaluation': 'evaluation',
        'level_code': 'levelCode',
        'percentages_distri': 'percentagesDistri'
    }

    def __init__(self, code=None, unit=None, evaluation=None, level_code=None, percentages_distri=None, local_vars_configuration=None):  # noqa: E501
        """ModelPrecision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._unit = None
        self._evaluation = None
        self._level_code = None
        self._percentages_distri = None
        self.discriminator = None

        self.code = code
        self.unit = unit
        self.evaluation = evaluation
        self.level_code = level_code
        self.percentages_distri = percentages_distri

    @property
    def code(self):
        """Gets the code of this ModelPrecision.  # noqa: E501

        指标 indicator code  # noqa: E501

        :return: The code of this ModelPrecision.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ModelPrecision.

        指标 indicator code  # noqa: E501

        :param code: The code of this ModelPrecision.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def unit(self):
        """Gets the unit of this ModelPrecision.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this ModelPrecision.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ModelPrecision.

        单位 unit  # noqa: E501

        :param unit: The unit of this ModelPrecision.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def evaluation(self):
        """Gets the evaluation of this ModelPrecision.  # noqa: E501

        总体评价 overall evaluation  # noqa: E501

        :return: The evaluation of this ModelPrecision.  # noqa: E501
        :rtype: str
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        """Sets the evaluation of this ModelPrecision.

        总体评价 overall evaluation  # noqa: E501

        :param evaluation: The evaluation of this ModelPrecision.  # noqa: E501
        :type: str
        """

        self._evaluation = evaluation

    @property
    def level_code(self):
        """Gets the level_code of this ModelPrecision.  # noqa: E501

        评价Code  # noqa: E501

        :return: The level_code of this ModelPrecision.  # noqa: E501
        :rtype: str
        """
        return self._level_code

    @level_code.setter
    def level_code(self, level_code):
        """Sets the level_code of this ModelPrecision.

        评价Code  # noqa: E501

        :param level_code: The level_code of this ModelPrecision.  # noqa: E501
        :type: str
        """

        self._level_code = level_code

    @property
    def percentages_distri(self):
        """Gets the percentages_distri of this ModelPrecision.  # noqa: E501

        精度百分比区间占比 precision region detailed data  # noqa: E501

        :return: The percentages_distri of this ModelPrecision.  # noqa: E501
        :rtype: list[PercentagesDto]
        """
        return self._percentages_distri

    @percentages_distri.setter
    def percentages_distri(self, percentages_distri):
        """Sets the percentages_distri of this ModelPrecision.

        精度百分比区间占比 precision region detailed data  # noqa: E501

        :param percentages_distri: The percentages_distri of this ModelPrecision.  # noqa: E501
        :type: list[PercentagesDto]
        """

        self._percentages_distri = percentages_distri

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
        if not isinstance(other, ModelPrecision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelPrecision):
            return True

        return self.to_dict() != other.to_dict()
