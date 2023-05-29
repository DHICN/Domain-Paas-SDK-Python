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


class AddPipeDto(object):
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
        'from_node': 'str',
        'to_node': 'str',
        'length': 'float',
        'diameter': 'float',
        'thickness': 'float',
        'pipe_status': 'int',
        'zone_id': 'str',
        'roughness': 'float',
        'loss_coeff': 'float',
        'material': 'str',
        'construction_year': 'datetime',
        'description': 'str',
        'data_source': 'str',
        'asset_name': 'str',
        'street_name': 'str',
        'from_x': 'float',
        'from_y': 'float',
        'to_x': 'float',
        'to_y': 'float',
        'operate': 'OperateEnum'
    }

    attribute_map = {
        'muid': 'muid',
        'from_node': 'fromNode',
        'to_node': 'toNode',
        'length': 'length',
        'diameter': 'diameter',
        'thickness': 'thickness',
        'pipe_status': 'pipeStatus',
        'zone_id': 'zoneID',
        'roughness': 'roughness',
        'loss_coeff': 'lossCoeff',
        'material': 'material',
        'construction_year': 'constructionYear',
        'description': 'description',
        'data_source': 'dataSource',
        'asset_name': 'assetName',
        'street_name': 'streetName',
        'from_x': 'fromX',
        'from_y': 'fromY',
        'to_x': 'toX',
        'to_y': 'toY',
        'operate': 'operate'
    }

    def __init__(self, muid=None, from_node=None, to_node=None, length=None, diameter=None, thickness=None, pipe_status=None, zone_id=None, roughness=None, loss_coeff=None, material=None, construction_year=None, description=None, data_source=None, asset_name=None, street_name=None, from_x=None, from_y=None, to_x=None, to_y=None, operate=None, local_vars_configuration=None):  # noqa: E501
        """AddPipeDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._muid = None
        self._from_node = None
        self._to_node = None
        self._length = None
        self._diameter = None
        self._thickness = None
        self._pipe_status = None
        self._zone_id = None
        self._roughness = None
        self._loss_coeff = None
        self._material = None
        self._construction_year = None
        self._description = None
        self._data_source = None
        self._asset_name = None
        self._street_name = None
        self._from_x = None
        self._from_y = None
        self._to_x = None
        self._to_y = None
        self._operate = None
        self.discriminator = None

        self.muid = muid
        self.from_node = from_node
        self.to_node = to_node
        if length is not None:
            self.length = length
        if diameter is not None:
            self.diameter = diameter
        if thickness is not None:
            self.thickness = thickness
        if pipe_status is not None:
            self.pipe_status = pipe_status
        self.zone_id = zone_id
        if roughness is not None:
            self.roughness = roughness
        if loss_coeff is not None:
            self.loss_coeff = loss_coeff
        self.material = material
        if construction_year is not None:
            self.construction_year = construction_year
        self.description = description
        self.data_source = data_source
        self.asset_name = asset_name
        self.street_name = street_name
        if from_x is not None:
            self.from_x = from_x
        if from_y is not None:
            self.from_y = from_y
        if to_x is not None:
            self.to_x = to_x
        if to_y is not None:
            self.to_y = to_y
        if operate is not None:
            self.operate = operate

    @property
    def muid(self):
        """Gets the muid of this AddPipeDto.  # noqa: E501

        模型中管段ID pipe muid  # noqa: E501

        :return: The muid of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._muid

    @muid.setter
    def muid(self, muid):
        """Sets the muid of this AddPipeDto.

        模型中管段ID pipe muid  # noqa: E501

        :param muid: The muid of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._muid = muid

    @property
    def from_node(self):
        """Gets the from_node of this AddPipeDto.  # noqa: E501

        起始节点 from node  # noqa: E501

        :return: The from_node of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._from_node

    @from_node.setter
    def from_node(self, from_node):
        """Sets the from_node of this AddPipeDto.

        起始节点 from node  # noqa: E501

        :param from_node: The from_node of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._from_node = from_node

    @property
    def to_node(self):
        """Gets the to_node of this AddPipeDto.  # noqa: E501

        终止节点 to node  # noqa: E501

        :return: The to_node of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._to_node

    @to_node.setter
    def to_node(self, to_node):
        """Sets the to_node of this AddPipeDto.

        终止节点 to node  # noqa: E501

        :param to_node: The to_node of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._to_node = to_node

    @property
    def length(self):
        """Gets the length of this AddPipeDto.  # noqa: E501

        管长 pipe length  # noqa: E501

        :return: The length of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this AddPipeDto.

        管长 pipe length  # noqa: E501

        :param length: The length of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def diameter(self):
        """Gets the diameter of this AddPipeDto.  # noqa: E501

        管径 pipe diameter  # noqa: E501

        :return: The diameter of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this AddPipeDto.

        管径 pipe diameter  # noqa: E501

        :param diameter: The diameter of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._diameter = diameter

    @property
    def thickness(self):
        """Gets the thickness of this AddPipeDto.  # noqa: E501

        管壁厚度 pipe wall thickness  # noqa: E501

        :return: The thickness of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._thickness

    @thickness.setter
    def thickness(self, thickness):
        """Sets the thickness of this AddPipeDto.

        管壁厚度 pipe wall thickness  # noqa: E501

        :param thickness: The thickness of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._thickness = thickness

    @property
    def pipe_status(self):
        """Gets the pipe_status of this AddPipeDto.  # noqa: E501

        管道状态 pipe status  # noqa: E501

        :return: The pipe_status of this AddPipeDto.  # noqa: E501
        :rtype: int
        """
        return self._pipe_status

    @pipe_status.setter
    def pipe_status(self, pipe_status):
        """Sets the pipe_status of this AddPipeDto.

        管道状态 pipe status  # noqa: E501

        :param pipe_status: The pipe_status of this AddPipeDto.  # noqa: E501
        :type: int
        """

        self._pipe_status = pipe_status

    @property
    def zone_id(self):
        """Gets the zone_id of this AddPipeDto.  # noqa: E501

        分区ID zone id  # noqa: E501

        :return: The zone_id of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this AddPipeDto.

        分区ID zone id  # noqa: E501

        :param zone_id: The zone_id of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def roughness(self):
        """Gets the roughness of this AddPipeDto.  # noqa: E501

        粗糙度 pipe roughness  # noqa: E501

        :return: The roughness of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._roughness

    @roughness.setter
    def roughness(self, roughness):
        """Sets the roughness of this AddPipeDto.

        粗糙度 pipe roughness  # noqa: E501

        :param roughness: The roughness of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._roughness = roughness

    @property
    def loss_coeff(self):
        """Gets the loss_coeff of this AddPipeDto.  # noqa: E501

        损失系数 loss coefficient  # noqa: E501

        :return: The loss_coeff of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._loss_coeff

    @loss_coeff.setter
    def loss_coeff(self, loss_coeff):
        """Sets the loss_coeff of this AddPipeDto.

        损失系数 loss coefficient  # noqa: E501

        :param loss_coeff: The loss_coeff of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._loss_coeff = loss_coeff

    @property
    def material(self):
        """Gets the material of this AddPipeDto.  # noqa: E501

        管材 pipe material  # noqa: E501

        :return: The material of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._material

    @material.setter
    def material(self, material):
        """Sets the material of this AddPipeDto.

        管材 pipe material  # noqa: E501

        :param material: The material of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._material = material

    @property
    def construction_year(self):
        """Gets the construction_year of this AddPipeDto.  # noqa: E501

        建设时间 construction time  # noqa: E501

        :return: The construction_year of this AddPipeDto.  # noqa: E501
        :rtype: datetime
        """
        return self._construction_year

    @construction_year.setter
    def construction_year(self, construction_year):
        """Sets the construction_year of this AddPipeDto.

        建设时间 construction time  # noqa: E501

        :param construction_year: The construction_year of this AddPipeDto.  # noqa: E501
        :type: datetime
        """

        self._construction_year = construction_year

    @property
    def description(self):
        """Gets the description of this AddPipeDto.  # noqa: E501

        描述 description  # noqa: E501

        :return: The description of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddPipeDto.

        描述 description  # noqa: E501

        :param description: The description of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def data_source(self):
        """Gets the data_source of this AddPipeDto.  # noqa: E501

        数据源 data source  # noqa: E501

        :return: The data_source of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this AddPipeDto.

        数据源 data source  # noqa: E501

        :param data_source: The data_source of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._data_source = data_source

    @property
    def asset_name(self):
        """Gets the asset_name of this AddPipeDto.  # noqa: E501

        资产名称 asset name  # noqa: E501

        :return: The asset_name of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this AddPipeDto.

        资产名称 asset name  # noqa: E501

        :param asset_name: The asset_name of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def street_name(self):
        """Gets the street_name of this AddPipeDto.  # noqa: E501

        街道名称 street name  # noqa: E501

        :return: The street_name of this AddPipeDto.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this AddPipeDto.

        街道名称 street name  # noqa: E501

        :param street_name: The street_name of this AddPipeDto.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def from_x(self):
        """Gets the from_x of this AddPipeDto.  # noqa: E501

        起始节点坐标X coordinate x of from-node  # noqa: E501

        :return: The from_x of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._from_x

    @from_x.setter
    def from_x(self, from_x):
        """Sets the from_x of this AddPipeDto.

        起始节点坐标X coordinate x of from-node  # noqa: E501

        :param from_x: The from_x of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._from_x = from_x

    @property
    def from_y(self):
        """Gets the from_y of this AddPipeDto.  # noqa: E501

        起始节点坐标Y coordinate y of from-node  # noqa: E501

        :return: The from_y of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._from_y

    @from_y.setter
    def from_y(self, from_y):
        """Sets the from_y of this AddPipeDto.

        起始节点坐标Y coordinate y of from-node  # noqa: E501

        :param from_y: The from_y of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._from_y = from_y

    @property
    def to_x(self):
        """Gets the to_x of this AddPipeDto.  # noqa: E501

        终止节点坐标X coordinate x of to-node  # noqa: E501

        :return: The to_x of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._to_x

    @to_x.setter
    def to_x(self, to_x):
        """Sets the to_x of this AddPipeDto.

        终止节点坐标X coordinate x of to-node  # noqa: E501

        :param to_x: The to_x of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._to_x = to_x

    @property
    def to_y(self):
        """Gets the to_y of this AddPipeDto.  # noqa: E501

        终止节点坐标Y coordinate y of to-node  # noqa: E501

        :return: The to_y of this AddPipeDto.  # noqa: E501
        :rtype: float
        """
        return self._to_y

    @to_y.setter
    def to_y(self, to_y):
        """Sets the to_y of this AddPipeDto.

        终止节点坐标Y coordinate y of to-node  # noqa: E501

        :param to_y: The to_y of this AddPipeDto.  # noqa: E501
        :type: float
        """

        self._to_y = to_y

    @property
    def operate(self):
        """Gets the operate of this AddPipeDto.  # noqa: E501


        :return: The operate of this AddPipeDto.  # noqa: E501
        :rtype: OperateEnum
        """
        return self._operate

    @operate.setter
    def operate(self, operate):
        """Sets the operate of this AddPipeDto.


        :param operate: The operate of this AddPipeDto.  # noqa: E501
        :type: OperateEnum
        """

        self._operate = operate

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
        if not isinstance(other, AddPipeDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddPipeDto):
            return True

        return self.to_dict() != other.to_dict()
