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


class OutletResult(object):
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
        'outlet_id': 'str',
        'start': 'str',
        'end': 'str',
        'flushing_duration': 'str',
        'required_duration': 'str',
        'static_pressure': 'float',
        'residual_pressure': 'float',
        'avg_discharge': 'float',
        'water_volume': 'float',
        'avg_flush_success': 'float',
        'avg_flush_velocity': 'float',
        'comment': 'str'
    }

    attribute_map = {
        'outlet_id': 'outletID',
        'start': 'start',
        'end': 'end',
        'flushing_duration': 'flushingDuration',
        'required_duration': 'requiredDuration',
        'static_pressure': 'staticPressure',
        'residual_pressure': 'residualPressure',
        'avg_discharge': 'avgDischarge',
        'water_volume': 'waterVolume',
        'avg_flush_success': 'avgFlushSuccess',
        'avg_flush_velocity': 'avgFlushVelocity',
        'comment': 'comment'
    }

    def __init__(self, outlet_id=None, start=None, end=None, flushing_duration=None, required_duration=None, static_pressure=None, residual_pressure=None, avg_discharge=None, water_volume=None, avg_flush_success=None, avg_flush_velocity=None, comment=None, local_vars_configuration=None):  # noqa: E501
        """OutletResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._outlet_id = None
        self._start = None
        self._end = None
        self._flushing_duration = None
        self._required_duration = None
        self._static_pressure = None
        self._residual_pressure = None
        self._avg_discharge = None
        self._water_volume = None
        self._avg_flush_success = None
        self._avg_flush_velocity = None
        self._comment = None
        self.discriminator = None

        self.outlet_id = outlet_id
        self.start = start
        self.end = end
        self.flushing_duration = flushing_duration
        self.required_duration = required_duration
        if static_pressure is not None:
            self.static_pressure = static_pressure
        if residual_pressure is not None:
            self.residual_pressure = residual_pressure
        if avg_discharge is not None:
            self.avg_discharge = avg_discharge
        if water_volume is not None:
            self.water_volume = water_volume
        if avg_flush_success is not None:
            self.avg_flush_success = avg_flush_success
        if avg_flush_velocity is not None:
            self.avg_flush_velocity = avg_flush_velocity
        self.comment = comment

    @property
    def outlet_id(self):
        """Gets the outlet_id of this OutletResult.  # noqa: E501


        :return: The outlet_id of this OutletResult.  # noqa: E501
        :rtype: str
        """
        return self._outlet_id

    @outlet_id.setter
    def outlet_id(self, outlet_id):
        """Sets the outlet_id of this OutletResult.


        :param outlet_id: The outlet_id of this OutletResult.  # noqa: E501
        :type: str
        """

        self._outlet_id = outlet_id

    @property
    def start(self):
        """Gets the start of this OutletResult.  # noqa: E501


        :return: The start of this OutletResult.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this OutletResult.


        :param start: The start of this OutletResult.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this OutletResult.  # noqa: E501


        :return: The end of this OutletResult.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this OutletResult.


        :param end: The end of this OutletResult.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def flushing_duration(self):
        """Gets the flushing_duration of this OutletResult.  # noqa: E501


        :return: The flushing_duration of this OutletResult.  # noqa: E501
        :rtype: str
        """
        return self._flushing_duration

    @flushing_duration.setter
    def flushing_duration(self, flushing_duration):
        """Sets the flushing_duration of this OutletResult.


        :param flushing_duration: The flushing_duration of this OutletResult.  # noqa: E501
        :type: str
        """

        self._flushing_duration = flushing_duration

    @property
    def required_duration(self):
        """Gets the required_duration of this OutletResult.  # noqa: E501


        :return: The required_duration of this OutletResult.  # noqa: E501
        :rtype: str
        """
        return self._required_duration

    @required_duration.setter
    def required_duration(self, required_duration):
        """Sets the required_duration of this OutletResult.


        :param required_duration: The required_duration of this OutletResult.  # noqa: E501
        :type: str
        """

        self._required_duration = required_duration

    @property
    def static_pressure(self):
        """Gets the static_pressure of this OutletResult.  # noqa: E501


        :return: The static_pressure of this OutletResult.  # noqa: E501
        :rtype: float
        """
        return self._static_pressure

    @static_pressure.setter
    def static_pressure(self, static_pressure):
        """Sets the static_pressure of this OutletResult.


        :param static_pressure: The static_pressure of this OutletResult.  # noqa: E501
        :type: float
        """

        self._static_pressure = static_pressure

    @property
    def residual_pressure(self):
        """Gets the residual_pressure of this OutletResult.  # noqa: E501


        :return: The residual_pressure of this OutletResult.  # noqa: E501
        :rtype: float
        """
        return self._residual_pressure

    @residual_pressure.setter
    def residual_pressure(self, residual_pressure):
        """Sets the residual_pressure of this OutletResult.


        :param residual_pressure: The residual_pressure of this OutletResult.  # noqa: E501
        :type: float
        """

        self._residual_pressure = residual_pressure

    @property
    def avg_discharge(self):
        """Gets the avg_discharge of this OutletResult.  # noqa: E501


        :return: The avg_discharge of this OutletResult.  # noqa: E501
        :rtype: float
        """
        return self._avg_discharge

    @avg_discharge.setter
    def avg_discharge(self, avg_discharge):
        """Sets the avg_discharge of this OutletResult.


        :param avg_discharge: The avg_discharge of this OutletResult.  # noqa: E501
        :type: float
        """

        self._avg_discharge = avg_discharge

    @property
    def water_volume(self):
        """Gets the water_volume of this OutletResult.  # noqa: E501


        :return: The water_volume of this OutletResult.  # noqa: E501
        :rtype: float
        """
        return self._water_volume

    @water_volume.setter
    def water_volume(self, water_volume):
        """Sets the water_volume of this OutletResult.


        :param water_volume: The water_volume of this OutletResult.  # noqa: E501
        :type: float
        """

        self._water_volume = water_volume

    @property
    def avg_flush_success(self):
        """Gets the avg_flush_success of this OutletResult.  # noqa: E501


        :return: The avg_flush_success of this OutletResult.  # noqa: E501
        :rtype: float
        """
        return self._avg_flush_success

    @avg_flush_success.setter
    def avg_flush_success(self, avg_flush_success):
        """Sets the avg_flush_success of this OutletResult.


        :param avg_flush_success: The avg_flush_success of this OutletResult.  # noqa: E501
        :type: float
        """

        self._avg_flush_success = avg_flush_success

    @property
    def avg_flush_velocity(self):
        """Gets the avg_flush_velocity of this OutletResult.  # noqa: E501


        :return: The avg_flush_velocity of this OutletResult.  # noqa: E501
        :rtype: float
        """
        return self._avg_flush_velocity

    @avg_flush_velocity.setter
    def avg_flush_velocity(self, avg_flush_velocity):
        """Sets the avg_flush_velocity of this OutletResult.


        :param avg_flush_velocity: The avg_flush_velocity of this OutletResult.  # noqa: E501
        :type: float
        """

        self._avg_flush_velocity = avg_flush_velocity

    @property
    def comment(self):
        """Gets the comment of this OutletResult.  # noqa: E501


        :return: The comment of this OutletResult.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this OutletResult.


        :param comment: The comment of this OutletResult.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if not isinstance(other, OutletResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutletResult):
            return True

        return self.to_dict() != other.to_dict()
