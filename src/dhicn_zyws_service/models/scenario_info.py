# coding: utf-8

"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dhicn_zyws_service.configuration import Configuration


class ScenarioInfo(object):
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
        'name': 'str',
        'min_io_bucket': 'str',
        'min_io_path': 'str',
        'tenant_id': 'str',
        'version': 'str',
        'description': 'str',
        'state': 'str',
        'auto_amend': 'int',
        'online_first': 'int',
        'published': 'int',
        'calculated': 'int',
        'checked': 'int',
        'modified': 'int',
        'auto_calculate': 'int',
        'create_time': 'str',
        'end_time': 'str',
        'start_time': 'str',
        'current_time': 'str',
        'project_file': 'str',
        'relative_folder': 'str',
        'enabled': 'int',
        'read_only': 'int',
        'inherited_scenario': 'str',
        'id': 'str',
        'scenario_code': 'str',
        'scenario_name': 'str',
        'model_type': 'str',
        'model_sub_type': 'str',
        'template': 'int'
    }

    attribute_map = {
        'name': 'name',
        'min_io_bucket': 'minIOBucket',
        'min_io_path': 'minIOPath',
        'tenant_id': 'tenantId',
        'version': 'version',
        'description': 'description',
        'state': 'state',
        'auto_amend': 'autoAmend',
        'online_first': 'onlineFirst',
        'published': 'published',
        'calculated': 'calculated',
        'checked': 'checked',
        'modified': 'modified',
        'auto_calculate': 'autoCalculate',
        'create_time': 'createTime',
        'end_time': 'endTime',
        'start_time': 'startTime',
        'current_time': 'currentTime',
        'project_file': 'projectFile',
        'relative_folder': 'relativeFolder',
        'enabled': 'enabled',
        'read_only': 'readOnly',
        'inherited_scenario': 'inheritedScenario',
        'id': 'id',
        'scenario_code': 'scenarioCode',
        'scenario_name': 'scenarioName',
        'model_type': 'modelType',
        'model_sub_type': 'modelSubType',
        'template': 'template'
    }

    def __init__(self, name=None, min_io_bucket=None, min_io_path=None, tenant_id=None, version=None, description=None, state=None, auto_amend=None, online_first=None, published=None, calculated=None, checked=None, modified=None, auto_calculate=None, create_time=None, end_time=None, start_time=None, current_time=None, project_file=None, relative_folder=None, enabled=None, read_only=None, inherited_scenario=None, id=None, scenario_code=None, scenario_name=None, model_type=None, model_sub_type=None, template=None, local_vars_configuration=None):  # noqa: E501
        """ScenarioInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._min_io_bucket = None
        self._min_io_path = None
        self._tenant_id = None
        self._version = None
        self._description = None
        self._state = None
        self._auto_amend = None
        self._online_first = None
        self._published = None
        self._calculated = None
        self._checked = None
        self._modified = None
        self._auto_calculate = None
        self._create_time = None
        self._end_time = None
        self._start_time = None
        self._current_time = None
        self._project_file = None
        self._relative_folder = None
        self._enabled = None
        self._read_only = None
        self._inherited_scenario = None
        self._id = None
        self._scenario_code = None
        self._scenario_name = None
        self._model_type = None
        self._model_sub_type = None
        self._template = None
        self.discriminator = None

        self.name = name
        self.min_io_bucket = min_io_bucket
        self.min_io_path = min_io_path
        self.tenant_id = tenant_id
        self.version = version
        self.description = description
        self.state = state
        if auto_amend is not None:
            self.auto_amend = auto_amend
        if online_first is not None:
            self.online_first = online_first
        if published is not None:
            self.published = published
        if calculated is not None:
            self.calculated = calculated
        if checked is not None:
            self.checked = checked
        if modified is not None:
            self.modified = modified
        if auto_calculate is not None:
            self.auto_calculate = auto_calculate
        self.create_time = create_time
        self.end_time = end_time
        self.start_time = start_time
        self.current_time = current_time
        self.project_file = project_file
        self.relative_folder = relative_folder
        if enabled is not None:
            self.enabled = enabled
        if read_only is not None:
            self.read_only = read_only
        if inherited_scenario is not None:
            self.inherited_scenario = inherited_scenario
        if id is not None:
            self.id = id
        self.scenario_code = scenario_code
        self.scenario_name = scenario_name
        self.model_type = model_type
        self.model_sub_type = model_sub_type
        if template is not None:
            self.template = template

    @property
    def name(self):
        """Gets the name of this ScenarioInfo.  # noqa: E501


        :return: The name of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScenarioInfo.


        :param name: The name of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def min_io_bucket(self):
        """Gets the min_io_bucket of this ScenarioInfo.  # noqa: E501


        :return: The min_io_bucket of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._min_io_bucket

    @min_io_bucket.setter
    def min_io_bucket(self, min_io_bucket):
        """Sets the min_io_bucket of this ScenarioInfo.


        :param min_io_bucket: The min_io_bucket of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._min_io_bucket = min_io_bucket

    @property
    def min_io_path(self):
        """Gets the min_io_path of this ScenarioInfo.  # noqa: E501


        :return: The min_io_path of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._min_io_path

    @min_io_path.setter
    def min_io_path(self, min_io_path):
        """Sets the min_io_path of this ScenarioInfo.


        :param min_io_path: The min_io_path of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._min_io_path = min_io_path

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ScenarioInfo.  # noqa: E501


        :return: The tenant_id of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ScenarioInfo.


        :param tenant_id: The tenant_id of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def version(self):
        """Gets the version of this ScenarioInfo.  # noqa: E501


        :return: The version of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ScenarioInfo.


        :param version: The version of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def description(self):
        """Gets the description of this ScenarioInfo.  # noqa: E501


        :return: The description of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScenarioInfo.


        :param description: The description of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def state(self):
        """Gets the state of this ScenarioInfo.  # noqa: E501


        :return: The state of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ScenarioInfo.


        :param state: The state of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def auto_amend(self):
        """Gets the auto_amend of this ScenarioInfo.  # noqa: E501


        :return: The auto_amend of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._auto_amend

    @auto_amend.setter
    def auto_amend(self, auto_amend):
        """Sets the auto_amend of this ScenarioInfo.


        :param auto_amend: The auto_amend of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._auto_amend = auto_amend

    @property
    def online_first(self):
        """Gets the online_first of this ScenarioInfo.  # noqa: E501


        :return: The online_first of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._online_first

    @online_first.setter
    def online_first(self, online_first):
        """Sets the online_first of this ScenarioInfo.


        :param online_first: The online_first of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._online_first = online_first

    @property
    def published(self):
        """Gets the published of this ScenarioInfo.  # noqa: E501


        :return: The published of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this ScenarioInfo.


        :param published: The published of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._published = published

    @property
    def calculated(self):
        """Gets the calculated of this ScenarioInfo.  # noqa: E501


        :return: The calculated of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._calculated

    @calculated.setter
    def calculated(self, calculated):
        """Sets the calculated of this ScenarioInfo.


        :param calculated: The calculated of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._calculated = calculated

    @property
    def checked(self):
        """Gets the checked of this ScenarioInfo.  # noqa: E501


        :return: The checked of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this ScenarioInfo.


        :param checked: The checked of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._checked = checked

    @property
    def modified(self):
        """Gets the modified of this ScenarioInfo.  # noqa: E501


        :return: The modified of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ScenarioInfo.


        :param modified: The modified of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._modified = modified

    @property
    def auto_calculate(self):
        """Gets the auto_calculate of this ScenarioInfo.  # noqa: E501


        :return: The auto_calculate of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._auto_calculate

    @auto_calculate.setter
    def auto_calculate(self, auto_calculate):
        """Sets the auto_calculate of this ScenarioInfo.


        :param auto_calculate: The auto_calculate of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._auto_calculate = auto_calculate

    @property
    def create_time(self):
        """Gets the create_time of this ScenarioInfo.  # noqa: E501


        :return: The create_time of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScenarioInfo.


        :param create_time: The create_time of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this ScenarioInfo.  # noqa: E501


        :return: The end_time of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScenarioInfo.


        :param end_time: The end_time of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this ScenarioInfo.  # noqa: E501


        :return: The start_time of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScenarioInfo.


        :param start_time: The start_time of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def current_time(self):
        """Gets the current_time of this ScenarioInfo.  # noqa: E501


        :return: The current_time of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """Sets the current_time of this ScenarioInfo.


        :param current_time: The current_time of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._current_time = current_time

    @property
    def project_file(self):
        """Gets the project_file of this ScenarioInfo.  # noqa: E501


        :return: The project_file of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._project_file

    @project_file.setter
    def project_file(self, project_file):
        """Sets the project_file of this ScenarioInfo.


        :param project_file: The project_file of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._project_file = project_file

    @property
    def relative_folder(self):
        """Gets the relative_folder of this ScenarioInfo.  # noqa: E501


        :return: The relative_folder of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._relative_folder

    @relative_folder.setter
    def relative_folder(self, relative_folder):
        """Sets the relative_folder of this ScenarioInfo.


        :param relative_folder: The relative_folder of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._relative_folder = relative_folder

    @property
    def enabled(self):
        """Gets the enabled of this ScenarioInfo.  # noqa: E501


        :return: The enabled of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ScenarioInfo.


        :param enabled: The enabled of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._enabled = enabled

    @property
    def read_only(self):
        """Gets the read_only of this ScenarioInfo.  # noqa: E501


        :return: The read_only of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ScenarioInfo.


        :param read_only: The read_only of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._read_only = read_only

    @property
    def inherited_scenario(self):
        """Gets the inherited_scenario of this ScenarioInfo.  # noqa: E501


        :return: The inherited_scenario of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._inherited_scenario

    @inherited_scenario.setter
    def inherited_scenario(self, inherited_scenario):
        """Sets the inherited_scenario of this ScenarioInfo.


        :param inherited_scenario: The inherited_scenario of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._inherited_scenario = inherited_scenario

    @property
    def id(self):
        """Gets the id of this ScenarioInfo.  # noqa: E501


        :return: The id of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScenarioInfo.


        :param id: The id of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def scenario_code(self):
        """Gets the scenario_code of this ScenarioInfo.  # noqa: E501


        :return: The scenario_code of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._scenario_code

    @scenario_code.setter
    def scenario_code(self, scenario_code):
        """Sets the scenario_code of this ScenarioInfo.


        :param scenario_code: The scenario_code of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._scenario_code = scenario_code

    @property
    def scenario_name(self):
        """Gets the scenario_name of this ScenarioInfo.  # noqa: E501


        :return: The scenario_name of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._scenario_name

    @scenario_name.setter
    def scenario_name(self, scenario_name):
        """Sets the scenario_name of this ScenarioInfo.


        :param scenario_name: The scenario_name of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._scenario_name = scenario_name

    @property
    def model_type(self):
        """Gets the model_type of this ScenarioInfo.  # noqa: E501


        :return: The model_type of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ScenarioInfo.


        :param model_type: The model_type of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._model_type = model_type

    @property
    def model_sub_type(self):
        """Gets the model_sub_type of this ScenarioInfo.  # noqa: E501


        :return: The model_sub_type of this ScenarioInfo.  # noqa: E501
        :rtype: str
        """
        return self._model_sub_type

    @model_sub_type.setter
    def model_sub_type(self, model_sub_type):
        """Sets the model_sub_type of this ScenarioInfo.


        :param model_sub_type: The model_sub_type of this ScenarioInfo.  # noqa: E501
        :type: str
        """

        self._model_sub_type = model_sub_type

    @property
    def template(self):
        """Gets the template of this ScenarioInfo.  # noqa: E501


        :return: The template of this ScenarioInfo.  # noqa: E501
        :rtype: int
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ScenarioInfo.


        :param template: The template of this ScenarioInfo.  # noqa: E501
        :type: int
        """

        self._template = template

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
        if not isinstance(other, ScenarioInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScenarioInfo):
            return True

        return self.to_dict() != other.to_dict()