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

from domain_paas_sdk_python.configuration import Configuration


class QueryBiochemicaltanksOutput(object):
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
        'tank_no': 'str',
        'tank_name': 'str'
    }

    attribute_map = {
        'tank_no': 'tankNo',
        'tank_name': 'tankName'
    }

    def __init__(self, tank_no=None, tank_name=None, local_vars_configuration=None):  # noqa: E501
        """QueryBiochemicaltanksOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tank_no = None
        self._tank_name = None
        self.discriminator = None

        self.tank_no = tank_no
        self.tank_name = tank_name

    @property
    def tank_no(self):
        """Gets the tank_no of this QueryBiochemicaltanksOutput.  # noqa: E501

        生化池序号 biochemical pool index  # noqa: E501

        :return: The tank_no of this QueryBiochemicaltanksOutput.  # noqa: E501
        :rtype: str
        """
        return self._tank_no

    @tank_no.setter
    def tank_no(self, tank_no):
        """Sets the tank_no of this QueryBiochemicaltanksOutput.

        生化池序号 biochemical pool index  # noqa: E501

        :param tank_no: The tank_no of this QueryBiochemicaltanksOutput.  # noqa: E501
        :type: str
        """

        self._tank_no = tank_no

    @property
    def tank_name(self):
        """Gets the tank_name of this QueryBiochemicaltanksOutput.  # noqa: E501

        生化池名称 biochemical pool name  # noqa: E501

        :return: The tank_name of this QueryBiochemicaltanksOutput.  # noqa: E501
        :rtype: str
        """
        return self._tank_name

    @tank_name.setter
    def tank_name(self, tank_name):
        """Sets the tank_name of this QueryBiochemicaltanksOutput.

        生化池名称 biochemical pool name  # noqa: E501

        :param tank_name: The tank_name of this QueryBiochemicaltanksOutput.  # noqa: E501
        :type: str
        """

        self._tank_name = tank_name

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
        if not isinstance(other, QueryBiochemicaltanksOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryBiochemicaltanksOutput):
            return True

        return self.to_dict() != other.to_dict()
