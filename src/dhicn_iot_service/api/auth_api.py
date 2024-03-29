# coding: utf-8

"""
    IoT服务

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dhicn_iot_service.api_client import ApiClient
from dhicn_iot_service.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AuthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_iot_turn_on_iot_func_get(self, user_manager_tenant_id, tripartite_tenant_name, **kwargs):  # noqa: E501
        """启用租户的IoT功能 Enable tenant IOT function  # noqa: E501

        此接口用于动态创建租户，并自动在IoT服务中创建租户和租户管理员账户 This interface is used to dynamically create tenants and automatically generate tenant and tenant administrator accounts in IOT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_iot_turn_on_iot_func_get(user_manager_tenant_id, tripartite_tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_manager_tenant_id: 用户管理系统租户ID tenant id in user management system (required)
        :param str tripartite_tenant_name: 第三方系统租户名称 tripartite tenant name (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_iot_turn_on_iot_func_get_with_http_info(user_manager_tenant_id, tripartite_tenant_name, **kwargs)  # noqa: E501

    def api_v1_iot_turn_on_iot_func_get_with_http_info(self, user_manager_tenant_id, tripartite_tenant_name, **kwargs):  # noqa: E501
        """启用租户的IoT功能 Enable tenant IOT function  # noqa: E501

        此接口用于动态创建租户，并自动在IoT服务中创建租户和租户管理员账户 This interface is used to dynamically create tenants and automatically generate tenant and tenant administrator accounts in IOT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_iot_turn_on_iot_func_get_with_http_info(user_manager_tenant_id, tripartite_tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_manager_tenant_id: 用户管理系统租户ID tenant id in user management system (required)
        :param str tripartite_tenant_name: 第三方系统租户名称 tripartite tenant name (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'user_manager_tenant_id',
            'tripartite_tenant_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_iot_turn_on_iot_func_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_manager_tenant_id' is set
        if self.api_client.client_side_validation and ('user_manager_tenant_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_manager_tenant_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_manager_tenant_id` when calling `api_v1_iot_turn_on_iot_func_get`")  # noqa: E501
        # verify the required parameter 'tripartite_tenant_name' is set
        if self.api_client.client_side_validation and ('tripartite_tenant_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['tripartite_tenant_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tripartite_tenant_name` when calling `api_v1_iot_turn_on_iot_func_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_manager_tenant_id' in local_var_params and local_var_params['user_manager_tenant_id'] is not None:  # noqa: E501
            query_params.append(('UserManagerTenantId', local_var_params['user_manager_tenant_id']))  # noqa: E501
        if 'tripartite_tenant_name' in local_var_params and local_var_params['tripartite_tenant_name'] is not None:  # noqa: E501
            query_params.append(('TripartiteTenantName', local_var_params['tripartite_tenant_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/iot/turn-on-iot-func', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
