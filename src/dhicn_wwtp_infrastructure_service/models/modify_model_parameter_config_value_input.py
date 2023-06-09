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


class ModifyModelParameterConfigValueInput(object):
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
        'value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value'
    }

    def __init__(self, id=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ModifyModelParameterConfigValueInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if value is not None:
            self.value = value

    @property
    def id(self):
        """Gets the id of this ModifyModelParameterConfigValueInput.  # noqa: E501

        模型参数配置ID config id  # noqa: E501

        :return: The id of this ModifyModelParameterConfigValueInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModifyModelParameterConfigValueInput.

        模型参数配置ID config id  # noqa: E501

        :param id: The id of this ModifyModelParameterConfigValueInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this ModifyModelParameterConfigValueInput.  # noqa: E501

        参数值 model parameter value  # noqa: E501

        :return: The value of this ModifyModelParameterConfigValueInput.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModifyModelParameterConfigValueInput.

        参数值 model parameter value  # noqa: E501

        :param value: The value of this ModifyModelParameterConfigValueInput.  # noqa: E501
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
        if not isinstance(other, ModifyModelParameterConfigValueInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyModelParameterConfigValueInput):
            return True

        return self.to_dict() != other.to_dict()
