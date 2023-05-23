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


class InlineObject(object):
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
        'client_id': 'str',
        'grant_type': 'str',
        'client_secret': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'grant_type': 'grant_type',
        'client_secret': 'client_secret',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, client_id=None, grant_type=None, client_secret=None, username=None, password=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._grant_type = None
        self._client_secret = None
        self._username = None
        self._password = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if grant_type is not None:
            self.grant_type = grant_type
        if client_secret is not None:
            self.client_secret = client_secret
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def client_id(self):
        """Gets the client_id of this InlineObject.  # noqa: E501


        :return: The client_id of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this InlineObject.


        :param client_id: The client_id of this InlineObject.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def grant_type(self):
        """Gets the grant_type of this InlineObject.  # noqa: E501


        :return: The grant_type of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this InlineObject.


        :param grant_type: The grant_type of this InlineObject.  # noqa: E501
        :type: str
        """

        self._grant_type = grant_type

    @property
    def client_secret(self):
        """Gets the client_secret of this InlineObject.  # noqa: E501


        :return: The client_secret of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this InlineObject.


        :param client_secret: The client_secret of this InlineObject.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def username(self):
        """Gets the username of this InlineObject.  # noqa: E501


        :return: The username of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InlineObject.


        :param username: The username of this InlineObject.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this InlineObject.  # noqa: E501


        :return: The password of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineObject.


        :param password: The password of this InlineObject.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if not isinstance(other, InlineObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject):
            return True

        return self.to_dict() != other.to_dict()
