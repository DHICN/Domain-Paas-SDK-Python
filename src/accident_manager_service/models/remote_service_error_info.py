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


class RemoteServiceErrorInfo(object):
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
        'code': 'str',
        'message': 'str',
        'details': 'str',
        'data': 'dict(str, str)',
        'validation_errors': 'list[RemoteServiceValidationErrorInfo]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'details': 'details',
        'data': 'data',
        'validation_errors': 'validationErrors'
    }

    def __init__(self, code=None, message=None, details=None, data=None, validation_errors=None, local_vars_configuration=None):  # noqa: E501
        """RemoteServiceErrorInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._message = None
        self._details = None
        self._data = None
        self._validation_errors = None
        self.discriminator = None

        self.code = code
        self.message = message
        self.details = details
        self.data = data
        self.validation_errors = validation_errors

    @property
    def code(self):
        """Gets the code of this RemoteServiceErrorInfo.  # noqa: E501


        :return: The code of this RemoteServiceErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RemoteServiceErrorInfo.


        :param code: The code of this RemoteServiceErrorInfo.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this RemoteServiceErrorInfo.  # noqa: E501


        :return: The message of this RemoteServiceErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RemoteServiceErrorInfo.


        :param message: The message of this RemoteServiceErrorInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """Gets the details of this RemoteServiceErrorInfo.  # noqa: E501


        :return: The details of this RemoteServiceErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this RemoteServiceErrorInfo.


        :param details: The details of this RemoteServiceErrorInfo.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def data(self):
        """Gets the data of this RemoteServiceErrorInfo.  # noqa: E501


        :return: The data of this RemoteServiceErrorInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RemoteServiceErrorInfo.


        :param data: The data of this RemoteServiceErrorInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._data = data

    @property
    def validation_errors(self):
        """Gets the validation_errors of this RemoteServiceErrorInfo.  # noqa: E501


        :return: The validation_errors of this RemoteServiceErrorInfo.  # noqa: E501
        :rtype: list[RemoteServiceValidationErrorInfo]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this RemoteServiceErrorInfo.


        :param validation_errors: The validation_errors of this RemoteServiceErrorInfo.  # noqa: E501
        :type: list[RemoteServiceValidationErrorInfo]
        """

        self._validation_errors = validation_errors

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
        if not isinstance(other, RemoteServiceErrorInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteServiceErrorInfo):
            return True

        return self.to_dict() != other.to_dict()
