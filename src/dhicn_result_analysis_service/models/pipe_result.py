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


class PipeResult(object):
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
        'pipe_id': 'str',
        'diameter': 'float',
        'length': 'float',
        'abs_flow': 'float',
        'headloss': 'float',
        'velocity_max': 'float',
        'velocity_change': 'float',
        'shear_stress': 'float',
        'criteria_type': 'str',
        'criteria_value': 'float',
        'criteria_pct': 'str',
        'flushing_time': 'float',
        'flushing_pct': 'float',
        'comment': 'str'
    }

    attribute_map = {
        'pipe_id': 'pipeID',
        'diameter': 'diameter',
        'length': 'length',
        'abs_flow': 'absFlow',
        'headloss': 'headloss',
        'velocity_max': 'velocityMax',
        'velocity_change': 'velocityChange',
        'shear_stress': 'shearStress',
        'criteria_type': 'criteriaType',
        'criteria_value': 'criteriaValue',
        'criteria_pct': 'criteriaPct',
        'flushing_time': 'flushingTime',
        'flushing_pct': 'flushingPct',
        'comment': 'comment'
    }

    def __init__(self, pipe_id=None, diameter=None, length=None, abs_flow=None, headloss=None, velocity_max=None, velocity_change=None, shear_stress=None, criteria_type=None, criteria_value=None, criteria_pct=None, flushing_time=None, flushing_pct=None, comment=None, local_vars_configuration=None):  # noqa: E501
        """PipeResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pipe_id = None
        self._diameter = None
        self._length = None
        self._abs_flow = None
        self._headloss = None
        self._velocity_max = None
        self._velocity_change = None
        self._shear_stress = None
        self._criteria_type = None
        self._criteria_value = None
        self._criteria_pct = None
        self._flushing_time = None
        self._flushing_pct = None
        self._comment = None
        self.discriminator = None

        self.pipe_id = pipe_id
        if diameter is not None:
            self.diameter = diameter
        if length is not None:
            self.length = length
        if abs_flow is not None:
            self.abs_flow = abs_flow
        if headloss is not None:
            self.headloss = headloss
        if velocity_max is not None:
            self.velocity_max = velocity_max
        if velocity_change is not None:
            self.velocity_change = velocity_change
        if shear_stress is not None:
            self.shear_stress = shear_stress
        self.criteria_type = criteria_type
        if criteria_value is not None:
            self.criteria_value = criteria_value
        self.criteria_pct = criteria_pct
        if flushing_time is not None:
            self.flushing_time = flushing_time
        if flushing_pct is not None:
            self.flushing_pct = flushing_pct
        self.comment = comment

    @property
    def pipe_id(self):
        """Gets the pipe_id of this PipeResult.  # noqa: E501


        :return: The pipe_id of this PipeResult.  # noqa: E501
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        """Sets the pipe_id of this PipeResult.


        :param pipe_id: The pipe_id of this PipeResult.  # noqa: E501
        :type: str
        """

        self._pipe_id = pipe_id

    @property
    def diameter(self):
        """Gets the diameter of this PipeResult.  # noqa: E501


        :return: The diameter of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this PipeResult.


        :param diameter: The diameter of this PipeResult.  # noqa: E501
        :type: float
        """

        self._diameter = diameter

    @property
    def length(self):
        """Gets the length of this PipeResult.  # noqa: E501


        :return: The length of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this PipeResult.


        :param length: The length of this PipeResult.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def abs_flow(self):
        """Gets the abs_flow of this PipeResult.  # noqa: E501


        :return: The abs_flow of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._abs_flow

    @abs_flow.setter
    def abs_flow(self, abs_flow):
        """Sets the abs_flow of this PipeResult.


        :param abs_flow: The abs_flow of this PipeResult.  # noqa: E501
        :type: float
        """

        self._abs_flow = abs_flow

    @property
    def headloss(self):
        """Gets the headloss of this PipeResult.  # noqa: E501


        :return: The headloss of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._headloss

    @headloss.setter
    def headloss(self, headloss):
        """Sets the headloss of this PipeResult.


        :param headloss: The headloss of this PipeResult.  # noqa: E501
        :type: float
        """

        self._headloss = headloss

    @property
    def velocity_max(self):
        """Gets the velocity_max of this PipeResult.  # noqa: E501


        :return: The velocity_max of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._velocity_max

    @velocity_max.setter
    def velocity_max(self, velocity_max):
        """Sets the velocity_max of this PipeResult.


        :param velocity_max: The velocity_max of this PipeResult.  # noqa: E501
        :type: float
        """

        self._velocity_max = velocity_max

    @property
    def velocity_change(self):
        """Gets the velocity_change of this PipeResult.  # noqa: E501


        :return: The velocity_change of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._velocity_change

    @velocity_change.setter
    def velocity_change(self, velocity_change):
        """Sets the velocity_change of this PipeResult.


        :param velocity_change: The velocity_change of this PipeResult.  # noqa: E501
        :type: float
        """

        self._velocity_change = velocity_change

    @property
    def shear_stress(self):
        """Gets the shear_stress of this PipeResult.  # noqa: E501


        :return: The shear_stress of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._shear_stress

    @shear_stress.setter
    def shear_stress(self, shear_stress):
        """Sets the shear_stress of this PipeResult.


        :param shear_stress: The shear_stress of this PipeResult.  # noqa: E501
        :type: float
        """

        self._shear_stress = shear_stress

    @property
    def criteria_type(self):
        """Gets the criteria_type of this PipeResult.  # noqa: E501


        :return: The criteria_type of this PipeResult.  # noqa: E501
        :rtype: str
        """
        return self._criteria_type

    @criteria_type.setter
    def criteria_type(self, criteria_type):
        """Sets the criteria_type of this PipeResult.


        :param criteria_type: The criteria_type of this PipeResult.  # noqa: E501
        :type: str
        """

        self._criteria_type = criteria_type

    @property
    def criteria_value(self):
        """Gets the criteria_value of this PipeResult.  # noqa: E501


        :return: The criteria_value of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._criteria_value

    @criteria_value.setter
    def criteria_value(self, criteria_value):
        """Sets the criteria_value of this PipeResult.


        :param criteria_value: The criteria_value of this PipeResult.  # noqa: E501
        :type: float
        """

        self._criteria_value = criteria_value

    @property
    def criteria_pct(self):
        """Gets the criteria_pct of this PipeResult.  # noqa: E501


        :return: The criteria_pct of this PipeResult.  # noqa: E501
        :rtype: str
        """
        return self._criteria_pct

    @criteria_pct.setter
    def criteria_pct(self, criteria_pct):
        """Sets the criteria_pct of this PipeResult.


        :param criteria_pct: The criteria_pct of this PipeResult.  # noqa: E501
        :type: str
        """

        self._criteria_pct = criteria_pct

    @property
    def flushing_time(self):
        """Gets the flushing_time of this PipeResult.  # noqa: E501


        :return: The flushing_time of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._flushing_time

    @flushing_time.setter
    def flushing_time(self, flushing_time):
        """Sets the flushing_time of this PipeResult.


        :param flushing_time: The flushing_time of this PipeResult.  # noqa: E501
        :type: float
        """

        self._flushing_time = flushing_time

    @property
    def flushing_pct(self):
        """Gets the flushing_pct of this PipeResult.  # noqa: E501


        :return: The flushing_pct of this PipeResult.  # noqa: E501
        :rtype: float
        """
        return self._flushing_pct

    @flushing_pct.setter
    def flushing_pct(self, flushing_pct):
        """Sets the flushing_pct of this PipeResult.


        :param flushing_pct: The flushing_pct of this PipeResult.  # noqa: E501
        :type: float
        """

        self._flushing_pct = flushing_pct

    @property
    def comment(self):
        """Gets the comment of this PipeResult.  # noqa: E501


        :return: The comment of this PipeResult.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PipeResult.


        :param comment: The comment of this PipeResult.  # noqa: E501
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
        if not isinstance(other, PipeResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipeResult):
            return True

        return self.to_dict() != other.to_dict()
