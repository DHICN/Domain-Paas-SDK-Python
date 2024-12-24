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

from dhicn_iot_service.configuration import Configuration


class HisDataSearchInput(object):
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
        'is_search_measure': 'bool',
        'is_search_simul': 'bool',
        'library_id': 'str',
        'device_code': 'str',
        'indicator': 'str',
        'start_ts': 'datetime',
        'end_ts': 'datetime',
        'order_by': 'str',
        'sample': 'str',
        'interval': 'int'
    }

    attribute_map = {
        'is_search_measure': 'isSearchMeasure',
        'is_search_simul': 'isSearchSimul',
        'library_id': 'libraryId',
        'device_code': 'deviceCode',
        'indicator': 'indicator',
        'start_ts': 'startTs',
        'end_ts': 'endTs',
        'order_by': 'orderBy',
        'sample': 'sample',
        'interval': 'interval'
    }

    def __init__(self, is_search_measure=None, is_search_simul=None, library_id=None, device_code=None, indicator=None, start_ts=None, end_ts=None, order_by=None, sample=None, interval=None, local_vars_configuration=None):  # noqa: E501
        """HisDataSearchInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_search_measure = None
        self._is_search_simul = None
        self._library_id = None
        self._device_code = None
        self._indicator = None
        self._start_ts = None
        self._end_ts = None
        self._order_by = None
        self._sample = None
        self._interval = None
        self.discriminator = None

        self.is_search_measure = is_search_measure
        self.is_search_simul = is_search_simul
        self.library_id = library_id
        self.device_code = device_code
        self.indicator = indicator
        self.start_ts = start_ts
        self.end_ts = end_ts
        self.order_by = order_by
        self.sample = sample
        if interval is not None:
            self.interval = interval

    @property
    def is_search_measure(self):
        """Gets the is_search_measure of this HisDataSearchInput.  # noqa: E501

        是否查询实测历史数据  # noqa: E501

        :return: The is_search_measure of this HisDataSearchInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_search_measure

    @is_search_measure.setter
    def is_search_measure(self, is_search_measure):
        """Sets the is_search_measure of this HisDataSearchInput.

        是否查询实测历史数据  # noqa: E501

        :param is_search_measure: The is_search_measure of this HisDataSearchInput.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_search_measure is None:  # noqa: E501
            raise ValueError("Invalid value for `is_search_measure`, must not be `None`")  # noqa: E501

        self._is_search_measure = is_search_measure

    @property
    def is_search_simul(self):
        """Gets the is_search_simul of this HisDataSearchInput.  # noqa: E501

        是否查询模拟历史数据  # noqa: E501

        :return: The is_search_simul of this HisDataSearchInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_search_simul

    @is_search_simul.setter
    def is_search_simul(self, is_search_simul):
        """Sets the is_search_simul of this HisDataSearchInput.

        是否查询模拟历史数据  # noqa: E501

        :param is_search_simul: The is_search_simul of this HisDataSearchInput.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_search_simul is None:  # noqa: E501
            raise ValueError("Invalid value for `is_search_simul`, must not be `None`")  # noqa: E501

        self._is_search_simul = is_search_simul

    @property
    def library_id(self):
        """Gets the library_id of this HisDataSearchInput.  # noqa: E501

        方案类库Id,即:模拟场景;若IsSearchSimul为true,此字段必填  # noqa: E501

        :return: The library_id of this HisDataSearchInput.  # noqa: E501
        :rtype: str
        """
        return self._library_id

    @library_id.setter
    def library_id(self, library_id):
        """Sets the library_id of this HisDataSearchInput.

        方案类库Id,即:模拟场景;若IsSearchSimul为true,此字段必填  # noqa: E501

        :param library_id: The library_id of this HisDataSearchInput.  # noqa: E501
        :type: str
        """

        self._library_id = library_id

    @property
    def device_code(self):
        """Gets the device_code of this HisDataSearchInput.  # noqa: E501

        设备名称,若当前项目下Indicator有重复,设备名称必传  # noqa: E501

        :return: The device_code of this HisDataSearchInput.  # noqa: E501
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        """Sets the device_code of this HisDataSearchInput.

        设备名称,若当前项目下Indicator有重复,设备名称必传  # noqa: E501

        :param device_code: The device_code of this HisDataSearchInput.  # noqa: E501
        :type: str
        """

        self._device_code = device_code

    @property
    def indicator(self):
        """Gets the indicator of this HisDataSearchInput.  # noqa: E501

        指标 indicator  # noqa: E501

        :return: The indicator of this HisDataSearchInput.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this HisDataSearchInput.

        指标 indicator  # noqa: E501

        :param indicator: The indicator of this HisDataSearchInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and indicator is None:  # noqa: E501
            raise ValueError("Invalid value for `indicator`, must not be `None`")  # noqa: E501

        self._indicator = indicator

    @property
    def start_ts(self):
        """Gets the start_ts of this HisDataSearchInput.  # noqa: E501

        查询开始时间 start time  # noqa: E501

        :return: The start_ts of this HisDataSearchInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this HisDataSearchInput.

        查询开始时间 start time  # noqa: E501

        :param start_ts: The start_ts of this HisDataSearchInput.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_ts is None:  # noqa: E501
            raise ValueError("Invalid value for `start_ts`, must not be `None`")  # noqa: E501

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this HisDataSearchInput.  # noqa: E501

        查询结束时间 end time  # noqa: E501

        :return: The end_ts of this HisDataSearchInput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this HisDataSearchInput.

        查询结束时间 end time  # noqa: E501

        :param end_ts: The end_ts of this HisDataSearchInput.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_ts is None:  # noqa: E501
            raise ValueError("Invalid value for `end_ts`, must not be `None`")  # noqa: E501

        self._end_ts = end_ts

    @property
    def order_by(self):
        """Gets the order_by of this HisDataSearchInput.  # noqa: E501

        排序方式，ASC (升序)，DESC (降序) sort order, ASC (ASCENDING) or DESC (DESCENDING);默认是降序DESC  # noqa: E501

        :return: The order_by of this HisDataSearchInput.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this HisDataSearchInput.

        排序方式，ASC (升序)，DESC (降序) sort order, ASC (ASCENDING) or DESC (DESCENDING);默认是降序DESC  # noqa: E501

        :param order_by: The order_by of this HisDataSearchInput.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def sample(self):
        """Gets the sample of this HisDataSearchInput.  # noqa: E501

        抽样类型,为空时代表不抽样,按:days hours year minutes years类型抽样  # noqa: E501

        :return: The sample of this HisDataSearchInput.  # noqa: E501
        :rtype: str
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this HisDataSearchInput.

        抽样类型,为空时代表不抽样,按:days hours year minutes years类型抽样  # noqa: E501

        :param sample: The sample of this HisDataSearchInput.  # noqa: E501
        :type: str
        """

        self._sample = sample

    @property
    def interval(self):
        """Gets the interval of this HisDataSearchInput.  # noqa: E501

        抽样频率,如:sample=minutes,interval=5,表示按照5分钟进行抽样  # noqa: E501

        :return: The interval of this HisDataSearchInput.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this HisDataSearchInput.

        抽样频率,如:sample=minutes,interval=5,表示按照5分钟进行抽样  # noqa: E501

        :param interval: The interval of this HisDataSearchInput.  # noqa: E501
        :type: int
        """

        self._interval = interval

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
        if not isinstance(other, HisDataSearchInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HisDataSearchInput):
            return True

        return self.to_dict() != other.to_dict()