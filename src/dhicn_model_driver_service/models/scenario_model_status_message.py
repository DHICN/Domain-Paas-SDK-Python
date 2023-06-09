# coding: utf-8

"""
    model-driver-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_model_driver_service.configuration import Configuration


class ScenarioModelStatusMessage(object):
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
        'app_id': 'str',
        'project_name': 'str',
        'scenario_id': 'str',
        'serial_no': 'str',
        'stage': 'ModelState',
        'process_status': 'float',
        'date_time': 'datetime',
        'has_error': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'app_id': 'appId',
        'project_name': 'projectName',
        'scenario_id': 'scenarioId',
        'serial_no': 'serialNo',
        'stage': 'stage',
        'process_status': 'processStatus',
        'date_time': 'dateTime',
        'has_error': 'hasError',
        'message': 'message'
    }

    def __init__(self, app_id=None, project_name=None, scenario_id=None, serial_no=None, stage=None, process_status=None, date_time=None, has_error=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ScenarioModelStatusMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._project_name = None
        self._scenario_id = None
        self._serial_no = None
        self._stage = None
        self._process_status = None
        self._date_time = None
        self._has_error = None
        self._message = None
        self.discriminator = None

        self.app_id = app_id
        self.project_name = project_name
        if scenario_id is not None:
            self.scenario_id = scenario_id
        if serial_no is not None:
            self.serial_no = serial_no
        if stage is not None:
            self.stage = stage
        if process_status is not None:
            self.process_status = process_status
        if date_time is not None:
            self.date_time = date_time
        if has_error is not None:
            self.has_error = has_error
        self.message = message

    @property
    def app_id(self):
        """Gets the app_id of this ScenarioModelStatusMessage.  # noqa: E501

        计算服务id Computer service app id  # noqa: E501

        :return: The app_id of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ScenarioModelStatusMessage.

        计算服务id Computer service app id  # noqa: E501

        :param app_id: The app_id of this ScenarioModelStatusMessage.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def project_name(self):
        """Gets the project_name of this ScenarioModelStatusMessage.  # noqa: E501

        项目名称 project name  # noqa: E501

        :return: The project_name of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ScenarioModelStatusMessage.

        项目名称 project name  # noqa: E501

        :param project_name: The project_name of this ScenarioModelStatusMessage.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def scenario_id(self):
        """Gets the scenario_id of this ScenarioModelStatusMessage.  # noqa: E501

        方案ID scenario id  # noqa: E501

        :return: The scenario_id of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this ScenarioModelStatusMessage.

        方案ID scenario id  # noqa: E501

        :param scenario_id: The scenario_id of this ScenarioModelStatusMessage.  # noqa: E501
        :type: str
        """

        self._scenario_id = scenario_id

    @property
    def serial_no(self):
        """Gets the serial_no of this ScenarioModelStatusMessage.  # noqa: E501

        序列ID serial id  # noqa: E501

        :return: The serial_no of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._serial_no

    @serial_no.setter
    def serial_no(self, serial_no):
        """Sets the serial_no of this ScenarioModelStatusMessage.

        序列ID serial id  # noqa: E501

        :param serial_no: The serial_no of this ScenarioModelStatusMessage.  # noqa: E501
        :type: str
        """

        self._serial_no = serial_no

    @property
    def stage(self):
        """Gets the stage of this ScenarioModelStatusMessage.  # noqa: E501


        :return: The stage of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: ModelState
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ScenarioModelStatusMessage.


        :param stage: The stage of this ScenarioModelStatusMessage.  # noqa: E501
        :type: ModelState
        """

        self._stage = stage

    @property
    def process_status(self):
        """Gets the process_status of this ScenarioModelStatusMessage.  # noqa: E501

        进度状态 Process status  # noqa: E501

        :return: The process_status of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: float
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        """Sets the process_status of this ScenarioModelStatusMessage.

        进度状态 Process status  # noqa: E501

        :param process_status: The process_status of this ScenarioModelStatusMessage.  # noqa: E501
        :type: float
        """

        self._process_status = process_status

    @property
    def date_time(self):
        """Gets the date_time of this ScenarioModelStatusMessage.  # noqa: E501

        状态更新时间 status last modification time  # noqa: E501

        :return: The date_time of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this ScenarioModelStatusMessage.

        状态更新时间 status last modification time  # noqa: E501

        :param date_time: The date_time of this ScenarioModelStatusMessage.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def has_error(self):
        """Gets the has_error of this ScenarioModelStatusMessage.  # noqa: E501

        是否存在错误 if error existed  # noqa: E501

        :return: The has_error of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this ScenarioModelStatusMessage.

        是否存在错误 if error existed  # noqa: E501

        :param has_error: The has_error of this ScenarioModelStatusMessage.  # noqa: E501
        :type: bool
        """

        self._has_error = has_error

    @property
    def message(self):
        """Gets the message of this ScenarioModelStatusMessage.  # noqa: E501

        包含进度信息的计算日志信息 log message with progress  # noqa: E501

        :return: The message of this ScenarioModelStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ScenarioModelStatusMessage.

        包含进度信息的计算日志信息 log message with progress  # noqa: E501

        :param message: The message of this ScenarioModelStatusMessage.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ScenarioModelStatusMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScenarioModelStatusMessage):
            return True

        return self.to_dict() != other.to_dict()
