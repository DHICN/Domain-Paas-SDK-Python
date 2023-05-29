# coding: utf-8

"""
    message-center-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from message_center_service.configuration import Configuration


class UserMsgOutputPage(object):
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
        'page_index': 'int',
        'page_size': 'int',
        'list': 'list[UserMsgOutput]',
        'total_count': 'int',
        'total_pages': 'int',
        'have_next_page': 'bool'
    }

    attribute_map = {
        'page_index': 'pageIndex',
        'page_size': 'pageSize',
        'list': 'list',
        'total_count': 'totalCount',
        'total_pages': 'totalPages',
        'have_next_page': 'haveNextPage'
    }

    def __init__(self, page_index=None, page_size=None, list=None, total_count=None, total_pages=None, have_next_page=None, local_vars_configuration=None):  # noqa: E501
        """UserMsgOutputPage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page_index = None
        self._page_size = None
        self._list = None
        self._total_count = None
        self._total_pages = None
        self._have_next_page = None
        self.discriminator = None

        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        self.list = list
        if total_count is not None:
            self.total_count = total_count
        if total_pages is not None:
            self.total_pages = total_pages
        if have_next_page is not None:
            self.have_next_page = have_next_page

    @property
    def page_index(self):
        """Gets the page_index of this UserMsgOutputPage.  # noqa: E501


        :return: The page_index of this UserMsgOutputPage.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this UserMsgOutputPage.


        :param page_index: The page_index of this UserMsgOutputPage.  # noqa: E501
        :type: int
        """

        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this UserMsgOutputPage.  # noqa: E501


        :return: The page_size of this UserMsgOutputPage.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this UserMsgOutputPage.


        :param page_size: The page_size of this UserMsgOutputPage.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def list(self):
        """Gets the list of this UserMsgOutputPage.  # noqa: E501


        :return: The list of this UserMsgOutputPage.  # noqa: E501
        :rtype: list[UserMsgOutput]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this UserMsgOutputPage.


        :param list: The list of this UserMsgOutputPage.  # noqa: E501
        :type: list[UserMsgOutput]
        """

        self._list = list

    @property
    def total_count(self):
        """Gets the total_count of this UserMsgOutputPage.  # noqa: E501


        :return: The total_count of this UserMsgOutputPage.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this UserMsgOutputPage.


        :param total_count: The total_count of this UserMsgOutputPage.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def total_pages(self):
        """Gets the total_pages of this UserMsgOutputPage.  # noqa: E501


        :return: The total_pages of this UserMsgOutputPage.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this UserMsgOutputPage.


        :param total_pages: The total_pages of this UserMsgOutputPage.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def have_next_page(self):
        """Gets the have_next_page of this UserMsgOutputPage.  # noqa: E501


        :return: The have_next_page of this UserMsgOutputPage.  # noqa: E501
        :rtype: bool
        """
        return self._have_next_page

    @have_next_page.setter
    def have_next_page(self, have_next_page):
        """Sets the have_next_page of this UserMsgOutputPage.


        :param have_next_page: The have_next_page of this UserMsgOutputPage.  # noqa: E501
        :type: bool
        """

        self._have_next_page = have_next_page

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
        if not isinstance(other, UserMsgOutputPage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMsgOutputPage):
            return True

        return self.to_dict() != other.to_dict()
