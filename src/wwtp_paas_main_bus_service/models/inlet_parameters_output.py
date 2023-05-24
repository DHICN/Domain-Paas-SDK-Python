# coding: utf-8

"""
    wwtp-paas-main-bus-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wwtp_paas_main_bus_service.configuration import Configuration


class InletParametersOutput(object):
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
        'id': 'str',
        'inlet_component': 'str',
        'description': 'str',
        'value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'inlet_component': 'inletComponent',
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, id=None, inlet_component=None, description=None, value=None, local_vars_configuration=None):  # noqa: E501
        """InletParametersOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._inlet_component = None
        self._description = None
        self._value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.inlet_component = inlet_component
        self.description = description
        if value is not None:
            self.value = value

    @property
    def id(self):
        """Gets the id of this InletParametersOutput.  # noqa: E501

        参数ID parameter id  # noqa: E501

        :return: The id of this InletParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InletParametersOutput.

        参数ID parameter id  # noqa: E501

        :param id: The id of this InletParametersOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inlet_component(self):
        """Gets the inlet_component of this InletParametersOutput.  # noqa: E501

        参数代码 parameter code  # noqa: E501

        :return: The inlet_component of this InletParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._inlet_component

    @inlet_component.setter
    def inlet_component(self, inlet_component):
        """Sets the inlet_component of this InletParametersOutput.

        参数代码 parameter code  # noqa: E501

        :param inlet_component: The inlet_component of this InletParametersOutput.  # noqa: E501
        :type: str
        """

        self._inlet_component = inlet_component

    @property
    def description(self):
        """Gets the description of this InletParametersOutput.  # noqa: E501

        参数描述 parameter description  # noqa: E501

        :return: The description of this InletParametersOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InletParametersOutput.

        参数描述 parameter description  # noqa: E501

        :param description: The description of this InletParametersOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this InletParametersOutput.  # noqa: E501

        参数值 parameter value  # noqa: E501

        :return: The value of this InletParametersOutput.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InletParametersOutput.

        参数值 parameter value  # noqa: E501

        :param value: The value of this InletParametersOutput.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if not isinstance(other, InletParametersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InletParametersOutput):
            return True

        return self.to_dict() != other.to_dict()
