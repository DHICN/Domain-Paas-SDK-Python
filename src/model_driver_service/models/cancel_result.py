# coding: utf-8

"""
    model-driver-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from model_driver_service.configuration import Configuration


class CancelResult(object):
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
        'has_error': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'has_error': 'hasError',
        'message': 'message'
    }

    def __init__(self, has_error=None, message=None, local_vars_configuration=None):  # noqa: E501
        """CancelResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._has_error = None
        self._message = None
        self.discriminator = None

        if has_error is not None:
            self.has_error = has_error
        self.message = message

    @property
    def has_error(self):
        """Gets the has_error of this CancelResult.  # noqa: E501

        是否有错  # noqa: E501

        :return: The has_error of this CancelResult.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this CancelResult.

        是否有错  # noqa: E501

        :param has_error: The has_error of this CancelResult.  # noqa: E501
        :type: bool
        """

        self._has_error = has_error

    @property
    def message(self):
        """Gets the message of this CancelResult.  # noqa: E501

        消息 message  # noqa: E501

        :return: The message of this CancelResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CancelResult.

        消息 message  # noqa: E501

        :param message: The message of this CancelResult.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, CancelResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CancelResult):
            return True

        return self.to_dict() != other.to_dict()