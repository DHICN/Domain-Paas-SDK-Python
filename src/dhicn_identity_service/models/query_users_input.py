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

from dhicn_identity_service.configuration import Configuration


class QueryUsersInput(object):
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
        'key_words': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'status': 'int',
        'is_trial_user': 'bool'
    }

    attribute_map = {
        'key_words': 'keyWords',
        'page_index': 'pageIndex',
        'page_size': 'pageSize',
        'status': 'status',
        'is_trial_user': 'isTrialUser'
    }

    def __init__(self, key_words=None, page_index=None, page_size=None, status=None, is_trial_user=None, local_vars_configuration=None):  # noqa: E501
        """QueryUsersInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_words = None
        self._page_index = None
        self._page_size = None
        self._status = None
        self._is_trial_user = None
        self.discriminator = None

        self.key_words = key_words
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        self.status = status
        self.is_trial_user = is_trial_user

    @property
    def key_words(self):
        """Gets the key_words of this QueryUsersInput.  # noqa: E501


        :return: The key_words of this QueryUsersInput.  # noqa: E501
        :rtype: str
        """
        return self._key_words

    @key_words.setter
    def key_words(self, key_words):
        """Sets the key_words of this QueryUsersInput.


        :param key_words: The key_words of this QueryUsersInput.  # noqa: E501
        :type: str
        """

        self._key_words = key_words

    @property
    def page_index(self):
        """Gets the page_index of this QueryUsersInput.  # noqa: E501


        :return: The page_index of this QueryUsersInput.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this QueryUsersInput.


        :param page_index: The page_index of this QueryUsersInput.  # noqa: E501
        :type: int
        """

        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this QueryUsersInput.  # noqa: E501


        :return: The page_size of this QueryUsersInput.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this QueryUsersInput.


        :param page_size: The page_size of this QueryUsersInput.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def status(self):
        """Gets the status of this QueryUsersInput.  # noqa: E501

        用户状态 user status  # noqa: E501

        :return: The status of this QueryUsersInput.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryUsersInput.

        用户状态 user status  # noqa: E501

        :param status: The status of this QueryUsersInput.  # noqa: E501
        :type: int
        """
        allowed_values = [None,0, 1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def is_trial_user(self):
        """Gets the is_trial_user of this QueryUsersInput.  # noqa: E501

        是否试用用户 if it is a trial user  # noqa: E501

        :return: The is_trial_user of this QueryUsersInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_trial_user

    @is_trial_user.setter
    def is_trial_user(self, is_trial_user):
        """Sets the is_trial_user of this QueryUsersInput.

        是否试用用户 if it is a trial user  # noqa: E501

        :param is_trial_user: The is_trial_user of this QueryUsersInput.  # noqa: E501
        :type: bool
        """

        self._is_trial_user = is_trial_user

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
        if not isinstance(other, QueryUsersInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryUsersInput):
            return True

        return self.to_dict() != other.to_dict()
