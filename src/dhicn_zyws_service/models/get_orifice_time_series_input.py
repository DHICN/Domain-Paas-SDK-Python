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


class GetOrificeTimeSeriesInput(object):
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
        'model_ids': 'list[str]',
        'scenario_id': 'str',
        'data_type': 'str'
    }

    attribute_map = {
        'model_ids': 'modelIds',
        'scenario_id': 'scenarioId',
        'data_type': 'dataType'
    }

    def __init__(self, model_ids=None, scenario_id=None, data_type=None, local_vars_configuration=None):  # noqa: E501
        """GetOrificeTimeSeriesInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_ids = None
        self._scenario_id = None
        self._data_type = None
        self.discriminator = None

        self.model_ids = model_ids
        self.scenario_id = scenario_id
        self.data_type = data_type

    @property
    def model_ids(self):
        """Gets the model_ids of this GetOrificeTimeSeriesInput.  # noqa: E501

        堰门Ids  # noqa: E501

        :return: The model_ids of this GetOrificeTimeSeriesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        """Sets the model_ids of this GetOrificeTimeSeriesInput.

        堰门Ids  # noqa: E501

        :param model_ids: The model_ids of this GetOrificeTimeSeriesInput.  # noqa: E501
        :type: list[str]
        """

        self._model_ids = model_ids

    @property
    def scenario_id(self):
        """Gets the scenario_id of this GetOrificeTimeSeriesInput.  # noqa: E501

        方案ID  # noqa: E501

        :return: The scenario_id of this GetOrificeTimeSeriesInput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this GetOrificeTimeSeriesInput.

        方案ID  # noqa: E501

        :param scenario_id: The scenario_id of this GetOrificeTimeSeriesInput.  # noqa: E501
        :type: str
        """

        self._scenario_id = scenario_id

    @property
    def data_type(self):
        """Gets the data_type of this GetOrificeTimeSeriesInput.  # noqa: E501

        堰门的数据类型，WaterLevel,DischargeInStructure  # noqa: E501

        :return: The data_type of this GetOrificeTimeSeriesInput.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this GetOrificeTimeSeriesInput.

        堰门的数据类型，WaterLevel,DischargeInStructure  # noqa: E501

        :param data_type: The data_type of this GetOrificeTimeSeriesInput.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

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
        if not isinstance(other, GetOrificeTimeSeriesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetOrificeTimeSeriesInput):
            return True

        return self.to_dict() != other.to_dict()
