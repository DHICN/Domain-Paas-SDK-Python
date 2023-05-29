# coding: utf-8

"""
    model-information-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from model_information_service.configuration import Configuration


class AddFlushingParaInput(object):
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
        'data': 'AddFlushingParaDto'
    }

    attribute_map = {
        'scenario_id': 'scenarioId',
        'data': 'data'
    }

    def __init__(self, scenario_id=None, data=None, local_vars_configuration=None):  # noqa: E501
        """AddFlushingParaInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scenario_id = None
        self._data = None
        self.discriminator = None

        self.scenario_id = scenario_id
        self.data = data

    @property
    def scenario_id(self):
        """Gets the scenario_id of this AddFlushingParaInput.  # noqa: E501

        方案Id scenario id  # noqa: E501

        :return: The scenario_id of this AddFlushingParaInput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this AddFlushingParaInput.

        方案Id scenario id  # noqa: E501

        :param scenario_id: The scenario_id of this AddFlushingParaInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scenario_id is None:  # noqa: E501
            raise ValueError("Invalid value for `scenario_id`, must not be `None`")  # noqa: E501

        self._scenario_id = scenario_id

    @property
    def data(self):
        """Gets the data of this AddFlushingParaInput.  # noqa: E501


        :return: The data of this AddFlushingParaInput.  # noqa: E501
        :rtype: AddFlushingParaDto
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AddFlushingParaInput.


        :param data: The data of this AddFlushingParaInput.  # noqa: E501
        :type: AddFlushingParaDto
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, AddFlushingParaInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddFlushingParaInput):
            return True

        return self.to_dict() != other.to_dict()
