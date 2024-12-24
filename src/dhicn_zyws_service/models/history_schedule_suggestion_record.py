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


class HistoryScheduleSuggestionRecord(object):
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
        'creation_time': 'datetime',
        'tenant_id': 'str',
        'last_modification_time': 'datetime',
        'indicator': 'str',
        'show_name': 'str',
        'date_type': 'str',
        'measure_value': 'float',
        'simulation_value': 'float',
        'suggestion': 'str',
        'operation': 'str',
        'time': 'datetime',
        'is_apply': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'creation_time': 'creationTime',
        'tenant_id': 'tenantId',
        'last_modification_time': 'lastModificationTime',
        'indicator': 'indicator',
        'show_name': 'showName',
        'date_type': 'dateType',
        'measure_value': 'measureValue',
        'simulation_value': 'simulationValue',
        'suggestion': 'suggestion',
        'operation': 'operation',
        'time': 'time',
        'is_apply': 'isApply'
    }

    def __init__(self, id=None, creation_time=None, tenant_id=None, last_modification_time=None, indicator=None, show_name=None, date_type=None, measure_value=None, simulation_value=None, suggestion=None, operation=None, time=None, is_apply=None, local_vars_configuration=None):  # noqa: E501
        """HistoryScheduleSuggestionRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._creation_time = None
        self._tenant_id = None
        self._last_modification_time = None
        self._indicator = None
        self._show_name = None
        self._date_type = None
        self._measure_value = None
        self._simulation_value = None
        self._suggestion = None
        self._operation = None
        self._time = None
        self._is_apply = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creation_time is not None:
            self.creation_time = creation_time
        self.tenant_id = tenant_id
        self.last_modification_time = last_modification_time
        self.indicator = indicator
        self.show_name = show_name
        self.date_type = date_type
        if measure_value is not None:
            self.measure_value = measure_value
        if simulation_value is not None:
            self.simulation_value = simulation_value
        self.suggestion = suggestion
        self.operation = operation
        if time is not None:
            self.time = time
        if is_apply is not None:
            self.is_apply = is_apply

    @property
    def id(self):
        """Gets the id of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The id of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryScheduleSuggestionRecord.


        :param id: The id of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_time(self):
        """Gets the creation_time of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The creation_time of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this HistoryScheduleSuggestionRecord.


        :param creation_time: The creation_time of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The tenant_id of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this HistoryScheduleSuggestionRecord.


        :param tenant_id: The tenant_id of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The last_modification_time of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this HistoryScheduleSuggestionRecord.


        :param last_modification_time: The last_modification_time of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def indicator(self):
        """Gets the indicator of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The indicator of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this HistoryScheduleSuggestionRecord.


        :param indicator: The indicator of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: str
        """

        self._indicator = indicator

    @property
    def show_name(self):
        """Gets the show_name of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The show_name of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        """Sets the show_name of this HistoryScheduleSuggestionRecord.


        :param show_name: The show_name of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: str
        """

        self._show_name = show_name

    @property
    def date_type(self):
        """Gets the date_type of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The date_type of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: str
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this HistoryScheduleSuggestionRecord.


        :param date_type: The date_type of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: str
        """

        self._date_type = date_type

    @property
    def measure_value(self):
        """Gets the measure_value of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The measure_value of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: float
        """
        return self._measure_value

    @measure_value.setter
    def measure_value(self, measure_value):
        """Sets the measure_value of this HistoryScheduleSuggestionRecord.


        :param measure_value: The measure_value of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: float
        """

        self._measure_value = measure_value

    @property
    def simulation_value(self):
        """Gets the simulation_value of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The simulation_value of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: float
        """
        return self._simulation_value

    @simulation_value.setter
    def simulation_value(self, simulation_value):
        """Sets the simulation_value of this HistoryScheduleSuggestionRecord.


        :param simulation_value: The simulation_value of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: float
        """

        self._simulation_value = simulation_value

    @property
    def suggestion(self):
        """Gets the suggestion of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The suggestion of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this HistoryScheduleSuggestionRecord.


        :param suggestion: The suggestion of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: str
        """

        self._suggestion = suggestion

    @property
    def operation(self):
        """Gets the operation of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The operation of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this HistoryScheduleSuggestionRecord.


        :param operation: The operation of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def time(self):
        """Gets the time of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The time of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this HistoryScheduleSuggestionRecord.


        :param time: The time of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def is_apply(self):
        """Gets the is_apply of this HistoryScheduleSuggestionRecord.  # noqa: E501


        :return: The is_apply of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :rtype: bool
        """
        return self._is_apply

    @is_apply.setter
    def is_apply(self, is_apply):
        """Sets the is_apply of this HistoryScheduleSuggestionRecord.


        :param is_apply: The is_apply of this HistoryScheduleSuggestionRecord.  # noqa: E501
        :type: bool
        """

        self._is_apply = is_apply

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
        if not isinstance(other, HistoryScheduleSuggestionRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HistoryScheduleSuggestionRecord):
            return True

        return self.to_dict() != other.to_dict()