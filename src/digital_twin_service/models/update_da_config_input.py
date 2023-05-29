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


class UpdateDaConfigInput(object):
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
        'show_name': 'str',
        'branch_name': 'str',
        'chainage': 'float',
        'variable_type': 'int',
        'component': 'int',
        'file': 'str',
        'file_num': 'int',
        'indicator_id': 'str',
        'template_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'show_name': 'showName',
        'branch_name': 'branchName',
        'chainage': 'chainage',
        'variable_type': 'variableType',
        'component': 'component',
        'file': 'file',
        'file_num': 'fileNum',
        'indicator_id': 'indicatorId',
        'template_id': 'templateId',
        'id': 'id'
    }

    def __init__(self, show_name=None, branch_name=None, chainage=None, variable_type=None, component=None, file=None, file_num=None, indicator_id=None, template_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """UpdateDaConfigInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._show_name = None
        self._branch_name = None
        self._chainage = None
        self._variable_type = None
        self._component = None
        self._file = None
        self._file_num = None
        self._indicator_id = None
        self._template_id = None
        self._id = None
        self.discriminator = None

        self.show_name = show_name
        self.branch_name = branch_name
        self.chainage = chainage
        self.variable_type = variable_type
        if component is not None:
            self.component = component
        self.file = file
        self.file_num = file_num
        self.indicator_id = indicator_id
        self.template_id = template_id
        self.id = id

    @property
    def show_name(self):
        """Gets the show_name of this UpdateDaConfigInput.  # noqa: E501

        实时校正点显示名称 DA point name  # noqa: E501

        :return: The show_name of this UpdateDaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        """Sets the show_name of this UpdateDaConfigInput.

        实时校正点显示名称 DA point name  # noqa: E501

        :param show_name: The show_name of this UpdateDaConfigInput.  # noqa: E501
        :type: str
        """

        self._show_name = show_name

    @property
    def branch_name(self):
        """Gets the branch_name of this UpdateDaConfigInput.  # noqa: E501

        河道名 branch name  # noqa: E501

        :return: The branch_name of this UpdateDaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this UpdateDaConfigInput.

        河道名 branch name  # noqa: E501

        :param branch_name: The branch_name of this UpdateDaConfigInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and branch_name is None:  # noqa: E501
            raise ValueError("Invalid value for `branch_name`, must not be `None`")  # noqa: E501

        self._branch_name = branch_name

    @property
    def chainage(self):
        """Gets the chainage of this UpdateDaConfigInput.  # noqa: E501

        里程数 chainage  # noqa: E501

        :return: The chainage of this UpdateDaConfigInput.  # noqa: E501
        :rtype: float
        """
        return self._chainage

    @chainage.setter
    def chainage(self, chainage):
        """Sets the chainage of this UpdateDaConfigInput.

        里程数 chainage  # noqa: E501

        :param chainage: The chainage of this UpdateDaConfigInput.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and chainage is None:  # noqa: E501
            raise ValueError("Invalid value for `chainage`, must not be `None`")  # noqa: E501

        self._chainage = chainage

    @property
    def variable_type(self):
        """Gets the variable_type of this UpdateDaConfigInput.  # noqa: E501

        0-WaterLevel(water level) 1-Discharge(discharge) 2-Concentration(concentration)   # noqa: E501

        :return: The variable_type of this UpdateDaConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        """Sets the variable_type of this UpdateDaConfigInput.

        0-WaterLevel(water level) 1-Discharge(discharge) 2-Concentration(concentration)   # noqa: E501

        :param variable_type: The variable_type of this UpdateDaConfigInput.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and variable_type is None:  # noqa: E501
            raise ValueError("Invalid value for `variable_type`, must not be `None`")  # noqa: E501
        allowed_values = [0, 1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and variable_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `variable_type` ({0}), must be one of {1}"  # noqa: E501
                .format(variable_type, allowed_values)
            )

        self._variable_type = variable_type

    @property
    def component(self):
        """Gets the component of this UpdateDaConfigInput.  # noqa: E501

        水质项序号 component number  # noqa: E501

        :return: The component of this UpdateDaConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this UpdateDaConfigInput.

        水质项序号 component number  # noqa: E501

        :param component: The component of this UpdateDaConfigInput.  # noqa: E501
        :type: int
        """

        self._component = component

    @property
    def file(self):
        """Gets the file of this UpdateDaConfigInput.  # noqa: E501

        dfs0文件相对路径 dfs0 file path  # noqa: E501

        :return: The file of this UpdateDaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this UpdateDaConfigInput.

        dfs0文件相对路径 dfs0 file path  # noqa: E501

        :param file: The file of this UpdateDaConfigInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def file_num(self):
        """Gets the file_num of this UpdateDaConfigInput.  # noqa: E501

        dfs0文件中项的序号 dfs0 data item number  # noqa: E501

        :return: The file_num of this UpdateDaConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._file_num

    @file_num.setter
    def file_num(self, file_num):
        """Sets the file_num of this UpdateDaConfigInput.

        dfs0文件中项的序号 dfs0 data item number  # noqa: E501

        :param file_num: The file_num of this UpdateDaConfigInput.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and file_num is None:  # noqa: E501
            raise ValueError("Invalid value for `file_num`, must not be `None`")  # noqa: E501

        self._file_num = file_num

    @property
    def indicator_id(self):
        """Gets the indicator_id of this UpdateDaConfigInput.  # noqa: E501

        指标Id device indicator id  # noqa: E501

        :return: The indicator_id of this UpdateDaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this UpdateDaConfigInput.

        指标Id device indicator id  # noqa: E501

        :param indicator_id: The indicator_id of this UpdateDaConfigInput.  # noqa: E501
        :type: str
        """

        self._indicator_id = indicator_id

    @property
    def template_id(self):
        """Gets the template_id of this UpdateDaConfigInput.  # noqa: E501

        模板方案Id template scenario id  # noqa: E501

        :return: The template_id of this UpdateDaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this UpdateDaConfigInput.

        模板方案Id template scenario id  # noqa: E501

        :param template_id: The template_id of this UpdateDaConfigInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def id(self):
        """Gets the id of this UpdateDaConfigInput.  # noqa: E501

        实时校正点ID DA point id  # noqa: E501

        :return: The id of this UpdateDaConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateDaConfigInput.

        实时校正点ID DA point id  # noqa: E501

        :param id: The id of this UpdateDaConfigInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, UpdateDaConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateDaConfigInput):
            return True

        return self.to_dict() != other.to_dict()
