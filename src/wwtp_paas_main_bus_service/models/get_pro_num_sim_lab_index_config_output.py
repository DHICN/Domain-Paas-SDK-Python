# coding: utf-8

"""
    wwtp-paas-main-bus-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from wwtp_paas_main_bus_service.configuration import Configuration


class GetProNumSimLabIndexConfigOutput(object):
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
        'code': 'str',
        'model_nodes': 'ScenarioModelNodeDto',
        'output_file': 'str',
        'rem_rate_file': 'str',
        'id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'model_nodes': 'modelNodes',
        'output_file': 'outputFile',
        'rem_rate_file': 'remRateFile',
        'id': 'id'
    }

    def __init__(self, code=None, model_nodes=None, output_file=None, rem_rate_file=None, id=None, local_vars_configuration=None):  # noqa: E501
        """GetProNumSimLabIndexConfigOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._model_nodes = None
        self._output_file = None
        self._rem_rate_file = None
        self._id = None
        self.discriminator = None

        self.code = code
        self.model_nodes = model_nodes
        self.output_file = output_file
        self.rem_rate_file = rem_rate_file
        if id is not None:
            self.id = id

    @property
    def code(self):
        """Gets the code of this GetProNumSimLabIndexConfigOutput.  # noqa: E501

        指标名称  # noqa: E501

        :return: The code of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GetProNumSimLabIndexConfigOutput.

        指标名称  # noqa: E501

        :param code: The code of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def model_nodes(self):
        """Gets the model_nodes of this GetProNumSimLabIndexConfigOutput.  # noqa: E501


        :return: The model_nodes of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :rtype: ScenarioModelNodeDto
        """
        return self._model_nodes

    @model_nodes.setter
    def model_nodes(self, model_nodes):
        """Sets the model_nodes of this GetProNumSimLabIndexConfigOutput.


        :param model_nodes: The model_nodes of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :type: ScenarioModelNodeDto
        """
        if self.local_vars_configuration.client_side_validation and model_nodes is None:  # noqa: E501
            raise ValueError("Invalid value for `model_nodes`, must not be `None`")  # noqa: E501

        self._model_nodes = model_nodes

    @property
    def output_file(self):
        """Gets the output_file of this GetProNumSimLabIndexConfigOutput.  # noqa: E501

        计算结果值,存入的文件名  # noqa: E501

        :return: The output_file of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file):
        """Sets the output_file of this GetProNumSimLabIndexConfigOutput.

        计算结果值,存入的文件名  # noqa: E501

        :param output_file: The output_file of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and output_file is None:  # noqa: E501
            raise ValueError("Invalid value for `output_file`, must not be `None`")  # noqa: E501

        self._output_file = output_file

    @property
    def rem_rate_file(self):
        """Gets the rem_rate_file of this GetProNumSimLabIndexConfigOutput.  # noqa: E501

        去除率结果值,存入的文件名  # noqa: E501

        :return: The rem_rate_file of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._rem_rate_file

    @rem_rate_file.setter
    def rem_rate_file(self, rem_rate_file):
        """Sets the rem_rate_file of this GetProNumSimLabIndexConfigOutput.

        去除率结果值,存入的文件名  # noqa: E501

        :param rem_rate_file: The rem_rate_file of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rem_rate_file is None:  # noqa: E501
            raise ValueError("Invalid value for `rem_rate_file`, must not be `None`")  # noqa: E501

        self._rem_rate_file = rem_rate_file

    @property
    def id(self):
        """Gets the id of this GetProNumSimLabIndexConfigOutput.  # noqa: E501


        :return: The id of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProNumSimLabIndexConfigOutput.


        :param id: The id of this GetProNumSimLabIndexConfigOutput.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, GetProNumSimLabIndexConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetProNumSimLabIndexConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
