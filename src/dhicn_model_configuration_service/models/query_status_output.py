# coding: utf-8

"""
    model-configuration-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_model_configuration_service.configuration import Configuration


class QueryStatusOutput(object):
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
        'step_code': 'str',
        'description': 'str',
        'status': 'ProjectInitializeStatusEnum',
        'execute_time': 'datetime',
        'param': 'str',
        'project_name': 'str',
        'step': 'ProjectInitializeStepEnum'
    }

    attribute_map = {
        'step_code': 'stepCode',
        'description': 'description',
        'status': 'status',
        'execute_time': 'executeTime',
        'param': 'param',
        'project_name': 'projectName',
        'step': 'step'
    }

    def __init__(self, step_code=None, description=None, status=None, execute_time=None, param=None, project_name=None, step=None, local_vars_configuration=None):  # noqa: E501
        """QueryStatusOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._step_code = None
        self._description = None
        self._status = None
        self._execute_time = None
        self._param = None
        self._project_name = None
        self._step = None
        self.discriminator = None

        self.step_code = step_code
        self.description = description
        if status is not None:
            self.status = status
        if execute_time is not None:
            self.execute_time = execute_time
        self.param = param
        self.project_name = project_name
        if step is not None:
            self.step = step

    @property
    def step_code(self):
        """Gets the step_code of this QueryStatusOutput.  # noqa: E501

        初始化步骤的代码 project initialization step code  # noqa: E501

        :return: The step_code of this QueryStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._step_code

    @step_code.setter
    def step_code(self, step_code):
        """Sets the step_code of this QueryStatusOutput.

        初始化步骤的代码 project initialization step code  # noqa: E501

        :param step_code: The step_code of this QueryStatusOutput.  # noqa: E501
        :type: str
        """

        self._step_code = step_code

    @property
    def description(self):
        """Gets the description of this QueryStatusOutput.  # noqa: E501

        初始化步骤的描述 initialization step description  # noqa: E501

        :return: The description of this QueryStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryStatusOutput.

        初始化步骤的描述 initialization step description  # noqa: E501

        :param description: The description of this QueryStatusOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this QueryStatusOutput.  # noqa: E501


        :return: The status of this QueryStatusOutput.  # noqa: E501
        :rtype: ProjectInitializeStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryStatusOutput.


        :param status: The status of this QueryStatusOutput.  # noqa: E501
        :type: ProjectInitializeStatusEnum
        """

        self._status = status

    @property
    def execute_time(self):
        """Gets the execute_time of this QueryStatusOutput.  # noqa: E501

        初始化步骤的执行时间 initialization step execution time  # noqa: E501

        :return: The execute_time of this QueryStatusOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        """Sets the execute_time of this QueryStatusOutput.

        初始化步骤的执行时间 initialization step execution time  # noqa: E501

        :param execute_time: The execute_time of this QueryStatusOutput.  # noqa: E501
        :type: datetime
        """

        self._execute_time = execute_time

    @property
    def param(self):
        """Gets the param of this QueryStatusOutput.  # noqa: E501

        初始化步骤涉及的参数 the parameters of the step  # noqa: E501

        :return: The param of this QueryStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this QueryStatusOutput.

        初始化步骤涉及的参数 the parameters of the step  # noqa: E501

        :param param: The param of this QueryStatusOutput.  # noqa: E501
        :type: str
        """

        self._param = param

    @property
    def project_name(self):
        """Gets the project_name of this QueryStatusOutput.  # noqa: E501

        项目名称 project name  # noqa: E501

        :return: The project_name of this QueryStatusOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this QueryStatusOutput.

        项目名称 project name  # noqa: E501

        :param project_name: The project_name of this QueryStatusOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def step(self):
        """Gets the step of this QueryStatusOutput.  # noqa: E501


        :return: The step of this QueryStatusOutput.  # noqa: E501
        :rtype: ProjectInitializeStepEnum
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this QueryStatusOutput.


        :param step: The step of this QueryStatusOutput.  # noqa: E501
        :type: ProjectInitializeStepEnum
        """

        self._step = step

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
        if not isinstance(other, QueryStatusOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryStatusOutput):
            return True

        return self.to_dict() != other.to_dict()
