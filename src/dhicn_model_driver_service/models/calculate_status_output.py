# coding: utf-8

"""
    model-driver-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_model_driver_service.configuration import Configuration


class CalculateStatusOutput(object):
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
        'queue_id': 'str',
        'scenario_id': 'str',
        'status': 'EnumStatus',
        'status_desc': 'str',
        'progress': 'float',
        'waiting_no': 'int'
    }

    attribute_map = {
        'queue_id': 'queueId',
        'scenario_id': 'scenarioId',
        'status': 'status',
        'status_desc': 'statusDesc',
        'progress': 'progress',
        'waiting_no': 'waitingNo'
    }

    def __init__(self, queue_id=None, scenario_id=None, status=None, status_desc=None, progress=None, waiting_no=None, local_vars_configuration=None):  # noqa: E501
        """CalculateStatusOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._queue_id = None
        self._scenario_id = None
        self._status = None
        self._status_desc = None
        self._progress = None
        self._waiting_no = None
        self.discriminator = None

        self.queue_id = queue_id
        if scenario_id is not None:
            self.scenario_id = scenario_id
        if status is not None:
            self.status = status
        self.status_desc = status_desc
        self.progress = progress
        self.waiting_no = waiting_no

    @property
    def queue_id(self):
        """Gets the queue_id of this CalculateStatusOutput.  # noqa: E501

        排队ID  # noqa: E501

        :return: The queue_id of this CalculateStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this CalculateStatusOutput.

        排队ID  # noqa: E501

        :param queue_id: The queue_id of this CalculateStatusOutput.  # noqa: E501
        :type: str
        """

        self._queue_id = queue_id

    @property
    def scenario_id(self):
        """Gets the scenario_id of this CalculateStatusOutput.  # noqa: E501

        方案ID  # noqa: E501

        :return: The scenario_id of this CalculateStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this CalculateStatusOutput.

        方案ID  # noqa: E501

        :param scenario_id: The scenario_id of this CalculateStatusOutput.  # noqa: E501
        :type: str
        """

        self._scenario_id = scenario_id

    @property
    def status(self):
        """Gets the status of this CalculateStatusOutput.  # noqa: E501


        :return: The status of this CalculateStatusOutput.  # noqa: E501
        :rtype: EnumStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CalculateStatusOutput.


        :param status: The status of this CalculateStatusOutput.  # noqa: E501
        :type: EnumStatus
        """

        self._status = status

    @property
    def status_desc(self):
        """Gets the status_desc of this CalculateStatusOutput.  # noqa: E501

        计算状态描述  # noqa: E501

        :return: The status_desc of this CalculateStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this CalculateStatusOutput.

        计算状态描述  # noqa: E501

        :param status_desc: The status_desc of this CalculateStatusOutput.  # noqa: E501
        :type: str
        """

        self._status_desc = status_desc

    @property
    def progress(self):
        """Gets the progress of this CalculateStatusOutput.  # noqa: E501

        计算进度  # noqa: E501

        :return: The progress of this CalculateStatusOutput.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this CalculateStatusOutput.

        计算进度  # noqa: E501

        :param progress: The progress of this CalculateStatusOutput.  # noqa: E501
        :type: float
        """

        self._progress = progress

    @property
    def waiting_no(self):
        """Gets the waiting_no of this CalculateStatusOutput.  # noqa: E501

        排队序号  # noqa: E501

        :return: The waiting_no of this CalculateStatusOutput.  # noqa: E501
        :rtype: int
        """
        return self._waiting_no

    @waiting_no.setter
    def waiting_no(self, waiting_no):
        """Sets the waiting_no of this CalculateStatusOutput.

        排队序号  # noqa: E501

        :param waiting_no: The waiting_no of this CalculateStatusOutput.  # noqa: E501
        :type: int
        """

        self._waiting_no = waiting_no

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
        if not isinstance(other, CalculateStatusOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalculateStatusOutput):
            return True

        return self.to_dict() != other.to_dict()
