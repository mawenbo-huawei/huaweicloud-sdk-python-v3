# coding: utf-8

from __future__ import absolute_import

# import LtsClient
from huaweicloudsdklts.v2.lts_client import LtsClient
from huaweicloudsdklts.v2.lts_async_client import LtsAsyncClient
# import models into sdk package
from huaweicloudsdklts.v2.model.access_config_base_log_info import AccessConfigBaseLogInfo
from huaweicloudsdklts.v2.model.access_config_base_log_info_create import AccessConfigBaseLogInfoCreate
from huaweicloudsdklts.v2.model.access_config_deatil import AccessConfigDeatil
from huaweicloudsdklts.v2.model.access_config_deatil_create import AccessConfigDeatilCreate
from huaweicloudsdklts.v2.model.access_config_format import AccessConfigFormat
from huaweicloudsdklts.v2.model.access_config_format_create import AccessConfigFormatCreate
from huaweicloudsdklts.v2.model.access_config_format_mutil import AccessConfigFormatMutil
from huaweicloudsdklts.v2.model.access_config_format_mutil_create import AccessConfigFormatMutilCreate
from huaweicloudsdklts.v2.model.access_config_format_single import AccessConfigFormatSingle
from huaweicloudsdklts.v2.model.access_config_format_single_create import AccessConfigFormatSingleCreate
from huaweicloudsdklts.v2.model.access_config_host_group_id_list import AccessConfigHostGroupIdList
from huaweicloudsdklts.v2.model.access_config_host_group_id_list_create import AccessConfigHostGroupIdListCreate
from huaweicloudsdklts.v2.model.access_config_info import AccessConfigInfo
from huaweicloudsdklts.v2.model.access_config_query_log_info import AccessConfigQueryLogInfo
from huaweicloudsdklts.v2.model.access_config_tag import AccessConfigTag
from huaweicloudsdklts.v2.model.access_config_time_offset import AccessConfigTimeOffset
from huaweicloudsdklts.v2.model.access_config_time_offset_create import AccessConfigTimeOffsetCreate
from huaweicloudsdklts.v2.model.access_config_windows_log_info import AccessConfigWindowsLogInfo
from huaweicloudsdklts.v2.model.access_config_windows_log_info_create import AccessConfigWindowsLogInfoCreate
from huaweicloudsdklts.v2.model.annotations import Annotations
from huaweicloudsdklts.v2.model.aom_mapping_log_stream_info import AomMappingLogStreamInfo
from huaweicloudsdklts.v2.model.aom_mapping_request_info import AomMappingRequestInfo
from huaweicloudsdklts.v2.model.aom_mapping_rule_info import AomMappingRuleInfo
from huaweicloudsdklts.v2.model.aom_mapping_rule_resp import AomMappingRuleResp
from huaweicloudsdklts.v2.model.aom_mappingfiles_info import AomMappingfilesInfo
from huaweicloudsdklts.v2.model.brief_struct_template_model import BriefStructTemplateModel
from huaweicloudsdklts.v2.model.change_alarm_rule_status import ChangeAlarmRuleStatus
from huaweicloudsdklts.v2.model.chart_config import ChartConfig
from huaweicloudsdklts.v2.model.create_access_config_request import CreateAccessConfigRequest
from huaweicloudsdklts.v2.model.create_access_config_request_body import CreateAccessConfigRequestBody
from huaweicloudsdklts.v2.model.create_access_config_response import CreateAccessConfigResponse
from huaweicloudsdklts.v2.model.create_aom_mapping_rules_request import CreateAomMappingRulesRequest
from huaweicloudsdklts.v2.model.create_aom_mapping_rules_response import CreateAomMappingRulesResponse
from huaweicloudsdklts.v2.model.create_host_group_request import CreateHostGroupRequest
from huaweicloudsdklts.v2.model.create_host_group_request_body import CreateHostGroupRequestBody
from huaweicloudsdklts.v2.model.create_host_group_response import CreateHostGroupResponse
from huaweicloudsdklts.v2.model.create_keywords_alarm_rule_request import CreateKeywordsAlarmRuleRequest
from huaweicloudsdklts.v2.model.create_keywords_alarm_rule_request_body import CreateKeywordsAlarmRuleRequestBody
from huaweicloudsdklts.v2.model.create_keywords_alarm_rule_response import CreateKeywordsAlarmRuleResponse
from huaweicloudsdklts.v2.model.create_log_dump_obs_request import CreateLogDumpObsRequest
from huaweicloudsdklts.v2.model.create_log_dump_obs_request_body import CreateLogDumpObsRequestBody
from huaweicloudsdklts.v2.model.create_log_dump_obs_response import CreateLogDumpObsResponse
from huaweicloudsdklts.v2.model.create_log_group_params import CreateLogGroupParams
from huaweicloudsdklts.v2.model.create_log_group_request import CreateLogGroupRequest
from huaweicloudsdklts.v2.model.create_log_group_response import CreateLogGroupResponse
from huaweicloudsdklts.v2.model.create_log_stream_params import CreateLogStreamParams
from huaweicloudsdklts.v2.model.create_log_stream_request import CreateLogStreamRequest
from huaweicloudsdklts.v2.model.create_log_stream_response import CreateLogStreamResponse
from huaweicloudsdklts.v2.model.create_notification_template_request import CreateNotificationTemplateRequest
from huaweicloudsdklts.v2.model.create_notification_template_request_body import CreateNotificationTemplateRequestBody
from huaweicloudsdklts.v2.model.create_notification_template_response import CreateNotificationTemplateResponse
from huaweicloudsdklts.v2.model.create_sql_alarm_rule_request import CreateSqlAlarmRuleRequest
from huaweicloudsdklts.v2.model.create_sql_alarm_rule_request_body import CreateSqlAlarmRuleRequestBody
from huaweicloudsdklts.v2.model.create_sql_alarm_rule_response import CreateSqlAlarmRuleResponse
from huaweicloudsdklts.v2.model.create_struct_config_request import CreateStructConfigRequest
from huaweicloudsdklts.v2.model.create_struct_config_response import CreateStructConfigResponse
from huaweicloudsdklts.v2.model.create_struct_template_request import CreateStructTemplateRequest
from huaweicloudsdklts.v2.model.create_struct_template_response import CreateStructTemplateResponse
from huaweicloudsdklts.v2.model.create_transfer_request import CreateTransferRequest
from huaweicloudsdklts.v2.model.create_transfer_request_body import CreateTransferRequestBody
from huaweicloudsdklts.v2.model.create_transfer_request_body_log_streams import CreateTransferRequestBodyLogStreams
from huaweicloudsdklts.v2.model.create_transfer_request_body_log_transfer_info import CreateTransferRequestBodyLogTransferInfo
from huaweicloudsdklts.v2.model.create_transfer_request_body_log_transfer_info_log_agency_transfer import CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer
from huaweicloudsdklts.v2.model.create_transfer_response import CreateTransferResponse
from huaweicloudsdklts.v2.model.create_transfer_response_body import CreateTransferResponseBody
from huaweicloudsdklts.v2.model.create_transfer_response_body_log_streams import CreateTransferResponseBodyLogStreams
from huaweicloudsdklts.v2.model.create_transfer_response_body_log_transfer_info import CreateTransferResponseBodyLogTransferInfo
from huaweicloudsdklts.v2.model.create_transfer_response_body_log_transfer_info_log_agency_transfer import CreateTransferResponseBodyLogTransferInfoLogAgencyTransfer
from huaweicloudsdklts.v2.model.delete_access_config_request import DeleteAccessConfigRequest
from huaweicloudsdklts.v2.model.delete_access_config_request_body import DeleteAccessConfigRequestBody
from huaweicloudsdklts.v2.model.delete_access_config_response import DeleteAccessConfigResponse
from huaweicloudsdklts.v2.model.delete_active_alarms_request import DeleteActiveAlarmsRequest
from huaweicloudsdklts.v2.model.delete_active_alarms_request_body import DeleteActiveAlarmsRequestBody
from huaweicloudsdklts.v2.model.delete_active_alarms_response import DeleteActiveAlarmsResponse
from huaweicloudsdklts.v2.model.delete_aom_mapping_rules_request import DeleteAomMappingRulesRequest
from huaweicloudsdklts.v2.model.delete_aom_mapping_rules_response import DeleteAomMappingRulesResponse
from huaweicloudsdklts.v2.model.delete_host_group_request import DeleteHostGroupRequest
from huaweicloudsdklts.v2.model.delete_host_group_request_body import DeleteHostGroupRequestBody
from huaweicloudsdklts.v2.model.delete_host_group_response import DeleteHostGroupResponse
from huaweicloudsdklts.v2.model.delete_keywords_alarm_rule_request import DeleteKeywordsAlarmRuleRequest
from huaweicloudsdklts.v2.model.delete_keywords_alarm_rule_response import DeleteKeywordsAlarmRuleResponse
from huaweicloudsdklts.v2.model.delete_log_group_request import DeleteLogGroupRequest
from huaweicloudsdklts.v2.model.delete_log_group_response import DeleteLogGroupResponse
from huaweicloudsdklts.v2.model.delete_log_stream_request import DeleteLogStreamRequest
from huaweicloudsdklts.v2.model.delete_log_stream_response import DeleteLogStreamResponse
from huaweicloudsdklts.v2.model.delete_notification_template_body import DeleteNotificationTemplateBody
from huaweicloudsdklts.v2.model.delete_notification_template_request import DeleteNotificationTemplateRequest
from huaweicloudsdklts.v2.model.delete_notification_template_response import DeleteNotificationTemplateResponse
from huaweicloudsdklts.v2.model.delete_sql_alarm_rule_request import DeleteSqlAlarmRuleRequest
from huaweicloudsdklts.v2.model.delete_sql_alarm_rule_response import DeleteSqlAlarmRuleResponse
from huaweicloudsdklts.v2.model.delete_struct_template_req_body import DeleteStructTemplateReqBody
from huaweicloudsdklts.v2.model.delete_struct_template_request import DeleteStructTemplateRequest
from huaweicloudsdklts.v2.model.delete_struct_template_response import DeleteStructTemplateResponse
from huaweicloudsdklts.v2.model.delete_transfer_request import DeleteTransferRequest
from huaweicloudsdklts.v2.model.delete_transfer_response import DeleteTransferResponse
from huaweicloudsdklts.v2.model.demo_field import DemoField
from huaweicloudsdklts.v2.model.disable_log_collection_request import DisableLogCollectionRequest
from huaweicloudsdklts.v2.model.disable_log_collection_response import DisableLogCollectionResponse
from huaweicloudsdklts.v2.model.enable_log_collection_request import EnableLogCollectionRequest
from huaweicloudsdklts.v2.model.enable_log_collection_response import EnableLogCollectionResponse
from huaweicloudsdklts.v2.model.event import Event
from huaweicloudsdklts.v2.model.events import Events
from huaweicloudsdklts.v2.model.field_model import FieldModel
from huaweicloudsdklts.v2.model.frequency import Frequency
from huaweicloudsdklts.v2.model.get_access_config_list_request_body import GetAccessConfigListRequestBody
from huaweicloudsdklts.v2.model.get_host_group_info import GetHostGroupInfo
from huaweicloudsdklts.v2.model.get_host_group_list_filter import GetHostGroupListFilter
from huaweicloudsdklts.v2.model.get_host_group_list_request_body import GetHostGroupListRequestBody
from huaweicloudsdklts.v2.model.get_host_group_list_tag import GetHostGroupListTag
from huaweicloudsdklts.v2.model.get_host_list_filter import GetHostListFilter
from huaweicloudsdklts.v2.model.get_host_list_info import GetHostListInfo
from huaweicloudsdklts.v2.model.get_host_list_request_body import GetHostListRequestBody
from huaweicloudsdklts.v2.model.host_group_tag import HostGroupTag
from huaweicloudsdklts.v2.model.keywords_alarm_rule_resp_list import KeywordsAlarmRuleRespList
from huaweicloudsdklts.v2.model.keywords_request import KeywordsRequest
from huaweicloudsdklts.v2.model.list_access_config_request import ListAccessConfigRequest
from huaweicloudsdklts.v2.model.list_access_config_response import ListAccessConfigResponse
from huaweicloudsdklts.v2.model.list_active_or_history_alarms_request import ListActiveOrHistoryAlarmsRequest
from huaweicloudsdklts.v2.model.list_active_or_history_alarms_request_body import ListActiveOrHistoryAlarmsRequestBody
from huaweicloudsdklts.v2.model.list_active_or_history_alarms_response import ListActiveOrHistoryAlarmsResponse
from huaweicloudsdklts.v2.model.list_breif_struct_template_request import ListBreifStructTemplateRequest
from huaweicloudsdklts.v2.model.list_breif_struct_template_response import ListBreifStructTemplateResponse
from huaweicloudsdklts.v2.model.list_charts_request import ListChartsRequest
from huaweicloudsdklts.v2.model.list_charts_response import ListChartsResponse
from huaweicloudsdklts.v2.model.list_host_group_request import ListHostGroupRequest
from huaweicloudsdklts.v2.model.list_host_group_response import ListHostGroupResponse
from huaweicloudsdklts.v2.model.list_host_request import ListHostRequest
from huaweicloudsdklts.v2.model.list_host_response import ListHostResponse
from huaweicloudsdklts.v2.model.list_keywords_alarm_rules_request import ListKeywordsAlarmRulesRequest
from huaweicloudsdklts.v2.model.list_keywords_alarm_rules_response import ListKeywordsAlarmRulesResponse
from huaweicloudsdklts.v2.model.list_log_groups_request import ListLogGroupsRequest
from huaweicloudsdklts.v2.model.list_log_groups_response import ListLogGroupsResponse
from huaweicloudsdklts.v2.model.list_log_histogram_request import ListLogHistogramRequest
from huaweicloudsdklts.v2.model.list_log_histogram_response import ListLogHistogramResponse
from huaweicloudsdklts.v2.model.list_log_stream_request import ListLogStreamRequest
from huaweicloudsdklts.v2.model.list_log_stream_response import ListLogStreamResponse
from huaweicloudsdklts.v2.model.list_log_streams_request import ListLogStreamsRequest
from huaweicloudsdklts.v2.model.list_log_streams_response import ListLogStreamsResponse
from huaweicloudsdklts.v2.model.list_log_streams_response_body1_log_streams import ListLogStreamsResponseBody1LogStreams
from huaweicloudsdklts.v2.model.list_logs_request import ListLogsRequest
from huaweicloudsdklts.v2.model.list_logs_response import ListLogsResponse
from huaweicloudsdklts.v2.model.list_notification_template_request import ListNotificationTemplateRequest
from huaweicloudsdklts.v2.model.list_notification_template_response import ListNotificationTemplateResponse
from huaweicloudsdklts.v2.model.list_notification_templates_request import ListNotificationTemplatesRequest
from huaweicloudsdklts.v2.model.list_notification_templates_response import ListNotificationTemplatesResponse
from huaweicloudsdklts.v2.model.list_notification_topics_request import ListNotificationTopicsRequest
from huaweicloudsdklts.v2.model.list_notification_topics_response import ListNotificationTopicsResponse
from huaweicloudsdklts.v2.model.list_query_structured_logs_request import ListQueryStructuredLogsRequest
from huaweicloudsdklts.v2.model.list_query_structured_logs_response import ListQueryStructuredLogsResponse
from huaweicloudsdklts.v2.model.list_sql_alarm_rules_request import ListSqlAlarmRulesRequest
from huaweicloudsdklts.v2.model.list_sql_alarm_rules_response import ListSqlAlarmRulesResponse
from huaweicloudsdklts.v2.model.list_struct_template_request import ListStructTemplateRequest
from huaweicloudsdklts.v2.model.list_struct_template_response import ListStructTemplateResponse
from huaweicloudsdklts.v2.model.list_structured_logs_with_time_range_request import ListStructuredLogsWithTimeRangeRequest
from huaweicloudsdklts.v2.model.list_structured_logs_with_time_range_response import ListStructuredLogsWithTimeRangeResponse
from huaweicloudsdklts.v2.model.list_time_line_traffic_statistics_request import ListTimeLineTrafficStatisticsRequest
from huaweicloudsdklts.v2.model.list_time_line_traffic_statistics_response import ListTimeLineTrafficStatisticsResponse
from huaweicloudsdklts.v2.model.list_transfers_request import ListTransfersRequest
from huaweicloudsdklts.v2.model.list_transfers_response import ListTransfersResponse
from huaweicloudsdklts.v2.model.log_contents import LogContents
from huaweicloudsdklts.v2.model.log_group import LogGroup
from huaweicloudsdklts.v2.model.log_stream import LogStream
from huaweicloudsdklts.v2.model.lts_struct_template_info import LtsStructTemplateInfo
from huaweicloudsdklts.v2.model.metadata import Metadata
from huaweicloudsdklts.v2.model.notification_save_rule import NotificationSaveRule
from huaweicloudsdklts.v2.model.notification_template import NotificationTemplate
from huaweicloudsdklts.v2.model.page_info import PageInfo
from huaweicloudsdklts.v2.model.preview_template_body import PreviewTemplateBody
from huaweicloudsdklts.v2.model.query_log_key_word_count_request_body import QueryLogKeyWordCountRequestBody
from huaweicloudsdklts.v2.model.query_lts_log_params import QueryLtsLogParams
from huaweicloudsdklts.v2.model.query_lts_struct_log_params import QueryLtsStructLogParams
from huaweicloudsdklts.v2.model.query_lts_struct_log_params_new import QueryLtsStructLogParamsNew
from huaweicloudsdklts.v2.model.register_dms_kafka_instance_request import RegisterDmsKafkaInstanceRequest
from huaweicloudsdklts.v2.model.register_dms_kafka_instance_request_body import RegisterDmsKafkaInstanceRequestBody
from huaweicloudsdklts.v2.model.register_dms_kafka_instance_request_body_connect_info import RegisterDmsKafkaInstanceRequestBodyConnectInfo
from huaweicloudsdklts.v2.model.register_dms_kafka_instance_response import RegisterDmsKafkaInstanceResponse
from huaweicloudsdklts.v2.model.resulits import Resulits
from huaweicloudsdklts.v2.model.rule import Rule
from huaweicloudsdklts.v2.model.show_aom_mapping_rule_request import ShowAomMappingRuleRequest
from huaweicloudsdklts.v2.model.show_aom_mapping_rule_response import ShowAomMappingRuleResponse
from huaweicloudsdklts.v2.model.show_aom_mapping_rules_request import ShowAomMappingRulesRequest
from huaweicloudsdklts.v2.model.show_aom_mapping_rules_response import ShowAomMappingRulesResponse
from huaweicloudsdklts.v2.model.show_notification_template_request import ShowNotificationTemplateRequest
from huaweicloudsdklts.v2.model.show_notification_template_response import ShowNotificationTemplateResponse
from huaweicloudsdklts.v2.model.show_struct_template_request import ShowStructTemplateRequest
from huaweicloudsdklts.v2.model.show_struct_template_response import ShowStructTemplateResponse
from huaweicloudsdklts.v2.model.show_struct_template_rule import ShowStructTemplateRule
from huaweicloudsdklts.v2.model.show_struct_templatecluster_info import ShowStructTemplateclusterInfo
from huaweicloudsdklts.v2.model.sort import Sort
from huaweicloudsdklts.v2.model.sql_alarm_rule_resp_list import SqlAlarmRuleRespList
from huaweicloudsdklts.v2.model.sql_request import SqlRequest
from huaweicloudsdklts.v2.model.struct_config import StructConfig
from huaweicloudsdklts.v2.model.struct_field_info import StructFieldInfo
from huaweicloudsdklts.v2.model.struct_field_info_return import StructFieldInfoReturn
from huaweicloudsdklts.v2.model.struct_log_contents import StructLogContents
from huaweicloudsdklts.v2.model.struct_template import StructTemplate
from huaweicloudsdklts.v2.model.struct_template_model import StructTemplateModel
from huaweicloudsdklts.v2.model.sub_template import SubTemplate
from huaweicloudsdklts.v2.model.tag_field import TagField
from huaweicloudsdklts.v2.model.tag_field_new import TagFieldNew
from huaweicloudsdklts.v2.model.tag_fields_info import TagFieldsInfo
from huaweicloudsdklts.v2.model.template_rule import TemplateRule
from huaweicloudsdklts.v2.model.time_range import TimeRange
from huaweicloudsdklts.v2.model.timeline_traffic_statistics_request_body import TimelineTrafficStatisticsRequestBody
from huaweicloudsdklts.v2.model.topics import Topics
from huaweicloudsdklts.v2.model.transfer_detail import TransferDetail
from huaweicloudsdklts.v2.model.update_access_config_request import UpdateAccessConfigRequest
from huaweicloudsdklts.v2.model.update_access_config_request_body import UpdateAccessConfigRequestBody
from huaweicloudsdklts.v2.model.update_access_config_response import UpdateAccessConfigResponse
from huaweicloudsdklts.v2.model.update_alarm_rule_status_request import UpdateAlarmRuleStatusRequest
from huaweicloudsdklts.v2.model.update_alarm_rule_status_response import UpdateAlarmRuleStatusResponse
from huaweicloudsdklts.v2.model.update_aom_mapping_rules_request import UpdateAomMappingRulesRequest
from huaweicloudsdklts.v2.model.update_aom_mapping_rules_response import UpdateAomMappingRulesResponse
from huaweicloudsdklts.v2.model.update_host_group_request import UpdateHostGroupRequest
from huaweicloudsdklts.v2.model.update_host_group_request_body import UpdateHostGroupRequestBody
from huaweicloudsdklts.v2.model.update_host_group_response import UpdateHostGroupResponse
from huaweicloudsdklts.v2.model.update_keywords_alarm_rule_request import UpdateKeywordsAlarmRuleRequest
from huaweicloudsdklts.v2.model.update_keywords_alarm_rule_request_body import UpdateKeywordsAlarmRuleRequestBody
from huaweicloudsdklts.v2.model.update_keywords_alarm_rule_response import UpdateKeywordsAlarmRuleResponse
from huaweicloudsdklts.v2.model.update_log_group_params import UpdateLogGroupParams
from huaweicloudsdklts.v2.model.update_log_group_request import UpdateLogGroupRequest
from huaweicloudsdklts.v2.model.update_log_group_response import UpdateLogGroupResponse
from huaweicloudsdklts.v2.model.update_notification_template_request import UpdateNotificationTemplateRequest
from huaweicloudsdklts.v2.model.update_notification_template_response import UpdateNotificationTemplateResponse
from huaweicloudsdklts.v2.model.update_sql_alarm_rule_request import UpdateSqlAlarmRuleRequest
from huaweicloudsdklts.v2.model.update_sql_alarm_rule_request_body import UpdateSqlAlarmRuleRequestBody
from huaweicloudsdklts.v2.model.update_sql_alarm_rule_response import UpdateSqlAlarmRuleResponse
from huaweicloudsdklts.v2.model.update_struct_config_request import UpdateStructConfigRequest
from huaweicloudsdklts.v2.model.update_struct_config_response import UpdateStructConfigResponse
from huaweicloudsdklts.v2.model.update_struct_template_request import UpdateStructTemplateRequest
from huaweicloudsdklts.v2.model.update_struct_template_response import UpdateStructTemplateResponse
from huaweicloudsdklts.v2.model.update_transfer_request import UpdateTransferRequest
from huaweicloudsdklts.v2.model.update_transfer_request_body import UpdateTransferRequestBody
from huaweicloudsdklts.v2.model.update_transfer_request_body_log_transfer_info import UpdateTransferRequestBodyLogTransferInfo
from huaweicloudsdklts.v2.model.update_transfer_response import UpdateTransferResponse

