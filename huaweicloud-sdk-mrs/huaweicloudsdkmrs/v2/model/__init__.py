# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkmrs.v2.model.add_component_request import AddComponentRequest
from huaweicloudsdkmrs.v2.model.add_component_response import AddComponentResponse
from huaweicloudsdkmrs.v2.model.add_components_req import AddComponentsReq
from huaweicloudsdkmrs.v2.model.add_jobs_req_v11 import AddJobsReqV11
from huaweicloudsdkmrs.v2.model.agency_mapping import AgencyMapping
from huaweicloudsdkmrs.v2.model.agency_mapping_array import AgencyMappingArray
from huaweicloudsdkmrs.v2.model.assigned_node_group import AssignedNodeGroup
from huaweicloudsdkmrs.v2.model.auto_scaling_policy import AutoScalingPolicy
from huaweicloudsdkmrs.v2.model.auto_scaling_policy_delete_req import AutoScalingPolicyDeleteReq
from huaweicloudsdkmrs.v2.model.auto_scaling_policy_info import AutoScalingPolicyInfo
from huaweicloudsdkmrs.v2.model.auto_scaling_policy_v2 import AutoScalingPolicyV2
from huaweicloudsdkmrs.v2.model.az_flavors import AzFlavors
from huaweicloudsdkmrs.v2.model.batch_delete_jobs_request import BatchDeleteJobsRequest
from huaweicloudsdkmrs.v2.model.batch_delete_jobs_response import BatchDeleteJobsResponse
from huaweicloudsdkmrs.v2.model.bootstrap_script import BootstrapScript
from huaweicloudsdkmrs.v2.model.cancel_sql_request import CancelSqlRequest
from huaweicloudsdkmrs.v2.model.cancel_sql_response import CancelSqlResponse
from huaweicloudsdkmrs.v2.model.cancel_sync_iam_user_request import CancelSyncIamUserRequest
from huaweicloudsdkmrs.v2.model.cancel_sync_iam_user_response import CancelSyncIamUserResponse
from huaweicloudsdkmrs.v2.model.cancel_sync_request import CancelSyncRequest
from huaweicloudsdkmrs.v2.model.charge_info import ChargeInfo
from huaweicloudsdkmrs.v2.model.cluster_data_connector_map import ClusterDataConnectorMap
from huaweicloudsdkmrs.v2.model.component_config import ComponentConfig
from huaweicloudsdkmrs.v2.model.component_install_mode import ComponentInstallMode
from huaweicloudsdkmrs.v2.model.config import Config
from huaweicloudsdkmrs.v2.model.create_auto_scaling_policy_request import CreateAutoScalingPolicyRequest
from huaweicloudsdkmrs.v2.model.create_auto_scaling_policy_response import CreateAutoScalingPolicyResponse
from huaweicloudsdkmrs.v2.model.create_cluster_req_v2 import CreateClusterReqV2
from huaweicloudsdkmrs.v2.model.create_cluster_request import CreateClusterRequest
from huaweicloudsdkmrs.v2.model.create_cluster_response import CreateClusterResponse
from huaweicloudsdkmrs.v2.model.create_data_connector_request import CreateDataConnectorRequest
from huaweicloudsdkmrs.v2.model.create_data_connector_response import CreateDataConnectorResponse
from huaweicloudsdkmrs.v2.model.create_execute_job_request import CreateExecuteJobRequest
from huaweicloudsdkmrs.v2.model.create_execute_job_response import CreateExecuteJobResponse
from huaweicloudsdkmrs.v2.model.data_connector import DataConnector
from huaweicloudsdkmrs.v2.model.data_connector_detail import DataConnectorDetail
from huaweicloudsdkmrs.v2.model.data_connector_req import DataConnectorReq
from huaweicloudsdkmrs.v2.model.delete_auto_scaling_policy_request import DeleteAutoScalingPolicyRequest
from huaweicloudsdkmrs.v2.model.delete_auto_scaling_policy_response import DeleteAutoScalingPolicyResponse
from huaweicloudsdkmrs.v2.model.delete_data_connector_request import DeleteDataConnectorRequest
from huaweicloudsdkmrs.v2.model.delete_data_connector_response import DeleteDataConnectorResponse
from huaweicloudsdkmrs.v2.model.execute_sql_request import ExecuteSqlRequest
from huaweicloudsdkmrs.v2.model.execute_sql_response import ExecuteSqlResponse
from huaweicloudsdkmrs.v2.model.expand_cluster_request import ExpandClusterRequest
from huaweicloudsdkmrs.v2.model.expand_cluster_response import ExpandClusterResponse
from huaweicloudsdkmrs.v2.model.expand_param import ExpandParam
from huaweicloudsdkmrs.v2.model.file_status_v2 import FileStatusV2
from huaweicloudsdkmrs.v2.model.flavor import Flavor
from huaweicloudsdkmrs.v2.model.job_batch_delete import JobBatchDelete
from huaweicloudsdkmrs.v2.model.job_execution import JobExecution
from huaweicloudsdkmrs.v2.model.job_query_bean import JobQueryBean
from huaweicloudsdkmrs.v2.model.job_submit_result import JobSubmitResult
from huaweicloudsdkmrs.v2.model.list_data_connector_request import ListDataConnectorRequest
from huaweicloudsdkmrs.v2.model.list_data_connector_response import ListDataConnectorResponse
from huaweicloudsdkmrs.v2.model.modify_default_tags_request_body import ModifyDefaultTagsRequestBody
from huaweicloudsdkmrs.v2.model.node_group_v2 import NodeGroupV2
from huaweicloudsdkmrs.v2.model.resources_plan import ResourcesPlan
from huaweicloudsdkmrs.v2.model.rule import Rule
from huaweicloudsdkmrs.v2.model.run_job_flow_command import RunJobFlowCommand
from huaweicloudsdkmrs.v2.model.run_job_flow_request import RunJobFlowRequest
from huaweicloudsdkmrs.v2.model.run_job_flow_response import RunJobFlowResponse
from huaweicloudsdkmrs.v2.model.scale_script import ScaleScript
from huaweicloudsdkmrs.v2.model.show_agency_mapping_request import ShowAgencyMappingRequest
from huaweicloudsdkmrs.v2.model.show_agency_mapping_response import ShowAgencyMappingResponse
from huaweicloudsdkmrs.v2.model.show_auto_scaling_policy_request import ShowAutoScalingPolicyRequest
from huaweicloudsdkmrs.v2.model.show_auto_scaling_policy_response import ShowAutoScalingPolicyResponse
from huaweicloudsdkmrs.v2.model.show_hdfs_file_list_request import ShowHdfsFileListRequest
from huaweicloudsdkmrs.v2.model.show_hdfs_file_list_response import ShowHdfsFileListResponse
from huaweicloudsdkmrs.v2.model.show_job_exe_list_new_request import ShowJobExeListNewRequest
from huaweicloudsdkmrs.v2.model.show_job_exe_list_new_response import ShowJobExeListNewResponse
from huaweicloudsdkmrs.v2.model.show_mrs_flavors_request import ShowMrsFlavorsRequest
from huaweicloudsdkmrs.v2.model.show_mrs_flavors_response import ShowMrsFlavorsResponse
from huaweicloudsdkmrs.v2.model.show_mrs_version_list_request import ShowMrsVersionListRequest
from huaweicloudsdkmrs.v2.model.show_mrs_version_list_response import ShowMrsVersionListResponse
from huaweicloudsdkmrs.v2.model.show_single_job_exe_request import ShowSingleJobExeRequest
from huaweicloudsdkmrs.v2.model.show_single_job_exe_response import ShowSingleJobExeResponse
from huaweicloudsdkmrs.v2.model.show_sql_result_request import ShowSqlResultRequest
from huaweicloudsdkmrs.v2.model.show_sql_result_response import ShowSqlResultResponse
from huaweicloudsdkmrs.v2.model.show_sql_result_with_job_request import ShowSqlResultWithJobRequest
from huaweicloudsdkmrs.v2.model.show_sql_result_with_job_response import ShowSqlResultWithJobResponse
from huaweicloudsdkmrs.v2.model.show_sync_iam_user_request import ShowSyncIamUserRequest
from huaweicloudsdkmrs.v2.model.show_sync_iam_user_response import ShowSyncIamUserResponse
from huaweicloudsdkmrs.v2.model.show_tag_quota_request import ShowTagQuotaRequest
from huaweicloudsdkmrs.v2.model.show_tag_quota_response import ShowTagQuotaResponse
from huaweicloudsdkmrs.v2.model.show_tag_status_request import ShowTagStatusRequest
from huaweicloudsdkmrs.v2.model.show_tag_status_response import ShowTagStatusResponse
from huaweicloudsdkmrs.v2.model.shrink_cluster_request import ShrinkClusterRequest
from huaweicloudsdkmrs.v2.model.shrink_cluster_response import ShrinkClusterResponse
from huaweicloudsdkmrs.v2.model.shrink_param import ShrinkParam
from huaweicloudsdkmrs.v2.model.smn_notify import SmnNotify
from huaweicloudsdkmrs.v2.model.sql_execution_req import SqlExecutionReq
from huaweicloudsdkmrs.v2.model.step_config import StepConfig
from huaweicloudsdkmrs.v2.model.stop_job_request import StopJobRequest
from huaweicloudsdkmrs.v2.model.stop_job_response import StopJobResponse
from huaweicloudsdkmrs.v2.model.switch_cluster_tags_request import SwitchClusterTagsRequest
from huaweicloudsdkmrs.v2.model.switch_cluster_tags_response import SwitchClusterTagsResponse
from huaweicloudsdkmrs.v2.model.tag import Tag
from huaweicloudsdkmrs.v2.model.trigger import Trigger
from huaweicloudsdkmrs.v2.model.update_agency_mapping_request import UpdateAgencyMappingRequest
from huaweicloudsdkmrs.v2.model.update_agency_mapping_response import UpdateAgencyMappingResponse
from huaweicloudsdkmrs.v2.model.update_auto_scaling_policy_request import UpdateAutoScalingPolicyRequest
from huaweicloudsdkmrs.v2.model.update_auto_scaling_policy_response import UpdateAutoScalingPolicyResponse
from huaweicloudsdkmrs.v2.model.update_cluster_name_request import UpdateClusterNameRequest
from huaweicloudsdkmrs.v2.model.update_cluster_name_response import UpdateClusterNameResponse
from huaweicloudsdkmrs.v2.model.update_cluster_req import UpdateClusterReq
from huaweicloudsdkmrs.v2.model.update_data_connector_request import UpdateDataConnectorRequest
from huaweicloudsdkmrs.v2.model.update_data_connector_response import UpdateDataConnectorResponse
from huaweicloudsdkmrs.v2.model.update_sync_iam_user_request import UpdateSyncIamUserRequest
from huaweicloudsdkmrs.v2.model.update_sync_iam_user_response import UpdateSyncIamUserResponse
from huaweicloudsdkmrs.v2.model.update_sync_request import UpdateSyncRequest
from huaweicloudsdkmrs.v2.model.volume import Volume
