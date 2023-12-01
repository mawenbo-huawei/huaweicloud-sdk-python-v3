# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkoms.v2.model.bandwidth_policy_dto import BandwidthPolicyDto
from huaweicloudsdkoms.v2.model.check_prefix_req import CheckPrefixReq
from huaweicloudsdkoms.v2.model.check_prefix_request import CheckPrefixRequest
from huaweicloudsdkoms.v2.model.check_prefix_response import CheckPrefixResponse
from huaweicloudsdkoms.v2.model.checked_key import CheckedKey
from huaweicloudsdkoms.v2.model.create_sync_events_request import CreateSyncEventsRequest
from huaweicloudsdkoms.v2.model.create_sync_events_response import CreateSyncEventsResponse
from huaweicloudsdkoms.v2.model.create_sync_task_req import CreateSyncTaskReq
from huaweicloudsdkoms.v2.model.create_sync_task_request import CreateSyncTaskRequest
from huaweicloudsdkoms.v2.model.create_sync_task_response import CreateSyncTaskResponse
from huaweicloudsdkoms.v2.model.create_task_group_req import CreateTaskGroupReq
from huaweicloudsdkoms.v2.model.create_task_group_request import CreateTaskGroupRequest
from huaweicloudsdkoms.v2.model.create_task_group_response import CreateTaskGroupResponse
from huaweicloudsdkoms.v2.model.create_task_req import CreateTaskReq
from huaweicloudsdkoms.v2.model.create_task_request import CreateTaskRequest
from huaweicloudsdkoms.v2.model.create_task_response import CreateTaskResponse
from huaweicloudsdkoms.v2.model.delete_sync_task_request import DeleteSyncTaskRequest
from huaweicloudsdkoms.v2.model.delete_sync_task_response import DeleteSyncTaskResponse
from huaweicloudsdkoms.v2.model.delete_task_group_request import DeleteTaskGroupRequest
from huaweicloudsdkoms.v2.model.delete_task_group_response import DeleteTaskGroupResponse
from huaweicloudsdkoms.v2.model.delete_task_request import DeleteTaskRequest
from huaweicloudsdkoms.v2.model.delete_task_response import DeleteTaskResponse
from huaweicloudsdkoms.v2.model.dst_node_req import DstNodeReq
from huaweicloudsdkoms.v2.model.dst_node_resp import DstNodeResp
from huaweicloudsdkoms.v2.model.error_reason_resp import ErrorReasonResp
from huaweicloudsdkoms.v2.model.failed_object_record_dto import FailedObjectRecordDto
from huaweicloudsdkoms.v2.model.link import Link
from huaweicloudsdkoms.v2.model.list_api_versions_request import ListApiVersionsRequest
from huaweicloudsdkoms.v2.model.list_api_versions_response import ListApiVersionsResponse
from huaweicloudsdkoms.v2.model.list_buckets_req import ListBucketsReq
from huaweicloudsdkoms.v2.model.list_file import ListFile
from huaweicloudsdkoms.v2.model.list_sync_task_statistic_request import ListSyncTaskStatisticRequest
from huaweicloudsdkoms.v2.model.list_sync_task_statistic_response import ListSyncTaskStatisticResponse
from huaweicloudsdkoms.v2.model.list_sync_tasks_request import ListSyncTasksRequest
from huaweicloudsdkoms.v2.model.list_sync_tasks_response import ListSyncTasksResponse
from huaweicloudsdkoms.v2.model.list_task_group_request import ListTaskGroupRequest
from huaweicloudsdkoms.v2.model.list_task_group_response import ListTaskGroupResponse
from huaweicloudsdkoms.v2.model.list_tasks_request import ListTasksRequest
from huaweicloudsdkoms.v2.model.list_tasks_response import ListTasksResponse
from huaweicloudsdkoms.v2.model.prefix_key_info import PrefixKeyInfo
from huaweicloudsdkoms.v2.model.region_info import RegionInfo
from huaweicloudsdkoms.v2.model.retry_task_group_req import RetryTaskGroupReq
from huaweicloudsdkoms.v2.model.retry_task_group_request import RetryTaskGroupRequest
from huaweicloudsdkoms.v2.model.retry_task_group_response import RetryTaskGroupResponse
from huaweicloudsdkoms.v2.model.show_api_info_request import ShowApiInfoRequest
from huaweicloudsdkoms.v2.model.show_api_info_response import ShowApiInfoResponse
from huaweicloudsdkoms.v2.model.show_bucket_list_request import ShowBucketListRequest
from huaweicloudsdkoms.v2.model.show_bucket_list_response import ShowBucketListResponse
from huaweicloudsdkoms.v2.model.show_bucket_objects_request import ShowBucketObjectsRequest
from huaweicloudsdkoms.v2.model.show_bucket_objects_response import ShowBucketObjectsResponse
from huaweicloudsdkoms.v2.model.show_bucket_record import ShowBucketRecord
from huaweicloudsdkoms.v2.model.show_bucket_region_req import ShowBucketRegionReq
from huaweicloudsdkoms.v2.model.show_bucket_region_request import ShowBucketRegionRequest
from huaweicloudsdkoms.v2.model.show_bucket_region_response import ShowBucketRegionResponse
from huaweicloudsdkoms.v2.model.show_bucket_req import ShowBucketReq
from huaweicloudsdkoms.v2.model.show_cdn_info_req import ShowCdnInfoReq
from huaweicloudsdkoms.v2.model.show_cdn_info_request import ShowCdnInfoRequest
from huaweicloudsdkoms.v2.model.show_cdn_info_response import ShowCdnInfoResponse
from huaweicloudsdkoms.v2.model.show_cloud_type_request import ShowCloudTypeRequest
from huaweicloudsdkoms.v2.model.show_cloud_type_response import ShowCloudTypeResponse
from huaweicloudsdkoms.v2.model.show_region_info_request import ShowRegionInfoRequest
from huaweicloudsdkoms.v2.model.show_region_info_resp import ShowRegionInfoResp
from huaweicloudsdkoms.v2.model.show_region_info_response import ShowRegionInfoResponse
from huaweicloudsdkoms.v2.model.show_sync_task_request import ShowSyncTaskRequest
from huaweicloudsdkoms.v2.model.show_sync_task_response import ShowSyncTaskResponse
from huaweicloudsdkoms.v2.model.show_task_group_request import ShowTaskGroupRequest
from huaweicloudsdkoms.v2.model.show_task_group_response import ShowTaskGroupResponse
from huaweicloudsdkoms.v2.model.show_task_request import ShowTaskRequest
from huaweicloudsdkoms.v2.model.show_task_response import ShowTaskResponse
from huaweicloudsdkoms.v2.model.smn_config import SmnConfig
from huaweicloudsdkoms.v2.model.smn_info import SmnInfo
from huaweicloudsdkoms.v2.model.source_cdn_req import SourceCdnReq
from huaweicloudsdkoms.v2.model.source_cdn_resp import SourceCdnResp
from huaweicloudsdkoms.v2.model.src_node_req import SrcNodeReq
from huaweicloudsdkoms.v2.model.src_node_resp import SrcNodeResp
from huaweicloudsdkoms.v2.model.start_sync_task_req import StartSyncTaskReq
from huaweicloudsdkoms.v2.model.start_sync_task_request import StartSyncTaskRequest
from huaweicloudsdkoms.v2.model.start_sync_task_response import StartSyncTaskResponse
from huaweicloudsdkoms.v2.model.start_task_group_req import StartTaskGroupReq
from huaweicloudsdkoms.v2.model.start_task_group_request import StartTaskGroupRequest
from huaweicloudsdkoms.v2.model.start_task_group_response import StartTaskGroupResponse
from huaweicloudsdkoms.v2.model.start_task_req import StartTaskReq
from huaweicloudsdkoms.v2.model.start_task_request import StartTaskRequest
from huaweicloudsdkoms.v2.model.start_task_response import StartTaskResponse
from huaweicloudsdkoms.v2.model.statistic_data import StatisticData
from huaweicloudsdkoms.v2.model.statistic_type_data import StatisticTypeData
from huaweicloudsdkoms.v2.model.stop_sync_task_request import StopSyncTaskRequest
from huaweicloudsdkoms.v2.model.stop_sync_task_response import StopSyncTaskResponse
from huaweicloudsdkoms.v2.model.stop_task_group_request import StopTaskGroupRequest
from huaweicloudsdkoms.v2.model.stop_task_group_response import StopTaskGroupResponse
from huaweicloudsdkoms.v2.model.stop_task_request import StopTaskRequest
from huaweicloudsdkoms.v2.model.stop_task_response import StopTaskResponse
from huaweicloudsdkoms.v2.model.sync_object_req import SyncObjectReq
from huaweicloudsdkoms.v2.model.sync_task_info import SyncTaskInfo
from huaweicloudsdkoms.v2.model.task_group_dst_node import TaskGroupDstNode
from huaweicloudsdkoms.v2.model.task_group_dst_node_resp import TaskGroupDstNodeResp
from huaweicloudsdkoms.v2.model.task_group_resp import TaskGroupResp
from huaweicloudsdkoms.v2.model.task_group_src_node import TaskGroupSrcNode
from huaweicloudsdkoms.v2.model.task_group_src_node_resp import TaskGroupSrcNodeResp
from huaweicloudsdkoms.v2.model.task_resp import TaskResp
from huaweicloudsdkoms.v2.model.update_bandwidth_policy_req import UpdateBandwidthPolicyReq
from huaweicloudsdkoms.v2.model.update_bandwidth_policy_request import UpdateBandwidthPolicyRequest
from huaweicloudsdkoms.v2.model.update_bandwidth_policy_response import UpdateBandwidthPolicyResponse
from huaweicloudsdkoms.v2.model.update_task_group_request import UpdateTaskGroupRequest
from huaweicloudsdkoms.v2.model.update_task_group_response import UpdateTaskGroupResponse
from huaweicloudsdkoms.v2.model.version import Version
