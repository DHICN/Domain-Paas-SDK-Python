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


class GlobalPrinciplesDetailsInput(object):
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
        'principle_id': 'str'
    }

    attribute_map = {
        'principle_id': 'principleId'
    }

    def __init__(self, principle_id=None, local_vars_configuration=None):  # noqa: E501
        """GlobalPrinciplesDetailsInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._principle_id = None
        self.discriminator = None

        self.principle_id = principle_id

    @property
    def principle_id(self):
        """Gets the principle_id of this GlobalPrinciplesDetailsInput.  # noqa: E501

        原则id  # noqa: E501

        :return: The principle_id of this GlobalPrinciplesDetailsInput.  # noqa: E501
        :rtype: str
        """
        return self._principle_id

    @principle_id.setter
    def principle_id(self, principle_id):
        """Sets the principle_id of this GlobalPrinciplesDetailsInput.

        原则id  # noqa: E501

        :param principle_id: The principle_id of this GlobalPrinciplesDetailsInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and principle_id is None:  # noqa: E501
            raise ValueError("Invalid value for `principle_id`, must not be `None`")  # noqa: E501

        self._principle_id = principle_id

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
        if not isinstance(other, GlobalPrinciplesDetailsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalPrinciplesDetailsInput):
            return True

        return self.to_dict() != other.to_dict()
