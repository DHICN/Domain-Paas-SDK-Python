# coding: utf-8

"""
    IoT服务

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_iot_service.configuration import Configuration


class ModelResultOutput(object):
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
        't': 'list[str]',
        'v': 'list[float]',
        'device_code': 'str',
        'indicator': 'str',
        'model_feature_id': 'str'
    }

    attribute_map = {
        't': 't',
        'v': 'v',
        'device_code': 'deviceCode',
        'indicator': 'indicator',
        'model_feature_id': 'modelFeatureId'
    }

    def __init__(self, t=None, v=None, device_code=None, indicator=None, model_feature_id=None, local_vars_configuration=None):  # noqa: E501
        """ModelResultOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._t = None
        self._v = None
        self._device_code = None
        self._indicator = None
        self._model_feature_id = None
        self.discriminator = None

        self.t = t
        self.v = v
        self.device_code = device_code
        self.indicator = indicator
        self.model_feature_id = model_feature_id

    @property
    def t(self):
        """Gets the t of this ModelResultOutput.  # noqa: E501


        :return: The t of this ModelResultOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this ModelResultOutput.


        :param t: The t of this ModelResultOutput.  # noqa: E501
        :type: list[str]
        """

        self._t = t

    @property
    def v(self):
        """Gets the v of this ModelResultOutput.  # noqa: E501


        :return: The v of this ModelResultOutput.  # noqa: E501
        :rtype: list[float]
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this ModelResultOutput.


        :param v: The v of this ModelResultOutput.  # noqa: E501
        :type: list[float]
        """

        self._v = v

    @property
    def device_code(self):
        """Gets the device_code of this ModelResultOutput.  # noqa: E501

        设备编码,若当前项目下Indicator有重复,设备编码必传  # noqa: E501

        :return: The device_code of this ModelResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        """Sets the device_code of this ModelResultOutput.

        设备编码,若当前项目下Indicator有重复,设备编码必传  # noqa: E501

        :param device_code: The device_code of this ModelResultOutput.  # noqa: E501
        :type: str
        """

        self._device_code = device_code

    @property
    def indicator(self):
        """Gets the indicator of this ModelResultOutput.  # noqa: E501

        指标  # noqa: E501

        :return: The indicator of this ModelResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this ModelResultOutput.

        指标  # noqa: E501

        :param indicator: The indicator of this ModelResultOutput.  # noqa: E501
        :type: str
        """

        self._indicator = indicator

    @property
    def model_feature_id(self):
        """Gets the model_feature_id of this ModelResultOutput.  # noqa: E501

        模型Id  # noqa: E501

        :return: The model_feature_id of this ModelResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_feature_id

    @model_feature_id.setter
    def model_feature_id(self, model_feature_id):
        """Sets the model_feature_id of this ModelResultOutput.

        模型Id  # noqa: E501

        :param model_feature_id: The model_feature_id of this ModelResultOutput.  # noqa: E501
        :type: str
        """

        self._model_feature_id = model_feature_id

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
        if not isinstance(other, ModelResultOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelResultOutput):
            return True

        return self.to_dict() != other.to_dict()
