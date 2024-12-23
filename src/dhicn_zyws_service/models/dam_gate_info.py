# coding: utf-8

"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_zyws_service.configuration import Configuration


class DamGateInfo(object):
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
        'sort': 'int',
        'dam_gate_code': 'str',
        'dam_gate_name': 'str',
        'dam_gate_width': 'float',
        'status': 'str',
        'is_scheduling': 'bool',
        'tag_weir_height': 'float',
        'orifice_calibration_width': 'float',
        'opening': 'float'
    }

    attribute_map = {
        'id': 'id',
        'sort': 'sort',
        'dam_gate_code': 'damGateCode',
        'dam_gate_name': 'damGateName',
        'dam_gate_width': 'damGateWidth',
        'status': 'status',
        'is_scheduling': 'isScheduling',
        'tag_weir_height': 'tagWeirHeight',
        'orifice_calibration_width': 'orificeCalibrationWidth',
        'opening': 'opening'
    }

    def __init__(self, id=None, sort=None, dam_gate_code=None, dam_gate_name=None, dam_gate_width=None, status=None, is_scheduling=None, tag_weir_height=None, orifice_calibration_width=None, opening=None, local_vars_configuration=None):  # noqa: E501
        """DamGateInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._sort = None
        self._dam_gate_code = None
        self._dam_gate_name = None
        self._dam_gate_width = None
        self._status = None
        self._is_scheduling = None
        self._tag_weir_height = None
        self._orifice_calibration_width = None
        self._opening = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sort is not None:
            self.sort = sort
        self.dam_gate_code = dam_gate_code
        self.dam_gate_name = dam_gate_name
        if dam_gate_width is not None:
            self.dam_gate_width = dam_gate_width
        self.status = status
        if is_scheduling is not None:
            self.is_scheduling = is_scheduling
        self.tag_weir_height = tag_weir_height
        if orifice_calibration_width is not None:
            self.orifice_calibration_width = orifice_calibration_width
        if opening is not None:
            self.opening = opening

    @property
    def id(self):
        """Gets the id of this DamGateInfo.  # noqa: E501

        堰门ID  # noqa: E501

        :return: The id of this DamGateInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DamGateInfo.

        堰门ID  # noqa: E501

        :param id: The id of this DamGateInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sort(self):
        """Gets the sort of this DamGateInfo.  # noqa: E501

        开堰顺序  # noqa: E501

        :return: The sort of this DamGateInfo.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this DamGateInfo.

        开堰顺序  # noqa: E501

        :param sort: The sort of this DamGateInfo.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def dam_gate_code(self):
        """Gets the dam_gate_code of this DamGateInfo.  # noqa: E501

        堰门编码  # noqa: E501

        :return: The dam_gate_code of this DamGateInfo.  # noqa: E501
        :rtype: str
        """
        return self._dam_gate_code

    @dam_gate_code.setter
    def dam_gate_code(self, dam_gate_code):
        """Sets the dam_gate_code of this DamGateInfo.

        堰门编码  # noqa: E501

        :param dam_gate_code: The dam_gate_code of this DamGateInfo.  # noqa: E501
        :type: str
        """

        self._dam_gate_code = dam_gate_code

    @property
    def dam_gate_name(self):
        """Gets the dam_gate_name of this DamGateInfo.  # noqa: E501

        堰门名称  # noqa: E501

        :return: The dam_gate_name of this DamGateInfo.  # noqa: E501
        :rtype: str
        """
        return self._dam_gate_name

    @dam_gate_name.setter
    def dam_gate_name(self, dam_gate_name):
        """Sets the dam_gate_name of this DamGateInfo.

        堰门名称  # noqa: E501

        :param dam_gate_name: The dam_gate_name of this DamGateInfo.  # noqa: E501
        :type: str
        """

        self._dam_gate_name = dam_gate_name

    @property
    def dam_gate_width(self):
        """Gets the dam_gate_width of this DamGateInfo.  # noqa: E501

        堰门宽度  # noqa: E501

        :return: The dam_gate_width of this DamGateInfo.  # noqa: E501
        :rtype: float
        """
        return self._dam_gate_width

    @dam_gate_width.setter
    def dam_gate_width(self, dam_gate_width):
        """Sets the dam_gate_width of this DamGateInfo.

        堰门宽度  # noqa: E501

        :param dam_gate_width: The dam_gate_width of this DamGateInfo.  # noqa: E501
        :type: float
        """

        self._dam_gate_width = dam_gate_width

    @property
    def status(self):
        """Gets the status of this DamGateInfo.  # noqa: E501

        堰门状态  # noqa: E501

        :return: The status of this DamGateInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DamGateInfo.

        堰门状态  # noqa: E501

        :param status: The status of this DamGateInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def is_scheduling(self):
        """Gets the is_scheduling of this DamGateInfo.  # noqa: E501

        堰门是否可被调度  # noqa: E501

        :return: The is_scheduling of this DamGateInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_scheduling

    @is_scheduling.setter
    def is_scheduling(self, is_scheduling):
        """Sets the is_scheduling of this DamGateInfo.

        堰门是否可被调度  # noqa: E501

        :param is_scheduling: The is_scheduling of this DamGateInfo.  # noqa: E501
        :type: bool
        """

        self._is_scheduling = is_scheduling

    @property
    def tag_weir_height(self):
        """Gets the tag_weir_height of this DamGateInfo.  # noqa: E501

        人工表达堰高  # noqa: E501

        :return: The tag_weir_height of this DamGateInfo.  # noqa: E501
        :rtype: float
        """
        return self._tag_weir_height

    @tag_weir_height.setter
    def tag_weir_height(self, tag_weir_height):
        """Sets the tag_weir_height of this DamGateInfo.

        人工表达堰高  # noqa: E501

        :param tag_weir_height: The tag_weir_height of this DamGateInfo.  # noqa: E501
        :type: float
        """

        self._tag_weir_height = tag_weir_height

    @property
    def orifice_calibration_width(self):
        """Gets the orifice_calibration_width of this DamGateInfo.  # noqa: E501

        堰门率定宽度  # noqa: E501

        :return: The orifice_calibration_width of this DamGateInfo.  # noqa: E501
        :rtype: float
        """
        return self._orifice_calibration_width

    @orifice_calibration_width.setter
    def orifice_calibration_width(self, orifice_calibration_width):
        """Sets the orifice_calibration_width of this DamGateInfo.

        堰门率定宽度  # noqa: E501

        :param orifice_calibration_width: The orifice_calibration_width of this DamGateInfo.  # noqa: E501
        :type: float
        """

        self._orifice_calibration_width = orifice_calibration_width

    @property
    def opening(self):
        """Gets the opening of this DamGateInfo.  # noqa: E501

        开度  # noqa: E501

        :return: The opening of this DamGateInfo.  # noqa: E501
        :rtype: float
        """
        return self._opening

    @opening.setter
    def opening(self, opening):
        """Sets the opening of this DamGateInfo.

        开度  # noqa: E501

        :param opening: The opening of this DamGateInfo.  # noqa: E501
        :type: float
        """

        self._opening = opening

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
        if not isinstance(other, DamGateInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DamGateInfo):
            return True

        return self.to_dict() != other.to_dict()
