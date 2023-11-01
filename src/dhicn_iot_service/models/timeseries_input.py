# coding: utf-8

"""
    IoT服务

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class TimeseriesInput(object):
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
        'device_id': 'str',
        'keys': 'list[str]',
        'start_ts': 'datetime',
        'end_ts': 'datetime',
        'order_by': 'str',
        'interval': 'int',
        'agg': 'str'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'keys': 'keys',
        'start_ts': 'startTs',
        'end_ts': 'endTs',
        'order_by': 'orderBy',
        'interval': 'interval',
        'agg': 'agg'
    }

    def __init__(self, device_id=None, keys=None, start_ts=None, end_ts=None, order_by=None, interval=None, agg=None, local_vars_configuration=None):  # noqa: E501
        """TimeseriesInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._keys = None
        self._start_ts = None
        self._end_ts = None
        self._order_by = None
        self._interval = None
        self._agg = None
        self.discriminator = None

        self.device_id = device_id
        self.keys = keys
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.order_by = order_by
        if interval is not None:
            self.interval = interval
        self.agg = agg

    @property
    def device_id(self):
        """Gets the device_id of this TimeseriesInput.  # noqa: E501

        设备ID device id  # noqa: E501

        :return: The device_id of this TimeseriesInput.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this TimeseriesInput.

        设备ID device id  # noqa: E501

        :param device_id: The device_id of this TimeseriesInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def keys(self):
        """Gets the keys of this TimeseriesInput.  # noqa: E501

        指标列表 indicators  # noqa: E501

        :return: The keys of this TimeseriesInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this TimeseriesInput.

        指标列表 indicators  # noqa: E501

        :param keys: The keys of this TimeseriesInput.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and keys is None:  # noqa: E501
            raise ValueError("Invalid value for `keys`, must not be `None`")  # noqa: E501

        self._keys = keys

    @property
    def start_ts(self):
        """Gets the start_ts of this TimeseriesInput.  # noqa: E501

        查询开始时间 start time  # noqa: E501

        :return: The start_ts of this TimeseriesInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this TimeseriesInput.

        查询开始时间 start time  # noqa: E501

        :param start_ts: The start_ts of this TimeseriesInput.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_ts is None:  # noqa: E501
            raise ValueError("Invalid value for `start_ts`, must not be `None`")  # noqa: E501

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this TimeseriesInput.  # noqa: E501

        查询结束时间 end time  # noqa: E501

        :return: The end_ts of this TimeseriesInput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this TimeseriesInput.

        查询结束时间 end time  # noqa: E501

        :param end_ts: The end_ts of this TimeseriesInput.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_ts is None:  # noqa: E501
            raise ValueError("Invalid value for `end_ts`, must not be `None`")  # noqa: E501

        self._end_ts = end_ts

    @property
    def order_by(self):
        """Gets the order_by of this TimeseriesInput.  # noqa: E501

        排序方式，ASC (升序)，DESC (降序) sort order, ASC (ASCENDING) or DESC (DESCENDING);默认是降序DESC  # noqa: E501

        :return: The order_by of this TimeseriesInput.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this TimeseriesInput.

        排序方式，ASC (升序)，DESC (降序) sort order, ASC (ASCENDING) or DESC (DESCENDING);默认是降序DESC  # noqa: E501

        :param order_by: The order_by of this TimeseriesInput.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def interval(self):
        """Gets the interval of this TimeseriesInput.  # noqa: E501


        :return: The interval of this TimeseriesInput.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this TimeseriesInput.


        :param interval: The interval of this TimeseriesInput.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def agg(self):
        """Gets the agg of this TimeseriesInput.  # noqa: E501


        :return: The agg of this TimeseriesInput.  # noqa: E501
        :rtype: str
        """
        return self._agg

    @agg.setter
    def agg(self, agg):
        """Sets the agg of this TimeseriesInput.


        :param agg: The agg of this TimeseriesInput.  # noqa: E501
        :type: str
        """

        self._agg = agg

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
        if not isinstance(other, TimeseriesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeseriesInput):
            return True

        return self.to_dict() != other.to_dict()
