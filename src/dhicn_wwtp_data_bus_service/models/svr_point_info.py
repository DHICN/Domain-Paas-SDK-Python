# coding: utf-8

"""
    wwtp-paas-main-bus-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wwtp_data_bus_service.configuration import Configuration


class SvrPointInfo(object):
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
        'data_source': 'int',
        'point_code': 'str'
    }

    attribute_map = {
        'data_source': 'dataSource',
        'point_code': 'pointCode'
    }

    def __init__(self, data_source=None, point_code=None, local_vars_configuration=None):  # noqa: E501
        """SvrPointInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_source = None
        self._point_code = None
        self.discriminator = None

        if data_source is not None:
            self.data_source = data_source
        self.point_code = point_code

    @property
    def data_source(self):
        """Gets the data_source of this SvrPointInfo.  # noqa: E501


        :return: The data_source of this SvrPointInfo.  # noqa: E501
        :rtype: int
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this SvrPointInfo.


        :param data_source: The data_source of this SvrPointInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_source not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_source` ({0}), must be one of {1}"  # noqa: E501
                .format(data_source, allowed_values)
            )

        self._data_source = data_source

    @property
    def point_code(self):
        """Gets the point_code of this SvrPointInfo.  # noqa: E501


        :return: The point_code of this SvrPointInfo.  # noqa: E501
        :rtype: str
        """
        return self._point_code

    @point_code.setter
    def point_code(self, point_code):
        """Sets the point_code of this SvrPointInfo.


        :param point_code: The point_code of this SvrPointInfo.  # noqa: E501
        :type: str
        """

        self._point_code = point_code

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
        if not isinstance(other, SvrPointInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SvrPointInfo):
            return True

        return self.to_dict() != other.to_dict()
