# coding: utf-8

"""
    accident-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from accident_manager_service.configuration import Configuration


class EventInfo(object):
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
        'scene_id': 'str',
        'name': 'str',
        'discharge_type': 'DischargeTypeEnum',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'discharge': 'float',
        'discharge_ts': 'str',
        'location': 'str',
        'remark': 'str',
        'event_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'scene_id': 'sceneId',
        'name': 'name',
        'discharge_type': 'dischargeType',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'discharge': 'discharge',
        'discharge_ts': 'dischargeTS',
        'location': 'location',
        'remark': 'remark',
        'event_type': 'eventType'
    }

    def __init__(self, id=None, scene_id=None, name=None, discharge_type=None, start_time=None, end_time=None, discharge=None, discharge_ts=None, location=None, remark=None, event_type=None, local_vars_configuration=None):  # noqa: E501
        """EventInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._scene_id = None
        self._name = None
        self._discharge_type = None
        self._start_time = None
        self._end_time = None
        self._discharge = None
        self._discharge_ts = None
        self._location = None
        self._remark = None
        self._event_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if scene_id is not None:
            self.scene_id = scene_id
        self.name = name
        if discharge_type is not None:
            self.discharge_type = discharge_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if discharge is not None:
            self.discharge = discharge
        self.discharge_ts = discharge_ts
        self.location = location
        self.remark = remark
        self.event_type = event_type

    @property
    def id(self):
        """Gets the id of this EventInfo.  # noqa: E501

        事件ID event id  # noqa: E501

        :return: The id of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventInfo.

        事件ID event id  # noqa: E501

        :param id: The id of this EventInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def scene_id(self):
        """Gets the scene_id of this EventInfo.  # noqa: E501

        情景ID scene id  # noqa: E501

        :return: The scene_id of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        """Sets the scene_id of this EventInfo.

        情景ID scene id  # noqa: E501

        :param scene_id: The scene_id of this EventInfo.  # noqa: E501
        :type: str
        """

        self._scene_id = scene_id

    @property
    def name(self):
        """Gets the name of this EventInfo.  # noqa: E501

        事件名称 event name  # noqa: E501

        :return: The name of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventInfo.

        事件名称 event name  # noqa: E501

        :param name: The name of this EventInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def discharge_type(self):
        """Gets the discharge_type of this EventInfo.  # noqa: E501


        :return: The discharge_type of this EventInfo.  # noqa: E501
        :rtype: DischargeTypeEnum
        """
        return self._discharge_type

    @discharge_type.setter
    def discharge_type(self, discharge_type):
        """Sets the discharge_type of this EventInfo.


        :param discharge_type: The discharge_type of this EventInfo.  # noqa: E501
        :type: DischargeTypeEnum
        """

        self._discharge_type = discharge_type

    @property
    def start_time(self):
        """Gets the start_time of this EventInfo.  # noqa: E501

        事件开始时间 event start time  # noqa: E501

        :return: The start_time of this EventInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this EventInfo.

        事件开始时间 event start time  # noqa: E501

        :param start_time: The start_time of this EventInfo.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this EventInfo.  # noqa: E501

        事件结束时间 event end time  # noqa: E501

        :return: The end_time of this EventInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this EventInfo.

        事件结束时间 event end time  # noqa: E501

        :param end_time: The end_time of this EventInfo.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def discharge(self):
        """Gets the discharge of this EventInfo.  # noqa: E501

        流量 discharge  # noqa: E501

        :return: The discharge of this EventInfo.  # noqa: E501
        :rtype: float
        """
        return self._discharge

    @discharge.setter
    def discharge(self, discharge):
        """Sets the discharge of this EventInfo.

        流量 discharge  # noqa: E501

        :param discharge: The discharge of this EventInfo.  # noqa: E501
        :type: float
        """

        self._discharge = discharge

    @property
    def discharge_ts(self):
        """Gets the discharge_ts of this EventInfo.  # noqa: E501

        流量时间序列ID discharge time series id  # noqa: E501

        :return: The discharge_ts of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._discharge_ts

    @discharge_ts.setter
    def discharge_ts(self, discharge_ts):
        """Sets the discharge_ts of this EventInfo.

        流量时间序列ID discharge time series id  # noqa: E501

        :param discharge_ts: The discharge_ts of this EventInfo.  # noqa: E501
        :type: str
        """

        self._discharge_ts = discharge_ts

    @property
    def location(self):
        """Gets the location of this EventInfo.  # noqa: E501

        事件地点 event location  # noqa: E501

        :return: The location of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EventInfo.

        事件地点 event location  # noqa: E501

        :param location: The location of this EventInfo.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def remark(self):
        """Gets the remark of this EventInfo.  # noqa: E501

        事件备注 event remark  # noqa: E501

        :return: The remark of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this EventInfo.

        事件备注 event remark  # noqa: E501

        :param remark: The remark of this EventInfo.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def event_type(self):
        """Gets the event_type of this EventInfo.  # noqa: E501

        事件类型 event type  # noqa: E501

        :return: The event_type of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventInfo.

        事件类型 event type  # noqa: E501

        :param event_type: The event_type of this EventInfo.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

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
        if not isinstance(other, EventInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventInfo):
            return True

        return self.to_dict() != other.to_dict()