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


class StatisticSettingOutput(object):
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
        'template_id': 'str',
        'result_type': 'str',
        'show_name': 'str',
        'code': 'str',
        'data_type': 'str',
        'unit': 'str',
        'model_ids': 'str',
        'sort': 'int',
        'is_show_in_chart': 'bool',
        'scenario_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'template_id': 'templateId',
        'result_type': 'resultType',
        'show_name': 'showName',
        'code': 'code',
        'data_type': 'dataType',
        'unit': 'unit',
        'model_ids': 'modelIds',
        'sort': 'sort',
        'is_show_in_chart': 'isShowInChart',
        'scenario_type': 'scenarioType'
    }

    def __init__(self, id=None, template_id=None, result_type=None, show_name=None, code=None, data_type=None, unit=None, model_ids=None, sort=None, is_show_in_chart=None, scenario_type=None, local_vars_configuration=None):  # noqa: E501
        """StatisticSettingOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._template_id = None
        self._result_type = None
        self._show_name = None
        self._code = None
        self._data_type = None
        self._unit = None
        self._model_ids = None
        self._sort = None
        self._is_show_in_chart = None
        self._scenario_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_id is not None:
            self.template_id = template_id
        self.result_type = result_type
        self.show_name = show_name
        self.code = code
        self.data_type = data_type
        self.unit = unit
        self.model_ids = model_ids
        if sort is not None:
            self.sort = sort
        if is_show_in_chart is not None:
            self.is_show_in_chart = is_show_in_chart
        self.scenario_type = scenario_type

    @property
    def id(self):
        """Gets the id of this StatisticSettingOutput.  # noqa: E501


        :return: The id of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatisticSettingOutput.


        :param id: The id of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def template_id(self):
        """Gets the template_id of this StatisticSettingOutput.  # noqa: E501


        :return: The template_id of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this StatisticSettingOutput.


        :param template_id: The template_id of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def result_type(self):
        """Gets the result_type of this StatisticSettingOutput.  # noqa: E501

        结果类型，0-OrificeStatistic、1-PumpStatistic、2-LinkStatistic  # noqa: E501

        :return: The result_type of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this StatisticSettingOutput.

        结果类型，0-OrificeStatistic、1-PumpStatistic、2-LinkStatistic  # noqa: E501

        :param result_type: The result_type of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._result_type = result_type

    @property
    def show_name(self):
        """Gets the show_name of this StatisticSettingOutput.  # noqa: E501


        :return: The show_name of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        """Sets the show_name of this StatisticSettingOutput.


        :param show_name: The show_name of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._show_name = show_name

    @property
    def code(self):
        """Gets the code of this StatisticSettingOutput.  # noqa: E501


        :return: The code of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StatisticSettingOutput.


        :param code: The code of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def data_type(self):
        """Gets the data_type of this StatisticSettingOutput.  # noqa: E501


        :return: The data_type of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this StatisticSettingOutput.


        :param data_type: The data_type of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def unit(self):
        """Gets the unit of this StatisticSettingOutput.  # noqa: E501


        :return: The unit of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this StatisticSettingOutput.


        :param unit: The unit of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def model_ids(self):
        """Gets the model_ids of this StatisticSettingOutput.  # noqa: E501


        :return: The model_ids of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        """Sets the model_ids of this StatisticSettingOutput.


        :param model_ids: The model_ids of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._model_ids = model_ids

    @property
    def sort(self):
        """Gets the sort of this StatisticSettingOutput.  # noqa: E501


        :return: The sort of this StatisticSettingOutput.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this StatisticSettingOutput.


        :param sort: The sort of this StatisticSettingOutput.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def is_show_in_chart(self):
        """Gets the is_show_in_chart of this StatisticSettingOutput.  # noqa: E501


        :return: The is_show_in_chart of this StatisticSettingOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_show_in_chart

    @is_show_in_chart.setter
    def is_show_in_chart(self, is_show_in_chart):
        """Sets the is_show_in_chart of this StatisticSettingOutput.


        :param is_show_in_chart: The is_show_in_chart of this StatisticSettingOutput.  # noqa: E501
        :type: bool
        """

        self._is_show_in_chart = is_show_in_chart

    @property
    def scenario_type(self):
        """Gets the scenario_type of this StatisticSettingOutput.  # noqa: E501


        :return: The scenario_type of this StatisticSettingOutput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, scenario_type):
        """Sets the scenario_type of this StatisticSettingOutput.


        :param scenario_type: The scenario_type of this StatisticSettingOutput.  # noqa: E501
        :type: str
        """

        self._scenario_type = scenario_type

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
        if not isinstance(other, StatisticSettingOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticSettingOutput):
            return True

        return self.to_dict() != other.to_dict()
