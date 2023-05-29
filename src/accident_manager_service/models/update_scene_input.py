# coding: utf-8

"""
    accident-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from accident_manager_service.configuration import Configuration


class UpdateSceneInput(object):
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
        'name': 'str',
        'remark': 'str',
        'scenario_id': 'str',
        'data_source': 'str',
        'operator': 'str',
        'operate_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark',
        'scenario_id': 'scenarioId',
        'data_source': 'dataSource',
        'operator': 'operator',
        'operate_time': 'operateTime'
    }

    def __init__(self, id=None, name=None, remark=None, scenario_id=None, data_source=None, operator=None, operate_time=None, local_vars_configuration=None):  # noqa: E501
        """UpdateSceneInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._remark = None
        self._scenario_id = None
        self._data_source = None
        self._operator = None
        self._operate_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.remark = remark
        self.scenario_id = scenario_id
        self.data_source = data_source
        self.operator = operator
        self.operate_time = operate_time

    @property
    def id(self):
        """Gets the id of this UpdateSceneInput.  # noqa: E501

        情景ID scene id  # noqa: E501

        :return: The id of this UpdateSceneInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateSceneInput.

        情景ID scene id  # noqa: E501

        :param id: The id of this UpdateSceneInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateSceneInput.  # noqa: E501

        情景名称 scene name  # noqa: E501

        :return: The name of this UpdateSceneInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSceneInput.

        情景名称 scene name  # noqa: E501

        :param name: The name of this UpdateSceneInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def remark(self):
        """Gets the remark of this UpdateSceneInput.  # noqa: E501

        情景备注 scene remark  # noqa: E501

        :return: The remark of this UpdateSceneInput.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this UpdateSceneInput.

        情景备注 scene remark  # noqa: E501

        :param remark: The remark of this UpdateSceneInput.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def scenario_id(self):
        """Gets the scenario_id of this UpdateSceneInput.  # noqa: E501

        对应的方案ID corresponding scenario id  # noqa: E501

        :return: The scenario_id of this UpdateSceneInput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this UpdateSceneInput.

        对应的方案ID corresponding scenario id  # noqa: E501

        :param scenario_id: The scenario_id of this UpdateSceneInput.  # noqa: E501
        :type: str
        """

        self._scenario_id = scenario_id

    @property
    def data_source(self):
        """Gets the data_source of this UpdateSceneInput.  # noqa: E501

        数据源 data source  # noqa: E501

        :return: The data_source of this UpdateSceneInput.  # noqa: E501
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this UpdateSceneInput.

        数据源 data source  # noqa: E501

        :param data_source: The data_source of this UpdateSceneInput.  # noqa: E501
        :type: str
        """

        self._data_source = data_source

    @property
    def operator(self):
        """Gets the operator of this UpdateSceneInput.  # noqa: E501

        操作人员 operator  # noqa: E501

        :return: The operator of this UpdateSceneInput.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this UpdateSceneInput.

        操作人员 operator  # noqa: E501

        :param operator: The operator of this UpdateSceneInput.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def operate_time(self):
        """Gets the operate_time of this UpdateSceneInput.  # noqa: E501

        操作时间 operate time  # noqa: E501

        :return: The operate_time of this UpdateSceneInput.  # noqa: E501
        :rtype: datetime
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this UpdateSceneInput.

        操作时间 operate time  # noqa: E501

        :param operate_time: The operate_time of this UpdateSceneInput.  # noqa: E501
        :type: datetime
        """

        self._operate_time = operate_time

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
        if not isinstance(other, UpdateSceneInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSceneInput):
            return True

        return self.to_dict() != other.to_dict()
