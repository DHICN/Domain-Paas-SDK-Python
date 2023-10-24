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

from dhicn_iot_service.configuration import Configuration


class AddModelPointsInput(object):
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
        'template_id': 'str',
        'model_type': 'str',
        'model_id': 'str',
        'model_point_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'template_id': 'templateId',
        'model_type': 'modelType',
        'model_id': 'modelId',
        'model_point_type': 'modelPointType',
        'name': 'name'
    }

    def __init__(self, template_id=None, model_type=None, model_id=None, model_point_type=None, name=None, local_vars_configuration=None):  # noqa: E501
        """AddModelPointsInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._template_id = None
        self._model_type = None
        self._model_id = None
        self._model_point_type = None
        self._name = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        self.model_type = model_type
        self.model_id = model_id
        self.model_point_type = model_point_type
        self.name = name

    @property
    def template_id(self):
        """Gets the template_id of this AddModelPointsInput.  # noqa: E501

        模板Id  # noqa: E501

        :return: The template_id of this AddModelPointsInput.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this AddModelPointsInput.

        模板Id  # noqa: E501

        :param template_id: The template_id of this AddModelPointsInput.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def model_type(self):
        """Gets the model_type of this AddModelPointsInput.  # noqa: E501

        模板类型，ModelTypeEnum 枚举  # noqa: E501

        :return: The model_type of this AddModelPointsInput.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this AddModelPointsInput.

        模板类型，ModelTypeEnum 枚举  # noqa: E501

        :param model_type: The model_type of this AddModelPointsInput.  # noqa: E501
        :type: str
        """

        self._model_type = model_type

    @property
    def model_id(self):
        """Gets the model_id of this AddModelPointsInput.  # noqa: E501

        模型点位里的 Id  # noqa: E501

        :return: The model_id of this AddModelPointsInput.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this AddModelPointsInput.

        模型点位里的 Id  # noqa: E501

        :param model_id: The model_id of this AddModelPointsInput.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def model_point_type(self):
        """Gets the model_point_type of this AddModelPointsInput.  # noqa: E501

        模型点位类型  # noqa: E501

        :return: The model_point_type of this AddModelPointsInput.  # noqa: E501
        :rtype: str
        """
        return self._model_point_type

    @model_point_type.setter
    def model_point_type(self, model_point_type):
        """Sets the model_point_type of this AddModelPointsInput.

        模型点位类型  # noqa: E501

        :param model_point_type: The model_point_type of this AddModelPointsInput.  # noqa: E501
        :type: str
        """

        self._model_point_type = model_point_type

    @property
    def name(self):
        """Gets the name of this AddModelPointsInput.  # noqa: E501

        模型点位名称  # noqa: E501

        :return: The name of this AddModelPointsInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddModelPointsInput.

        模型点位名称  # noqa: E501

        :param name: The name of this AddModelPointsInput.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, AddModelPointsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddModelPointsInput):
            return True

        return self.to_dict() != other.to_dict()
