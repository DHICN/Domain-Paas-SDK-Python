# coding: utf-8

"""
    result-analysis-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dhicn_result_analysis_service.api_client import ApiClient
from dhicn_result_analysis_service.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UrbanFloodingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_result_urban_flooding_flooding_area_by_page_get(self, scenario_id, **kwargs):  # noqa: E501
        """分页查询内涝积水区域信息 Get flooding area  # noqa: E501

        分页查询内涝方案的结果中，所有最大积水深度大于指定水深阈值的网格信息Get elements in the flooding area whose maximum water depth are above the specified threshold of a flood scenario.  order by elements id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_flooding_area_by_page_get(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param int page_index: 分页的序号，从1开始 page index, start from 1
        :param int page_size: 分页的大小 page size
        :param float threshold: 内涝积水深度阈值 flood water depth threshold
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: StringPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_result_urban_flooding_flooding_area_by_page_get_with_http_info(scenario_id, **kwargs)  # noqa: E501

    def api_v1_result_urban_flooding_flooding_area_by_page_get_with_http_info(self, scenario_id, **kwargs):  # noqa: E501
        """分页查询内涝积水区域信息 Get flooding area  # noqa: E501

        分页查询内涝方案的结果中，所有最大积水深度大于指定水深阈值的网格信息Get elements in the flooding area whose maximum water depth are above the specified threshold of a flood scenario.  order by elements id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_flooding_area_by_page_get_with_http_info(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param int page_index: 分页的序号，从1开始 page index, start from 1
        :param int page_size: 分页的大小 page size
        :param float threshold: 内涝积水深度阈值 flood water depth threshold
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(StringPage, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'scenario_id',
            'page_index',
            'page_size',
            'threshold'
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
                    " to method api_v1_result_urban_flooding_flooding_area_by_page_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scenario_id' is set
        if self.api_client.client_side_validation and ('scenario_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['scenario_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scenario_id` when calling `api_v1_result_urban_flooding_flooding_area_by_page_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_index' in local_var_params and local_var_params['page_index'] is not None:  # noqa: E501
            query_params.append(('PageIndex', local_var_params['page_index']))  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('PageSize', local_var_params['page_size']))  # noqa: E501
        if 'threshold' in local_var_params and local_var_params['threshold'] is not None:  # noqa: E501
            query_params.append(('Threshold', local_var_params['threshold']))  # noqa: E501
        if 'scenario_id' in local_var_params and local_var_params['scenario_id'] is not None:  # noqa: E501
            query_params.append(('ScenarioId', local_var_params['scenario_id']))  # noqa: E501

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
            '/api/v1/result/urban-flooding/flooding-area/by-page', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StringPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_result_urban_flooding_flooding_area_get(self, scenario_id, **kwargs):  # noqa: E501
        """获取内涝积水区域信息 Get flooding area  # noqa: E501

        获取内涝方案的结果中，所有最大积水深度大于指定水深阈值的网格信息 Get all the elements in the flooding area whose maximum water depth are above the specified threshold of a flood scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_flooding_area_get(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param float threshold: 内涝积水深度阈值 flood water depth threshold
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_result_urban_flooding_flooding_area_get_with_http_info(scenario_id, **kwargs)  # noqa: E501

    def api_v1_result_urban_flooding_flooding_area_get_with_http_info(self, scenario_id, **kwargs):  # noqa: E501
        """获取内涝积水区域信息 Get flooding area  # noqa: E501

        获取内涝方案的结果中，所有最大积水深度大于指定水深阈值的网格信息 Get all the elements in the flooding area whose maximum water depth are above the specified threshold of a flood scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_flooding_area_get_with_http_info(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param float threshold: 内涝积水深度阈值 flood water depth threshold
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[str], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'scenario_id',
            'threshold'
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
                    " to method api_v1_result_urban_flooding_flooding_area_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scenario_id' is set
        if self.api_client.client_side_validation and ('scenario_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['scenario_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scenario_id` when calling `api_v1_result_urban_flooding_flooding_area_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'threshold' in local_var_params and local_var_params['threshold'] is not None:  # noqa: E501
            query_params.append(('Threshold', local_var_params['threshold']))  # noqa: E501
        if 'scenario_id' in local_var_params and local_var_params['scenario_id'] is not None:  # noqa: E501
            query_params.append(('ScenarioId', local_var_params['scenario_id']))  # noqa: E501

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
            '/api/v1/result/urban-flooding/flooding-area', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_result_urban_flooding_flooding_risk_get(self, scenario_id, **kwargs):  # noqa: E501
        """获取洪水风险信息 Get Flood risk  result  # noqa: E501

        获取内涝方案的不同等级洪水风险区域信息，包括风险区域的几何形状和面积等 Get flood risk area information, including geometry and area of a flood scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_flooding_risk_get(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[FloodingRiskInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_result_urban_flooding_flooding_risk_get_with_http_info(scenario_id, **kwargs)  # noqa: E501

    def api_v1_result_urban_flooding_flooding_risk_get_with_http_info(self, scenario_id, **kwargs):  # noqa: E501
        """获取洪水风险信息 Get Flood risk  result  # noqa: E501

        获取内涝方案的不同等级洪水风险区域信息，包括风险区域的几何形状和面积等 Get flood risk area information, including geometry and area of a flood scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_flooding_risk_get_with_http_info(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[FloodingRiskInfo], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'scenario_id'
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
                    " to method api_v1_result_urban_flooding_flooding_risk_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scenario_id' is set
        if self.api_client.client_side_validation and ('scenario_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['scenario_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scenario_id` when calling `api_v1_result_urban_flooding_flooding_risk_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scenario_id' in local_var_params and local_var_params['scenario_id'] is not None:  # noqa: E501
            query_params.append(('ScenarioId', local_var_params['scenario_id']))  # noqa: E501

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
            '/api/v1/result/urban-flooding/flooding-risk', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FloodingRiskInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_result_urban_flooding_sensitive_points_statistics_get(self, scenario_id, **kwargs):  # noqa: E501
        """获取易涝点统计信息 Get flood sensitive points statistics  # noqa: E501

        获取内涝方案的易涝点统计结果，每个易涝点返回一组平均水深、最小水深、最大水深的时间序列 Get average water depth,min water depth and max water depth of all the flood sensitive points of a flood scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_sensitive_points_statistics_get(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[SensitivePointsStatistic]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_result_urban_flooding_sensitive_points_statistics_get_with_http_info(scenario_id, **kwargs)  # noqa: E501

    def api_v1_result_urban_flooding_sensitive_points_statistics_get_with_http_info(self, scenario_id, **kwargs):  # noqa: E501
        """获取易涝点统计信息 Get flood sensitive points statistics  # noqa: E501

        获取内涝方案的易涝点统计结果，每个易涝点返回一组平均水深、最小水深、最大水深的时间序列 Get average water depth,min water depth and max water depth of all the flood sensitive points of a flood scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_result_urban_flooding_sensitive_points_statistics_get_with_http_info(scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scenario_id: 方案的ID scenario’s ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[SensitivePointsStatistic], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'scenario_id'
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
                    " to method api_v1_result_urban_flooding_sensitive_points_statistics_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scenario_id' is set
        if self.api_client.client_side_validation and ('scenario_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['scenario_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scenario_id` when calling `api_v1_result_urban_flooding_sensitive_points_statistics_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scenario_id' in local_var_params and local_var_params['scenario_id'] is not None:  # noqa: E501
            query_params.append(('ScenarioId', local_var_params['scenario_id']))  # noqa: E501

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
            '/api/v1/result/urban-flooding/sensitive-points-statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SensitivePointsStatistic]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
