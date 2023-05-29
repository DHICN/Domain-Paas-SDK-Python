# coding: utf-8

"""
    scenario-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from scenario_manager_service.configuration import Configuration


class CreateTemplateScenarioPara2(object):
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
        'model_file': 'str',
        'group_id': 'str',
        'new_template_name': 'str',
        'sub_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'model_file': 'modelFile',
        'group_id': 'groupId',
        'new_template_name': 'newTemplateName',
        'sub_type': 'subType',
        'description': 'description'
    }

    def __init__(self, model_file=None, group_id=None, new_template_name=None, sub_type=None, description=None, local_vars_configuration=None):  # noqa: E501
        """CreateTemplateScenarioPara2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_file = None
        self._group_id = None
        self._new_template_name = None
        self._sub_type = None
        self._description = None
        self.discriminator = None

        self.model_file = model_file
        self.group_id = group_id
        self.new_template_name = new_template_name
        self.sub_type = sub_type
        self.description = description

    @property
    def model_file(self):
        """Gets the model_file of this CreateTemplateScenarioPara2.  # noqa: E501

        模型文件的绝对路径 absolute path of the model file  # noqa: E501

        :return: The model_file of this CreateTemplateScenarioPara2.  # noqa: E501
        :rtype: str
        """
        return self._model_file

    @model_file.setter
    def model_file(self, model_file):
        """Sets the model_file of this CreateTemplateScenarioPara2.

        模型文件的绝对路径 absolute path of the model file  # noqa: E501

        :param model_file: The model_file of this CreateTemplateScenarioPara2.  # noqa: E501
        :type: str
        """

        self._model_file = model_file

    @property
    def group_id(self):
        """Gets the group_id of this CreateTemplateScenarioPara2.  # noqa: E501

        模板的方案组ID template scenario's group Id  # noqa: E501

        :return: The group_id of this CreateTemplateScenarioPara2.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateTemplateScenarioPara2.

        模板的方案组ID template scenario's group Id  # noqa: E501

        :param group_id: The group_id of this CreateTemplateScenarioPara2.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def new_template_name(self):
        """Gets the new_template_name of this CreateTemplateScenarioPara2.  # noqa: E501

        模板方案名称 template scenario name  # noqa: E501

        :return: The new_template_name of this CreateTemplateScenarioPara2.  # noqa: E501
        :rtype: str
        """
        return self._new_template_name

    @new_template_name.setter
    def new_template_name(self, new_template_name):
        """Sets the new_template_name of this CreateTemplateScenarioPara2.

        模板方案名称 template scenario name  # noqa: E501

        :param new_template_name: The new_template_name of this CreateTemplateScenarioPara2.  # noqa: E501
        :type: str
        """

        self._new_template_name = new_template_name

    @property
    def sub_type(self):
        """Gets the sub_type of this CreateTemplateScenarioPara2.  # noqa: E501

        模板方案的子类型 template scenario subtype  # noqa: E501

        :return: The sub_type of this CreateTemplateScenarioPara2.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this CreateTemplateScenarioPara2.

        模板方案的子类型 template scenario subtype  # noqa: E501

        :param sub_type: The sub_type of this CreateTemplateScenarioPara2.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def description(self):
        """Gets the description of this CreateTemplateScenarioPara2.  # noqa: E501

        模板方案描述 template scenario description  # noqa: E501

        :return: The description of this CreateTemplateScenarioPara2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTemplateScenarioPara2.

        模板方案描述 template scenario description  # noqa: E501

        :param description: The description of this CreateTemplateScenarioPara2.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, CreateTemplateScenarioPara2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTemplateScenarioPara2):
            return True

        return self.to_dict() != other.to_dict()