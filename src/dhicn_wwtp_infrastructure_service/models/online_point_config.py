# coding: utf-8

"""
    wwtp-paas-infrastructure-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_wwtp_infrastructure_service.configuration import Configuration


class OnlinePointConfig(object):
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
        'id': 'str',
        'tenant_id': 'str',
        'point_code': 'str',
        'position': 'str',
        'point_name': 'str',
        'station_code': 'str',
        'unit': 'str',
        'is_key_point': 'bool',
        'is_input': 'bool',
        'is_use': 'bool',
        'default_value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenantId',
        'point_code': 'pointCode',
        'position': 'position',
        'point_name': 'pointName',
        'station_code': 'stationCode',
        'unit': 'unit',
        'is_key_point': 'isKeyPoint',
        'is_input': 'isInput',
        'is_use': 'isUse',
        'default_value': 'defaultValue'
    }

    def __init__(self, id=None, tenant_id=None, point_code=None, position=None, point_name=None, station_code=None, unit=None, is_key_point=None, is_input=None, is_use=None, default_value=None, local_vars_configuration=None):  # noqa: E501
        """OnlinePointConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._tenant_id = None
        self._point_code = None
        self._position = None
        self._point_name = None
        self._station_code = None
        self._unit = None
        self._is_key_point = None
        self._is_input = None
        self._is_use = None
        self._default_value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.tenant_id = tenant_id
        self.point_code = point_code
        self.position = position
        self.point_name = point_name
        self.station_code = station_code
        self.unit = unit
        if is_key_point is not None:
            self.is_key_point = is_key_point
        if is_input is not None:
            self.is_input = is_input
        if is_use is not None:
            self.is_use = is_use
        if default_value is not None:
            self.default_value = default_value

    @property
    def id(self):
        """Gets the id of this OnlinePointConfig.  # noqa: E501


        :return: The id of this OnlinePointConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OnlinePointConfig.


        :param id: The id of this OnlinePointConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this OnlinePointConfig.  # noqa: E501


        :return: The tenant_id of this OnlinePointConfig.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this OnlinePointConfig.


        :param tenant_id: The tenant_id of this OnlinePointConfig.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def point_code(self):
        """Gets the point_code of this OnlinePointConfig.  # noqa: E501


        :return: The point_code of this OnlinePointConfig.  # noqa: E501
        :rtype: str
        """
        return self._point_code

    @point_code.setter
    def point_code(self, point_code):
        """Sets the point_code of this OnlinePointConfig.


        :param point_code: The point_code of this OnlinePointConfig.  # noqa: E501
        :type: str
        """

        self._point_code = point_code

    @property
    def position(self):
        """Gets the position of this OnlinePointConfig.  # noqa: E501


        :return: The position of this OnlinePointConfig.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this OnlinePointConfig.


        :param position: The position of this OnlinePointConfig.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def point_name(self):
        """Gets the point_name of this OnlinePointConfig.  # noqa: E501


        :return: The point_name of this OnlinePointConfig.  # noqa: E501
        :rtype: str
        """
        return self._point_name

    @point_name.setter
    def point_name(self, point_name):
        """Sets the point_name of this OnlinePointConfig.


        :param point_name: The point_name of this OnlinePointConfig.  # noqa: E501
        :type: str
        """

        self._point_name = point_name

    @property
    def station_code(self):
        """Gets the station_code of this OnlinePointConfig.  # noqa: E501


        :return: The station_code of this OnlinePointConfig.  # noqa: E501
        :rtype: str
        """
        return self._station_code

    @station_code.setter
    def station_code(self, station_code):
        """Sets the station_code of this OnlinePointConfig.


        :param station_code: The station_code of this OnlinePointConfig.  # noqa: E501
        :type: str
        """

        self._station_code = station_code

    @property
    def unit(self):
        """Gets the unit of this OnlinePointConfig.  # noqa: E501


        :return: The unit of this OnlinePointConfig.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this OnlinePointConfig.


        :param unit: The unit of this OnlinePointConfig.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def is_key_point(self):
        """Gets the is_key_point of this OnlinePointConfig.  # noqa: E501


        :return: The is_key_point of this OnlinePointConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_key_point

    @is_key_point.setter
    def is_key_point(self, is_key_point):
        """Sets the is_key_point of this OnlinePointConfig.


        :param is_key_point: The is_key_point of this OnlinePointConfig.  # noqa: E501
        :type: bool
        """

        self._is_key_point = is_key_point

    @property
    def is_input(self):
        """Gets the is_input of this OnlinePointConfig.  # noqa: E501


        :return: The is_input of this OnlinePointConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_input

    @is_input.setter
    def is_input(self, is_input):
        """Sets the is_input of this OnlinePointConfig.


        :param is_input: The is_input of this OnlinePointConfig.  # noqa: E501
        :type: bool
        """

        self._is_input = is_input

    @property
    def is_use(self):
        """Gets the is_use of this OnlinePointConfig.  # noqa: E501


        :return: The is_use of this OnlinePointConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_use

    @is_use.setter
    def is_use(self, is_use):
        """Sets the is_use of this OnlinePointConfig.


        :param is_use: The is_use of this OnlinePointConfig.  # noqa: E501
        :type: bool
        """

        self._is_use = is_use

    @property
    def default_value(self):
        """Gets the default_value of this OnlinePointConfig.  # noqa: E501


        :return: The default_value of this OnlinePointConfig.  # noqa: E501
        :rtype: float
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this OnlinePointConfig.


        :param default_value: The default_value of this OnlinePointConfig.  # noqa: E501
        :type: float
        """

        self._default_value = default_value

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
        if not isinstance(other, OnlinePointConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OnlinePointConfig):
            return True

        return self.to_dict() != other.to_dict()
