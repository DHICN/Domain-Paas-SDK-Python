# coding: utf-8

"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_zyws_service.configuration import Configuration


class RecommendDetails(object):
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
        'recommend_tag': 'str',
        'operation': 'str',
        'measure_value': 'float',
        'value': 'float',
        'content': 'str',
        'big_screen_recommend': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'recommend_tag': 'recommendTag',
        'operation': 'operation',
        'measure_value': 'measureValue',
        'value': 'value',
        'content': 'content',
        'big_screen_recommend': 'bigScreenRecommend',
        'unit': 'unit'
    }

    def __init__(self, recommend_tag=None, operation=None, measure_value=None, value=None, content=None, big_screen_recommend=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """RecommendDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._recommend_tag = None
        self._operation = None
        self._measure_value = None
        self._value = None
        self._content = None
        self._big_screen_recommend = None
        self._unit = None
        self.discriminator = None

        self.recommend_tag = recommend_tag
        self.operation = operation
        if measure_value is not None:
            self.measure_value = measure_value
        if value is not None:
            self.value = value
        self.content = content
        self.big_screen_recommend = big_screen_recommend
        self.unit = unit

    @property
    def recommend_tag(self):
        """Gets the recommend_tag of this RecommendDetails.  # noqa: E501

        建议标记  # noqa: E501

        :return: The recommend_tag of this RecommendDetails.  # noqa: E501
        :rtype: str
        """
        return self._recommend_tag

    @recommend_tag.setter
    def recommend_tag(self, recommend_tag):
        """Sets the recommend_tag of this RecommendDetails.

        建议标记  # noqa: E501

        :param recommend_tag: The recommend_tag of this RecommendDetails.  # noqa: E501
        :type: str
        """

        self._recommend_tag = recommend_tag

    @property
    def operation(self):
        """Gets the operation of this RecommendDetails.  # noqa: E501

        建议操作，up/down,open/close  # noqa: E501

        :return: The operation of this RecommendDetails.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this RecommendDetails.

        建议操作，up/down,open/close  # noqa: E501

        :param operation: The operation of this RecommendDetails.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def measure_value(self):
        """Gets the measure_value of this RecommendDetails.  # noqa: E501

        实测值  # noqa: E501

        :return: The measure_value of this RecommendDetails.  # noqa: E501
        :rtype: float
        """
        return self._measure_value

    @measure_value.setter
    def measure_value(self, measure_value):
        """Sets the measure_value of this RecommendDetails.

        实测值  # noqa: E501

        :param measure_value: The measure_value of this RecommendDetails.  # noqa: E501
        :type: float
        """

        self._measure_value = measure_value

    @property
    def value(self):
        """Gets the value of this RecommendDetails.  # noqa: E501

        建议值  # noqa: E501

        :return: The value of this RecommendDetails.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RecommendDetails.

        建议值  # noqa: E501

        :param value: The value of this RecommendDetails.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def content(self):
        """Gets the content of this RecommendDetails.  # noqa: E501

        建议内容  # noqa: E501

        :return: The content of this RecommendDetails.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this RecommendDetails.

        建议内容  # noqa: E501

        :param content: The content of this RecommendDetails.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def big_screen_recommend(self):
        """Gets the big_screen_recommend of this RecommendDetails.  # noqa: E501

        大屏模块要显示的建议内容  # noqa: E501

        :return: The big_screen_recommend of this RecommendDetails.  # noqa: E501
        :rtype: str
        """
        return self._big_screen_recommend

    @big_screen_recommend.setter
    def big_screen_recommend(self, big_screen_recommend):
        """Sets the big_screen_recommend of this RecommendDetails.

        大屏模块要显示的建议内容  # noqa: E501

        :param big_screen_recommend: The big_screen_recommend of this RecommendDetails.  # noqa: E501
        :type: str
        """

        self._big_screen_recommend = big_screen_recommend

    @property
    def unit(self):
        """Gets the unit of this RecommendDetails.  # noqa: E501

        单位  # noqa: E501

        :return: The unit of this RecommendDetails.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this RecommendDetails.

        单位  # noqa: E501

        :param unit: The unit of this RecommendDetails.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, RecommendDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecommendDetails):
            return True

        return self.to_dict() != other.to_dict()
