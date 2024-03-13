# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkces.v2.model.add_alarm_rule_resources_request import AddAlarmRuleResourcesRequest
from huaweicloudsdkces.v2.model.add_alarm_rule_resources_response import AddAlarmRuleResourcesResponse
from huaweicloudsdkces.v2.model.additional_info import AdditionalInfo
from huaweicloudsdkces.v2.model.agent_dimension import AgentDimension
from huaweicloudsdkces.v2.model.alarm_condition import AlarmCondition
from huaweicloudsdkces.v2.model.alarm_description import AlarmDescription
from huaweicloudsdkces.v2.model.alarm_enabled import AlarmEnabled
from huaweicloudsdkces.v2.model.alarm_history_item_v2 import AlarmHistoryItemV2
from huaweicloudsdkces.v2.model.alarm_id import AlarmID
from huaweicloudsdkces.v2.model.alarm_level import AlarmLevel
from huaweicloudsdkces.v2.model.alarm_name import AlarmName
from huaweicloudsdkces.v2.model.alarm_policy_id import AlarmPolicyID
from huaweicloudsdkces.v2.model.alarm_template_id import AlarmTemplateID
from huaweicloudsdkces.v2.model.alarm_template_policies import AlarmTemplatePolicies
from huaweicloudsdkces.v2.model.alarm_templates import AlarmTemplates
from huaweicloudsdkces.v2.model.alarm_type import AlarmType
from huaweicloudsdkces.v2.model.base_widget_info import BaseWidgetInfo
from huaweicloudsdkces.v2.model.batch_create_resources_request import BatchCreateResourcesRequest
from huaweicloudsdkces.v2.model.batch_create_resources_response import BatchCreateResourcesResponse
from huaweicloudsdkces.v2.model.batch_delete_alarm_rules_request import BatchDeleteAlarmRulesRequest
from huaweicloudsdkces.v2.model.batch_delete_alarm_rules_response import BatchDeleteAlarmRulesResponse
from huaweicloudsdkces.v2.model.batch_delete_alarm_templates_request import BatchDeleteAlarmTemplatesRequest
from huaweicloudsdkces.v2.model.batch_delete_alarm_templates_request_body import BatchDeleteAlarmTemplatesRequestBody
from huaweicloudsdkces.v2.model.batch_delete_alarm_templates_response import BatchDeleteAlarmTemplatesResponse
from huaweicloudsdkces.v2.model.batch_delete_alarms_request_body import BatchDeleteAlarmsRequestBody
from huaweicloudsdkces.v2.model.batch_delete_dashboard_request_body import BatchDeleteDashboardRequestBody
from huaweicloudsdkces.v2.model.batch_delete_dashboard_resp_info import BatchDeleteDashboardRespInfo
from huaweicloudsdkces.v2.model.batch_delete_notification_masks_request import BatchDeleteNotificationMasksRequest
from huaweicloudsdkces.v2.model.batch_delete_notification_masks_request_body import BatchDeleteNotificationMasksRequestBody
from huaweicloudsdkces.v2.model.batch_delete_notification_masks_response import BatchDeleteNotificationMasksResponse
from huaweicloudsdkces.v2.model.batch_delete_one_click_alarms_request import BatchDeleteOneClickAlarmsRequest
from huaweicloudsdkces.v2.model.batch_delete_one_click_alarms_request_body import BatchDeleteOneClickAlarmsRequestBody
from huaweicloudsdkces.v2.model.batch_delete_one_click_alarms_response import BatchDeleteOneClickAlarmsResponse
from huaweicloudsdkces.v2.model.batch_delete_resource_groups_request import BatchDeleteResourceGroupsRequest
from huaweicloudsdkces.v2.model.batch_delete_resource_groups_request_body import BatchDeleteResourceGroupsRequestBody
from huaweicloudsdkces.v2.model.batch_delete_resource_groups_response import BatchDeleteResourceGroupsResponse
from huaweicloudsdkces.v2.model.batch_delete_resources_request import BatchDeleteResourcesRequest
from huaweicloudsdkces.v2.model.batch_delete_resources_response import BatchDeleteResourcesResponse
from huaweicloudsdkces.v2.model.batch_enable_alarm_policies_request_body import BatchEnableAlarmPoliciesRequestBody
from huaweicloudsdkces.v2.model.batch_enable_alarm_rules_request import BatchEnableAlarmRulesRequest
from huaweicloudsdkces.v2.model.batch_enable_alarm_rules_response import BatchEnableAlarmRulesResponse
from huaweicloudsdkces.v2.model.batch_enable_alarms_request_body import BatchEnableAlarmsRequestBody
from huaweicloudsdkces.v2.model.batch_update_notification_mask_time_request import BatchUpdateNotificationMaskTimeRequest
from huaweicloudsdkces.v2.model.batch_update_notification_mask_time_request_body import BatchUpdateNotificationMaskTimeRequestBody
from huaweicloudsdkces.v2.model.batch_update_notification_mask_time_response import BatchUpdateNotificationMaskTimeResponse
from huaweicloudsdkces.v2.model.batch_update_notification_masks_request import BatchUpdateNotificationMasksRequest
from huaweicloudsdkces.v2.model.batch_update_notification_masks_request_body import BatchUpdateNotificationMasksRequestBody
from huaweicloudsdkces.v2.model.batch_update_notification_masks_response import BatchUpdateNotificationMasksResponse
from huaweicloudsdkces.v2.model.batch_update_one_click_alarm_policies_enabled_state_request import BatchUpdateOneClickAlarmPoliciesEnabledStateRequest
from huaweicloudsdkces.v2.model.batch_update_one_click_alarm_policies_enabled_state_response import BatchUpdateOneClickAlarmPoliciesEnabledStateResponse
from huaweicloudsdkces.v2.model.batch_update_one_click_alarms_enabled_state_request import BatchUpdateOneClickAlarmsEnabledStateRequest
from huaweicloudsdkces.v2.model.batch_update_one_click_alarms_enabled_state_response import BatchUpdateOneClickAlarmsEnabledStateResponse
from huaweicloudsdkces.v2.model.batch_update_widget_info import BatchUpdateWidgetInfo
from huaweicloudsdkces.v2.model.batch_update_widgets_request import BatchUpdateWidgetsRequest
from huaweicloudsdkces.v2.model.batch_update_widgets_response import BatchUpdateWidgetsResponse
from huaweicloudsdkces.v2.model.comparison_operator import ComparisonOperator
from huaweicloudsdkces.v2.model.count import Count
from huaweicloudsdkces.v2.model.create_alarm_rules_request import CreateAlarmRulesRequest
from huaweicloudsdkces.v2.model.create_alarm_rules_response import CreateAlarmRulesResponse
from huaweicloudsdkces.v2.model.create_alarm_template_request import CreateAlarmTemplateRequest
from huaweicloudsdkces.v2.model.create_alarm_template_request_body import CreateAlarmTemplateRequestBody
from huaweicloudsdkces.v2.model.create_alarm_template_response import CreateAlarmTemplateResponse
from huaweicloudsdkces.v2.model.create_dashboard_request_body import CreateDashboardRequestBody
from huaweicloudsdkces.v2.model.create_dashboard_widgets_request import CreateDashboardWidgetsRequest
from huaweicloudsdkces.v2.model.create_dashboard_widgets_response import CreateDashboardWidgetsResponse
from huaweicloudsdkces.v2.model.create_one_click_alarm_request import CreateOneClickAlarmRequest
from huaweicloudsdkces.v2.model.create_one_click_alarm_response import CreateOneClickAlarmResponse
from huaweicloudsdkces.v2.model.create_one_dashboard_request import CreateOneDashboardRequest
from huaweicloudsdkces.v2.model.create_one_dashboard_response import CreateOneDashboardResponse
from huaweicloudsdkces.v2.model.create_resource_group_request import CreateResourceGroupRequest
from huaweicloudsdkces.v2.model.create_resource_group_request_body import CreateResourceGroupRequestBody
from huaweicloudsdkces.v2.model.create_resource_group_response import CreateResourceGroupResponse
from huaweicloudsdkces.v2.model.create_time import CreateTime
from huaweicloudsdkces.v2.model.dash_board_id_item import DashBoardIdItem
from huaweicloudsdkces.v2.model.dash_board_info import DashBoardInfo
from huaweicloudsdkces.v2.model.dash_board_name_item import DashBoardNameItem
from huaweicloudsdkces.v2.model.data_point_info import DataPointInfo
from huaweicloudsdkces.v2.model.delete_alarm_rule_resources_request import DeleteAlarmRuleResourcesRequest
from huaweicloudsdkces.v2.model.delete_alarm_rule_resources_response import DeleteAlarmRuleResourcesResponse
from huaweicloudsdkces.v2.model.delete_dashboards_request import DeleteDashboardsRequest
from huaweicloudsdkces.v2.model.delete_dashboards_response import DeleteDashboardsResponse
from huaweicloudsdkces.v2.model.delete_one_widget_request import DeleteOneWidgetRequest
from huaweicloudsdkces.v2.model.delete_one_widget_response import DeleteOneWidgetResponse
from huaweicloudsdkces.v2.model.dimension import Dimension
from huaweicloudsdkces.v2.model.dimension2 import Dimension2
from huaweicloudsdkces.v2.model.dimension_info import DimensionInfo
from huaweicloudsdkces.v2.model.dimension_name import DimensionName
from huaweicloudsdkces.v2.model.dimension_names import DimensionNames
from huaweicloudsdkces.v2.model.enable_one_click_alarm_request_body import EnableOneClickAlarmRequestBody
from huaweicloudsdkces.v2.model.enabled import Enabled
from huaweicloudsdkces.v2.model.end_date import EndDate
from huaweicloudsdkces.v2.model.end_time import EndTime
from huaweicloudsdkces.v2.model.enterprise_id_item import EnterpriseIdItem
from huaweicloudsdkces.v2.model.enterprise_project_id import EnterpriseProjectID
from huaweicloudsdkces.v2.model.event_dimension_name import EventDimensionName
from huaweicloudsdkces.v2.model.extra_info import ExtraInfo
from huaweicloudsdkces.v2.model.filter import Filter
from huaweicloudsdkces.v2.model.get_resource_group_resources import GetResourceGroupResources
from huaweicloudsdkces.v2.model.is_favorite_item import IsFavoriteItem
from huaweicloudsdkces.v2.model.level import Level
from huaweicloudsdkces.v2.model.list_agent_dimension_info_request import ListAgentDimensionInfoRequest
from huaweicloudsdkces.v2.model.list_agent_dimension_info_response import ListAgentDimensionInfoResponse
from huaweicloudsdkces.v2.model.list_alarm_histories_request import ListAlarmHistoriesRequest
from huaweicloudsdkces.v2.model.list_alarm_histories_response import ListAlarmHistoriesResponse
from huaweicloudsdkces.v2.model.list_alarm_response_alarms import ListAlarmResponseAlarms
from huaweicloudsdkces.v2.model.list_alarm_rule_policies_request import ListAlarmRulePoliciesRequest
from huaweicloudsdkces.v2.model.list_alarm_rule_policies_response import ListAlarmRulePoliciesResponse
from huaweicloudsdkces.v2.model.list_alarm_rule_resources_request import ListAlarmRuleResourcesRequest
from huaweicloudsdkces.v2.model.list_alarm_rule_resources_response import ListAlarmRuleResourcesResponse
from huaweicloudsdkces.v2.model.list_alarm_rules_request import ListAlarmRulesRequest
from huaweicloudsdkces.v2.model.list_alarm_rules_response import ListAlarmRulesResponse
from huaweicloudsdkces.v2.model.list_alarm_template_association_alarms_request import ListAlarmTemplateAssociationAlarmsRequest
from huaweicloudsdkces.v2.model.list_alarm_template_association_alarms_response import ListAlarmTemplateAssociationAlarmsResponse
from huaweicloudsdkces.v2.model.list_alarm_templates_request import ListAlarmTemplatesRequest
from huaweicloudsdkces.v2.model.list_alarm_templates_response import ListAlarmTemplatesResponse
from huaweicloudsdkces.v2.model.list_alarms_resp_alarms import ListAlarmsRespAlarms
from huaweicloudsdkces.v2.model.list_association_alarms_response_alarms import ListAssociationAlarmsResponseAlarms
from huaweicloudsdkces.v2.model.list_ces_target_project_tags_request import ListCesTargetProjectTagsRequest
from huaweicloudsdkces.v2.model.list_ces_target_project_tags_response import ListCesTargetProjectTagsResponse
from huaweicloudsdkces.v2.model.list_dashboard_infos_request import ListDashboardInfosRequest
from huaweicloudsdkces.v2.model.list_dashboard_infos_response import ListDashboardInfosResponse
from huaweicloudsdkces.v2.model.list_dashboard_widgets_request import ListDashboardWidgetsRequest
from huaweicloudsdkces.v2.model.list_dashboard_widgets_response import ListDashboardWidgetsResponse
from huaweicloudsdkces.v2.model.list_notification_mask_request_body import ListNotificationMaskRequestBody
from huaweicloudsdkces.v2.model.list_notification_mask_resources_request import ListNotificationMaskResourcesRequest
from huaweicloudsdkces.v2.model.list_notification_mask_resources_response import ListNotificationMaskResourcesResponse
from huaweicloudsdkces.v2.model.list_notification_mask_resp_notification_masks import ListNotificationMaskRespNotificationMasks
from huaweicloudsdkces.v2.model.list_notification_masks_request import ListNotificationMasksRequest
from huaweicloudsdkces.v2.model.list_notification_masks_response import ListNotificationMasksResponse
from huaweicloudsdkces.v2.model.list_one_click_alarm_rules_request import ListOneClickAlarmRulesRequest
from huaweicloudsdkces.v2.model.list_one_click_alarm_rules_response import ListOneClickAlarmRulesResponse
from huaweicloudsdkces.v2.model.list_one_click_alarms_request import ListOneClickAlarmsRequest
from huaweicloudsdkces.v2.model.list_one_click_alarms_resp_one_click_alarms import ListOneClickAlarmsRespOneClickAlarms
from huaweicloudsdkces.v2.model.list_one_click_alarms_response import ListOneClickAlarmsResponse
from huaweicloudsdkces.v2.model.list_policy import ListPolicy
from huaweicloudsdkces.v2.model.list_relation_type import ListRelationType
from huaweicloudsdkces.v2.model.list_resource_groups_request import ListResourceGroupsRequest
from huaweicloudsdkces.v2.model.list_resource_groups_response import ListResourceGroupsResponse
from huaweicloudsdkces.v2.model.list_resource_groups_services_resources_request import ListResourceGroupsServicesResourcesRequest
from huaweicloudsdkces.v2.model.list_resource_groups_services_resources_response import ListResourceGroupsServicesResourcesResponse
from huaweicloudsdkces.v2.model.mask_name import MaskName
from huaweicloudsdkces.v2.model.mask_status import MaskStatus
from huaweicloudsdkces.v2.model.mask_type import MaskType
from huaweicloudsdkces.v2.model.metric import Metric
from huaweicloudsdkces.v2.model.metric_dimension import MetricDimension
from huaweicloudsdkces.v2.model.metric_dimension_name import MetricDimensionName
from huaweicloudsdkces.v2.model.metric_extra_info import MetricExtraInfo
from huaweicloudsdkces.v2.model.metric_name import MetricName
from huaweicloudsdkces.v2.model.namespace import Namespace
from huaweicloudsdkces.v2.model.namespace_allowed_empty import NamespaceAllowedEmpty
from huaweicloudsdkces.v2.model.notification import Notification
from huaweicloudsdkces.v2.model.notification_begin_time import NotificationBeginTime
from huaweicloudsdkces.v2.model.notification_enabled import NotificationEnabled
from huaweicloudsdkces.v2.model.notification_end_time import NotificationEndTime
from huaweicloudsdkces.v2.model.notification_mask_id import NotificationMaskID
from huaweicloudsdkces.v2.model.one_click_alarm_description import OneClickAlarmDescription
from huaweicloudsdkces.v2.model.one_click_alarm_id import OneClickAlarmID
from huaweicloudsdkces.v2.model.one_click_alarm_policy import OneClickAlarmPolicy
from huaweicloudsdkces.v2.model.one_resource_group_resp import OneResourceGroupResp
from huaweicloudsdkces.v2.model.period import Period
from huaweicloudsdkces.v2.model.policies import Policies
from huaweicloudsdkces.v2.model.policies_in_list_resp import PoliciesInListResp
from huaweicloudsdkces.v2.model.policies_req_v2 import PoliciesReqV2
from huaweicloudsdkces.v2.model.policy import Policy
from huaweicloudsdkces.v2.model.post_alarms_req_v2 import PostAlarmsReqV2
from huaweicloudsdkces.v2.model.put_alarm_notification_req import PutAlarmNotificationReq
from huaweicloudsdkces.v2.model.put_resource_group_req import PutResourceGroupReq
from huaweicloudsdkces.v2.model.relation_id import RelationID
from huaweicloudsdkces.v2.model.relation_type import RelationType
from huaweicloudsdkces.v2.model.resource import Resource
from huaweicloudsdkces.v2.model.resource_category import ResourceCategory
from huaweicloudsdkces.v2.model.resource_group_id import ResourceGroupID
from huaweicloudsdkces.v2.model.resource_group_tag_relation import ResourceGroupTagRelation
from huaweicloudsdkces.v2.model.resources_in_list_resp import ResourcesInListResp
from huaweicloudsdkces.v2.model.resources_req import ResourcesReq
from huaweicloudsdkces.v2.model.resources_req_v2 import ResourcesReqV2
from huaweicloudsdkces.v2.model.smn_urn import SMNUrn
from huaweicloudsdkces.v2.model.show_alarm_template_request import ShowAlarmTemplateRequest
from huaweicloudsdkces.v2.model.show_alarm_template_response import ShowAlarmTemplateResponse
from huaweicloudsdkces.v2.model.show_resource_group_request import ShowResourceGroupRequest
from huaweicloudsdkces.v2.model.show_resource_group_response import ShowResourceGroupResponse
from huaweicloudsdkces.v2.model.show_widget_request import ShowWidgetRequest
from huaweicloudsdkces.v2.model.show_widget_response import ShowWidgetResponse
from huaweicloudsdkces.v2.model.start_date import StartDate
from huaweicloudsdkces.v2.model.start_time import StartTime
from huaweicloudsdkces.v2.model.suppress_duration import SuppressDuration
from huaweicloudsdkces.v2.model.tag import Tag
from huaweicloudsdkces.v2.model.template_description import TemplateDescription
from huaweicloudsdkces.v2.model.template_id import TemplateID
from huaweicloudsdkces.v2.model.template_name import TemplateName
from huaweicloudsdkces.v2.model.template_type import TemplateType
from huaweicloudsdkces.v2.model.unit import Unit
from huaweicloudsdkces.v2.model.unit_item import UnitItem
from huaweicloudsdkces.v2.model.update_alarm_notifications_request import UpdateAlarmNotificationsRequest
from huaweicloudsdkces.v2.model.update_alarm_notifications_response import UpdateAlarmNotificationsResponse
from huaweicloudsdkces.v2.model.update_alarm_rule_policies_request import UpdateAlarmRulePoliciesRequest
from huaweicloudsdkces.v2.model.update_alarm_rule_policies_response import UpdateAlarmRulePoliciesResponse
from huaweicloudsdkces.v2.model.update_alarm_template_request import UpdateAlarmTemplateRequest
from huaweicloudsdkces.v2.model.update_alarm_template_request_body import UpdateAlarmTemplateRequestBody
from huaweicloudsdkces.v2.model.update_alarm_template_response import UpdateAlarmTemplateResponse
from huaweicloudsdkces.v2.model.update_dashboard_request import UpdateDashboardRequest
from huaweicloudsdkces.v2.model.update_dashboard_request_body import UpdateDashboardRequestBody
from huaweicloudsdkces.v2.model.update_dashboard_response import UpdateDashboardResponse
from huaweicloudsdkces.v2.model.update_notification_mask_request import UpdateNotificationMaskRequest
from huaweicloudsdkces.v2.model.update_notification_mask_response import UpdateNotificationMaskResponse
from huaweicloudsdkces.v2.model.update_notification_masks_request_body import UpdateNotificationMasksRequestBody
from huaweicloudsdkces.v2.model.update_one_click_alarm_notifications_request import UpdateOneClickAlarmNotificationsRequest
from huaweicloudsdkces.v2.model.update_one_click_alarm_notifications_response import UpdateOneClickAlarmNotificationsResponse
from huaweicloudsdkces.v2.model.update_policy import UpdatePolicy
from huaweicloudsdkces.v2.model.update_resource_group_request import UpdateResourceGroupRequest
from huaweicloudsdkces.v2.model.update_resource_group_response import UpdateResourceGroupResponse
from huaweicloudsdkces.v2.model.update_widget_info import UpdateWidgetInfo
from huaweicloudsdkces.v2.model.update_widget_info_location import UpdateWidgetInfoLocation
from huaweicloudsdkces.v2.model.update_widget_info_properties import UpdateWidgetInfoProperties
from huaweicloudsdkces.v2.model.value import Value
from huaweicloudsdkces.v2.model.widget_display_mode import WidgetDisplayMode
from huaweicloudsdkces.v2.model.widget_id_item import WidgetIdItem
from huaweicloudsdkces.v2.model.widget_info import WidgetInfo
from huaweicloudsdkces.v2.model.widget_info_with_id import WidgetInfoWithId
from huaweicloudsdkces.v2.model.widget_metric import WidgetMetric
