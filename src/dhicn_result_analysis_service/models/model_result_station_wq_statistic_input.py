# coding: utf-8

"""
    result-analysis-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_result_analysis_service.configuration import Configuration


class ModelResultStationWqStatisticInput(object):
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
        'scenario_id': 'str',
        'wq_item': 'str',
        'key_section_location': 'list[str]'
    }

    attribute_map = {
        'scenario_id': 'scenarioId',
        'wq_item': 'wqItem',
        'key_section_location': 'keySectionLocation'
    }

    def __init__(self, scenario_id=None, wq_item=None, key_section_location=None, local_vars_configuration=None):  # noqa: E501
        """ModelResultStationWqStatisticInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scenario_id = None
        self._wq_item = None
        self._key_section_location = None
        self.discriminator = None

        self.scenario_id = scenario_id
        self.wq_item = wq_item
        self.key_section_location = key_section_location

    @property
    def scenario_id(self):
        """Gets the scenario_id of this ModelResultStationWqStatisticInput.  # noqa: E501

        方案id scenario id  # noqa: E501

        :return: The scenario_id of this ModelResultStationWqStatisticInput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this ModelResultStationWqStatisticInput.

        方案id scenario id  # noqa: E501

        :param scenario_id: The scenario_id of this ModelResultStationWqStatisticInput.  # noqa: E501
        :type: str
        """

        self._scenario_id = scenario_id

    @property
    def wq_item(self):
        """Gets the wq_item of this ModelResultStationWqStatisticInput.  # noqa: E501

        水质项 water quality item  # noqa: E501

        :return: The wq_item of this ModelResultStationWqStatisticInput.  # noqa: E501
        :rtype: str
        """
        return self._wq_item

    @wq_item.setter
    def wq_item(self, wq_item):
        """Sets the wq_item of this ModelResultStationWqStatisticInput.

        水质项 water quality item  # noqa: E501

        :param wq_item: The wq_item of this ModelResultStationWqStatisticInput.  # noqa: E501
        :type: str
        """

        self._wq_item = wq_item

    @property
    def key_section_location(self):
        """Gets the key_section_location of this ModelResultStationWqStatisticInput.  # noqa: E501

        考核断面（河道名，里程）assessment section (river name, chainage)  # noqa: E501

        :return: The key_section_location of this ModelResultStationWqStatisticInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._key_section_location

    @key_section_location.setter
    def key_section_location(self, key_section_location):
        """Sets the key_section_location of this ModelResultStationWqStatisticInput.

        考核断面（河道名，里程）assessment section (river name, chainage)  # noqa: E501

        :param key_section_location: The key_section_location of this ModelResultStationWqStatisticInput.  # noqa: E501
        :type: list[str]
        """

        self._key_section_location = key_section_location

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
        if not isinstance(other, ModelResultStationWqStatisticInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelResultStationWqStatisticInput):
            return True

        return self.to_dict() != other.to_dict()
