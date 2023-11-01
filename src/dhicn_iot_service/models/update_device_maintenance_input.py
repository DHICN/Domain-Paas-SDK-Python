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


class UpdateDeviceMaintenanceInput(object):
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
        'entity_id': 'str',
        'entity_type': 'int',
        'maintenance': 'str',
        'time': 'datetime',
        'id': 'str'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'entity_type': 'entityType',
        'maintenance': 'maintenance',
        'time': 'time',
        'id': 'id'
    }

    def __init__(self, entity_id=None, entity_type=None, maintenance=None, time=None, id=None, local_vars_configuration=None):  # noqa: E501
        """UpdateDeviceMaintenanceInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entity_id = None
        self._entity_type = None
        self._maintenance = None
        self._time = None
        self._id = None
        self.discriminator = None

        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = entity_type
        self.maintenance = maintenance
        if time is not None:
            self.time = time
        if id is not None:
            self.id = id

    @property
    def entity_id(self):
        """Gets the entity_id of this UpdateDeviceMaintenanceInput.  # noqa: E501


        :return: The entity_id of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this UpdateDeviceMaintenanceInput.


        :param entity_id: The entity_id of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this UpdateDeviceMaintenanceInput.  # noqa: E501

        0-TENANT_PROFILE(租户配置实体) 1-TENANT(租户实体) 2-CUSTOMER(客户实体) 3-DEVICE(设备实体) 4-ASSET(资产实体) 5-DEVICE_PROFILE(资产实体)   # noqa: E501

        :return: The entity_type of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :rtype: int
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this UpdateDeviceMaintenanceInput.

        0-TENANT_PROFILE(租户配置实体) 1-TENANT(租户实体) 2-CUSTOMER(客户实体) 3-DEVICE(设备实体) 4-ASSET(资产实体) 5-DEVICE_PROFILE(资产实体)   # noqa: E501

        :param entity_type: The entity_type of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and entity_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def maintenance(self):
        """Gets the maintenance of this UpdateDeviceMaintenanceInput.  # noqa: E501


        :return: The maintenance of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :rtype: str
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """Sets the maintenance of this UpdateDeviceMaintenanceInput.


        :param maintenance: The maintenance of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :type: str
        """

        self._maintenance = maintenance

    @property
    def time(self):
        """Gets the time of this UpdateDeviceMaintenanceInput.  # noqa: E501


        :return: The time of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this UpdateDeviceMaintenanceInput.


        :param time: The time of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def id(self):
        """Gets the id of this UpdateDeviceMaintenanceInput.  # noqa: E501


        :return: The id of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateDeviceMaintenanceInput.


        :param id: The id of this UpdateDeviceMaintenanceInput.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, UpdateDeviceMaintenanceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateDeviceMaintenanceInput):
            return True

        return self.to_dict() != other.to_dict()
