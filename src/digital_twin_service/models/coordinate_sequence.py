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

from digital_twin_service.configuration import Configuration


class CoordinateSequence(object):
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
        'dimension': 'int',
        'measures': 'int',
        'spatial': 'int',
        'ordinates': 'int',
        'has_z': 'bool',
        'has_m': 'bool',
        'z_ordinate_index': 'int',
        'm_ordinate_index': 'int',
        'first': 'Coordinate',
        'last': 'Coordinate',
        'count': 'int'
    }

    attribute_map = {
        'dimension': 'dimension',
        'measures': 'measures',
        'spatial': 'spatial',
        'ordinates': 'ordinates',
        'has_z': 'hasZ',
        'has_m': 'hasM',
        'z_ordinate_index': 'zOrdinateIndex',
        'm_ordinate_index': 'mOrdinateIndex',
        'first': 'first',
        'last': 'last',
        'count': 'count'
    }

    def __init__(self, dimension=None, measures=None, spatial=None, ordinates=None, has_z=None, has_m=None, z_ordinate_index=None, m_ordinate_index=None, first=None, last=None, count=None, local_vars_configuration=None):  # noqa: E501
        """CoordinateSequence - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dimension = None
        self._measures = None
        self._spatial = None
        self._ordinates = None
        self._has_z = None
        self._has_m = None
        self._z_ordinate_index = None
        self._m_ordinate_index = None
        self._first = None
        self._last = None
        self._count = None
        self.discriminator = None

        if dimension is not None:
            self.dimension = dimension
        if measures is not None:
            self.measures = measures
        if spatial is not None:
            self.spatial = spatial
        if ordinates is not None:
            self.ordinates = ordinates
        if has_z is not None:
            self.has_z = has_z
        if has_m is not None:
            self.has_m = has_m
        if z_ordinate_index is not None:
            self.z_ordinate_index = z_ordinate_index
        if m_ordinate_index is not None:
            self.m_ordinate_index = m_ordinate_index
        if first is not None:
            self.first = first
        if last is not None:
            self.last = last
        if count is not None:
            self.count = count

    @property
    def dimension(self):
        """Gets the dimension of this CoordinateSequence.  # noqa: E501


        :return: The dimension of this CoordinateSequence.  # noqa: E501
        :rtype: int
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this CoordinateSequence.


        :param dimension: The dimension of this CoordinateSequence.  # noqa: E501
        :type: int
        """

        self._dimension = dimension

    @property
    def measures(self):
        """Gets the measures of this CoordinateSequence.  # noqa: E501


        :return: The measures of this CoordinateSequence.  # noqa: E501
        :rtype: int
        """
        return self._measures

    @measures.setter
    def measures(self, measures):
        """Sets the measures of this CoordinateSequence.


        :param measures: The measures of this CoordinateSequence.  # noqa: E501
        :type: int
        """

        self._measures = measures

    @property
    def spatial(self):
        """Gets the spatial of this CoordinateSequence.  # noqa: E501


        :return: The spatial of this CoordinateSequence.  # noqa: E501
        :rtype: int
        """
        return self._spatial

    @spatial.setter
    def spatial(self, spatial):
        """Sets the spatial of this CoordinateSequence.


        :param spatial: The spatial of this CoordinateSequence.  # noqa: E501
        :type: int
        """

        self._spatial = spatial

    @property
    def ordinates(self):
        """Gets the ordinates of this CoordinateSequence.  # noqa: E501

        0-None 1-X 1-Spatial1 2-Y 2-Spatial2 3-XY 4-Spatial3 4-Z 7-XYZ 8-Spatial4 16-Spatial5 32-Spatial6 64-Spatial7 128-Spatial8 256-Spatial9 512-Spatial10 1024-Spatial11 2048-Spatial12 4096-Spatial13 8192-Spatial14 16384-Spatial15 32768-Spatial16 65535-AllSpatialOrdinates 65536-Measure1 65536-M 65539-XYM 65543-XYZM 131072-Measure2 262144-Measure3 524288-Measure4 1048576-Measure5 2097152-Measure6 4194304-Measure7 8388608-Measure8 16777216-Measure9 33554432-Measure10 67108864-Measure11 134217728-Measure12 268435456-Measure13 536870912-Measure14 1073741824-Measure15 -2147483648-Measure16 -65536-AllMeasureOrdinates -1-AllOrdinates   # noqa: E501

        :return: The ordinates of this CoordinateSequence.  # noqa: E501
        :rtype: int
        """
        return self._ordinates

    @ordinates.setter
    def ordinates(self, ordinates):
        """Sets the ordinates of this CoordinateSequence.

        0-None 1-X 1-Spatial1 2-Y 2-Spatial2 3-XY 4-Spatial3 4-Z 7-XYZ 8-Spatial4 16-Spatial5 32-Spatial6 64-Spatial7 128-Spatial8 256-Spatial9 512-Spatial10 1024-Spatial11 2048-Spatial12 4096-Spatial13 8192-Spatial14 16384-Spatial15 32768-Spatial16 65535-AllSpatialOrdinates 65536-Measure1 65536-M 65539-XYM 65543-XYZM 131072-Measure2 262144-Measure3 524288-Measure4 1048576-Measure5 2097152-Measure6 4194304-Measure7 8388608-Measure8 16777216-Measure9 33554432-Measure10 67108864-Measure11 134217728-Measure12 268435456-Measure13 536870912-Measure14 1073741824-Measure15 -2147483648-Measure16 -65536-AllMeasureOrdinates -1-AllOrdinates   # noqa: E501

        :param ordinates: The ordinates of this CoordinateSequence.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 7, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65535, 65536, 65539, 65543, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, -2147483648, -65536, -1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ordinates not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ordinates` ({0}), must be one of {1}"  # noqa: E501
                .format(ordinates, allowed_values)
            )

        self._ordinates = ordinates

    @property
    def has_z(self):
        """Gets the has_z of this CoordinateSequence.  # noqa: E501


        :return: The has_z of this CoordinateSequence.  # noqa: E501
        :rtype: bool
        """
        return self._has_z

    @has_z.setter
    def has_z(self, has_z):
        """Sets the has_z of this CoordinateSequence.


        :param has_z: The has_z of this CoordinateSequence.  # noqa: E501
        :type: bool
        """

        self._has_z = has_z

    @property
    def has_m(self):
        """Gets the has_m of this CoordinateSequence.  # noqa: E501


        :return: The has_m of this CoordinateSequence.  # noqa: E501
        :rtype: bool
        """
        return self._has_m

    @has_m.setter
    def has_m(self, has_m):
        """Sets the has_m of this CoordinateSequence.


        :param has_m: The has_m of this CoordinateSequence.  # noqa: E501
        :type: bool
        """

        self._has_m = has_m

    @property
    def z_ordinate_index(self):
        """Gets the z_ordinate_index of this CoordinateSequence.  # noqa: E501


        :return: The z_ordinate_index of this CoordinateSequence.  # noqa: E501
        :rtype: int
        """
        return self._z_ordinate_index

    @z_ordinate_index.setter
    def z_ordinate_index(self, z_ordinate_index):
        """Sets the z_ordinate_index of this CoordinateSequence.


        :param z_ordinate_index: The z_ordinate_index of this CoordinateSequence.  # noqa: E501
        :type: int
        """

        self._z_ordinate_index = z_ordinate_index

    @property
    def m_ordinate_index(self):
        """Gets the m_ordinate_index of this CoordinateSequence.  # noqa: E501


        :return: The m_ordinate_index of this CoordinateSequence.  # noqa: E501
        :rtype: int
        """
        return self._m_ordinate_index

    @m_ordinate_index.setter
    def m_ordinate_index(self, m_ordinate_index):
        """Sets the m_ordinate_index of this CoordinateSequence.


        :param m_ordinate_index: The m_ordinate_index of this CoordinateSequence.  # noqa: E501
        :type: int
        """

        self._m_ordinate_index = m_ordinate_index

    @property
    def first(self):
        """Gets the first of this CoordinateSequence.  # noqa: E501


        :return: The first of this CoordinateSequence.  # noqa: E501
        :rtype: Coordinate
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this CoordinateSequence.


        :param first: The first of this CoordinateSequence.  # noqa: E501
        :type: Coordinate
        """

        self._first = first

    @property
    def last(self):
        """Gets the last of this CoordinateSequence.  # noqa: E501


        :return: The last of this CoordinateSequence.  # noqa: E501
        :rtype: Coordinate
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this CoordinateSequence.


        :param last: The last of this CoordinateSequence.  # noqa: E501
        :type: Coordinate
        """

        self._last = last

    @property
    def count(self):
        """Gets the count of this CoordinateSequence.  # noqa: E501


        :return: The count of this CoordinateSequence.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CoordinateSequence.


        :param count: The count of this CoordinateSequence.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, CoordinateSequence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoordinateSequence):
            return True

        return self.to_dict() != other.to_dict()
