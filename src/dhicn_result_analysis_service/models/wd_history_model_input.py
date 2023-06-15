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


class WdHistoryModelInput(object):
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
        'start_time': 'datetime',
        'end_time': 'datetime',
        'frequency': 'int',
        'data_type': 'SysWdDataTypeEnum'
    }

    attribute_map = {
        'model_ids': 'modelIds',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'frequency': 'frequency',
        'data_type': 'dataType'
    }

    def __init__(self, model_ids=None, start_time=None, end_time=None, frequency=None, data_type=None, local_vars_configuration=None):  # noqa: E501
        """WdHistoryModelInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_ids = None
        self._start_time = None
        self._end_time = None
        self._frequency = None
        self._data_type = None
        self.discriminator = None

        self.model_ids = model_ids
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if frequency is not None:
            self.frequency = frequency
        if data_type is not None:
            self.data_type = data_type

    @property
    def model_ids(self):
        """Gets the model_ids of this WdHistoryModelInput.  # noqa: E501


        :return: The model_ids of this WdHistoryModelInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        """Sets the model_ids of this WdHistoryModelInput.


        :param model_ids: The model_ids of this WdHistoryModelInput.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and model_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `model_ids`, must not be `None`")  # noqa: E501

        self._model_ids = model_ids

    @property
    def start_time(self):
        """Gets the start_time of this WdHistoryModelInput.  # noqa: E501


        :return: The start_time of this WdHistoryModelInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WdHistoryModelInput.


        :param start_time: The start_time of this WdHistoryModelInput.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this WdHistoryModelInput.  # noqa: E501


        :return: The end_time of this WdHistoryModelInput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this WdHistoryModelInput.


        :param end_time: The end_time of this WdHistoryModelInput.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def frequency(self):
        """Gets the frequency of this WdHistoryModelInput.  # noqa: E501


        :return: The frequency of this WdHistoryModelInput.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this WdHistoryModelInput.


        :param frequency: The frequency of this WdHistoryModelInput.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def data_type(self):
        """Gets the data_type of this WdHistoryModelInput.  # noqa: E501


        :return: The data_type of this WdHistoryModelInput.  # noqa: E501
        :rtype: SysWdDataTypeEnum
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this WdHistoryModelInput.


        :param data_type: The data_type of this WdHistoryModelInput.  # noqa: E501
        :type: SysWdDataTypeEnum
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
        if not isinstance(other, WdHistoryModelInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WdHistoryModelInput):
            return True

        return self.to_dict() != other.to_dict()