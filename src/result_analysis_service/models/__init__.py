# coding: utf-8

# flake8: noqa
"""
    result-analysis-service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from result_analysis_service.models.base_dynamic_output import BaseDynamicOutput
from result_analysis_service.models.base_static_output import BaseStaticOutput
from result_analysis_service.models.base_timeseries_batch_output import BaseTimeseriesBatchOutput
from result_analysis_service.models.base_timeseries_output import BaseTimeseriesOutput
from result_analysis_service.models.cs_current_model_output import CsCurrentModelOutput
from result_analysis_service.models.cs_history_model_output import CsHistoryModelOutput
from result_analysis_service.models.data_type_enum import DataTypeEnum
from result_analysis_service.models.filter_condition_enum import FilterConditionEnum
from result_analysis_service.models.filter_model_result_dto import FilterModelResultDto
from result_analysis_service.models.flooding_risk_info import FloodingRiskInfo
from result_analysis_service.models.flooding_risk_item import FloodingRiskItem
from result_analysis_service.models.flushing_result_entity import FlushingResultEntity
from result_analysis_service.models.gate_info import GateInfo
from result_analysis_service.models.gate_statistic_info import GateStatisticInfo
from result_analysis_service.models.gate_statistics_output import GateStatisticsOutput
from result_analysis_service.models.geo_point_item import GeoPointItem
from result_analysis_service.models.get_filter_model_result_input import GetFilterModelResultInput
from result_analysis_service.models.get_statistic_result_input import GetStatisticResultInput
from result_analysis_service.models.get_time_statistic_result_input import GetTimeStatisticResultInput
from result_analysis_service.models.log_simulation_item import LogSimulationItem
from result_analysis_service.models.m2_d_by_range_time_input import M2DByRangeTimeInput
from result_analysis_service.models.m2_d_data_type_enum import M2DDataTypeEnum
from result_analysis_service.models.m2_d_statistic_type_enum import M2DStatisticTypeEnum
from result_analysis_service.models.model_result_branch_affected_info_output import ModelResultBranchAffectedInfoOutput
from result_analysis_service.models.model_result_pipe_dispatch_statistic_output import ModelResultPipeDispatchStatisticOutput
from result_analysis_service.models.model_result_pipe_pump_statistic_output import ModelResultPipePumpStatisticOutput
from result_analysis_service.models.model_result_pipe_pump_volume_statistic_output import ModelResultPipePumpVolumeStatisticOutput
from result_analysis_service.models.model_result_pipe_sewage_plant_avg_statistic_output import ModelResultPipeSewagePlantAvgStatisticOutput
from result_analysis_service.models.model_result_pipe_sewage_plant_instant_statistic_output import ModelResultPipeSewagePlantInstantStatisticOutput
from result_analysis_service.models.model_result_pipe_sewage_plant_statistic_output import ModelResultPipeSewagePlantStatisticOutput
from result_analysis_service.models.model_result_pipe_smart_well_over_flow_statistic_output import ModelResultPipeSmartWellOverFlowStatisticOutput
from result_analysis_service.models.model_result_pipe_smart_well_statistic_output import ModelResultPipeSmartWellStatisticOutput
from result_analysis_service.models.model_result_pipe_smart_well_total_load_statistic_output import ModelResultPipeSmartWellTotalLoadStatisticOutput
from result_analysis_service.models.model_result_pipe_storage_statistic_output import ModelResultPipeStorageStatisticOutput
from result_analysis_service.models.model_result_pipe_valve_statistic_output import ModelResultPipeValveStatisticOutput
from result_analysis_service.models.model_result_pipe_w_qs_output import ModelResultPipeWQsOutput
from result_analysis_service.models.model_result_pipe_wq_input import ModelResultPipeWqInput
from result_analysis_service.models.model_result_pipe_wq_output import ModelResultPipeWqOutput
from result_analysis_service.models.model_result_river_control_statistic_output import ModelResultRiverControlStatisticOutput
from result_analysis_service.models.model_result_river_dam_statistic_output import ModelResultRiverDamStatisticOutput
from result_analysis_service.models.model_result_river_gate_pump_statistic_output import ModelResultRiverGatePumpStatisticOutput
from result_analysis_service.models.model_result_river_gate_statistic_output import ModelResultRiverGateStatisticOutput
from result_analysis_service.models.model_result_river_gate_total_statistic_output import ModelResultRiverGateTotalStatisticOutput
from result_analysis_service.models.model_result_river_pump_statistic_output import ModelResultRiverPumpStatisticOutput
from result_analysis_service.models.model_result_river_pump_total_statistic_output import ModelResultRiverPumpTotalStatisticOutput
from result_analysis_service.models.model_result_river_qualified_statistic_output import ModelResultRiverQualifiedStatisticOutput
from result_analysis_service.models.model_result_river_w_qs_output import ModelResultRiverWQsOutput
from result_analysis_service.models.model_result_river_wq_input import ModelResultRiverWqInput
from result_analysis_service.models.model_result_river_wq_output import ModelResultRiverWqOutput
from result_analysis_service.models.model_result_river_wq_statistic_output import ModelResultRiverWqStatisticOutput
from result_analysis_service.models.model_result_station_wq_statistic_input import ModelResultStationWqStatisticInput
from result_analysis_service.models.model_result_station_wq_statistic_output import ModelResultStationWqStatisticOutput
from result_analysis_service.models.model_result_times_output import ModelResultTimesOutput
from result_analysis_service.models.model_result_wq_timeseries_input import ModelResultWqTimeseriesInput
from result_analysis_service.models.model_result_wq_timeseries_output import ModelResultWqTimeseriesOutput
from result_analysis_service.models.model_state_enum import ModelStateEnum
from result_analysis_service.models.network_node_static_type_enum import NetworkNodeStaticTypeEnum
from result_analysis_service.models.network_profile import NetworkProfile
from result_analysis_service.models.network_statistics_output import NetworkStatisticsOutput
from result_analysis_service.models.node_data_type_enum import NodeDataTypeEnum
from result_analysis_service.models.node_item import NodeItem
from result_analysis_service.models.node_profile_data import NodeProfileData
from result_analysis_service.models.node_profile_data_profile_data_item import NodeProfileDataProfileDataItem
from result_analysis_service.models.node_type_enum import NodeTypeEnum
from result_analysis_service.models.object_id import ObjectId
from result_analysis_service.models.outlet_result import OutletResult
from result_analysis_service.models.overflow_statistics_item import OverflowStatisticsItem
from result_analysis_service.models.pipe_data_type_enum import PipeDataTypeEnum
from result_analysis_service.models.pipe_profile_item import PipeProfileItem
from result_analysis_service.models.pipe_result import PipeResult
from result_analysis_service.models.pump_info import PumpInfo
from result_analysis_service.models.pump_statistic_info import PumpStatisticInfo
from result_analysis_service.models.pump_statistics_output import PumpStatisticsOutput
from result_analysis_service.models.pump_volume import PumpVolume
from result_analysis_service.models.query_rain_output import QueryRainOutput
from result_analysis_service.models.rainfall_runoff_summary_output import RainfallRunoffSummaryOutput
from result_analysis_service.models.rainfall_status_enum import RainfallStatusEnum
from result_analysis_service.models.remote_service_error_info import RemoteServiceErrorInfo
from result_analysis_service.models.remote_service_error_response import RemoteServiceErrorResponse
from result_analysis_service.models.remote_service_validation_error_info import RemoteServiceValidationErrorInfo
from result_analysis_service.models.river_data_type_enum import RiverDataTypeEnum
from result_analysis_service.models.river_profile import RiverProfile
from result_analysis_service.models.river_water_level import RiverWaterLevel
from result_analysis_service.models.river_water_level_profile_data_item import RiverWaterLevelProfileDataItem
from result_analysis_service.models.rr_summary_per_catchment import RrSummaryPerCatchment
from result_analysis_service.models.scenario_time_info import ScenarioTimeInfo
from result_analysis_service.models.sensitive_points_statistic import SensitivePointsStatistic
from result_analysis_service.models.sensitive_points_timeseries import SensitivePointsTimeseries
from result_analysis_service.models.smart_well_valve_ts_data import SmartWellValveTsData
from result_analysis_service.models.statistic_model_id_item_dto import StatisticModelIdItemDto
from result_analysis_service.models.statistic_time_item_dto import StatisticTimeItemDto
from result_analysis_service.models.statistic_type_enum import StatisticTypeEnum
from result_analysis_service.models.statistics_model_id_result_dto import StatisticsModelIdResultDto
from result_analysis_service.models.statistics_time_result_dto import StatisticsTimeResultDto
from result_analysis_service.models.storage_data import StorageData
from result_analysis_service.models.string_page import StringPage
from result_analysis_service.models.structure_type_enum import StructureTypeEnum
from result_analysis_service.models.structures_item_enum import StructuresItemEnum
from result_analysis_service.models.sys_wd_data_type_enum import SysWdDataTypeEnum
from result_analysis_service.models.trace_wq_close_pipe import TraceWqClosePipe
from result_analysis_service.models.trace_wq_close_pipe_result import TraceWqClosePipeResult
from result_analysis_service.models.trace_wq_valve_info import TraceWqValveInfo
from result_analysis_service.models.ts_pair_object import TsPairObject
from result_analysis_service.models.ts_pairs import TsPairs
from result_analysis_service.models.user_info import UserInfo
from result_analysis_service.models.valve_statistic_list import ValveStatisticList
from result_analysis_service.models.valve_statistics_output import ValveStatisticsOutput
from result_analysis_service.models.wd_batch_timeseries_input import WdBatchTimeseriesInput
from result_analysis_service.models.wd_calculate_type_enum import WdCalculateTypeEnum
from result_analysis_service.models.wd_data_type_enum import WdDataTypeEnum
from result_analysis_service.models.wd_feature_type_enum import WdFeatureTypeEnum
from result_analysis_service.models.wd_history_model_input import WdHistoryModelInput
from result_analysis_service.models.wd_history_model_output import WdHistoryModelOutput
from result_analysis_service.models.wd_statistic_shut_off_user_dto import WdStatisticShutOffUserDto
from result_analysis_service.models.wd_zone_model_result_input import WdZoneModelResultInput
from result_analysis_service.models.wd_zone_model_result_output import WdZoneModelResultOutput
from result_analysis_service.models.wq_info_value import WqInfoValue
from result_analysis_service.models.wq_instant_statistic_info import WqInstantStatisticInfo
from result_analysis_service.models.wq_load_info import WqLoadInfo
from result_analysis_service.models.wq_max_statistic import WqMaxStatistic
from result_analysis_service.models.wq_statistic import WqStatistic
from result_analysis_service.models.wq_value_info import WqValueInfo