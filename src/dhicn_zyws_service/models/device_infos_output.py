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


class DeviceInfosOutput(object):
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
        'label': 'str',
        'type': 'str',
        'description': 'str',
        'attributes': 'list[StringStringKeyValue]',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'type': 'type',
        'description': 'description',
        'attributes': 'attributes',
        'id': 'id'
    }

    def __init__(self, name=None, label=None, type=None, description=None, attributes=None, id=None, local_vars_configuration=None):  # noqa: E501
        """DeviceInfosOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._label = None
        self._type = None
        self._description = None
        self._attributes = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.label = label
        self.type = type
        self.description = description
        self.attributes = attributes
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this DeviceInfosOutput.  # noqa: E501


        :return: The name of this DeviceInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceInfosOutput.


        :param name: The name of this DeviceInfosOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this DeviceInfosOutput.  # noqa: E501


        :return: The label of this DeviceInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DeviceInfosOutput.


        :param label: The label of this DeviceInfosOutput.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this DeviceInfosOutput.  # noqa: E501


        :return: The type of this DeviceInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceInfosOutput.


        :param type: The type of this DeviceInfosOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this DeviceInfosOutput.  # noqa: E501


        :return: The description of this DeviceInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceInfosOutput.


        :param description: The description of this DeviceInfosOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def attributes(self):
        """Gets the attributes of this DeviceInfosOutput.  # noqa: E501


        :return: The attributes of this DeviceInfosOutput.  # noqa: E501
        :rtype: list[StringStringKeyValue]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DeviceInfosOutput.


        :param attributes: The attributes of this DeviceInfosOutput.  # noqa: E501
        :type: list[StringStringKeyValue]
        """

        self._attributes = attributes

    @property
    def id(self):
        """Gets the id of this DeviceInfosOutput.  # noqa: E501


        :return: The id of this DeviceInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceInfosOutput.


        :param id: The id of this DeviceInfosOutput.  # noqa: E501
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
        if not isinstance(other, DeviceInfosOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceInfosOutput):
            return True

        return self.to_dict() != other.to_dict()
