# coding: utf-8

"""
    wd-domain-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wd_service_domain.configuration import Configuration


class CurveTsInfo(object):
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
        't': 'list[int]',
        'v': 'list[float]',
        'model_feature_id': 'str',
        'id': 'str',
        'indicator_id': 'str'
    }

    attribute_map = {
        't': 't',
        'v': 'v',
        'model_feature_id': 'modelFeatureId',
        'id': 'id',
        'indicator_id': 'indicatorId'
    }

    def __init__(self, t=None, v=None, model_feature_id=None, id=None, indicator_id=None, local_vars_configuration=None):  # noqa: E501
        """CurveTsInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._t = None
        self._v = None
        self._model_feature_id = None
        self._id = None
        self._indicator_id = None
        self.discriminator = None

        self.t = t
        self.v = v
        self.model_feature_id = model_feature_id
        self.id = id
        self.indicator_id = indicator_id

    @property
    def t(self):
        """Gets the t of this CurveTsInfo.  # noqa: E501

        时间  # noqa: E501

        :return: The t of this CurveTsInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this CurveTsInfo.

        时间  # noqa: E501

        :param t: The t of this CurveTsInfo.  # noqa: E501
        :type: list[int]
        """

        self._t = t

    @property
    def v(self):
        """Gets the v of this CurveTsInfo.  # noqa: E501


        :return: The v of this CurveTsInfo.  # noqa: E501
        :rtype: list[float]
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this CurveTsInfo.


        :param v: The v of this CurveTsInfo.  # noqa: E501
        :type: list[float]
        """

        self._v = v

    @property
    def model_feature_id(self):
        """Gets the model_feature_id of this CurveTsInfo.  # noqa: E501

        模型点位  # noqa: E501

        :return: The model_feature_id of this CurveTsInfo.  # noqa: E501
        :rtype: str
        """
        return self._model_feature_id

    @model_feature_id.setter
    def model_feature_id(self, model_feature_id):
        """Sets the model_feature_id of this CurveTsInfo.

        模型点位  # noqa: E501

        :param model_feature_id: The model_feature_id of this CurveTsInfo.  # noqa: E501
        :type: str
        """

        self._model_feature_id = model_feature_id

    @property
    def id(self):
        """Gets the id of this CurveTsInfo.  # noqa: E501

        数据ID  # noqa: E501

        :return: The id of this CurveTsInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurveTsInfo.

        数据ID  # noqa: E501

        :param id: The id of this CurveTsInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def indicator_id(self):
        """Gets the indicator_id of this CurveTsInfo.  # noqa: E501

        指标Id  # noqa: E501

        :return: The indicator_id of this CurveTsInfo.  # noqa: E501
        :rtype: str
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this CurveTsInfo.

        指标Id  # noqa: E501

        :param indicator_id: The indicator_id of this CurveTsInfo.  # noqa: E501
        :type: str
        """

        self._indicator_id = indicator_id

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
        if not isinstance(other, CurveTsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurveTsInfo):
            return True

        return self.to_dict() != other.to_dict()
