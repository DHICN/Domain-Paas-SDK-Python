# coding: utf-8

"""
    digital-twin-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_digital_twin_service.configuration import Configuration


class AddKeyPointInput(object):
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
        'show_name': 'str',
        'key_point_details': 'list[KeyPointDetailsInput]',
        'attributes': 'list[StringStringKeyValue]'
    }

    attribute_map = {
        'show_name': 'showName',
        'key_point_details': 'keyPointDetails',
        'attributes': 'attributes'
    }

    def __init__(self, show_name=None, key_point_details=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """AddKeyPointInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._show_name = None
        self._key_point_details = None
        self._attributes = None
        self.discriminator = None

        self.show_name = show_name
        self.key_point_details = key_point_details
        self.attributes = attributes

    @property
    def show_name(self):
        """Gets the show_name of this AddKeyPointInput.  # noqa: E501

        重要点位显示名称 key point show name  # noqa: E501

        :return: The show_name of this AddKeyPointInput.  # noqa: E501
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        """Sets the show_name of this AddKeyPointInput.

        重要点位显示名称 key point show name  # noqa: E501

        :param show_name: The show_name of this AddKeyPointInput.  # noqa: E501
        :type: str
        """

        self._show_name = show_name

    @property
    def key_point_details(self):
        """Gets the key_point_details of this AddKeyPointInput.  # noqa: E501

        重要点位详细信息 key point detail info  # noqa: E501

        :return: The key_point_details of this AddKeyPointInput.  # noqa: E501
        :rtype: list[KeyPointDetailsInput]
        """
        return self._key_point_details

    @key_point_details.setter
    def key_point_details(self, key_point_details):
        """Sets the key_point_details of this AddKeyPointInput.

        重要点位详细信息 key point detail info  # noqa: E501

        :param key_point_details: The key_point_details of this AddKeyPointInput.  # noqa: E501
        :type: list[KeyPointDetailsInput]
        """

        self._key_point_details = key_point_details

    @property
    def attributes(self):
        """Gets the attributes of this AddKeyPointInput.  # noqa: E501

        重要点位属性 key point attributes  # noqa: E501

        :return: The attributes of this AddKeyPointInput.  # noqa: E501
        :rtype: list[StringStringKeyValue]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AddKeyPointInput.

        重要点位属性 key point attributes  # noqa: E501

        :param attributes: The attributes of this AddKeyPointInput.  # noqa: E501
        :type: list[StringStringKeyValue]
        """

        self._attributes = attributes

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
        if not isinstance(other, AddKeyPointInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddKeyPointInput):
            return True

        return self.to_dict() != other.to_dict()
