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


class CreateTemplateScenarioOutput(object):
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
        'scenario_code': 'str',
        'scenario_name': 'str',
        'model_type': 'str',
        'model_sub_type': 'str',
        'template': 'int',
        'inherited_scenario': 'str',
        'read_only': 'int',
        'enabled': 'int',
        'relativefolder': 'str',
        'project_file': 'str',
        'current_time': 'datetime',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'create_time': 'datetime',
        'auto_calculate': 'int'
    }

    attribute_map = {
        'id': 'id',
        'scenario_code': 'scenarioCode',
        'scenario_name': 'scenarioName',
        'model_type': 'modelType',
        'model_sub_type': 'modelSubType',
        'template': 'template',
        'inherited_scenario': 'inheritedScenario',
        'read_only': 'readOnly',
        'enabled': 'enabled',
        'relativefolder': 'relativefolder',
        'project_file': 'projectFile',
        'current_time': 'currentTime',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'create_time': 'createTime',
        'auto_calculate': 'autoCalculate'
    }

    def __init__(self, id=None, scenario_code=None, scenario_name=None, model_type=None, model_sub_type=None, template=None, inherited_scenario=None, read_only=None, enabled=None, relativefolder=None, project_file=None, current_time=None, start_time=None, end_time=None, create_time=None, auto_calculate=None, local_vars_configuration=None):  # noqa: E501
        """CreateTemplateScenarioOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._scenario_code = None
        self._scenario_name = None
        self._model_type = None
        self._model_sub_type = None
        self._template = None
        self._inherited_scenario = None
        self._read_only = None
        self._enabled = None
        self._relativefolder = None
        self._project_file = None
        self._current_time = None
        self._start_time = None
        self._end_time = None
        self._create_time = None
        self._auto_calculate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.scenario_code = scenario_code
        self.scenario_name = scenario_name
        self.model_type = model_type
        self.model_sub_type = model_sub_type
        if template is not None:
            self.template = template
        if inherited_scenario is not None:
            self.inherited_scenario = inherited_scenario
        if read_only is not None:
            self.read_only = read_only
        if enabled is not None:
            self.enabled = enabled
        self.relativefolder = relativefolder
        self.project_file = project_file
        if current_time is not None:
            self.current_time = current_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time
        if auto_calculate is not None:
            self.auto_calculate = auto_calculate

    @property
    def id(self):
        """Gets the id of this CreateTemplateScenarioOutput.  # noqa: E501

        模板方案ID template scenario id  # noqa: E501

        :return: The id of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateTemplateScenarioOutput.

        模板方案ID template scenario id  # noqa: E501

        :param id: The id of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def scenario_code(self):
        """Gets the scenario_code of this CreateTemplateScenarioOutput.  # noqa: E501

        模板方案代码 template scenario code  # noqa: E501

        :return: The scenario_code of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_code

    @scenario_code.setter
    def scenario_code(self, scenario_code):
        """Sets the scenario_code of this CreateTemplateScenarioOutput.

        模板方案代码 template scenario code  # noqa: E501

        :param scenario_code: The scenario_code of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._scenario_code = scenario_code

    @property
    def scenario_name(self):
        """Gets the scenario_name of this CreateTemplateScenarioOutput.  # noqa: E501

        模板方案名称 template scenario name  # noqa: E501

        :return: The scenario_name of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._scenario_name

    @scenario_name.setter
    def scenario_name(self, scenario_name):
        """Sets the scenario_name of this CreateTemplateScenarioOutput.

        模板方案名称 template scenario name  # noqa: E501

        :param scenario_name: The scenario_name of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._scenario_name = scenario_name

    @property
    def model_type(self):
        """Gets the model_type of this CreateTemplateScenarioOutput.  # noqa: E501

        模型类型，包括但不限于 model type, including but not limited to:  0-MIKE11Model(MIKE 11 model),  2-MIKE21Model(MIKE 21 model),  3-MIKE21FMModel(MIKE 21FM model),  4-MIKE3FMModel(MIKE 3FM model),  5-MIKEFloodModel(MIKE Flood model),  7-MIKEUrbanCSModel(MIKE Urban CS model),  8-MIKEUrbanWDModel(MIKE Urban WD model),  9-HydroBasinModel(MIKE HYDRO Basin model),  12-FeflowModel(MIKE Feflow model),  13-WestModel(West model),  20-HammerModel(Hammer model of WD),  21-MIKEPlusFloodModel(MIKE Plus Flood model),  22-MIKEPlusWDModel(MIKE Plus WD model),  99-Unknown(Unknown),  # noqa: E501

        :return: The model_type of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this CreateTemplateScenarioOutput.

        模型类型，包括但不限于 model type, including but not limited to:  0-MIKE11Model(MIKE 11 model),  2-MIKE21Model(MIKE 21 model),  3-MIKE21FMModel(MIKE 21FM model),  4-MIKE3FMModel(MIKE 3FM model),  5-MIKEFloodModel(MIKE Flood model),  7-MIKEUrbanCSModel(MIKE Urban CS model),  8-MIKEUrbanWDModel(MIKE Urban WD model),  9-HydroBasinModel(MIKE HYDRO Basin model),  12-FeflowModel(MIKE Feflow model),  13-WestModel(West model),  20-HammerModel(Hammer model of WD),  21-MIKEPlusFloodModel(MIKE Plus Flood model),  22-MIKEPlusWDModel(MIKE Plus WD model),  99-Unknown(Unknown),  # noqa: E501

        :param model_type: The model_type of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._model_type = model_type

    @property
    def model_sub_type(self):
        """Gets the model_sub_type of this CreateTemplateScenarioOutput.  # noqa: E501

        方案子类型，包括但不限于 scenario subtype, including but not limited to:  0-ManualSchedule(Manual schedule),  2-OptimizeSchedule(Optimization schedule),  5-EmerResponse(Emergency response),  6-Forecast(Forecast and warning),  8-Scenario(Scenario simulation),  9-Incident(Accident),  12-WQEvaluation(Water quality evaluation),  14-Planning(Planning),  15-OilSpill(Oil spill accident),  19-PumpShutdown(Pump shut down scenario),  20-PipeBurst(Pipe burst scenario),  99-Unknown(Unknown),  # noqa: E501

        :return: The model_sub_type of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_sub_type

    @model_sub_type.setter
    def model_sub_type(self, model_sub_type):
        """Sets the model_sub_type of this CreateTemplateScenarioOutput.

        方案子类型，包括但不限于 scenario subtype, including but not limited to:  0-ManualSchedule(Manual schedule),  2-OptimizeSchedule(Optimization schedule),  5-EmerResponse(Emergency response),  6-Forecast(Forecast and warning),  8-Scenario(Scenario simulation),  9-Incident(Accident),  12-WQEvaluation(Water quality evaluation),  14-Planning(Planning),  15-OilSpill(Oil spill accident),  19-PumpShutdown(Pump shut down scenario),  20-PipeBurst(Pipe burst scenario),  99-Unknown(Unknown),  # noqa: E501

        :param model_sub_type: The model_sub_type of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._model_sub_type = model_sub_type

    @property
    def template(self):
        """Gets the template of this CreateTemplateScenarioOutput.  # noqa: E501

        1表示模板方案，0表示非模板方案 1 or 0, indicating if the scenario is a template or not  # noqa: E501

        :return: The template of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: int
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateTemplateScenarioOutput.

        1表示模板方案，0表示非模板方案 1 or 0, indicating if the scenario is a template or not  # noqa: E501

        :param template: The template of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: int
        """

        self._template = template

    @property
    def inherited_scenario(self):
        """Gets the inherited_scenario of this CreateTemplateScenarioOutput.  # noqa: E501

        父方案ID parent scenario Id  # noqa: E501

        :return: The inherited_scenario of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._inherited_scenario

    @inherited_scenario.setter
    def inherited_scenario(self, inherited_scenario):
        """Sets the inherited_scenario of this CreateTemplateScenarioOutput.

        父方案ID parent scenario Id  # noqa: E501

        :param inherited_scenario: The inherited_scenario of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._inherited_scenario = inherited_scenario

    @property
    def read_only(self):
        """Gets the read_only of this CreateTemplateScenarioOutput.  # noqa: E501

        1表示只读，0表示可读写 1 for readonly, 0 for not readonly  # noqa: E501

        :return: The read_only of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: int
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this CreateTemplateScenarioOutput.

        1表示只读，0表示可读写 1 for readonly, 0 for not readonly  # noqa: E501

        :param read_only: The read_only of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: int
        """

        self._read_only = read_only

    @property
    def enabled(self):
        """Gets the enabled of this CreateTemplateScenarioOutput.  # noqa: E501

        1表示启用，0表示不启用 1 for enabled, 0 for disabled  # noqa: E501

        :return: The enabled of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateTemplateScenarioOutput.

        1表示启用，0表示不启用 1 for enabled, 0 for disabled  # noqa: E501

        :param enabled: The enabled of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: int
        """

        self._enabled = enabled

    @property
    def relativefolder(self):
        """Gets the relativefolder of this CreateTemplateScenarioOutput.  # noqa: E501

        方案文件夹相对于WorkFolder的路径 scenario's relative path to WorkFolder  # noqa: E501

        :return: The relativefolder of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._relativefolder

    @relativefolder.setter
    def relativefolder(self, relativefolder):
        """Sets the relativefolder of this CreateTemplateScenarioOutput.

        方案文件夹相对于WorkFolder的路径 scenario's relative path to WorkFolder  # noqa: E501

        :param relativefolder: The relativefolder of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._relativefolder = relativefolder

    @property
    def project_file(self):
        """Gets the project_file of this CreateTemplateScenarioOutput.  # noqa: E501

        模型文件名称 model file name  # noqa: E501

        :return: The project_file of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_file

    @project_file.setter
    def project_file(self, project_file):
        """Sets the project_file of this CreateTemplateScenarioOutput.

        模型文件名称 model file name  # noqa: E501

        :param project_file: The project_file of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: str
        """

        self._project_file = project_file

    @property
    def current_time(self):
        """Gets the current_time of this CreateTemplateScenarioOutput.  # noqa: E501

        模型预报时刻 model current time or forecast time  # noqa: E501

        :return: The current_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """Sets the current_time of this CreateTemplateScenarioOutput.

        模型预报时刻 model current time or forecast time  # noqa: E501

        :param current_time: The current_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: datetime
        """

        self._current_time = current_time

    @property
    def start_time(self):
        """Gets the start_time of this CreateTemplateScenarioOutput.  # noqa: E501

        模型开始时刻 model start time  # noqa: E501

        :return: The start_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateTemplateScenarioOutput.

        模型开始时刻 model start time  # noqa: E501

        :param start_time: The start_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CreateTemplateScenarioOutput.  # noqa: E501

        模型结束时刻 model end time  # noqa: E501

        :return: The end_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateTemplateScenarioOutput.

        模型结束时刻 model end time  # noqa: E501

        :param end_time: The end_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def create_time(self):
        """Gets the create_time of this CreateTemplateScenarioOutput.  # noqa: E501

        方案创建时刻 scenario create time  # noqa: E501

        :return: The create_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateTemplateScenarioOutput.

        方案创建时刻 scenario create time  # noqa: E501

        :param create_time: The create_time of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def auto_calculate(self):
        """Gets the auto_calculate of this CreateTemplateScenarioOutput.  # noqa: E501

        1表示自动计算，0表示非自动计算 1 for auto calculate, 0 for not auto calculate  # noqa: E501

        :return: The auto_calculate of this CreateTemplateScenarioOutput.  # noqa: E501
        :rtype: int
        """
        return self._auto_calculate

    @auto_calculate.setter
    def auto_calculate(self, auto_calculate):
        """Sets the auto_calculate of this CreateTemplateScenarioOutput.

        1表示自动计算，0表示非自动计算 1 for auto calculate, 0 for not auto calculate  # noqa: E501

        :param auto_calculate: The auto_calculate of this CreateTemplateScenarioOutput.  # noqa: E501
        :type: int
        """

        self._auto_calculate = auto_calculate

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
        if not isinstance(other, CreateTemplateScenarioOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTemplateScenarioOutput):
            return True

        return self.to_dict() != other.to_dict()