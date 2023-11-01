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

from openapi_client.configuration import Configuration


class AddOrUpdateOnlineDatasInput(object):
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
        'oper_type': 'int',
        'input_datas': 'list[TsDataInputOutput]'
    }

    attribute_map = {
        'oper_type': 'operType',
        'input_datas': 'inputDatas'
    }

    def __init__(self, oper_type=None, input_datas=None, local_vars_configuration=None):  # noqa: E501
        """AddOrUpdateOnlineDatasInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._oper_type = None
        self._input_datas = None
        self.discriminator = None

        if oper_type is not None:
            self.oper_type = oper_type
        self.input_datas = input_datas

    @property
    def oper_type(self):
        """Gets the oper_type of this AddOrUpdateOnlineDatasInput.  # noqa: E501

        1-ClearProcess(Clean) 2-ManualModify(Manually update)   # noqa: E501

        :return: The oper_type of this AddOrUpdateOnlineDatasInput.  # noqa: E501
        :rtype: int
        """
        return self._oper_type

    @oper_type.setter
    def oper_type(self, oper_type):
        """Sets the oper_type of this AddOrUpdateOnlineDatasInput.

        1-ClearProcess(Clean) 2-ManualModify(Manually update)   # noqa: E501

        :param oper_type: The oper_type of this AddOrUpdateOnlineDatasInput.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and oper_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `oper_type` ({0}), must be one of {1}"  # noqa: E501
                .format(oper_type, allowed_values)
            )

        self._oper_type = oper_type

    @property
    def input_datas(self):
        """Gets the input_datas of this AddOrUpdateOnlineDatasInput.  # noqa: E501

        更新或新增的数据 data to be added or updated  # noqa: E501

        :return: The input_datas of this AddOrUpdateOnlineDatasInput.  # noqa: E501
        :rtype: list[TsDataInputOutput]
        """
        return self._input_datas

    @input_datas.setter
    def input_datas(self, input_datas):
        """Sets the input_datas of this AddOrUpdateOnlineDatasInput.

        更新或新增的数据 data to be added or updated  # noqa: E501

        :param input_datas: The input_datas of this AddOrUpdateOnlineDatasInput.  # noqa: E501
        :type: list[TsDataInputOutput]
        """

        self._input_datas = input_datas

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
        if not isinstance(other, AddOrUpdateOnlineDatasInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddOrUpdateOnlineDatasInput):
            return True

        return self.to_dict() != other.to_dict()
