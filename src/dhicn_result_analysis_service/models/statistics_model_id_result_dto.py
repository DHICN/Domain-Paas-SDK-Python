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


class StatisticsModelIdResultDto(object):
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
        'model_id': 'str',
        'statistic_model_id_item': 'StatisticModelIdItemDto'
    }

    attribute_map = {
        'model_id': 'modelId',
        'statistic_model_id_item': 'statisticModelIdItem'
    }

    def __init__(self, model_id=None, statistic_model_id_item=None, local_vars_configuration=None):  # noqa: E501
        """StatisticsModelIdResultDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_id = None
        self._statistic_model_id_item = None
        self.discriminator = None

        self.model_id = model_id
        if statistic_model_id_item is not None:
            self.statistic_model_id_item = statistic_model_id_item

    @property
    def model_id(self):
        """Gets the model_id of this StatisticsModelIdResultDto.  # noqa: E501


        :return: The model_id of this StatisticsModelIdResultDto.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this StatisticsModelIdResultDto.


        :param model_id: The model_id of this StatisticsModelIdResultDto.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def statistic_model_id_item(self):
        """Gets the statistic_model_id_item of this StatisticsModelIdResultDto.  # noqa: E501


        :return: The statistic_model_id_item of this StatisticsModelIdResultDto.  # noqa: E501
        :rtype: StatisticModelIdItemDto
        """
        return self._statistic_model_id_item

    @statistic_model_id_item.setter
    def statistic_model_id_item(self, statistic_model_id_item):
        """Sets the statistic_model_id_item of this StatisticsModelIdResultDto.


        :param statistic_model_id_item: The statistic_model_id_item of this StatisticsModelIdResultDto.  # noqa: E501
        :type: StatisticModelIdItemDto
        """

        self._statistic_model_id_item = statistic_model_id_item

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
        if not isinstance(other, StatisticsModelIdResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticsModelIdResultDto):
            return True

        return self.to_dict() != other.to_dict()