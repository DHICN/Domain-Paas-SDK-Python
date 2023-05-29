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

from digital_twin_service.configuration import Configuration


class ModelPointListInput(object):
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
        'template_id': 'str',
        'model_point_type': 'str'
    }

    attribute_map = {
        'key_words': 'keyWords',
        'page_index': 'pageIndex',
        'page_size': 'pageSize',
        'template_id': 'templateId',
        'model_point_type': 'modelPointType'
    }

    def __init__(self, key_words=None, page_index=None, page_size=None, template_id=None, model_point_type=None, local_vars_configuration=None):  # noqa: E501
        """ModelPointListInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_words = None
        self._page_index = None
        self._page_size = None
        self._template_id = None
        self._model_point_type = None
        self.discriminator = None

        self.key_words = key_words
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        self.template_id = template_id
        self.model_point_type = model_point_type

    @property
    def key_words(self):
        """Gets the key_words of this ModelPointListInput.  # noqa: E501


        :return: The key_words of this ModelPointListInput.  # noqa: E501
        :rtype: str
        """
        return self._key_words

    @key_words.setter
    def key_words(self, key_words):
        """Sets the key_words of this ModelPointListInput.


        :param key_words: The key_words of this ModelPointListInput.  # noqa: E501
        :type: str
        """

        self._key_words = key_words

    @property
    def page_index(self):
        """Gets the page_index of this ModelPointListInput.  # noqa: E501


        :return: The page_index of this ModelPointListInput.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ModelPointListInput.


        :param page_index: The page_index of this ModelPointListInput.  # noqa: E501
        :type: int
        """

        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ModelPointListInput.  # noqa: E501


        :return: The page_size of this ModelPointListInput.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ModelPointListInput.


        :param page_size: The page_size of this ModelPointListInput.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def template_id(self):
        """Gets the template_id of this ModelPointListInput.  # noqa: E501

        模板方案ID template scenario id  # noqa: E501

        :return: The template_id of this ModelPointListInput.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ModelPointListInput.

        模板方案ID template scenario id  # noqa: E501

        :param template_id: The template_id of this ModelPointListInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def model_point_type(self):
        """Gets the model_point_type of this ModelPointListInput.  # noqa: E501

        模型点位类型 model point type  # noqa: E501

        :return: The model_point_type of this ModelPointListInput.  # noqa: E501
        :rtype: str
        """
        return self._model_point_type

    @model_point_type.setter
    def model_point_type(self, model_point_type):
        """Sets the model_point_type of this ModelPointListInput.

        模型点位类型 model point type  # noqa: E501

        :param model_point_type: The model_point_type of this ModelPointListInput.  # noqa: E501
        :type: str
        """

        self._model_point_type = model_point_type

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
        if not isinstance(other, ModelPointListInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelPointListInput):
            return True

        return self.to_dict() != other.to_dict()
