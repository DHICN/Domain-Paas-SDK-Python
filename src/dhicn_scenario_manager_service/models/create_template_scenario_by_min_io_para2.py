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

from dhicn_scenario_manager_service.configuration import Configuration


class CreateTemplateScenarioByMinIoPara2(object):
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
        'min_io_path': 'str',
        'min_io_bucket': 'str',
        'project_file': 'str',
        'type': 'ModelTypeEnum',
        'group_id': 'str',
        'new_template_name': 'str',
        'sub_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'min_io_path': 'minIOPath',
        'min_io_bucket': 'minIOBucket',
        'project_file': 'projectFile',
        'type': 'type',
        'group_id': 'groupId',
        'new_template_name': 'newTemplateName',
        'sub_type': 'subType',
        'description': 'description'
    }

    def __init__(self, min_io_path=None, min_io_bucket=None, project_file=None, type=None, group_id=None, new_template_name=None, sub_type=None, description=None, local_vars_configuration=None):  # noqa: E501
        """CreateTemplateScenarioByMinIoPara2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._min_io_path = None
        self._min_io_bucket = None
        self._project_file = None
        self._type = None
        self._group_id = None
        self._new_template_name = None
        self._sub_type = None
        self._description = None
        self.discriminator = None

        self.min_io_path = min_io_path
        self.min_io_bucket = min_io_bucket
        self.project_file = project_file
        if type is not None:
            self.type = type
        self.group_id = group_id
        self.new_template_name = new_template_name
        self.sub_type = sub_type
        self.description = description

    @property
    def min_io_path(self):
        """Gets the min_io_path of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501

        模型文件在分布式文件系统上的路径 path of the model file on distributed file system  # noqa: E501

        :return: The min_io_path of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: str
        """
        return self._min_io_path

    @min_io_path.setter
    def min_io_path(self, min_io_path):
        """Sets the min_io_path of this CreateTemplateScenarioByMinIoPara2.

        模型文件在分布式文件系统上的路径 path of the model file on distributed file system  # noqa: E501

        :param min_io_path: The min_io_path of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :type: str
        """

        self._min_io_path = min_io_path

    @property
    def min_io_bucket(self):
        """Gets the min_io_bucket of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501

        模型文件在分布式文件系统上的桶 bucket of the model file on distributed file system  # noqa: E501

        :return: The min_io_bucket of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: str
        """
        return self._min_io_bucket

    @min_io_bucket.setter
    def min_io_bucket(self, min_io_bucket):
        """Sets the min_io_bucket of this CreateTemplateScenarioByMinIoPara2.

        模型文件在分布式文件系统上的桶 bucket of the model file on distributed file system  # noqa: E501

        :param min_io_bucket: The min_io_bucket of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :type: str
        """

        self._min_io_bucket = min_io_bucket

    @property
    def project_file(self):
        """Gets the project_file of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501

        主模型文件相对于模型文件夹的路径 main model file's (eg. .mupp file) relative path to the model folder  # noqa: E501

        :return: The project_file of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: str
        """
        return self._project_file

    @project_file.setter
    def project_file(self, project_file):
        """Sets the project_file of this CreateTemplateScenarioByMinIoPara2.

        主模型文件相对于模型文件夹的路径 main model file's (eg. .mupp file) relative path to the model folder  # noqa: E501

        :param project_file: The project_file of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :type: str
        """

        self._project_file = project_file

    @property
    def type(self):
        """Gets the type of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501


        :return: The type of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: ModelTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateTemplateScenarioByMinIoPara2.


        :param type: The type of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :type: ModelTypeEnum
        """

        self._type = type

    @property
    def group_id(self):
        """Gets the group_id of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501

        模板的方案组ID template scenario's group Id  # noqa: E501

        :return: The group_id of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateTemplateScenarioByMinIoPara2.

        模板的方案组ID template scenario's group Id  # noqa: E501

        :param group_id: The group_id of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def new_template_name(self):
        """Gets the new_template_name of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501

        模板方案名称 template scenario name  # noqa: E501

        :return: The new_template_name of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: str
        """
        return self._new_template_name

    @new_template_name.setter
    def new_template_name(self, new_template_name):
        """Sets the new_template_name of this CreateTemplateScenarioByMinIoPara2.

        模板方案名称 template scenario name  # noqa: E501

        :param new_template_name: The new_template_name of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :type: str
        """

        self._new_template_name = new_template_name

    @property
    def sub_type(self):
        """Gets the sub_type of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501

        模板方案子类型 template scenario subtype  # noqa: E501

        :return: The sub_type of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this CreateTemplateScenarioByMinIoPara2.

        模板方案子类型 template scenario subtype  # noqa: E501

        :param sub_type: The sub_type of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def description(self):
        """Gets the description of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501

        模板方案描述 template scenario description  # noqa: E501

        :return: The description of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTemplateScenarioByMinIoPara2.

        模板方案描述 template scenario description  # noqa: E501

        :param description: The description of this CreateTemplateScenarioByMinIoPara2.  # noqa: E501
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
        if not isinstance(other, CreateTemplateScenarioByMinIoPara2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTemplateScenarioByMinIoPara2):
            return True

        return self.to_dict() != other.to_dict()
