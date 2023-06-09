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

from dhicn_wwtp_infrastructure_service.configuration import Configuration


class ModelNodeConfig(object):
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
        'tenant_id': 'str',
        'node_code': 'str',
        'node_name': 'str',
        'unit': 'str',
        'data_type': 'str',
        'model_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenantId',
        'node_code': 'nodeCode',
        'node_name': 'nodeName',
        'unit': 'unit',
        'data_type': 'dataType',
        'model_name': 'modelName'
    }

    def __init__(self, id=None, tenant_id=None, node_code=None, node_name=None, unit=None, data_type=None, model_name=None, local_vars_configuration=None):  # noqa: E501
        """ModelNodeConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._tenant_id = None
        self._node_code = None
        self._node_name = None
        self._unit = None
        self._data_type = None
        self._model_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.tenant_id = tenant_id
        self.node_code = node_code
        self.node_name = node_name
        self.unit = unit
        self.data_type = data_type
        self.model_name = model_name

    @property
    def id(self):
        """Gets the id of this ModelNodeConfig.  # noqa: E501


        :return: The id of this ModelNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelNodeConfig.


        :param id: The id of this ModelNodeConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ModelNodeConfig.  # noqa: E501


        :return: The tenant_id of this ModelNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ModelNodeConfig.


        :param tenant_id: The tenant_id of this ModelNodeConfig.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def node_code(self):
        """Gets the node_code of this ModelNodeConfig.  # noqa: E501


        :return: The node_code of this ModelNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._node_code

    @node_code.setter
    def node_code(self, node_code):
        """Sets the node_code of this ModelNodeConfig.


        :param node_code: The node_code of this ModelNodeConfig.  # noqa: E501
        :type: str
        """

        self._node_code = node_code

    @property
    def node_name(self):
        """Gets the node_name of this ModelNodeConfig.  # noqa: E501


        :return: The node_name of this ModelNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this ModelNodeConfig.


        :param node_name: The node_name of this ModelNodeConfig.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def unit(self):
        """Gets the unit of this ModelNodeConfig.  # noqa: E501


        :return: The unit of this ModelNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ModelNodeConfig.


        :param unit: The unit of this ModelNodeConfig.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def data_type(self):
        """Gets the data_type of this ModelNodeConfig.  # noqa: E501


        :return: The data_type of this ModelNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ModelNodeConfig.


        :param data_type: The data_type of this ModelNodeConfig.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def model_name(self):
        """Gets the model_name of this ModelNodeConfig.  # noqa: E501


        :return: The model_name of this ModelNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this ModelNodeConfig.


        :param model_name: The model_name of this ModelNodeConfig.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

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
        if not isinstance(other, ModelNodeConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelNodeConfig):
            return True

        return self.to_dict() != other.to_dict()
