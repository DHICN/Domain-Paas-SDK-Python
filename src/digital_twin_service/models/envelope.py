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


class Envelope(object):
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
        'is_null': 'bool',
        'width': 'float',
        'height': 'float',
        'diameter': 'float',
        'min_x': 'float',
        'max_x': 'float',
        'min_y': 'float',
        'max_y': 'float',
        'area': 'float',
        'min_extent': 'float',
        'max_extent': 'float',
        'centre': 'Coordinate'
    }

    attribute_map = {
        'is_null': 'isNull',
        'width': 'width',
        'height': 'height',
        'diameter': 'diameter',
        'min_x': 'minX',
        'max_x': 'maxX',
        'min_y': 'minY',
        'max_y': 'maxY',
        'area': 'area',
        'min_extent': 'minExtent',
        'max_extent': 'maxExtent',
        'centre': 'centre'
    }

    def __init__(self, is_null=None, width=None, height=None, diameter=None, min_x=None, max_x=None, min_y=None, max_y=None, area=None, min_extent=None, max_extent=None, centre=None, local_vars_configuration=None):  # noqa: E501
        """Envelope - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_null = None
        self._width = None
        self._height = None
        self._diameter = None
        self._min_x = None
        self._max_x = None
        self._min_y = None
        self._max_y = None
        self._area = None
        self._min_extent = None
        self._max_extent = None
        self._centre = None
        self.discriminator = None

        if is_null is not None:
            self.is_null = is_null
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if diameter is not None:
            self.diameter = diameter
        if min_x is not None:
            self.min_x = min_x
        if max_x is not None:
            self.max_x = max_x
        if min_y is not None:
            self.min_y = min_y
        if max_y is not None:
            self.max_y = max_y
        if area is not None:
            self.area = area
        if min_extent is not None:
            self.min_extent = min_extent
        if max_extent is not None:
            self.max_extent = max_extent
        if centre is not None:
            self.centre = centre

    @property
    def is_null(self):
        """Gets the is_null of this Envelope.  # noqa: E501


        :return: The is_null of this Envelope.  # noqa: E501
        :rtype: bool
        """
        return self._is_null

    @is_null.setter
    def is_null(self, is_null):
        """Sets the is_null of this Envelope.


        :param is_null: The is_null of this Envelope.  # noqa: E501
        :type: bool
        """

        self._is_null = is_null

    @property
    def width(self):
        """Gets the width of this Envelope.  # noqa: E501


        :return: The width of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Envelope.


        :param width: The width of this Envelope.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Envelope.  # noqa: E501


        :return: The height of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Envelope.


        :param height: The height of this Envelope.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def diameter(self):
        """Gets the diameter of this Envelope.  # noqa: E501


        :return: The diameter of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this Envelope.


        :param diameter: The diameter of this Envelope.  # noqa: E501
        :type: float
        """

        self._diameter = diameter

    @property
    def min_x(self):
        """Gets the min_x of this Envelope.  # noqa: E501


        :return: The min_x of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._min_x

    @min_x.setter
    def min_x(self, min_x):
        """Sets the min_x of this Envelope.


        :param min_x: The min_x of this Envelope.  # noqa: E501
        :type: float
        """

        self._min_x = min_x

    @property
    def max_x(self):
        """Gets the max_x of this Envelope.  # noqa: E501


        :return: The max_x of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._max_x

    @max_x.setter
    def max_x(self, max_x):
        """Sets the max_x of this Envelope.


        :param max_x: The max_x of this Envelope.  # noqa: E501
        :type: float
        """

        self._max_x = max_x

    @property
    def min_y(self):
        """Gets the min_y of this Envelope.  # noqa: E501


        :return: The min_y of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._min_y

    @min_y.setter
    def min_y(self, min_y):
        """Sets the min_y of this Envelope.


        :param min_y: The min_y of this Envelope.  # noqa: E501
        :type: float
        """

        self._min_y = min_y

    @property
    def max_y(self):
        """Gets the max_y of this Envelope.  # noqa: E501


        :return: The max_y of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._max_y

    @max_y.setter
    def max_y(self, max_y):
        """Sets the max_y of this Envelope.


        :param max_y: The max_y of this Envelope.  # noqa: E501
        :type: float
        """

        self._max_y = max_y

    @property
    def area(self):
        """Gets the area of this Envelope.  # noqa: E501


        :return: The area of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Envelope.


        :param area: The area of this Envelope.  # noqa: E501
        :type: float
        """

        self._area = area

    @property
    def min_extent(self):
        """Gets the min_extent of this Envelope.  # noqa: E501


        :return: The min_extent of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._min_extent

    @min_extent.setter
    def min_extent(self, min_extent):
        """Sets the min_extent of this Envelope.


        :param min_extent: The min_extent of this Envelope.  # noqa: E501
        :type: float
        """

        self._min_extent = min_extent

    @property
    def max_extent(self):
        """Gets the max_extent of this Envelope.  # noqa: E501


        :return: The max_extent of this Envelope.  # noqa: E501
        :rtype: float
        """
        return self._max_extent

    @max_extent.setter
    def max_extent(self, max_extent):
        """Sets the max_extent of this Envelope.


        :param max_extent: The max_extent of this Envelope.  # noqa: E501
        :type: float
        """

        self._max_extent = max_extent

    @property
    def centre(self):
        """Gets the centre of this Envelope.  # noqa: E501


        :return: The centre of this Envelope.  # noqa: E501
        :rtype: Coordinate
        """
        return self._centre

    @centre.setter
    def centre(self, centre):
        """Sets the centre of this Envelope.


        :param centre: The centre of this Envelope.  # noqa: E501
        :type: Coordinate
        """

        self._centre = centre

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
        if not isinstance(other, Envelope):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Envelope):
            return True

        return self.to_dict() != other.to_dict()
