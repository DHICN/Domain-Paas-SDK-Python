# coding: utf-8

"""
    digital-twin-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from digital_twin_service.api_client import ApiClient
from digital_twin_service.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ModelPointApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_model_point_attributes_get(self, template_scenario_id, model_id, **kwargs):  # noqa: E501
        """获取指定模型点位的详细信息 Get model point detailed information by id  # noqa: E501

        根据ID查询模型点位的详细信息，包括属性值 Get model point detailed information by id, including attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_attributes_get(template_scenario_id, model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str template_scenario_id: 模板方案ID template scenario id (required)
        :param str model_id: 模型中的ID model muid (required)
        :param str model_point_type: 模型点位类型 model point type
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ModelPointOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_model_point_attributes_get_with_http_info(template_scenario_id, model_id, **kwargs)  # noqa: E501

    def api_v1_model_point_attributes_get_with_http_info(self, template_scenario_id, model_id, **kwargs):  # noqa: E501
        """获取指定模型点位的详细信息 Get model point detailed information by id  # noqa: E501

        根据ID查询模型点位的详细信息，包括属性值 Get model point detailed information by id, including attributes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_attributes_get_with_http_info(template_scenario_id, model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str template_scenario_id: 模板方案ID template scenario id (required)
        :param str model_id: 模型中的ID model muid (required)
        :param str model_point_type: 模型点位类型 model point type
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ModelPointOutput, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'template_scenario_id',
            'model_id',
            'model_point_type'
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
                    " to method api_v1_model_point_attributes_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'template_scenario_id' is set
        if self.api_client.client_side_validation and ('template_scenario_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['template_scenario_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `template_scenario_id` when calling `api_v1_model_point_attributes_get`")  # noqa: E501
        # verify the required parameter 'model_id' is set
        if self.api_client.client_side_validation and ('model_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['model_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `model_id` when calling `api_v1_model_point_attributes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_scenario_id' in local_var_params and local_var_params['template_scenario_id'] is not None:  # noqa: E501
            query_params.append(('TemplateScenarioId', local_var_params['template_scenario_id']))  # noqa: E501
        if 'model_id' in local_var_params and local_var_params['model_id'] is not None:  # noqa: E501
            query_params.append(('ModelId', local_var_params['model_id']))  # noqa: E501
        if 'model_point_type' in local_var_params and local_var_params['model_point_type'] is not None:  # noqa: E501
            query_params.append(('ModelPointType', local_var_params['model_point_type']))  # noqa: E501

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
            '/api/v1/model-point/attributes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelPointOutput',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_model_point_page_search_by_type_post(self, **kwargs):  # noqa: E501
        """根据点位类型获取模型点位的详细信息 Get model point detailed information by point type  # noqa: E501

        根据点位类型查询模型点位的详细信息，包括属性值，同时可利用ModelIds对返回的模型点位进行过滤 Get model point detailed information by point type, including attributes, meanwhile ModelIds can be used to filter the model points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_page_search_by_type_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryPageModelPointByTypeInput query_page_model_point_by_type_input:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ModelPointOutputPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_model_point_page_search_by_type_post_with_http_info(**kwargs)  # noqa: E501

    def api_v1_model_point_page_search_by_type_post_with_http_info(self, **kwargs):  # noqa: E501
        """根据点位类型获取模型点位的详细信息 Get model point detailed information by point type  # noqa: E501

        根据点位类型查询模型点位的详细信息，包括属性值，同时可利用ModelIds对返回的模型点位进行过滤 Get model point detailed information by point type, including attributes, meanwhile ModelIds can be used to filter the model points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_page_search_by_type_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryPageModelPointByTypeInput query_page_model_point_by_type_input:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ModelPointOutputPage, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'query_page_model_point_by_type_input'
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
                    " to method api_v1_model_point_page_search_by_type_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query_page_model_point_by_type_input' in local_var_params:
            body_params = local_var_params['query_page_model_point_by_type_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/model-point/page-search-by-type', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelPointOutputPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_model_point_search_by_condition_post(self, **kwargs):  # noqa: E501
        """根据属性获取模型点位的详细信息  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_search_by_condition_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryModelPointByConditionInput query_model_point_by_condition_input:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ModelPointOutput]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_model_point_search_by_condition_post_with_http_info(**kwargs)  # noqa: E501

    def api_v1_model_point_search_by_condition_post_with_http_info(self, **kwargs):  # noqa: E501
        """根据属性获取模型点位的详细信息  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_search_by_condition_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryModelPointByConditionInput query_model_point_by_condition_input:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ModelPointOutput], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'query_model_point_by_condition_input'
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
                    " to method api_v1_model_point_search_by_condition_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query_model_point_by_condition_input' in local_var_params:
            body_params = local_var_params['query_model_point_by_condition_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/model-point/search-by-condition', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelPointOutput]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_model_point_search_by_model_id_post(self, **kwargs):  # noqa: E501
        """根据模型点位id获取模型点位的详细信息 Get model point detailed information by model id  # noqa: E501

        根据模型点位id查询模型点位的详细信息，包括属性值，同时可利用ModelIds对返回的模型点位进行过滤 Get model point detailed information by model id, including attributes, meanwhile ModelIds can be used to filter the model points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_search_by_model_id_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryModelPointByIdsInput query_model_point_by_ids_input:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ModelPointOutput]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_model_point_search_by_model_id_post_with_http_info(**kwargs)  # noqa: E501

    def api_v1_model_point_search_by_model_id_post_with_http_info(self, **kwargs):  # noqa: E501
        """根据模型点位id获取模型点位的详细信息 Get model point detailed information by model id  # noqa: E501

        根据模型点位id查询模型点位的详细信息，包括属性值，同时可利用ModelIds对返回的模型点位进行过滤 Get model point detailed information by model id, including attributes, meanwhile ModelIds can be used to filter the model points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_search_by_model_id_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryModelPointByIdsInput query_model_point_by_ids_input:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ModelPointOutput], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'query_model_point_by_ids_input'
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
                    " to method api_v1_model_point_search_by_model_id_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query_model_point_by_ids_input' in local_var_params:
            body_params = local_var_params['query_model_point_by_ids_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/model-point/search-by-model-id', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelPointOutput]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_model_point_search_by_type_post(self, **kwargs):  # noqa: E501
        """根据点位类型获取模型点位的详细信息 Get model point detailed information by point type  # noqa: E501

        根据点位类型查询模型点位的详细信息，包括属性值，同时可利用ModelIds对返回的模型点位进行过滤 Get model point detailed information by point type, including attributes, meanwhile ModelIds can be used to filter the model points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_search_by_type_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryModelPointByTypeInput query_model_point_by_type_input:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ModelPointOutput]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_model_point_search_by_type_post_with_http_info(**kwargs)  # noqa: E501

    def api_v1_model_point_search_by_type_post_with_http_info(self, **kwargs):  # noqa: E501
        """根据点位类型获取模型点位的详细信息 Get model point detailed information by point type  # noqa: E501

        根据点位类型查询模型点位的详细信息，包括属性值，同时可利用ModelIds对返回的模型点位进行过滤 Get model point detailed information by point type, including attributes, meanwhile ModelIds can be used to filter the model points  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_model_point_search_by_type_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param QueryModelPointByTypeInput query_model_point_by_type_input:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ModelPointOutput], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'query_model_point_by_type_input'
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
                    " to method api_v1_model_point_search_by_type_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query_model_point_by_type_input' in local_var_params:
            body_params = local_var_params['query_model_point_by_type_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/model-point/search-by-type', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelPointOutput]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)