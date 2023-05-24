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


class OutputModelPrecisionOutput(object):
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
        'time': 'datetime',
        'step_value': 'float',
        'precision_diff_value': 'float',
        'node_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'step_value': 'stepValue',
        'precision_diff_value': 'precisionDiffValue',
        'node_code': 'nodeCode'
    }

    def __init__(self, id=None, time=None, step_value=None, precision_diff_value=None, node_code=None, local_vars_configuration=None):  # noqa: E501
        """OutputModelPrecisionOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._time = None
        self._step_value = None
        self._precision_diff_value = None
        self._node_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if time is not None:
            self.time = time
        if step_value is not None:
            self.step_value = step_value
        if precision_diff_value is not None:
            self.precision_diff_value = precision_diff_value
        self.node_code = node_code

    @property
    def id(self):
        """Gets the id of this OutputModelPrecisionOutput.  # noqa: E501


        :return: The id of this OutputModelPrecisionOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OutputModelPrecisionOutput.


        :param id: The id of this OutputModelPrecisionOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this OutputModelPrecisionOutput.  # noqa: E501

        时间 time  # noqa: E501

        :return: The time of this OutputModelPrecisionOutput.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OutputModelPrecisionOutput.

        时间 time  # noqa: E501

        :param time: The time of this OutputModelPrecisionOutput.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def step_value(self):
        """Gets the step_value of this OutputModelPrecisionOutput.  # noqa: E501

        精度百分比 precision ratio (onlineValue - modelResultValue / onlineValue)  # noqa: E501

        :return: The step_value of this OutputModelPrecisionOutput.  # noqa: E501
        :rtype: float
        """
        return self._step_value

    @step_value.setter
    def step_value(self, step_value):
        """Sets the step_value of this OutputModelPrecisionOutput.

        精度百分比 precision ratio (onlineValue - modelResultValue / onlineValue)  # noqa: E501

        :param step_value: The step_value of this OutputModelPrecisionOutput.  # noqa: E501
        :type: float
        """

        self._step_value = step_value

    @property
    def precision_diff_value(self):
        """Gets the precision_diff_value of this OutputModelPrecisionOutput.  # noqa: E501

        精度差值 precision difference (onlineValue - modelResultValue)  # noqa: E501

        :return: The precision_diff_value of this OutputModelPrecisionOutput.  # noqa: E501
        :rtype: float
        """
        return self._precision_diff_value

    @precision_diff_value.setter
    def precision_diff_value(self, precision_diff_value):
        """Sets the precision_diff_value of this OutputModelPrecisionOutput.

        精度差值 precision difference (onlineValue - modelResultValue)  # noqa: E501

        :param precision_diff_value: The precision_diff_value of this OutputModelPrecisionOutput.  # noqa: E501
        :type: float
        """

        self._precision_diff_value = precision_diff_value

    @property
    def node_code(self):
        """Gets the node_code of this OutputModelPrecisionOutput.  # noqa: E501

        模型节点 model node  # noqa: E501

        :return: The node_code of this OutputModelPrecisionOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_code

    @node_code.setter
    def node_code(self, node_code):
        """Sets the node_code of this OutputModelPrecisionOutput.

        模型节点 model node  # noqa: E501

        :param node_code: The node_code of this OutputModelPrecisionOutput.  # noqa: E501
        :type: str
        """

        self._node_code = node_code

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
        if not isinstance(other, OutputModelPrecisionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutputModelPrecisionOutput):
            return True

        return self.to_dict() != other.to_dict()
