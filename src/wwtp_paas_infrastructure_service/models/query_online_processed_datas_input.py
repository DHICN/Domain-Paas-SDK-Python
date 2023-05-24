# coding: utf-8

"""
    wwtp-paas-infrastructure-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wwtp_paas_infrastructure_service.configuration import Configuration


class QueryOnlineProcessedDatasInput(object):
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
        'start_time': 'str',
        'end_time': 'str',
        'codes': 'list[str]',
        'tag': 'str'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'codes': 'codes',
        'tag': 'tag'
    }

    def __init__(self, start_time=None, end_time=None, codes=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """QueryOnlineProcessedDatasInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_time = None
        self._end_time = None
        self._codes = None
        self._tag = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.codes = codes
        self.tag = tag

    @property
    def start_time(self):
        """Gets the start_time of this QueryOnlineProcessedDatasInput.  # noqa: E501

        开始时间 start time  # noqa: E501

        :return: The start_time of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryOnlineProcessedDatasInput.

        开始时间 start time  # noqa: E501

        :param start_time: The start_time of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryOnlineProcessedDatasInput.  # noqa: E501

        结束时间 end time  # noqa: E501

        :return: The end_time of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryOnlineProcessedDatasInput.

        结束时间 end time  # noqa: E501

        :param end_time: The end_time of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and end_time is None:  # noqa: E501
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def codes(self):
        """Gets the codes of this QueryOnlineProcessedDatasInput.  # noqa: E501

        点位编码 online point codes  # noqa: E501

        :return: The codes of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this QueryOnlineProcessedDatasInput.

        点位编码 online point codes  # noqa: E501

        :param codes: The codes of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def tag(self):
        """Gets the tag of this QueryOnlineProcessedDatasInput.  # noqa: E501

        清洗标签 clean tag  # noqa: E501

        :return: The tag of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this QueryOnlineProcessedDatasInput.

        清洗标签 clean tag  # noqa: E501

        :param tag: The tag of this QueryOnlineProcessedDatasInput.  # noqa: E501
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, QueryOnlineProcessedDatasInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryOnlineProcessedDatasInput):
            return True

        return self.to_dict() != other.to_dict()
