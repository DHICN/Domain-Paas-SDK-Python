# coding: utf-8

"""
    digital-twin-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from digital_twin_service.configuration import Configuration


class QueryModelPointByTypeInput(object):
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
        'template_scenario_id': 'str',
        'model_ids': 'list[str]',
        'model_point_type': 'str',
        'attributes': 'list[str]'
    }

    attribute_map = {
        'template_scenario_id': 'templateScenarioId',
        'model_ids': 'modelIds',
        'model_point_type': 'modelPointType',
        'attributes': 'attributes'
    }

    def __init__(self, template_scenario_id=None, model_ids=None, model_point_type=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """QueryModelPointByTypeInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._template_scenario_id = None
        self._model_ids = None
        self._model_point_type = None
        self._attributes = None
        self.discriminator = None

        self.template_scenario_id = template_scenario_id
        self.model_ids = model_ids
        self.model_point_type = model_point_type
        self.attributes = attributes

    @property
    def template_scenario_id(self):
        """Gets the template_scenario_id of this QueryModelPointByTypeInput.  # noqa: E501

        模板方案ID template scenario id  # noqa: E501

        :return: The template_scenario_id of this QueryModelPointByTypeInput.  # noqa: E501
        :rtype: str
        """
        return self._template_scenario_id

    @template_scenario_id.setter
    def template_scenario_id(self, template_scenario_id):
        """Sets the template_scenario_id of this QueryModelPointByTypeInput.

        模板方案ID template scenario id  # noqa: E501

        :param template_scenario_id: The template_scenario_id of this QueryModelPointByTypeInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template_scenario_id is None:  # noqa: E501
            raise ValueError("Invalid value for `template_scenario_id`, must not be `None`")  # noqa: E501

        self._template_scenario_id = template_scenario_id

    @property
    def model_ids(self):
        """Gets the model_ids of this QueryModelPointByTypeInput.  # noqa: E501

        模型中的ID列表，可为空 model muid list, can be empty  # noqa: E501

        :return: The model_ids of this QueryModelPointByTypeInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        """Sets the model_ids of this QueryModelPointByTypeInput.

        模型中的ID列表，可为空 model muid list, can be empty  # noqa: E501

        :param model_ids: The model_ids of this QueryModelPointByTypeInput.  # noqa: E501
        :type: list[str]
        """

        self._model_ids = model_ids

    @property
    def model_point_type(self):
        """Gets the model_point_type of this QueryModelPointByTypeInput.  # noqa: E501

        模型点位类型 model point type  # noqa: E501

        :return: The model_point_type of this QueryModelPointByTypeInput.  # noqa: E501
        :rtype: str
        """
        return self._model_point_type

    @model_point_type.setter
    def model_point_type(self, model_point_type):
        """Sets the model_point_type of this QueryModelPointByTypeInput.

        模型点位类型 model point type  # noqa: E501

        :param model_point_type: The model_point_type of this QueryModelPointByTypeInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model_point_type is None:  # noqa: E501
            raise ValueError("Invalid value for `model_point_type`, must not be `None`")  # noqa: E501

        self._model_point_type = model_point_type

    @property
    def attributes(self):
        """Gets the attributes of this QueryModelPointByTypeInput.  # noqa: E501

        要获取的模型点位的属性列表，为空代表所有属性都要获取。A list of attributes for the model point to retrieve; empty means all attributes should be retrieved  # noqa: E501

        :return: The attributes of this QueryModelPointByTypeInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this QueryModelPointByTypeInput.

        要获取的模型点位的属性列表，为空代表所有属性都要获取。A list of attributes for the model point to retrieve; empty means all attributes should be retrieved  # noqa: E501

        :param attributes: The attributes of this QueryModelPointByTypeInput.  # noqa: E501
        :type: list[str]
        """

        self._attributes = attributes

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
        if not isinstance(other, QueryModelPointByTypeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryModelPointByTypeInput):
            return True

        return self.to_dict() != other.to_dict()
