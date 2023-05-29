# coding: utf-8

"""
    model-information-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from model_information_service.configuration import Configuration


class InitialCondition(object):
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
        'hotstart_scenario': 'str',
        'm1_d_hot_start_id': 'str',
        'm1_d_hotstart_file': 'str',
        'm2_d_hotstart_file': 'str'
    }

    attribute_map = {
        'hotstart_scenario': 'hotstartScenario',
        'm1_d_hot_start_id': 'm1DHotStartID',
        'm1_d_hotstart_file': 'm1DHotstartFile',
        'm2_d_hotstart_file': 'm2DHotstartFile'
    }

    def __init__(self, hotstart_scenario=None, m1_d_hot_start_id=None, m1_d_hotstart_file=None, m2_d_hotstart_file=None, local_vars_configuration=None):  # noqa: E501
        """InitialCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hotstart_scenario = None
        self._m1_d_hot_start_id = None
        self._m1_d_hotstart_file = None
        self._m2_d_hotstart_file = None
        self.discriminator = None

        self.hotstart_scenario = hotstart_scenario
        self.m1_d_hot_start_id = m1_d_hot_start_id
        self.m1_d_hotstart_file = m1_d_hotstart_file
        self.m2_d_hotstart_file = m2_d_hotstart_file

    @property
    def hotstart_scenario(self):
        """Gets the hotstart_scenario of this InitialCondition.  # noqa: E501

        热启动方案ID hotstart scenario ID  # noqa: E501

        :return: The hotstart_scenario of this InitialCondition.  # noqa: E501
        :rtype: str
        """
        return self._hotstart_scenario

    @hotstart_scenario.setter
    def hotstart_scenario(self, hotstart_scenario):
        """Sets the hotstart_scenario of this InitialCondition.

        热启动方案ID hotstart scenario ID  # noqa: E501

        :param hotstart_scenario: The hotstart_scenario of this InitialCondition.  # noqa: E501
        :type: str
        """

        self._hotstart_scenario = hotstart_scenario

    @property
    def m1_d_hot_start_id(self):
        """Gets the m1_d_hot_start_id of this InitialCondition.  # noqa: E501

        河道模型热启动文件 river hotstart file  # noqa: E501

        :return: The m1_d_hot_start_id of this InitialCondition.  # noqa: E501
        :rtype: str
        """
        return self._m1_d_hot_start_id

    @m1_d_hot_start_id.setter
    def m1_d_hot_start_id(self, m1_d_hot_start_id):
        """Sets the m1_d_hot_start_id of this InitialCondition.

        河道模型热启动文件 river hotstart file  # noqa: E501

        :param m1_d_hot_start_id: The m1_d_hot_start_id of this InitialCondition.  # noqa: E501
        :type: str
        """

        self._m1_d_hot_start_id = m1_d_hot_start_id

    @property
    def m1_d_hotstart_file(self):
        """Gets the m1_d_hotstart_file of this InitialCondition.  # noqa: E501

        管网模型热启动文件 pipe hotstart file  # noqa: E501

        :return: The m1_d_hotstart_file of this InitialCondition.  # noqa: E501
        :rtype: str
        """
        return self._m1_d_hotstart_file

    @m1_d_hotstart_file.setter
    def m1_d_hotstart_file(self, m1_d_hotstart_file):
        """Sets the m1_d_hotstart_file of this InitialCondition.

        管网模型热启动文件 pipe hotstart file  # noqa: E501

        :param m1_d_hotstart_file: The m1_d_hotstart_file of this InitialCondition.  # noqa: E501
        :type: str
        """

        self._m1_d_hotstart_file = m1_d_hotstart_file

    @property
    def m2_d_hotstart_file(self):
        """Gets the m2_d_hotstart_file of this InitialCondition.  # noqa: E501

        二维模型热启动文件 2D hotstart file  # noqa: E501

        :return: The m2_d_hotstart_file of this InitialCondition.  # noqa: E501
        :rtype: str
        """
        return self._m2_d_hotstart_file

    @m2_d_hotstart_file.setter
    def m2_d_hotstart_file(self, m2_d_hotstart_file):
        """Sets the m2_d_hotstart_file of this InitialCondition.

        二维模型热启动文件 2D hotstart file  # noqa: E501

        :param m2_d_hotstart_file: The m2_d_hotstart_file of this InitialCondition.  # noqa: E501
        :type: str
        """

        self._m2_d_hotstart_file = m2_d_hotstart_file

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
        if not isinstance(other, InitialCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InitialCondition):
            return True

        return self.to_dict() != other.to_dict()
