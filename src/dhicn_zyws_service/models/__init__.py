# coding: utf-8

# flake8: noqa
"""
    竹园污水项目

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from dhicn_zyws_service.models.add_control_device_input import AddControlDeviceInput
from dhicn_zyws_service.models.add_dam_gate_scenario_input import AddDamGateScenarioInput
from dhicn_zyws_service.models.add_orifice_result_input import AddOrificeResultInput
from dhicn_zyws_service.models.add_principle_input import AddPrincipleInput
from dhicn_zyws_service.models.all_global_principles_output import AllGlobalPrinciplesOutput
from dhicn_zyws_service.models.apply_schedule_suggestions_input import ApplyScheduleSuggestionsInput
from dhicn_zyws_service.models.apply_to_auto_input import ApplyToAutoInput
from dhicn_zyws_service.models.asset_info_output import AssetInfoOutput
from dhicn_zyws_service.models.asset_rel import AssetRel
from dhicn_zyws_service.models.calculate_orifice_height_input import CalculateOrificeHeightInput
from dhicn_zyws_service.models.configuration_model import ConfigurationModel
from dhicn_zyws_service.models.control_device import ControlDevice
from dhicn_zyws_service.models.control_device_details import ControlDeviceDetails
from dhicn_zyws_service.models.control_device_output import ControlDeviceOutput
from dhicn_zyws_service.models.control_device_ts_details import ControlDeviceTsDetails
from dhicn_zyws_service.models.control_devices_input import ControlDevicesInput
from dhicn_zyws_service.models.control_devices_output import ControlDevicesOutput
from dhicn_zyws_service.models.control_devices_ts import ControlDevicesTs
from dhicn_zyws_service.models.control_devices_ts_input import ControlDevicesTsInput
from dhicn_zyws_service.models.control_devices_ts_output import ControlDevicesTsOutput
from dhicn_zyws_service.models.control_orifice_discharge_output import ControlOrificeDischargeOutput
from dhicn_zyws_service.models.control_orifice_height_output import ControlOrificeHeightOutput
from dhicn_zyws_service.models.create_plan_scenario_input import CreatePlanScenarioInput
from dhicn_zyws_service.models.dam_gate_configuration import DamGateConfiguration
from dhicn_zyws_service.models.dam_gate_configuration_input_output import DamGateConfigurationInputOutput
from dhicn_zyws_service.models.dam_gate_default_output import DamGateDefaultOutput
from dhicn_zyws_service.models.dam_gate_height_list_input import DamGateHeightListInput
from dhicn_zyws_service.models.dam_gate_info import DamGateInfo
from dhicn_zyws_service.models.dam_gate_list_output import DamGateListOutput
from dhicn_zyws_service.models.dam_gate_scenario_output import DamGateScenarioOutput
from dhicn_zyws_service.models.dam_gate_status_info import DamGateStatusInfo
from dhicn_zyws_service.models.data_result import DataResult
from dhicn_zyws_service.models.device_infos_output import DeviceInfosOutput
from dhicn_zyws_service.models.device_rel import DeviceRel
from dhicn_zyws_service.models.devices_list import DevicesList
from dhicn_zyws_service.models.factory_config import FactoryConfig
from dhicn_zyws_service.models.factory_opened_ofirice_count_output import FactoryOpenedOfiriceCountOutput
from dhicn_zyws_service.models.factory_opened_orifice_count_output import FactoryOpenedOrificeCountOutput
from dhicn_zyws_service.models.get_dam_gate_scenario_input import GetDamGateScenarioInput
from dhicn_zyws_service.models.get_measure_and_simul_data_input import GetMeasureAndSimulDataInput
from dhicn_zyws_service.models.get_orifice_contorl_result_input import GetOrificeContorlResultInput
from dhicn_zyws_service.models.get_orifice_control_result_input import GetOrificeControlResultInput
from dhicn_zyws_service.models.get_orifice_time_series_input import GetOrificeTimeSeriesInput
from dhicn_zyws_service.models.get_result_statistic_input import GetResultStatisticInput
from dhicn_zyws_service.models.get_schedule_suggestions_input import GetScheduleSuggestionsInput
from dhicn_zyws_service.models.get_schedule_suggestions_output import GetScheduleSuggestionsOutput
from dhicn_zyws_service.models.global_principles_details_input import GlobalPrinciplesDetailsInput
from dhicn_zyws_service.models.history_schedule_suggestion_record import HistoryScheduleSuggestionRecord
from dhicn_zyws_service.models.history_schedule_suggestion_record_dto import HistoryScheduleSuggestionRecordDto
from dhicn_zyws_service.models.ids_input import IdsInput
from dhicn_zyws_service.models.inlet_excel_data import InletExcelData
from dhicn_zyws_service.models.inlet_excel_download_input import InletExcelDownloadInput
from dhicn_zyws_service.models.inline_object import InlineObject
from dhicn_zyws_service.models.latest_opened_orifice_count_output import LatestOpenedOrificeCountOutput
from dhicn_zyws_service.models.latest_recommend_output import LatestRecommendOutput
from dhicn_zyws_service.models.latest_time_series_input_v3 import LatestTimeSeriesInputV3
from dhicn_zyws_service.models.latest_time_series_output import LatestTimeSeriesOutput
from dhicn_zyws_service.models.latest_warning_output import LatestWarningOutput
from dhicn_zyws_service.models.multiple_tenant_data_input import MultipleTenantDataInput
from dhicn_zyws_service.models.multiple_tenant_data_output import MultipleTenantDataOutput
from dhicn_zyws_service.models.mutilple_tenant_batch_data_input import MutilpleTenantBatchDataInput
from dhicn_zyws_service.models.mutilple_tenant_batch_data_output import MutilpleTenantBatchDataOutput
from dhicn_zyws_service.models.mutilple_tenant_data_input import MutilpleTenantDataInput
from dhicn_zyws_service.models.mutilple_tenant_data_output import MutilpleTenantDataOutput
from dhicn_zyws_service.models.node_input import NodeInput
from dhicn_zyws_service.models.node_volume_output import NodeVolumeOutput
from dhicn_zyws_service.models.orifice_contorl_result_output import OrificeContorlResultOutput
from dhicn_zyws_service.models.orifice_control_result_output import OrificeControlResultOutput
from dhicn_zyws_service.models.orifice_result_output import OrificeResultOutput
from dhicn_zyws_service.models.orifice_schedule_statistic_output import OrificeScheduleStatisticOutput
from dhicn_zyws_service.models.orifice_time_series_output import OrificeTimeSeriesOutput
from dhicn_zyws_service.models.principle_details_output import PrincipleDetailsOutput
from dhicn_zyws_service.models.principle_info import PrincipleInfo
from dhicn_zyws_service.models.processed_model_result_input import ProcessedModelResultInput
from dhicn_zyws_service.models.pump_base_configuration import PumpBaseConfiguration
from dhicn_zyws_service.models.query_boundary_input import QueryBoundaryInput
from dhicn_zyws_service.models.query_boundary_output import QueryBoundaryOutput
from dhicn_zyws_service.models.query_system_setting_default_input import QuerySystemSettingDefaultInput
from dhicn_zyws_service.models.query_system_setting_input import QuerySystemSettingInput
from dhicn_zyws_service.models.recommend_details import RecommendDetails
from dhicn_zyws_service.models.recomment_details import RecommentDetails
from dhicn_zyws_service.models.remote_service_error_info import RemoteServiceErrorInfo
from dhicn_zyws_service.models.remote_service_error_response import RemoteServiceErrorResponse
from dhicn_zyws_service.models.remote_service_validation_error_info import RemoteServiceValidationErrorInfo
from dhicn_zyws_service.models.result_statistic_output import ResultStatisticOutput
from dhicn_zyws_service.models.result_time_series import ResultTimeSeries
from dhicn_zyws_service.models.root_object import RootObject
from dhicn_zyws_service.models.save_scenario_principle_input import SaveScenarioPrincipleInput
from dhicn_zyws_service.models.save_schedule_suggestion_input import SaveScheduleSuggestionInput
from dhicn_zyws_service.models.scenario_info import ScenarioInfo
from dhicn_zyws_service.models.scenario_principle_details_dto import ScenarioPrincipleDetailsDto
from dhicn_zyws_service.models.schedule_statistic_basic import ScheduleStatisticBasic
from dhicn_zyws_service.models.search_indicator import SearchIndicator
from dhicn_zyws_service.models.search_output import SearchOutput
from dhicn_zyws_service.models.set_mutilple_tenant_batch_data_to_redis_input import SetMutilpleTenantBatchDataToRedisInput
from dhicn_zyws_service.models.statistic_setting_input import StatisticSettingInput
from dhicn_zyws_service.models.statistic_setting_output import StatisticSettingOutput
from dhicn_zyws_service.models.string_string_key_value import StringStringKeyValue
from dhicn_zyws_service.models.system_setting_output import SystemSettingOutput
from dhicn_zyws_service.models.time_span import TimeSpan
from dhicn_zyws_service.models.timeseries_batch_for_v3_input import TimeseriesBatchForV3Input
from dhicn_zyws_service.models.timeseries_batch_for_v3_output import TimeseriesBatchForV3Output
from dhicn_zyws_service.models.ts_pairs import TsPairs
from dhicn_zyws_service.models.update_boundary_ts_input import UpdateBoundaryTsInput
from dhicn_zyws_service.models.update_system_setting_input import UpdateSystemSettingInput
from dhicn_zyws_service.models.water_delivery_principle_scenario import WaterDeliveryPrincipleScenario
from dhicn_zyws_service.models.water_volume_optim_output import WaterVolumeOptimOutput
from dhicn_zyws_service.models.weir_adjustment_parameter import WeirAdjustmentParameter
from dhicn_zyws_service.models.write_pump_configuration import WritePumpConfiguration
from dhicn_zyws_service.models.write_pump_configuration_input import WritePumpConfigurationInput
