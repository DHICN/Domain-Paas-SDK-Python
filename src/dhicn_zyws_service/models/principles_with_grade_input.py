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


class PrinciplesWithGradeInput(object):
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
        'principle_name': 'str',
        'principle_infos': 'list[PrincipleInfoWithGradeInput]',
        'system_setting_infos': 'list[SystemSettingOutput]'
    }

    attribute_map = {
        'principle_name': 'principleName',
        'principle_infos': 'principleInfos',
        'system_setting_infos': 'systemSettingInfos'
    }

    def __init__(self, principle_name=None, principle_infos=None, system_setting_infos=None, local_vars_configuration=None):  # noqa: E501
        """PrinciplesWithGradeInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._principle_name = None
        self._principle_infos = None
        self._system_setting_infos = None
        self.discriminator = None

        self.principle_name = principle_name
        self.principle_infos = principle_infos
        self.system_setting_infos = system_setting_infos

    @property
    def principle_name(self):
        """Gets the principle_name of this PrinciplesWithGradeInput.  # noqa: E501

        原则名称  # noqa: E501

        :return: The principle_name of this PrinciplesWithGradeInput.  # noqa: E501
        :rtype: str
        """
        return self._principle_name

    @principle_name.setter
    def principle_name(self, principle_name):
        """Sets the principle_name of this PrinciplesWithGradeInput.

        原则名称  # noqa: E501

        :param principle_name: The principle_name of this PrinciplesWithGradeInput.  # noqa: E501
        :type: str
        """

        self._principle_name = principle_name

    @property
    def principle_infos(self):
        """Gets the principle_infos of this PrinciplesWithGradeInput.  # noqa: E501

        原则下的具体详情项列表  # noqa: E501

        :return: The principle_infos of this PrinciplesWithGradeInput.  # noqa: E501
        :rtype: list[PrincipleInfoWithGradeInput]
        """
        return self._principle_infos

    @principle_infos.setter
    def principle_infos(self, principle_infos):
        """Sets the principle_infos of this PrinciplesWithGradeInput.

        原则下的具体详情项列表  # noqa: E501

        :param principle_infos: The principle_infos of this PrinciplesWithGradeInput.  # noqa: E501
        :type: list[PrincipleInfoWithGradeInput]
        """

        self._principle_infos = principle_infos

    @property
    def system_setting_infos(self):
        """Gets the system_setting_infos of this PrinciplesWithGradeInput.  # noqa: E501

        原则下的具体配水算法设置列表  # noqa: E501

        :return: The system_setting_infos of this PrinciplesWithGradeInput.  # noqa: E501
        :rtype: list[SystemSettingOutput]
        """
        return self._system_setting_infos

    @system_setting_infos.setter
    def system_setting_infos(self, system_setting_infos):
        """Sets the system_setting_infos of this PrinciplesWithGradeInput.

        原则下的具体配水算法设置列表  # noqa: E501

        :param system_setting_infos: The system_setting_infos of this PrinciplesWithGradeInput.  # noqa: E501
        :type: list[SystemSettingOutput]
        """

        self._system_setting_infos = system_setting_infos

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
        if not isinstance(other, PrinciplesWithGradeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrinciplesWithGradeInput):
            return True

        return self.to_dict() != other.to_dict()
