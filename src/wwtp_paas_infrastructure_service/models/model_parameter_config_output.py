# coding: utf-8

"""
    wwtp-paas-infrastructure-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wwtp_paas_infrastructure_service.configuration import Configuration


class ModelParameterConfigOutput(object):
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
        'model_code': 'str',
        'model_name': 'str',
        'para_code': 'str',
        'value': 'float',
        'unit': 'str',
        'production_line': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'model_code': 'modelCode',
        'model_name': 'modelName',
        'para_code': 'paraCode',
        'value': 'value',
        'unit': 'unit',
        'production_line': 'productionLine',
        'description': 'description'
    }

    def __init__(self, id=None, model_code=None, model_name=None, para_code=None, value=None, unit=None, production_line=None, description=None, local_vars_configuration=None):  # noqa: E501
        """ModelParameterConfigOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._model_code = None
        self._model_name = None
        self._para_code = None
        self._value = None
        self._unit = None
        self._production_line = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.model_code = model_code
        self.model_name = model_name
        self.para_code = para_code
        if value is not None:
            self.value = value
        self.unit = unit
        self.production_line = production_line
        self.description = description

    @property
    def id(self):
        """Gets the id of this ModelParameterConfigOutput.  # noqa: E501

        模型参数配置ID config id  # noqa: E501

        :return: The id of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelParameterConfigOutput.

        模型参数配置ID config id  # noqa: E501

        :param id: The id of this ModelParameterConfigOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model_code(self):
        """Gets the model_code of this ModelParameterConfigOutput.  # noqa: E501

        模板模型名称（即模板方案名称） template scenario name  # noqa: E501

        :return: The model_code of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_code

    @model_code.setter
    def model_code(self, model_code):
        """Sets the model_code of this ModelParameterConfigOutput.

        模板模型名称（即模板方案名称） template scenario name  # noqa: E501

        :param model_code: The model_code of this ModelParameterConfigOutput.  # noqa: E501
        :type: str
        """

        self._model_code = model_code

    @property
    def model_name(self):
        """Gets the model_name of this ModelParameterConfigOutput.  # noqa: E501

        模板模型名称（即模板方案名称） template scenario name  # noqa: E501

        :return: The model_name of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this ModelParameterConfigOutput.

        模板模型名称（即模板方案名称） template scenario name  # noqa: E501

        :param model_name: The model_name of this ModelParameterConfigOutput.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def para_code(self):
        """Gets the para_code of this ModelParameterConfigOutput.  # noqa: E501

        参数 model parameter code  # noqa: E501

        :return: The para_code of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._para_code

    @para_code.setter
    def para_code(self, para_code):
        """Sets the para_code of this ModelParameterConfigOutput.

        参数 model parameter code  # noqa: E501

        :param para_code: The para_code of this ModelParameterConfigOutput.  # noqa: E501
        :type: str
        """

        self._para_code = para_code

    @property
    def value(self):
        """Gets the value of this ModelParameterConfigOutput.  # noqa: E501

        参数值 model parameter value  # noqa: E501

        :return: The value of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelParameterConfigOutput.

        参数值 model parameter value  # noqa: E501

        :param value: The value of this ModelParameterConfigOutput.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this ModelParameterConfigOutput.  # noqa: E501

        单位 model parameter unit  # noqa: E501

        :return: The unit of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ModelParameterConfigOutput.

        单位 model parameter unit  # noqa: E501

        :param unit: The unit of this ModelParameterConfigOutput.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def production_line(self):
        """Gets the production_line of this ModelParameterConfigOutput.  # noqa: E501

        工艺线 product line code  # noqa: E501

        :return: The production_line of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._production_line

    @production_line.setter
    def production_line(self, production_line):
        """Sets the production_line of this ModelParameterConfigOutput.

        工艺线 product line code  # noqa: E501

        :param production_line: The production_line of this ModelParameterConfigOutput.  # noqa: E501
        :type: str
        """

        self._production_line = production_line

    @property
    def description(self):
        """Gets the description of this ModelParameterConfigOutput.  # noqa: E501

        中文说明 description  # noqa: E501

        :return: The description of this ModelParameterConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelParameterConfigOutput.

        中文说明 description  # noqa: E501

        :param description: The description of this ModelParameterConfigOutput.  # noqa: E501
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
        if not isinstance(other, ModelParameterConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelParameterConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
