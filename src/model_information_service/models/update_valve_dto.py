# coding: utf-8

"""
    model-information-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from model_information_service.configuration import Configuration


class UpdateValveDto(object):
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
        'muid': 'str',
        'setting': 'float',
        'setting_no': 'WdValveSettingNo',
        'valve_type': 'WdValveTypeNo',
        'valve_status': 'WdValveStatusNo',
        'geom_wkt': 'str',
        'to_y': 'float',
        'to_x': 'float',
        'from_y': 'float',
        'from_x': 'float',
        'coor_str': 'str',
        'street_name': 'str',
        'description': 'str',
        'note': 'str',
        'data_source': 'str',
        'zone_id': 'str',
        'loss_coeff': 'float',
        'diameter': 'float',
        'to_node': 'str',
        'from_node': 'str',
        'oper_curve_id': 'str',
        'valve_curve_id': 'str',
        'create_time': 'datetime',
        'id': 'str'
    }

    attribute_map = {
        'muid': 'muid',
        'setting': 'setting',
        'setting_no': 'settingNo',
        'valve_type': 'valveType',
        'valve_status': 'valveStatus',
        'geom_wkt': 'geomWKT',
        'to_y': 'toY',
        'to_x': 'toX',
        'from_y': 'fromY',
        'from_x': 'fromX',
        'coor_str': 'coorStr',
        'street_name': 'streetName',
        'description': 'description',
        'note': 'note',
        'data_source': 'dataSource',
        'zone_id': 'zoneID',
        'loss_coeff': 'lossCoeff',
        'diameter': 'diameter',
        'to_node': 'toNode',
        'from_node': 'fromNode',
        'oper_curve_id': 'operCurveID',
        'valve_curve_id': 'valveCurveID',
        'create_time': 'createTime',
        'id': 'id'
    }

    def __init__(self, muid=None, setting=None, setting_no=None, valve_type=None, valve_status=None, geom_wkt=None, to_y=None, to_x=None, from_y=None, from_x=None, coor_str=None, street_name=None, description=None, note=None, data_source=None, zone_id=None, loss_coeff=None, diameter=None, to_node=None, from_node=None, oper_curve_id=None, valve_curve_id=None, create_time=None, id=None, local_vars_configuration=None):  # noqa: E501
        """UpdateValveDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._muid = None
        self._setting = None
        self._setting_no = None
        self._valve_type = None
        self._valve_status = None
        self._geom_wkt = None
        self._to_y = None
        self._to_x = None
        self._from_y = None
        self._from_x = None
        self._coor_str = None
        self._street_name = None
        self._description = None
        self._note = None
        self._data_source = None
        self._zone_id = None
        self._loss_coeff = None
        self._diameter = None
        self._to_node = None
        self._from_node = None
        self._oper_curve_id = None
        self._valve_curve_id = None
        self._create_time = None
        self._id = None
        self.discriminator = None

        self.muid = muid
        if setting is not None:
            self.setting = setting
        if setting_no is not None:
            self.setting_no = setting_no
        if valve_type is not None:
            self.valve_type = valve_type
        if valve_status is not None:
            self.valve_status = valve_status
        self.geom_wkt = geom_wkt
        if to_y is not None:
            self.to_y = to_y
        if to_x is not None:
            self.to_x = to_x
        if from_y is not None:
            self.from_y = from_y
        if from_x is not None:
            self.from_x = from_x
        self.coor_str = coor_str
        self.street_name = street_name
        self.description = description
        self.note = note
        self.data_source = data_source
        self.zone_id = zone_id
        if loss_coeff is not None:
            self.loss_coeff = loss_coeff
        if diameter is not None:
            self.diameter = diameter
        self.to_node = to_node
        self.from_node = from_node
        self.oper_curve_id = oper_curve_id
        self.valve_curve_id = valve_curve_id
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id

    @property
    def muid(self):
        """Gets the muid of this UpdateValveDto.  # noqa: E501

        模型中阀门的ID valve muid  # noqa: E501

        :return: The muid of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._muid

    @muid.setter
    def muid(self, muid):
        """Sets the muid of this UpdateValveDto.

        模型中阀门的ID valve muid  # noqa: E501

        :param muid: The muid of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._muid = muid

    @property
    def setting(self):
        """Gets the setting of this UpdateValveDto.  # noqa: E501

        设置的数值 setting valve  # noqa: E501

        :return: The setting of this UpdateValveDto.  # noqa: E501
        :rtype: float
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        """Sets the setting of this UpdateValveDto.

        设置的数值 setting valve  # noqa: E501

        :param setting: The setting of this UpdateValveDto.  # noqa: E501
        :type: float
        """

        self._setting = setting

    @property
    def setting_no(self):
        """Gets the setting_no of this UpdateValveDto.  # noqa: E501


        :return: The setting_no of this UpdateValveDto.  # noqa: E501
        :rtype: WdValveSettingNo
        """
        return self._setting_no

    @setting_no.setter
    def setting_no(self, setting_no):
        """Sets the setting_no of this UpdateValveDto.


        :param setting_no: The setting_no of this UpdateValveDto.  # noqa: E501
        :type: WdValveSettingNo
        """

        self._setting_no = setting_no

    @property
    def valve_type(self):
        """Gets the valve_type of this UpdateValveDto.  # noqa: E501


        :return: The valve_type of this UpdateValveDto.  # noqa: E501
        :rtype: WdValveTypeNo
        """
        return self._valve_type

    @valve_type.setter
    def valve_type(self, valve_type):
        """Sets the valve_type of this UpdateValveDto.


        :param valve_type: The valve_type of this UpdateValveDto.  # noqa: E501
        :type: WdValveTypeNo
        """

        self._valve_type = valve_type

    @property
    def valve_status(self):
        """Gets the valve_status of this UpdateValveDto.  # noqa: E501


        :return: The valve_status of this UpdateValveDto.  # noqa: E501
        :rtype: WdValveStatusNo
        """
        return self._valve_status

    @valve_status.setter
    def valve_status(self, valve_status):
        """Sets the valve_status of this UpdateValveDto.


        :param valve_status: The valve_status of this UpdateValveDto.  # noqa: E501
        :type: WdValveStatusNo
        """

        self._valve_status = valve_status

    @property
    def geom_wkt(self):
        """Gets the geom_wkt of this UpdateValveDto.  # noqa: E501

        阀门空间信息 valve geometry in wkt format  # noqa: E501

        :return: The geom_wkt of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._geom_wkt

    @geom_wkt.setter
    def geom_wkt(self, geom_wkt):
        """Sets the geom_wkt of this UpdateValveDto.

        阀门空间信息 valve geometry in wkt format  # noqa: E501

        :param geom_wkt: The geom_wkt of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._geom_wkt = geom_wkt

    @property
    def to_y(self):
        """Gets the to_y of this UpdateValveDto.  # noqa: E501

        终止节点坐标值Y coordinate y of to-node  # noqa: E501

        :return: The to_y of this UpdateValveDto.  # noqa: E501
        :rtype: float
        """
        return self._to_y

    @to_y.setter
    def to_y(self, to_y):
        """Sets the to_y of this UpdateValveDto.

        终止节点坐标值Y coordinate y of to-node  # noqa: E501

        :param to_y: The to_y of this UpdateValveDto.  # noqa: E501
        :type: float
        """

        self._to_y = to_y

    @property
    def to_x(self):
        """Gets the to_x of this UpdateValveDto.  # noqa: E501

        终止节点坐标值X coordinate x of to-node  # noqa: E501

        :return: The to_x of this UpdateValveDto.  # noqa: E501
        :rtype: float
        """
        return self._to_x

    @to_x.setter
    def to_x(self, to_x):
        """Sets the to_x of this UpdateValveDto.

        终止节点坐标值X coordinate x of to-node  # noqa: E501

        :param to_x: The to_x of this UpdateValveDto.  # noqa: E501
        :type: float
        """

        self._to_x = to_x

    @property
    def from_y(self):
        """Gets the from_y of this UpdateValveDto.  # noqa: E501

        起始节点坐标值Y coordinate y of from-node  # noqa: E501

        :return: The from_y of this UpdateValveDto.  # noqa: E501
        :rtype: float
        """
        return self._from_y

    @from_y.setter
    def from_y(self, from_y):
        """Sets the from_y of this UpdateValveDto.

        起始节点坐标值Y coordinate y of from-node  # noqa: E501

        :param from_y: The from_y of this UpdateValveDto.  # noqa: E501
        :type: float
        """

        self._from_y = from_y

    @property
    def from_x(self):
        """Gets the from_x of this UpdateValveDto.  # noqa: E501

        起始节点坐标值X coordinate x of from-node  # noqa: E501

        :return: The from_x of this UpdateValveDto.  # noqa: E501
        :rtype: float
        """
        return self._from_x

    @from_x.setter
    def from_x(self, from_x):
        """Sets the from_x of this UpdateValveDto.

        起始节点坐标值X coordinate x of from-node  # noqa: E501

        :param from_x: The from_x of this UpdateValveDto.  # noqa: E501
        :type: float
        """

        self._from_x = from_x

    @property
    def coor_str(self):
        """Gets the coor_str of this UpdateValveDto.  # noqa: E501

        坐标信息 coordinate  # noqa: E501

        :return: The coor_str of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._coor_str

    @coor_str.setter
    def coor_str(self, coor_str):
        """Sets the coor_str of this UpdateValveDto.

        坐标信息 coordinate  # noqa: E501

        :param coor_str: The coor_str of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._coor_str = coor_str

    @property
    def street_name(self):
        """Gets the street_name of this UpdateValveDto.  # noqa: E501

        街道名称 street name  # noqa: E501

        :return: The street_name of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this UpdateValveDto.

        街道名称 street name  # noqa: E501

        :param street_name: The street_name of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def description(self):
        """Gets the description of this UpdateValveDto.  # noqa: E501

        描述 description  # noqa: E501

        :return: The description of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateValveDto.

        描述 description  # noqa: E501

        :param description: The description of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def note(self):
        """Gets the note of this UpdateValveDto.  # noqa: E501

        备注 note  # noqa: E501

        :return: The note of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this UpdateValveDto.

        备注 note  # noqa: E501

        :param note: The note of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def data_source(self):
        """Gets the data_source of this UpdateValveDto.  # noqa: E501

        数据源 data source  # noqa: E501

        :return: The data_source of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this UpdateValveDto.

        数据源 data source  # noqa: E501

        :param data_source: The data_source of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._data_source = data_source

    @property
    def zone_id(self):
        """Gets the zone_id of this UpdateValveDto.  # noqa: E501

        分区ID zone id  # noqa: E501

        :return: The zone_id of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this UpdateValveDto.

        分区ID zone id  # noqa: E501

        :param zone_id: The zone_id of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def loss_coeff(self):
        """Gets the loss_coeff of this UpdateValveDto.  # noqa: E501

        损失系数 loss coefficient  # noqa: E501

        :return: The loss_coeff of this UpdateValveDto.  # noqa: E501
        :rtype: float
        """
        return self._loss_coeff

    @loss_coeff.setter
    def loss_coeff(self, loss_coeff):
        """Sets the loss_coeff of this UpdateValveDto.

        损失系数 loss coefficient  # noqa: E501

        :param loss_coeff: The loss_coeff of this UpdateValveDto.  # noqa: E501
        :type: float
        """

        self._loss_coeff = loss_coeff

    @property
    def diameter(self):
        """Gets the diameter of this UpdateValveDto.  # noqa: E501

        直径 diameter  # noqa: E501

        :return: The diameter of this UpdateValveDto.  # noqa: E501
        :rtype: float
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this UpdateValveDto.

        直径 diameter  # noqa: E501

        :param diameter: The diameter of this UpdateValveDto.  # noqa: E501
        :type: float
        """

        self._diameter = diameter

    @property
    def to_node(self):
        """Gets the to_node of this UpdateValveDto.  # noqa: E501

        终止节点 to node  # noqa: E501

        :return: The to_node of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._to_node

    @to_node.setter
    def to_node(self, to_node):
        """Sets the to_node of this UpdateValveDto.

        终止节点 to node  # noqa: E501

        :param to_node: The to_node of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._to_node = to_node

    @property
    def from_node(self):
        """Gets the from_node of this UpdateValveDto.  # noqa: E501

        起始节点 from node  # noqa: E501

        :return: The from_node of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._from_node

    @from_node.setter
    def from_node(self, from_node):
        """Sets the from_node of this UpdateValveDto.

        起始节点 from node  # noqa: E501

        :param from_node: The from_node of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._from_node = from_node

    @property
    def oper_curve_id(self):
        """Gets the oper_curve_id of this UpdateValveDto.  # noqa: E501

        调度曲线ID operation schedule curve id  # noqa: E501

        :return: The oper_curve_id of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._oper_curve_id

    @oper_curve_id.setter
    def oper_curve_id(self, oper_curve_id):
        """Sets the oper_curve_id of this UpdateValveDto.

        调度曲线ID operation schedule curve id  # noqa: E501

        :param oper_curve_id: The oper_curve_id of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._oper_curve_id = oper_curve_id

    @property
    def valve_curve_id(self):
        """Gets the valve_curve_id of this UpdateValveDto.  # noqa: E501

        阀门曲线ID valve characteristic curve id  # noqa: E501

        :return: The valve_curve_id of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._valve_curve_id

    @valve_curve_id.setter
    def valve_curve_id(self, valve_curve_id):
        """Sets the valve_curve_id of this UpdateValveDto.

        阀门曲线ID valve characteristic curve id  # noqa: E501

        :param valve_curve_id: The valve_curve_id of this UpdateValveDto.  # noqa: E501
        :type: str
        """

        self._valve_curve_id = valve_curve_id

    @property
    def create_time(self):
        """Gets the create_time of this UpdateValveDto.  # noqa: E501

        创建时间 create time  # noqa: E501

        :return: The create_time of this UpdateValveDto.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateValveDto.

        创建时间 create time  # noqa: E501

        :param create_time: The create_time of this UpdateValveDto.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this UpdateValveDto.  # noqa: E501

        阀门ID valve id  # noqa: E501

        :return: The id of this UpdateValveDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateValveDto.

        阀门ID valve id  # noqa: E501

        :param id: The id of this UpdateValveDto.  # noqa: E501
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
        if not isinstance(other, UpdateValveDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateValveDto):
            return True

        return self.to_dict() != other.to_dict()
