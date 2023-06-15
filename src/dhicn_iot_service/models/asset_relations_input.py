# coding: utf-8

"""
    iot-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_iot_service.configuration import Configuration


class AssetRelationsInput(object):
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
        'asset_id': 'str',
        'entity_type': 'int',
        'entity_ids': 'list[str]'
    }

    attribute_map = {
        'asset_id': 'assetId',
        'entity_type': 'entityType',
        'entity_ids': 'entityIds'
    }

    def __init__(self, asset_id=None, entity_type=None, entity_ids=None, local_vars_configuration=None):  # noqa: E501
        """AssetRelationsInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_id = None
        self._entity_type = None
        self._entity_ids = None
        self.discriminator = None

        self.asset_id = asset_id
        self.entity_type = entity_type
        self.entity_ids = entity_ids

    @property
    def asset_id(self):
        """Gets the asset_id of this AssetRelationsInput.  # noqa: E501

        资产Id asset id  # noqa: E501

        :return: The asset_id of this AssetRelationsInput.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this AssetRelationsInput.

        资产Id asset id  # noqa: E501

        :param asset_id: The asset_id of this AssetRelationsInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and asset_id is None:  # noqa: E501
            raise ValueError("Invalid value for `asset_id`, must not be `None`")  # noqa: E501

        self._asset_id = asset_id

    @property
    def entity_type(self):
        """Gets the entity_type of this AssetRelationsInput.  # noqa: E501

        0-TENANT_PROFILE(租户配置实体) 1-TENANT(租户实体) 2-CUSTOMER(客户实体) 3-DEVICE(设备实体) 4-ASSET(资产实体) 5-DEVICE_PROFILE(资产实体)   # noqa: E501

        :return: The entity_type of this AssetRelationsInput.  # noqa: E501
        :rtype: int
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this AssetRelationsInput.

        0-TENANT_PROFILE(租户配置实体) 1-TENANT(租户实体) 2-CUSTOMER(客户实体) 3-DEVICE(设备实体) 4-ASSET(资产实体) 5-DEVICE_PROFILE(资产实体)   # noqa: E501

        :param entity_type: The entity_type of this AssetRelationsInput.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1, 2, 3, 4, 5]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and entity_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def entity_ids(self):
        """Gets the entity_ids of this AssetRelationsInput.  # noqa: E501

        实体Id列表 entity ids  # noqa: E501

        :return: The entity_ids of this AssetRelationsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_ids

    @entity_ids.setter
    def entity_ids(self, entity_ids):
        """Sets the entity_ids of this AssetRelationsInput.

        实体Id列表 entity ids  # noqa: E501

        :param entity_ids: The entity_ids of this AssetRelationsInput.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and entity_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_ids`, must not be `None`")  # noqa: E501

        self._entity_ids = entity_ids

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
        if not isinstance(other, AssetRelationsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetRelationsInput):
            return True

        return self.to_dict() != other.to_dict()