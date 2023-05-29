# coding: utf-8

"""
    wd-domain-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wd_service_domain.configuration import Configuration


class SavePipeBurstInfoInput(object):
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
        'accident_name': 'str',
        'scenario_id': 'str',
        'pipe_burst_events': 'list[WdEventDetailInput]',
        'gis_valve_info_list': 'list[GisValveInfo]'
    }

    attribute_map = {
        'accident_name': 'accidentName',
        'scenario_id': 'scenarioId',
        'pipe_burst_events': 'pipeBurstEvents',
        'gis_valve_info_list': 'gisValveInfoList'
    }

    def __init__(self, accident_name=None, scenario_id=None, pipe_burst_events=None, gis_valve_info_list=None, local_vars_configuration=None):  # noqa: E501
        """SavePipeBurstInfoInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accident_name = None
        self._scenario_id = None
        self._pipe_burst_events = None
        self._gis_valve_info_list = None
        self.discriminator = None

        self.accident_name = accident_name
        if scenario_id is not None:
            self.scenario_id = scenario_id
        self.pipe_burst_events = pipe_burst_events
        self.gis_valve_info_list = gis_valve_info_list

    @property
    def accident_name(self):
        """Gets the accident_name of this SavePipeBurstInfoInput.  # noqa: E501

        事故名称  # noqa: E501

        :return: The accident_name of this SavePipeBurstInfoInput.  # noqa: E501
        :rtype: str
        """
        return self._accident_name

    @accident_name.setter
    def accident_name(self, accident_name):
        """Sets the accident_name of this SavePipeBurstInfoInput.

        事故名称  # noqa: E501

        :param accident_name: The accident_name of this SavePipeBurstInfoInput.  # noqa: E501
        :type: str
        """

        self._accident_name = accident_name

    @property
    def scenario_id(self):
        """Gets the scenario_id of this SavePipeBurstInfoInput.  # noqa: E501

        方案id  # noqa: E501

        :return: The scenario_id of this SavePipeBurstInfoInput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this SavePipeBurstInfoInput.

        方案id  # noqa: E501

        :param scenario_id: The scenario_id of this SavePipeBurstInfoInput.  # noqa: E501
        :type: str
        """

        self._scenario_id = scenario_id

    @property
    def pipe_burst_events(self):
        """Gets the pipe_burst_events of this SavePipeBurstInfoInput.  # noqa: E501

        爆管事件列表  # noqa: E501

        :return: The pipe_burst_events of this SavePipeBurstInfoInput.  # noqa: E501
        :rtype: list[WdEventDetailInput]
        """
        return self._pipe_burst_events

    @pipe_burst_events.setter
    def pipe_burst_events(self, pipe_burst_events):
        """Sets the pipe_burst_events of this SavePipeBurstInfoInput.

        爆管事件列表  # noqa: E501

        :param pipe_burst_events: The pipe_burst_events of this SavePipeBurstInfoInput.  # noqa: E501
        :type: list[WdEventDetailInput]
        """

        self._pipe_burst_events = pipe_burst_events

    @property
    def gis_valve_info_list(self):
        """Gets the gis_valve_info_list of this SavePipeBurstInfoInput.  # noqa: E501

        阀门信息  # noqa: E501

        :return: The gis_valve_info_list of this SavePipeBurstInfoInput.  # noqa: E501
        :rtype: list[GisValveInfo]
        """
        return self._gis_valve_info_list

    @gis_valve_info_list.setter
    def gis_valve_info_list(self, gis_valve_info_list):
        """Sets the gis_valve_info_list of this SavePipeBurstInfoInput.

        阀门信息  # noqa: E501

        :param gis_valve_info_list: The gis_valve_info_list of this SavePipeBurstInfoInput.  # noqa: E501
        :type: list[GisValveInfo]
        """

        self._gis_valve_info_list = gis_valve_info_list

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
        if not isinstance(other, SavePipeBurstInfoInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SavePipeBurstInfoInput):
            return True

        return self.to_dict() != other.to_dict()
