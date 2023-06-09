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

from dhicn_wd_domain_service.configuration import Configuration


class UpdatePipeRiskPropertyInput(object):
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
        'pipe_model_id': 'str',
        'pipe_material': 'float',
        'pipe_age': 'float',
        'interface_type': 'float',
        'pipe_broken_num': 'float',
        'earthing_type': 'float',
        'road_load': 'float',
        'pressure_wave': 'float',
        'id': 'str'
    }

    attribute_map = {
        'pipe_model_id': 'pipeModelId',
        'pipe_material': 'pipeMaterial',
        'pipe_age': 'pipeAge',
        'interface_type': 'interfaceType',
        'pipe_broken_num': 'pipeBrokenNum',
        'earthing_type': 'earthingType',
        'road_load': 'roadLoad',
        'pressure_wave': 'pressureWave',
        'id': 'id'
    }

    def __init__(self, pipe_model_id=None, pipe_material=None, pipe_age=None, interface_type=None, pipe_broken_num=None, earthing_type=None, road_load=None, pressure_wave=None, id=None, local_vars_configuration=None):  # noqa: E501
        """UpdatePipeRiskPropertyInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pipe_model_id = None
        self._pipe_material = None
        self._pipe_age = None
        self._interface_type = None
        self._pipe_broken_num = None
        self._earthing_type = None
        self._road_load = None
        self._pressure_wave = None
        self._id = None
        self.discriminator = None

        self.pipe_model_id = pipe_model_id
        self.pipe_material = pipe_material
        self.pipe_age = pipe_age
        self.interface_type = interface_type
        self.pipe_broken_num = pipe_broken_num
        self.earthing_type = earthing_type
        self.road_load = road_load
        self.pressure_wave = pressure_wave
        self.id = id

    @property
    def pipe_model_id(self):
        """Gets the pipe_model_id of this UpdatePipeRiskPropertyInput.  # noqa: E501

        管道模型id  # noqa: E501

        :return: The pipe_model_id of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: str
        """
        return self._pipe_model_id

    @pipe_model_id.setter
    def pipe_model_id(self, pipe_model_id):
        """Sets the pipe_model_id of this UpdatePipeRiskPropertyInput.

        管道模型id  # noqa: E501

        :param pipe_model_id: The pipe_model_id of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pipe_model_id is None:  # noqa: E501
            raise ValueError("Invalid value for `pipe_model_id`, must not be `None`")  # noqa: E501

        self._pipe_model_id = pipe_model_id

    @property
    def pipe_material(self):
        """Gets the pipe_material of this UpdatePipeRiskPropertyInput.  # noqa: E501

        管材  # noqa: E501

        :return: The pipe_material of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: float
        """
        return self._pipe_material

    @pipe_material.setter
    def pipe_material(self, pipe_material):
        """Sets the pipe_material of this UpdatePipeRiskPropertyInput.

        管材  # noqa: E501

        :param pipe_material: The pipe_material of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and pipe_material is None:  # noqa: E501
            raise ValueError("Invalid value for `pipe_material`, must not be `None`")  # noqa: E501

        self._pipe_material = pipe_material

    @property
    def pipe_age(self):
        """Gets the pipe_age of this UpdatePipeRiskPropertyInput.  # noqa: E501

        管龄  # noqa: E501

        :return: The pipe_age of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: float
        """
        return self._pipe_age

    @pipe_age.setter
    def pipe_age(self, pipe_age):
        """Sets the pipe_age of this UpdatePipeRiskPropertyInput.

        管龄  # noqa: E501

        :param pipe_age: The pipe_age of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and pipe_age is None:  # noqa: E501
            raise ValueError("Invalid value for `pipe_age`, must not be `None`")  # noqa: E501

        self._pipe_age = pipe_age

    @property
    def interface_type(self):
        """Gets the interface_type of this UpdatePipeRiskPropertyInput.  # noqa: E501

        接口类型  # noqa: E501

        :return: The interface_type of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: float
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this UpdatePipeRiskPropertyInput.

        接口类型  # noqa: E501

        :param interface_type: The interface_type of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and interface_type is None:  # noqa: E501
            raise ValueError("Invalid value for `interface_type`, must not be `None`")  # noqa: E501

        self._interface_type = interface_type

    @property
    def pipe_broken_num(self):
        """Gets the pipe_broken_num of this UpdatePipeRiskPropertyInput.  # noqa: E501

        爆管次数  # noqa: E501

        :return: The pipe_broken_num of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: float
        """
        return self._pipe_broken_num

    @pipe_broken_num.setter
    def pipe_broken_num(self, pipe_broken_num):
        """Sets the pipe_broken_num of this UpdatePipeRiskPropertyInput.

        爆管次数  # noqa: E501

        :param pipe_broken_num: The pipe_broken_num of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and pipe_broken_num is None:  # noqa: E501
            raise ValueError("Invalid value for `pipe_broken_num`, must not be `None`")  # noqa: E501

        self._pipe_broken_num = pipe_broken_num

    @property
    def earthing_type(self):
        """Gets the earthing_type of this UpdatePipeRiskPropertyInput.  # noqa: E501

        覆土类型  # noqa: E501

        :return: The earthing_type of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: float
        """
        return self._earthing_type

    @earthing_type.setter
    def earthing_type(self, earthing_type):
        """Sets the earthing_type of this UpdatePipeRiskPropertyInput.

        覆土类型  # noqa: E501

        :param earthing_type: The earthing_type of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and earthing_type is None:  # noqa: E501
            raise ValueError("Invalid value for `earthing_type`, must not be `None`")  # noqa: E501

        self._earthing_type = earthing_type

    @property
    def road_load(self):
        """Gets the road_load of this UpdatePipeRiskPropertyInput.  # noqa: E501

        路面负荷  # noqa: E501

        :return: The road_load of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: float
        """
        return self._road_load

    @road_load.setter
    def road_load(self, road_load):
        """Sets the road_load of this UpdatePipeRiskPropertyInput.

        路面负荷  # noqa: E501

        :param road_load: The road_load of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and road_load is None:  # noqa: E501
            raise ValueError("Invalid value for `road_load`, must not be `None`")  # noqa: E501

        self._road_load = road_load

    @property
    def pressure_wave(self):
        """Gets the pressure_wave of this UpdatePipeRiskPropertyInput.  # noqa: E501

        压力波动  # noqa: E501

        :return: The pressure_wave of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: float
        """
        return self._pressure_wave

    @pressure_wave.setter
    def pressure_wave(self, pressure_wave):
        """Sets the pressure_wave of this UpdatePipeRiskPropertyInput.

        压力波动  # noqa: E501

        :param pressure_wave: The pressure_wave of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and pressure_wave is None:  # noqa: E501
            raise ValueError("Invalid value for `pressure_wave`, must not be `None`")  # noqa: E501

        self._pressure_wave = pressure_wave

    @property
    def id(self):
        """Gets the id of this UpdatePipeRiskPropertyInput.  # noqa: E501


        :return: The id of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatePipeRiskPropertyInput.


        :param id: The id of this UpdatePipeRiskPropertyInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, UpdatePipeRiskPropertyInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatePipeRiskPropertyInput):
            return True

        return self.to_dict() != other.to_dict()
