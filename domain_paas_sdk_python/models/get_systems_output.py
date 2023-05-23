# coding: utf-8

"""
    identity-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from domain_paas_sdk_python.configuration import Configuration


class GetSystemsOutput(object):
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
        'name': 'str',
        'business_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'business_type': 'businessType'
    }

    def __init__(self, id=None, name=None, business_type=None, local_vars_configuration=None):  # noqa: E501
        """GetSystemsOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._business_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if business_type is not None:
            self.business_type = business_type

    @property
    def id(self):
        """Gets the id of this GetSystemsOutput.  # noqa: E501

        系统ID system id  # noqa: E501

        :return: The id of this GetSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSystemsOutput.

        系统ID system id  # noqa: E501

        :param id: The id of this GetSystemsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetSystemsOutput.  # noqa: E501

        系统名称 system name  # noqa: E501

        :return: The name of this GetSystemsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetSystemsOutput.

        系统名称 system name  # noqa: E501

        :param name: The name of this GetSystemsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def business_type(self):
        """Gets the business_type of this GetSystemsOutput.  # noqa: E501

        0-Undefined(Undefined) 1-WaterEnvironment(Water environment) 2-UrbanFlooding(Urban flooding) 3-UrbanWD(Water distribution) 4-RiverFlood(River flood) 5-WWTP(Waste water treatment plant)   # noqa: E501

        :return: The business_type of this GetSystemsOutput.  # noqa: E501
        :rtype: int
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this GetSystemsOutput.

        0-Undefined(Undefined) 1-WaterEnvironment(Water environment) 2-UrbanFlooding(Urban flooding) 3-UrbanWD(Water distribution) 4-RiverFlood(River flood) 5-WWTP(Waste water treatment plant)   # noqa: E501

        :param business_type: The business_type of this GetSystemsOutput.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and business_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `business_type` ({0}), must be one of {1}"  # noqa: E501
                .format(business_type, allowed_values)
            )

        self._business_type = business_type

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
        if not isinstance(other, GetSystemsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSystemsOutput):
            return True

        return self.to_dict() != other.to_dict()
