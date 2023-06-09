# coding: utf-8

"""
    identity-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_identity_service.configuration import Configuration


class ModelPrecisionConfigsDto(object):
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
        'region_name': 'str',
        'rec_probability': 'str',
        'region_s_value': 'float',
        'region_e_value': 'float',
        'sort': 'int',
        'code': 'str',
        'id': 'str',
        'unit': 'str',
        'rec_probability_s_value': 'float',
        'rec_probability_e_value': 'float',
        'score': 'float',
        'level_code': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'region_name': 'regionName',
        'rec_probability': 'recProbability',
        'region_s_value': 'regionSValue',
        'region_e_value': 'regionEValue',
        'sort': 'sort',
        'code': 'code',
        'id': 'id',
        'unit': 'unit',
        'rec_probability_s_value': 'recProbabilitySValue',
        'rec_probability_e_value': 'recProbabilityEValue',
        'score': 'score',
        'level_code': 'levelCode',
        'remark': 'remark'
    }

    def __init__(self, region_name=None, rec_probability=None, region_s_value=None, region_e_value=None, sort=None, code=None, id=None, unit=None, rec_probability_s_value=None, rec_probability_e_value=None, score=None, level_code=None, remark=None, local_vars_configuration=None):  # noqa: E501
        """ModelPrecisionConfigsDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._region_name = None
        self._rec_probability = None
        self._region_s_value = None
        self._region_e_value = None
        self._sort = None
        self._code = None
        self._id = None
        self._unit = None
        self._rec_probability_s_value = None
        self._rec_probability_e_value = None
        self._score = None
        self._level_code = None
        self._remark = None
        self.discriminator = None

        self.region_name = region_name
        self.rec_probability = rec_probability
        if region_s_value is not None:
            self.region_s_value = region_s_value
        if region_e_value is not None:
            self.region_e_value = region_e_value
        if sort is not None:
            self.sort = sort
        self.code = code
        if id is not None:
            self.id = id
        self.unit = unit
        if rec_probability_s_value is not None:
            self.rec_probability_s_value = rec_probability_s_value
        if rec_probability_e_value is not None:
            self.rec_probability_e_value = rec_probability_e_value
        if score is not None:
            self.score = score
        self.level_code = level_code
        self.remark = remark

    @property
    def region_name(self):
        """Gets the region_name of this ModelPrecisionConfigsDto.  # noqa: E501

        百分比区间名称,如:80-100(优秀) precision region name  # noqa: E501

        :return: The region_name of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ModelPrecisionConfigsDto.

        百分比区间名称,如:80-100(优秀) precision region name  # noqa: E501

        :param region_name: The region_name of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def rec_probability(self):
        """Gets the rec_probability of this ModelPrecisionConfigsDto.  # noqa: E501

        百分比区间推荐:如:>70 precison region recommended proportion  # noqa: E501

        :return: The rec_probability of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: str
        """
        return self._rec_probability

    @rec_probability.setter
    def rec_probability(self, rec_probability):
        """Sets the rec_probability of this ModelPrecisionConfigsDto.

        百分比区间推荐:如:>70 precison region recommended proportion  # noqa: E501

        :param rec_probability: The rec_probability of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: str
        """

        self._rec_probability = rec_probability

    @property
    def region_s_value(self):
        """Gets the region_s_value of this ModelPrecisionConfigsDto.  # noqa: E501

        百分比区间开始,如:80 precision region start value  # noqa: E501

        :return: The region_s_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: float
        """
        return self._region_s_value

    @region_s_value.setter
    def region_s_value(self, region_s_value):
        """Sets the region_s_value of this ModelPrecisionConfigsDto.

        百分比区间开始,如:80 precision region start value  # noqa: E501

        :param region_s_value: The region_s_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: float
        """

        self._region_s_value = region_s_value

    @property
    def region_e_value(self):
        """Gets the region_e_value of this ModelPrecisionConfigsDto.  # noqa: E501

        百分比区间截止,如:100 precision region end value  # noqa: E501

        :return: The region_e_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: float
        """
        return self._region_e_value

    @region_e_value.setter
    def region_e_value(self, region_e_value):
        """Sets the region_e_value of this ModelPrecisionConfigsDto.

        百分比区间截止,如:100 precision region end value  # noqa: E501

        :param region_e_value: The region_e_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: float
        """

        self._region_e_value = region_e_value

    @property
    def sort(self):
        """Gets the sort of this ModelPrecisionConfigsDto.  # noqa: E501

        排序号,越小越靠前 precision region index  # noqa: E501

        :return: The sort of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ModelPrecisionConfigsDto.

        排序号,越小越靠前 precision region index  # noqa: E501

        :param sort: The sort of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def code(self):
        """Gets the code of this ModelPrecisionConfigsDto.  # noqa: E501

        指标 system point code  # noqa: E501

        :return: The code of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ModelPrecisionConfigsDto.

        指标 system point code  # noqa: E501

        :param code: The code of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def id(self):
        """Gets the id of this ModelPrecisionConfigsDto.  # noqa: E501

        配置ID config id  # noqa: E501

        :return: The id of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelPrecisionConfigsDto.

        配置ID config id  # noqa: E501

        :param id: The id of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def unit(self):
        """Gets the unit of this ModelPrecisionConfigsDto.  # noqa: E501

        单位 unit  # noqa: E501

        :return: The unit of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ModelPrecisionConfigsDto.

        单位 unit  # noqa: E501

        :param unit: The unit of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def rec_probability_s_value(self):
        """Gets the rec_probability_s_value of this ModelPrecisionConfigsDto.  # noqa: E501

        推荐概率最小值，如70 minimum recommended proportion  # noqa: E501

        :return: The rec_probability_s_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: float
        """
        return self._rec_probability_s_value

    @rec_probability_s_value.setter
    def rec_probability_s_value(self, rec_probability_s_value):
        """Sets the rec_probability_s_value of this ModelPrecisionConfigsDto.

        推荐概率最小值，如70 minimum recommended proportion  # noqa: E501

        :param rec_probability_s_value: The rec_probability_s_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: float
        """

        self._rec_probability_s_value = rec_probability_s_value

    @property
    def rec_probability_e_value(self):
        """Gets the rec_probability_e_value of this ModelPrecisionConfigsDto.  # noqa: E501

        推荐概率最大值，如100 maximum recommended proportion  # noqa: E501

        :return: The rec_probability_e_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: float
        """
        return self._rec_probability_e_value

    @rec_probability_e_value.setter
    def rec_probability_e_value(self, rec_probability_e_value):
        """Sets the rec_probability_e_value of this ModelPrecisionConfigsDto.

        推荐概率最大值，如100 maximum recommended proportion  # noqa: E501

        :param rec_probability_e_value: The rec_probability_e_value of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: float
        """

        self._rec_probability_e_value = rec_probability_e_value

    @property
    def score(self):
        """Gets the score of this ModelPrecisionConfigsDto.  # noqa: E501

        得分 score  # noqa: E501

        :return: The score of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ModelPrecisionConfigsDto.

        得分 score  # noqa: E501

        :param score: The score of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def level_code(self):
        """Gets the level_code of this ModelPrecisionConfigsDto.  # noqa: E501

        评价Code  # noqa: E501

        :return: The level_code of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: str
        """
        return self._level_code

    @level_code.setter
    def level_code(self, level_code):
        """Sets the level_code of this ModelPrecisionConfigsDto.

        评价Code  # noqa: E501

        :param level_code: The level_code of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: str
        """

        self._level_code = level_code

    @property
    def remark(self):
        """Gets the remark of this ModelPrecisionConfigsDto.  # noqa: E501

        总体评价 overall evaluation  # noqa: E501

        :return: The remark of this ModelPrecisionConfigsDto.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ModelPrecisionConfigsDto.

        总体评价 overall evaluation  # noqa: E501

        :param remark: The remark of this ModelPrecisionConfigsDto.  # noqa: E501
        :type: str
        """

        self._remark = remark

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
        if not isinstance(other, ModelPrecisionConfigsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelPrecisionConfigsDto):
            return True

        return self.to_dict() != other.to_dict()
