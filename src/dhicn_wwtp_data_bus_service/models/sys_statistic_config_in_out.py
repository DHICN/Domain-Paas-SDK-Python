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


class SysStatisticConfigInOut(object):
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
        'statistic_code': 'str',
        'statistic_name': 'str',
        'statistic_type': 'int',
        'statistic_var_ref': 'str',
        'statistic_var_ref_info': 'StatisticVarRefDto',
        'creation_time': 'datetime',
        'is_display': 'bool',
        'unit': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'statistic_code': 'statisticCode',
        'statistic_name': 'statisticName',
        'statistic_type': 'statisticType',
        'statistic_var_ref': 'statisticVarRef',
        'statistic_var_ref_info': 'statisticVarRefInfo',
        'creation_time': 'creationTime',
        'is_display': 'isDisplay',
        'unit': 'unit',
        'group_name': 'groupName'
    }

    def __init__(self, id=None, statistic_code=None, statistic_name=None, statistic_type=None, statistic_var_ref=None, statistic_var_ref_info=None, creation_time=None, is_display=None, unit=None, group_name=None, local_vars_configuration=None):  # noqa: E501
        """SysStatisticConfigInOut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._statistic_code = None
        self._statistic_name = None
        self._statistic_type = None
        self._statistic_var_ref = None
        self._statistic_var_ref_info = None
        self._creation_time = None
        self._is_display = None
        self._unit = None
        self._group_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.statistic_code = statistic_code
        self.statistic_name = statistic_name
        if statistic_type is not None:
            self.statistic_type = statistic_type
        self.statistic_var_ref = statistic_var_ref
        if statistic_var_ref_info is not None:
            self.statistic_var_ref_info = statistic_var_ref_info
        if creation_time is not None:
            self.creation_time = creation_time
        if is_display is not None:
            self.is_display = is_display
        self.unit = unit
        self.group_name = group_name

    @property
    def id(self):
        """Gets the id of this SysStatisticConfigInOut.  # noqa: E501

        配置ID config id  # noqa: E501

        :return: The id of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SysStatisticConfigInOut.

        配置ID config id  # noqa: E501

        :param id: The id of this SysStatisticConfigInOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def statistic_code(self):
        """Gets the statistic_code of this SysStatisticConfigInOut.  # noqa: E501

        统计编码 statistic code  # noqa: E501

        :return: The statistic_code of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._statistic_code

    @statistic_code.setter
    def statistic_code(self, statistic_code):
        """Sets the statistic_code of this SysStatisticConfigInOut.

        统计编码 statistic code  # noqa: E501

        :param statistic_code: The statistic_code of this SysStatisticConfigInOut.  # noqa: E501
        :type: str
        """

        self._statistic_code = statistic_code

    @property
    def statistic_name(self):
        """Gets the statistic_name of this SysStatisticConfigInOut.  # noqa: E501

        统计名称 statistic name  # noqa: E501

        :return: The statistic_name of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._statistic_name

    @statistic_name.setter
    def statistic_name(self, statistic_name):
        """Sets the statistic_name of this SysStatisticConfigInOut.

        统计名称 statistic name  # noqa: E501

        :param statistic_name: The statistic_name of this SysStatisticConfigInOut.  # noqa: E501
        :type: str
        """

        self._statistic_name = statistic_name

    @property
    def statistic_type(self):
        """Gets the statistic_type of this SysStatisticConfigInOut.  # noqa: E501

        统计类型 statistic type  # noqa: E501

        :return: The statistic_type of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: int
        """
        return self._statistic_type

    @statistic_type.setter
    def statistic_type(self, statistic_type):
        """Sets the statistic_type of this SysStatisticConfigInOut.

        统计类型 statistic type  # noqa: E501

        :param statistic_type: The statistic_type of this SysStatisticConfigInOut.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and statistic_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `statistic_type` ({0}), must be one of {1}"  # noqa: E501
                .format(statistic_type, allowed_values)
            )

        self._statistic_type = statistic_type

    @property
    def statistic_var_ref(self):
        """Gets the statistic_var_ref of this SysStatisticConfigInOut.  # noqa: E501

        统计方式-用json表示 statistic method in json format  # noqa: E501

        :return: The statistic_var_ref of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._statistic_var_ref

    @statistic_var_ref.setter
    def statistic_var_ref(self, statistic_var_ref):
        """Sets the statistic_var_ref of this SysStatisticConfigInOut.

        统计方式-用json表示 statistic method in json format  # noqa: E501

        :param statistic_var_ref: The statistic_var_ref of this SysStatisticConfigInOut.  # noqa: E501
        :type: str
        """

        self._statistic_var_ref = statistic_var_ref

    @property
    def statistic_var_ref_info(self):
        """Gets the statistic_var_ref_info of this SysStatisticConfigInOut.  # noqa: E501


        :return: The statistic_var_ref_info of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: StatisticVarRefDto
        """
        return self._statistic_var_ref_info

    @statistic_var_ref_info.setter
    def statistic_var_ref_info(self, statistic_var_ref_info):
        """Sets the statistic_var_ref_info of this SysStatisticConfigInOut.


        :param statistic_var_ref_info: The statistic_var_ref_info of this SysStatisticConfigInOut.  # noqa: E501
        :type: StatisticVarRefDto
        """

        self._statistic_var_ref_info = statistic_var_ref_info

    @property
    def creation_time(self):
        """Gets the creation_time of this SysStatisticConfigInOut.  # noqa: E501

        创建时间 creation time  # noqa: E501

        :return: The creation_time of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SysStatisticConfigInOut.

        创建时间 creation time  # noqa: E501

        :param creation_time: The creation_time of this SysStatisticConfigInOut.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def is_display(self):
        """Gets the is_display of this SysStatisticConfigInOut.  # noqa: E501

        是否展示该条统计信息 if display on the front end  # noqa: E501

        :return: The is_display of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: bool
        """
        return self._is_display

    @is_display.setter
    def is_display(self, is_display):
        """Sets the is_display of this SysStatisticConfigInOut.

        是否展示该条统计信息 if display on the front end  # noqa: E501

        :param is_display: The is_display of this SysStatisticConfigInOut.  # noqa: E501
        :type: bool
        """

        self._is_display = is_display

    @property
    def unit(self):
        """Gets the unit of this SysStatisticConfigInOut.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this SysStatisticConfigInOut.

        单位 unit  # noqa: E501

        :param unit: The unit of this SysStatisticConfigInOut.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def group_name(self):
        """Gets the group_name of this SysStatisticConfigInOut.  # noqa: E501

        统计分组 statistic group  # noqa: E501

        :return: The group_name of this SysStatisticConfigInOut.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this SysStatisticConfigInOut.

        统计分组 statistic group  # noqa: E501

        :param group_name: The group_name of this SysStatisticConfigInOut.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

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
        if not isinstance(other, SysStatisticConfigInOut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SysStatisticConfigInOut):
            return True

        return self.to_dict() != other.to_dict()
