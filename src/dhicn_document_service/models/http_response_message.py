# coding: utf-8

"""
    document-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_document_service.configuration import Configuration


class HttpResponseMessage(object):
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
        'version': 'Version',
        'content': 'HttpContent',
        'status_code': 'HttpStatusCode',
        'reason_phrase': 'str',
        'headers': 'list[StringStringIEnumerableKeyValuePair]',
        'trailing_headers': 'list[StringStringIEnumerableKeyValuePair]',
        'request_message': 'HttpRequestMessage',
        'is_success_status_code': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'content': 'content',
        'status_code': 'statusCode',
        'reason_phrase': 'reasonPhrase',
        'headers': 'headers',
        'trailing_headers': 'trailingHeaders',
        'request_message': 'requestMessage',
        'is_success_status_code': 'isSuccessStatusCode'
    }

    def __init__(self, version=None, content=None, status_code=None, reason_phrase=None, headers=None, trailing_headers=None, request_message=None, is_success_status_code=None, local_vars_configuration=None):  # noqa: E501
        """HttpResponseMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._content = None
        self._status_code = None
        self._reason_phrase = None
        self._headers = None
        self._trailing_headers = None
        self._request_message = None
        self._is_success_status_code = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if content is not None:
            self.content = content
        if status_code is not None:
            self.status_code = status_code
        self.reason_phrase = reason_phrase
        self.headers = headers
        self.trailing_headers = trailing_headers
        if request_message is not None:
            self.request_message = request_message
        if is_success_status_code is not None:
            self.is_success_status_code = is_success_status_code

    @property
    def version(self):
        """Gets the version of this HttpResponseMessage.  # noqa: E501


        :return: The version of this HttpResponseMessage.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HttpResponseMessage.


        :param version: The version of this HttpResponseMessage.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def content(self):
        """Gets the content of this HttpResponseMessage.  # noqa: E501


        :return: The content of this HttpResponseMessage.  # noqa: E501
        :rtype: HttpContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this HttpResponseMessage.


        :param content: The content of this HttpResponseMessage.  # noqa: E501
        :type: HttpContent
        """

        self._content = content

    @property
    def status_code(self):
        """Gets the status_code of this HttpResponseMessage.  # noqa: E501


        :return: The status_code of this HttpResponseMessage.  # noqa: E501
        :rtype: HttpStatusCode
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this HttpResponseMessage.


        :param status_code: The status_code of this HttpResponseMessage.  # noqa: E501
        :type: HttpStatusCode
        """

        self._status_code = status_code

    @property
    def reason_phrase(self):
        """Gets the reason_phrase of this HttpResponseMessage.  # noqa: E501


        :return: The reason_phrase of this HttpResponseMessage.  # noqa: E501
        :rtype: str
        """
        return self._reason_phrase

    @reason_phrase.setter
    def reason_phrase(self, reason_phrase):
        """Sets the reason_phrase of this HttpResponseMessage.


        :param reason_phrase: The reason_phrase of this HttpResponseMessage.  # noqa: E501
        :type: str
        """

        self._reason_phrase = reason_phrase

    @property
    def headers(self):
        """Gets the headers of this HttpResponseMessage.  # noqa: E501


        :return: The headers of this HttpResponseMessage.  # noqa: E501
        :rtype: list[StringStringIEnumerableKeyValuePair]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this HttpResponseMessage.


        :param headers: The headers of this HttpResponseMessage.  # noqa: E501
        :type: list[StringStringIEnumerableKeyValuePair]
        """

        self._headers = headers

    @property
    def trailing_headers(self):
        """Gets the trailing_headers of this HttpResponseMessage.  # noqa: E501


        :return: The trailing_headers of this HttpResponseMessage.  # noqa: E501
        :rtype: list[StringStringIEnumerableKeyValuePair]
        """
        return self._trailing_headers

    @trailing_headers.setter
    def trailing_headers(self, trailing_headers):
        """Sets the trailing_headers of this HttpResponseMessage.


        :param trailing_headers: The trailing_headers of this HttpResponseMessage.  # noqa: E501
        :type: list[StringStringIEnumerableKeyValuePair]
        """

        self._trailing_headers = trailing_headers

    @property
    def request_message(self):
        """Gets the request_message of this HttpResponseMessage.  # noqa: E501


        :return: The request_message of this HttpResponseMessage.  # noqa: E501
        :rtype: HttpRequestMessage
        """
        return self._request_message

    @request_message.setter
    def request_message(self, request_message):
        """Sets the request_message of this HttpResponseMessage.


        :param request_message: The request_message of this HttpResponseMessage.  # noqa: E501
        :type: HttpRequestMessage
        """

        self._request_message = request_message

    @property
    def is_success_status_code(self):
        """Gets the is_success_status_code of this HttpResponseMessage.  # noqa: E501


        :return: The is_success_status_code of this HttpResponseMessage.  # noqa: E501
        :rtype: bool
        """
        return self._is_success_status_code

    @is_success_status_code.setter
    def is_success_status_code(self, is_success_status_code):
        """Sets the is_success_status_code of this HttpResponseMessage.


        :param is_success_status_code: The is_success_status_code of this HttpResponseMessage.  # noqa: E501
        :type: bool
        """

        self._is_success_status_code = is_success_status_code

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
        if not isinstance(other, HttpResponseMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HttpResponseMessage):
            return True

        return self.to_dict() != other.to_dict()
