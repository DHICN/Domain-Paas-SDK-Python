# coding: utf-8

"""
    scenario-compute-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from scenario_compute_service.configuration import Configuration


class DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput(object):
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
        'new_scenario_name': 'str',
        'scene_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'new_scenario_name': 'newScenarioName',
        'scene_id': 'sceneId',
        'start_time': 'startTime',
        'end_time': 'endTime'
    }

    def __init__(self, new_scenario_name=None, scene_id=None, start_time=None, end_time=None, local_vars_configuration=None):  # noqa: E501
        """DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._new_scenario_name = None
        self._scene_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.new_scenario_name = new_scenario_name
        self.scene_id = scene_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def new_scenario_name(self):
        """Gets the new_scenario_name of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501

        accident scenario name  # noqa: E501

        :return: The new_scenario_name of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :rtype: str
        """
        return self._new_scenario_name

    @new_scenario_name.setter
    def new_scenario_name(self, new_scenario_name):
        """Sets the new_scenario_name of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.

        accident scenario name  # noqa: E501

        :param new_scenario_name: The new_scenario_name of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :type: str
        """

        self._new_scenario_name = new_scenario_name

    @property
    def scene_id(self):
        """Gets the scene_id of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501

        情景Id  # noqa: E501

        :return: The scene_id of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        """Sets the scene_id of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.

        情景Id  # noqa: E501

        :param scene_id: The scene_id of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :type: str
        """

        self._scene_id = scene_id

    @property
    def start_time(self):
        """Gets the start_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501

        Scenario starttime  # noqa: E501

        :return: The start_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.

        Scenario starttime  # noqa: E501

        :param start_time: The start_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501

        Sceanrio endtime  # noqa: E501

        :return: The end_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.

        Sceanrio endtime  # noqa: E501

        :param end_time: The end_time of this DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

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
        if not isinstance(other, DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DhiDssScenarioComputeScenarioDtosCreateWqAccidentScenarioInput):
            return True

        return self.to_dict() != other.to_dict()
