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


class ValueInfo(object):
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
        'key': 'str',
        'key_id': 'str',
        'value_type': 'ValueTypeEnum',
        'value': 'Null'
    }

    attribute_map = {
        'key': 'key',
        'key_id': 'keyId',
        'value_type': 'valueType',
        'value': 'value'
    }

    def __init__(self, key=None, key_id=None, value_type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ValueInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._key_id = None
        self._value_type = None
        self._value = None
        self.discriminator = None

        self.key = key
        if key_id is not None:
            self.key_id = key_id
        if value_type is not None:
            self.value_type = value_type
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this ValueInfo.  # noqa: E501

        属性名称 attribute name  # noqa: E501

        :return: The key of this ValueInfo.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ValueInfo.

        属性名称 attribute name  # noqa: E501

        :param key: The key of this ValueInfo.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def key_id(self):
        """Gets the key_id of this ValueInfo.  # noqa: E501

        属性ID attribute id  # noqa: E501

        :return: The key_id of this ValueInfo.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this ValueInfo.

        属性ID attribute id  # noqa: E501

        :param key_id: The key_id of this ValueInfo.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def value_type(self):
        """Gets the value_type of this ValueInfo.  # noqa: E501


        :return: The value_type of this ValueInfo.  # noqa: E501
        :rtype: ValueTypeEnum
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ValueInfo.


        :param value_type: The value_type of this ValueInfo.  # noqa: E501
        :type: ValueTypeEnum
        """

        self._value_type = value_type

    @property
    def value(self):
        """Gets the value of this ValueInfo.  # noqa: E501

        属性值 attribute value  # noqa: E501

        :return: The value of this ValueInfo.  # noqa: E501
        :rtype: Null
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ValueInfo.

        属性值 attribute value  # noqa: E501

        :param value: The value of this ValueInfo.  # noqa: E501
        :type: Null
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
        if not isinstance(other, ValueInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValueInfo):
            return True

        return self.to_dict() != other.to_dict()