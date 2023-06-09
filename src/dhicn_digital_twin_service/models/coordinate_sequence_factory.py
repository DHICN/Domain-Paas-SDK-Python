# coding: utf-8

"""
    digital-twin-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_digital_twin_service.configuration import Configuration


class CoordinateSequenceFactory(object):
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
        'ordinates': 'int'
    }

    attribute_map = {
        'ordinates': 'ordinates'
    }

    def __init__(self, ordinates=None, local_vars_configuration=None):  # noqa: E501
        """CoordinateSequenceFactory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ordinates = None
        self.discriminator = None

        if ordinates is not None:
            self.ordinates = ordinates

    @property
    def ordinates(self):
        """Gets the ordinates of this CoordinateSequenceFactory.  # noqa: E501

        0-None 1-X 1-Spatial1 2-Y 2-Spatial2 3-XY 4-Spatial3 4-Z 7-XYZ 8-Spatial4 16-Spatial5 32-Spatial6 64-Spatial7 128-Spatial8 256-Spatial9 512-Spatial10 1024-Spatial11 2048-Spatial12 4096-Spatial13 8192-Spatial14 16384-Spatial15 32768-Spatial16 65535-AllSpatialOrdinates 65536-Measure1 65536-M 65539-XYM 65543-XYZM 131072-Measure2 262144-Measure3 524288-Measure4 1048576-Measure5 2097152-Measure6 4194304-Measure7 8388608-Measure8 16777216-Measure9 33554432-Measure10 67108864-Measure11 134217728-Measure12 268435456-Measure13 536870912-Measure14 1073741824-Measure15 -2147483648-Measure16 -65536-AllMeasureOrdinates -1-AllOrdinates   # noqa: E501

        :return: The ordinates of this CoordinateSequenceFactory.  # noqa: E501
        :rtype: int
        """
        return self._ordinates

    @ordinates.setter
    def ordinates(self, ordinates):
        """Sets the ordinates of this CoordinateSequenceFactory.

        0-None 1-X 1-Spatial1 2-Y 2-Spatial2 3-XY 4-Spatial3 4-Z 7-XYZ 8-Spatial4 16-Spatial5 32-Spatial6 64-Spatial7 128-Spatial8 256-Spatial9 512-Spatial10 1024-Spatial11 2048-Spatial12 4096-Spatial13 8192-Spatial14 16384-Spatial15 32768-Spatial16 65535-AllSpatialOrdinates 65536-Measure1 65536-M 65539-XYM 65543-XYZM 131072-Measure2 262144-Measure3 524288-Measure4 1048576-Measure5 2097152-Measure6 4194304-Measure7 8388608-Measure8 16777216-Measure9 33554432-Measure10 67108864-Measure11 134217728-Measure12 268435456-Measure13 536870912-Measure14 1073741824-Measure15 -2147483648-Measure16 -65536-AllMeasureOrdinates -1-AllOrdinates   # noqa: E501

        :param ordinates: The ordinates of this CoordinateSequenceFactory.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 7, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65535, 65536, 65539, 65543, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, -2147483648, -65536, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ordinates not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ordinates` ({0}), must be one of {1}"  # noqa: E501
                .format(ordinates, allowed_values)
            )

        self._ordinates = ordinates

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
        if not isinstance(other, CoordinateSequenceFactory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoordinateSequenceFactory):
            return True

        return self.to_dict() != other.to_dict()
