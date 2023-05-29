# coding: utf-8

"""
    accident-manager-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from accident_manager_service.configuration import Configuration


class ComponentInfo(object):
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
        'code': 'str',
        'name': 'str',
        'event_id': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'event_id': 'eventId',
        'remark': 'remark'
    }

    def __init__(self, id=None, code=None, name=None, event_id=None, remark=None, local_vars_configuration=None):  # noqa: E501
        """ComponentInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._code = None
        self._name = None
        self._event_id = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.code = code
        self.name = name
        if event_id is not None:
            self.event_id = event_id
        self.remark = remark

    @property
    def id(self):
        """Gets the id of this ComponentInfo.  # noqa: E501

        污染物ID pollutant id  # noqa: E501

        :return: The id of this ComponentInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentInfo.

        污染物ID pollutant id  # noqa: E501

        :param id: The id of this ComponentInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this ComponentInfo.  # noqa: E501

        污染物代码 pollutant code  # noqa: E501

        :return: The code of this ComponentInfo.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ComponentInfo.

        污染物代码 pollutant code  # noqa: E501

        :param code: The code of this ComponentInfo.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this ComponentInfo.  # noqa: E501

        污染物名称 pollutant name  # noqa: E501

        :return: The name of this ComponentInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentInfo.

        污染物名称 pollutant name  # noqa: E501

        :param name: The name of this ComponentInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def event_id(self):
        """Gets the event_id of this ComponentInfo.  # noqa: E501

        事件ID event id  # noqa: E501

        :return: The event_id of this ComponentInfo.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ComponentInfo.

        事件ID event id  # noqa: E501

        :param event_id: The event_id of this ComponentInfo.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def remark(self):
        """Gets the remark of this ComponentInfo.  # noqa: E501

        污染物备注 pollutant remark  # noqa: E501

        :return: The remark of this ComponentInfo.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ComponentInfo.

        污染物备注 pollutant remark  # noqa: E501

        :param remark: The remark of this ComponentInfo.  # noqa: E501
        :type: str
        """

        self._remark = remark

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
        if not isinstance(other, ComponentInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentInfo):
            return True

        return self.to_dict() != other.to_dict()
