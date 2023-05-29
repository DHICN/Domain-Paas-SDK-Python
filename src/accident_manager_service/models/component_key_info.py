# coding: utf-8

"""
    accident-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from accident_manager_service.configuration import Configuration


class ComponentKeyInfo(object):
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
        'business_type': 'BusinessTypeEnum',
        'key': 'str',
        'value_type': 'ValueTypeEnum'
    }

    attribute_map = {
        'id': 'id',
        'business_type': 'businessType',
        'key': 'key',
        'value_type': 'valueType'
    }

    def __init__(self, id=None, business_type=None, key=None, value_type=None, local_vars_configuration=None):  # noqa: E501
        """ComponentKeyInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._business_type = None
        self._key = None
        self._value_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if business_type is not None:
            self.business_type = business_type
        self.key = key
        if value_type is not None:
            self.value_type = value_type

    @property
    def id(self):
        """Gets the id of this ComponentKeyInfo.  # noqa: E501

        污染物属性ID pollutant attribute id  # noqa: E501

        :return: The id of this ComponentKeyInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentKeyInfo.

        污染物属性ID pollutant attribute id  # noqa: E501

        :param id: The id of this ComponentKeyInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def business_type(self):
        """Gets the business_type of this ComponentKeyInfo.  # noqa: E501


        :return: The business_type of this ComponentKeyInfo.  # noqa: E501
        :rtype: BusinessTypeEnum
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this ComponentKeyInfo.


        :param business_type: The business_type of this ComponentKeyInfo.  # noqa: E501
        :type: BusinessTypeEnum
        """

        self._business_type = business_type

    @property
    def key(self):
        """Gets the key of this ComponentKeyInfo.  # noqa: E501

        污染物属性名称 pollutant attribute name  # noqa: E501

        :return: The key of this ComponentKeyInfo.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ComponentKeyInfo.

        污染物属性名称 pollutant attribute name  # noqa: E501

        :param key: The key of this ComponentKeyInfo.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value_type(self):
        """Gets the value_type of this ComponentKeyInfo.  # noqa: E501


        :return: The value_type of this ComponentKeyInfo.  # noqa: E501
        :rtype: ValueTypeEnum
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ComponentKeyInfo.


        :param value_type: The value_type of this ComponentKeyInfo.  # noqa: E501
        :type: ValueTypeEnum
        """

        self._value_type = value_type

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
        if not isinstance(other, ComponentKeyInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentKeyInfo):
            return True

        return self.to_dict() != other.to_dict()
