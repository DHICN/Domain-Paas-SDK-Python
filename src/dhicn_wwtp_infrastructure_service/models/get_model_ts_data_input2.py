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

from dhicn_wwtp_infrastructure_service.configuration import Configuration


class GetModelTsDataInput2(object):
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
        'scenario_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'code_assemblys': 'list[CodeAssembly]'
    }

    attribute_map = {
        'scenario_id': 'scenarioId',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'code_assemblys': 'codeAssemblys'
    }

    def __init__(self, scenario_id=None, start_time=None, end_time=None, code_assemblys=None, local_vars_configuration=None):  # noqa: E501
        """GetModelTsDataInput2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scenario_id = None
        self._start_time = None
        self._end_time = None
        self._code_assemblys = None
        self.discriminator = None

        self.scenario_id = scenario_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.code_assemblys = code_assemblys

    @property
    def scenario_id(self):
        """Gets the scenario_id of this GetModelTsDataInput2.  # noqa: E501


        :return: The scenario_id of this GetModelTsDataInput2.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this GetModelTsDataInput2.


        :param scenario_id: The scenario_id of this GetModelTsDataInput2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scenario_id is None:  # noqa: E501
            raise ValueError("Invalid value for `scenario_id`, must not be `None`")  # noqa: E501

        self._scenario_id = scenario_id

    @property
    def start_time(self):
        """Gets the start_time of this GetModelTsDataInput2.  # noqa: E501

        开始时间 start time  # noqa: E501

        :return: The start_time of this GetModelTsDataInput2.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GetModelTsDataInput2.

        开始时间 start time  # noqa: E501

        :param start_time: The start_time of this GetModelTsDataInput2.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this GetModelTsDataInput2.  # noqa: E501

        结束时间 end time  # noqa: E501

        :return: The end_time of this GetModelTsDataInput2.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GetModelTsDataInput2.

        结束时间 end time  # noqa: E501

        :param end_time: The end_time of this GetModelTsDataInput2.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def code_assemblys(self):
        """Gets the code_assemblys of this GetModelTsDataInput2.  # noqa: E501

        模型点位信息 model node codes  # noqa: E501

        :return: The code_assemblys of this GetModelTsDataInput2.  # noqa: E501
        :rtype: list[CodeAssembly]
        """
        return self._code_assemblys

    @code_assemblys.setter
    def code_assemblys(self, code_assemblys):
        """Sets the code_assemblys of this GetModelTsDataInput2.

        模型点位信息 model node codes  # noqa: E501

        :param code_assemblys: The code_assemblys of this GetModelTsDataInput2.  # noqa: E501
        :type: list[CodeAssembly]
        """
        if self.local_vars_configuration.client_side_validation and code_assemblys is None:  # noqa: E501
            raise ValueError("Invalid value for `code_assemblys`, must not be `None`")  # noqa: E501

        self._code_assemblys = code_assemblys

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
        if not isinstance(other, GetModelTsDataInput2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetModelTsDataInput2):
            return True

        return self.to_dict() != other.to_dict()
