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

from document_manager_service.configuration import Configuration


class Document(object):
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
        'title': 'str',
        'author': 'str',
        'summary': 'str',
        'description': 'str',
        'language': 'str',
        'keywords': 'str',
        'data_id': 'str',
        'format': 'str',
        'modified_time': 'datetime',
        'data_storage': 'str',
        'version': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'author': 'author',
        'summary': 'summary',
        'description': 'description',
        'language': 'language',
        'keywords': 'keywords',
        'data_id': 'dataId',
        'format': 'format',
        'modified_time': 'modifiedTime',
        'data_storage': 'dataStorage',
        'version': 'version',
        'tenant_id': 'tenantId'
    }

    def __init__(self, id=None, title=None, author=None, summary=None, description=None, language=None, keywords=None, data_id=None, format=None, modified_time=None, data_storage=None, version=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """Document - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._author = None
        self._summary = None
        self._description = None
        self._language = None
        self._keywords = None
        self._data_id = None
        self._format = None
        self._modified_time = None
        self._data_storage = None
        self._version = None
        self._tenant_id = None
        self.discriminator = None

        self.id = id
        self.title = title
        self.author = author
        self.summary = summary
        self.description = description
        self.language = language
        self.keywords = keywords
        self.data_id = data_id
        self.format = format
        self.modified_time = modified_time
        self.data_storage = data_storage
        if version is not None:
            self.version = version
        self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this Document.  # noqa: E501


        :return: The id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Document.


        :param id: The id of this Document.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this Document.  # noqa: E501


        :return: The title of this Document.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Document.


        :param title: The title of this Document.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) > 255):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 0):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `0`")  # noqa: E501

        self._title = title

    @property
    def author(self):
        """Gets the author of this Document.  # noqa: E501


        :return: The author of this Document.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Document.


        :param author: The author of this Document.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and author is None:  # noqa: E501
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                author is not None and len(author) > 255):
            raise ValueError("Invalid value for `author`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                author is not None and len(author) < 0):
            raise ValueError("Invalid value for `author`, length must be greater than or equal to `0`")  # noqa: E501

        self._author = author

    @property
    def summary(self):
        """Gets the summary of this Document.  # noqa: E501


        :return: The summary of this Document.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Document.


        :param summary: The summary of this Document.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                summary is not None and len(summary) > 8000):
            raise ValueError("Invalid value for `summary`, length must be less than or equal to `8000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                summary is not None and len(summary) < 0):
            raise ValueError("Invalid value for `summary`, length must be greater than or equal to `0`")  # noqa: E501

        self._summary = summary

    @property
    def description(self):
        """Gets the description of this Document.  # noqa: E501


        :return: The description of this Document.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Document.


        :param description: The description of this Document.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 8000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def language(self):
        """Gets the language of this Document.  # noqa: E501


        :return: The language of this Document.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Document.


        :param language: The language of this Document.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) > 50):
            raise ValueError("Invalid value for `language`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) < 0):
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `0`")  # noqa: E501

        self._language = language

    @property
    def keywords(self):
        """Gets the keywords of this Document.  # noqa: E501


        :return: The keywords of this Document.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Document.


        :param keywords: The keywords of this Document.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                keywords is not None and len(keywords) > 1024):
            raise ValueError("Invalid value for `keywords`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                keywords is not None and len(keywords) < 0):
            raise ValueError("Invalid value for `keywords`, length must be greater than or equal to `0`")  # noqa: E501

        self._keywords = keywords

    @property
    def data_id(self):
        """Gets the data_id of this Document.  # noqa: E501


        :return: The data_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """Sets the data_id of this Document.


        :param data_id: The data_id of this Document.  # noqa: E501
        :type: str
        """

        self._data_id = data_id

    @property
    def format(self):
        """Gets the format of this Document.  # noqa: E501


        :return: The format of this Document.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Document.


        :param format: The format of this Document.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and format is None:  # noqa: E501
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                format is not None and len(format) > 50):
            raise ValueError("Invalid value for `format`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                format is not None and len(format) < 0):
            raise ValueError("Invalid value for `format`, length must be greater than or equal to `0`")  # noqa: E501

        self._format = format

    @property
    def modified_time(self):
        """Gets the modified_time of this Document.  # noqa: E501


        :return: The modified_time of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this Document.


        :param modified_time: The modified_time of this Document.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_time is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_time`, must not be `None`")  # noqa: E501

        self._modified_time = modified_time

    @property
    def data_storage(self):
        """Gets the data_storage of this Document.  # noqa: E501


        :return: The data_storage of this Document.  # noqa: E501
        :rtype: str
        """
        return self._data_storage

    @data_storage.setter
    def data_storage(self, data_storage):
        """Sets the data_storage of this Document.


        :param data_storage: The data_storage of this Document.  # noqa: E501
        :type: str
        """

        self._data_storage = data_storage

    @property
    def version(self):
        """Gets the version of this Document.  # noqa: E501


        :return: The version of this Document.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Document.


        :param version: The version of this Document.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Document.  # noqa: E501


        :return: The tenant_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Document.


        :param tenant_id: The tenant_id of this Document.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

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
        if not isinstance(other, Document):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Document):
            return True

        return self.to_dict() != other.to_dict()