# coding: utf-8

"""
    wd-domain-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wd_service_domain.configuration import Configuration


class PumpInfo(object):
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
        'muid': 'str',
        'tenant_id': 'str',
        'show_name': 'str',
        'item_type': 'str',
        'device_indicator_infos': 'list[DeviceIndicatorInfo]'
    }

    attribute_map = {
        'id': 'id',
        'muid': 'muid',
        'tenant_id': 'tenantId',
        'show_name': 'showName',
        'item_type': 'itemType',
        'device_indicator_infos': 'deviceIndicatorInfos'
    }

    def __init__(self, id=None, muid=None, tenant_id=None, show_name=None, item_type=None, device_indicator_infos=None, local_vars_configuration=None):  # noqa: E501
        """PumpInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._muid = None
        self._tenant_id = None
        self._show_name = None
        self._item_type = None
        self._device_indicator_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.muid = muid
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.show_name = show_name
        self.item_type = item_type
        self.device_indicator_infos = device_indicator_infos

    @property
    def id(self):
        """Gets the id of this PumpInfo.  # noqa: E501

        数据Id  # noqa: E501

        :return: The id of this PumpInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PumpInfo.

        数据Id  # noqa: E501

        :param id: The id of this PumpInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def muid(self):
        """Gets the muid of this PumpInfo.  # noqa: E501

        模型中的Id  # noqa: E501

        :return: The muid of this PumpInfo.  # noqa: E501
        :rtype: str
        """
        return self._muid

    @muid.setter
    def muid(self, muid):
        """Sets the muid of this PumpInfo.

        模型中的Id  # noqa: E501

        :param muid: The muid of this PumpInfo.  # noqa: E501
        :type: str
        """

        self._muid = muid

    @property
    def tenant_id(self):
        """Gets the tenant_id of this PumpInfo.  # noqa: E501

        租户信息  # noqa: E501

        :return: The tenant_id of this PumpInfo.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this PumpInfo.

        租户信息  # noqa: E501

        :param tenant_id: The tenant_id of this PumpInfo.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def show_name(self):
        """Gets the show_name of this PumpInfo.  # noqa: E501

        展示名  # noqa: E501

        :return: The show_name of this PumpInfo.  # noqa: E501
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        """Sets the show_name of this PumpInfo.

        展示名  # noqa: E501

        :param show_name: The show_name of this PumpInfo.  # noqa: E501
        :type: str
        """

        self._show_name = show_name

    @property
    def item_type(self):
        """Gets the item_type of this PumpInfo.  # noqa: E501

        数据项类型  # noqa: E501

        :return: The item_type of this PumpInfo.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this PumpInfo.

        数据项类型  # noqa: E501

        :param item_type: The item_type of this PumpInfo.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def device_indicator_infos(self):
        """Gets the device_indicator_infos of this PumpInfo.  # noqa: E501

        边界点位对应的测点指标信息  # noqa: E501

        :return: The device_indicator_infos of this PumpInfo.  # noqa: E501
        :rtype: list[DeviceIndicatorInfo]
        """
        return self._device_indicator_infos

    @device_indicator_infos.setter
    def device_indicator_infos(self, device_indicator_infos):
        """Sets the device_indicator_infos of this PumpInfo.

        边界点位对应的测点指标信息  # noqa: E501

        :param device_indicator_infos: The device_indicator_infos of this PumpInfo.  # noqa: E501
        :type: list[DeviceIndicatorInfo]
        """

        self._device_indicator_infos = device_indicator_infos

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
        if not isinstance(other, PumpInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PumpInfo):
            return True

        return self.to_dict() != other.to_dict()
