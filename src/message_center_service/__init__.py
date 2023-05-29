# coding: utf-8

# flake8: noqa

"""
    message-center-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from message_center_service.api.message_type_api import MessageTypeApi
from message_center_service.api.message_type_temp_local_api import MessageTypeTempLocalApi
from message_center_service.api.task_schedule_api import TaskScheduleApi
from message_center_service.api.uni_push_api import UniPushApi
from message_center_service.api.user_client_api import UserClientApi
from message_center_service.api.user_message_center_api import UserMessageCenterApi

# import ApiClient
from message_center_service.api_client import ApiClient
from message_center_service.configuration import Configuration
from message_center_service.exceptions import OpenApiException
from message_center_service.exceptions import ApiTypeError
from message_center_service.exceptions import ApiValueError
from message_center_service.exceptions import ApiKeyError
from message_center_service.exceptions import ApiException
# import models into sdk package
from message_center_service.models.add_message_type_input import AddMessageTypeInput
from message_center_service.models.add_msg_type_temp_local_input import AddMsgTypeTempLocalInput
from message_center_service.models.add_user_msg import AddUserMsg
from message_center_service.models.count_by_level import CountByLevel
from message_center_service.models.delete_client_input import DeleteClientInput
from message_center_service.models.get_lastest_message_input import GetLastestMessageInput
from message_center_service.models.last_msg import LastMsg
from message_center_service.models.lastest_message_by_msg_type_input import LastestMessageByMsgTypeInput
from message_center_service.models.message_type_output import MessageTypeOutput
from message_center_service.models.message_type_output_page import MessageTypeOutputPage
from message_center_service.models.msg_template_obj import MsgTemplateObj
from message_center_service.models.msg_type_temp_local_output import MsgTypeTempLocalOutput
from message_center_service.models.msg_type_temp_local_output_page import MsgTypeTempLocalOutputPage
from message_center_service.models.remote_service_error_info import RemoteServiceErrorInfo
from message_center_service.models.remote_service_error_response import RemoteServiceErrorResponse
from message_center_service.models.remote_service_validation_error_info import RemoteServiceValidationErrorInfo
from message_center_service.models.save_client_input import SaveClientInput
from message_center_service.models.unread_count_query_input import UnreadCountQueryInput
from message_center_service.models.unread_count_query_output import UnreadCountQueryOutput
from message_center_service.models.update_message_type_input import UpdateMessageTypeInput
from message_center_service.models.update_msg_type_temp_local_input import UpdateMsgTypeTempLocalInput
from message_center_service.models.update_user_msg_status import UpdateUserMsgStatus
from message_center_service.models.user_message_object import UserMessageObject
from message_center_service.models.user_msg_output import UserMsgOutput
from message_center_service.models.user_msg_output_page import UserMsgOutputPage

