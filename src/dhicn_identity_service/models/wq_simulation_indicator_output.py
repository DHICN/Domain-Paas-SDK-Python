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


class WqSimulationIndicatorOutput(object):
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
        'config_name': 'str',
        'config_desc': 'str',
        'is_display': 'bool',
        'index': 'int'
    }

    attribute_map = {
        'id': 'id',
        'config_name': 'configName',
        'config_desc': 'configDesc',
        'is_display': 'isDisplay',
        'index': 'index'
    }

    def __init__(self, id=None, config_name=None, config_desc=None, is_display=None, index=None, local_vars_configuration=None):  # noqa: E501
        """WqSimulationIndicatorOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._config_name = None
        self._config_desc = None
        self._is_display = None
        self._index = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.config_name = config_name
        self.config_desc = config_desc
        if is_display is not None:
            self.is_display = is_display
        if index is not None:
            self.index = index

    @property
    def id(self):
        """Gets the id of this WqSimulationIndicatorOutput.  # noqa: E501

        指标ID indicator id  # noqa: E501

        :return: The id of this WqSimulationIndicatorOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WqSimulationIndicatorOutput.

        指标ID indicator id  # noqa: E501

        :param id: The id of this WqSimulationIndicatorOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def config_name(self):
        """Gets the config_name of this WqSimulationIndicatorOutput.  # noqa: E501

        指标代码 indicator code  # noqa: E501

        :return: The config_name of this WqSimulationIndicatorOutput.  # noqa: E501
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this WqSimulationIndicatorOutput.

        指标代码 indicator code  # noqa: E501

        :param config_name: The config_name of this WqSimulationIndicatorOutput.  # noqa: E501
        :type: str
        """

        self._config_name = config_name

    @property
    def config_desc(self):
        """Gets the config_desc of this WqSimulationIndicatorOutput.  # noqa: E501

        指标描述 indicator description  # noqa: E501

        :return: The config_desc of this WqSimulationIndicatorOutput.  # noqa: E501
        :rtype: str
        """
        return self._config_desc

    @config_desc.setter
    def config_desc(self, config_desc):
        """Sets the config_desc of this WqSimulationIndicatorOutput.

        指标描述 indicator description  # noqa: E501

        :param config_desc: The config_desc of this WqSimulationIndicatorOutput.  # noqa: E501
        :type: str
        """

        self._config_desc = config_desc

    @property
    def is_display(self):
        """Gets the is_display of this WqSimulationIndicatorOutput.  # noqa: E501

        是否展示 if display at the front end  # noqa: E501

        :return: The is_display of this WqSimulationIndicatorOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_display

    @is_display.setter
    def is_display(self, is_display):
        """Sets the is_display of this WqSimulationIndicatorOutput.

        是否展示 if display at the front end  # noqa: E501

        :param is_display: The is_display of this WqSimulationIndicatorOutput.  # noqa: E501
        :type: bool
        """

        self._is_display = is_display

    @property
    def index(self):
        """Gets the index of this WqSimulationIndicatorOutput.  # noqa: E501

        展示序号 display index  # noqa: E501

        :return: The index of this WqSimulationIndicatorOutput.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this WqSimulationIndicatorOutput.

        展示序号 display index  # noqa: E501

        :param index: The index of this WqSimulationIndicatorOutput.  # noqa: E501
        :type: int
        """

        self._index = index

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
        if not isinstance(other, WqSimulationIndicatorOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WqSimulationIndicatorOutput):
            return True

        return self.to_dict() != other.to_dict()
