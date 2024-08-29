# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkevs.v2.model.attachment import Attachment
from huaweicloudsdkevs.v2.model.az_info import AzInfo
from huaweicloudsdkevs.v2.model.batch_create_volume_tags_request import BatchCreateVolumeTagsRequest
from huaweicloudsdkevs.v2.model.batch_create_volume_tags_request_body import BatchCreateVolumeTagsRequestBody
from huaweicloudsdkevs.v2.model.batch_create_volume_tags_response import BatchCreateVolumeTagsResponse
from huaweicloudsdkevs.v2.model.batch_delete_volume_tags_request import BatchDeleteVolumeTagsRequest
from huaweicloudsdkevs.v2.model.batch_delete_volume_tags_request_body import BatchDeleteVolumeTagsRequestBody
from huaweicloudsdkevs.v2.model.batch_delete_volume_tags_response import BatchDeleteVolumeTagsResponse
from huaweicloudsdkevs.v2.model.bss_param2 import BssParam2
from huaweicloudsdkevs.v2.model.bss_param_for_create_volume import BssParamForCreateVolume
from huaweicloudsdkevs.v2.model.bss_param_for_resize_volume import BssParamForResizeVolume
from huaweicloudsdkevs.v2.model.bss_param_for_retype_volume import BssParamForRetypeVolume
from huaweicloudsdkevs.v2.model.change_volume_charge_mode_request import ChangeVolumeChargeModeRequest
from huaweicloudsdkevs.v2.model.change_volume_charge_mode_request_body import ChangeVolumeChargeModeRequestBody
from huaweicloudsdkevs.v2.model.change_volume_charge_mode_response import ChangeVolumeChargeModeResponse
from huaweicloudsdkevs.v2.model.cinder_accept_volume_transfer_option import CinderAcceptVolumeTransferOption
from huaweicloudsdkevs.v2.model.cinder_accept_volume_transfer_request import CinderAcceptVolumeTransferRequest
from huaweicloudsdkevs.v2.model.cinder_accept_volume_transfer_request_body import CinderAcceptVolumeTransferRequestBody
from huaweicloudsdkevs.v2.model.cinder_accept_volume_transfer_response import CinderAcceptVolumeTransferResponse
from huaweicloudsdkevs.v2.model.cinder_create_volume_transfer_request import CinderCreateVolumeTransferRequest
from huaweicloudsdkevs.v2.model.cinder_create_volume_transfer_request_body import CinderCreateVolumeTransferRequestBody
from huaweicloudsdkevs.v2.model.cinder_create_volume_transfer_response import CinderCreateVolumeTransferResponse
from huaweicloudsdkevs.v2.model.cinder_delete_volume_transfer_request import CinderDeleteVolumeTransferRequest
from huaweicloudsdkevs.v2.model.cinder_delete_volume_transfer_response import CinderDeleteVolumeTransferResponse
from huaweicloudsdkevs.v2.model.cinder_list_availability_zones_request import CinderListAvailabilityZonesRequest
from huaweicloudsdkevs.v2.model.cinder_list_availability_zones_response import CinderListAvailabilityZonesResponse
from huaweicloudsdkevs.v2.model.cinder_list_quotas_request import CinderListQuotasRequest
from huaweicloudsdkevs.v2.model.cinder_list_quotas_response import CinderListQuotasResponse
from huaweicloudsdkevs.v2.model.cinder_list_volume_transfers_request import CinderListVolumeTransfersRequest
from huaweicloudsdkevs.v2.model.cinder_list_volume_transfers_response import CinderListVolumeTransfersResponse
from huaweicloudsdkevs.v2.model.cinder_list_volume_types_request import CinderListVolumeTypesRequest
from huaweicloudsdkevs.v2.model.cinder_list_volume_types_response import CinderListVolumeTypesResponse
from huaweicloudsdkevs.v2.model.cinder_show_volume_transfer_request import CinderShowVolumeTransferRequest
from huaweicloudsdkevs.v2.model.cinder_show_volume_transfer_response import CinderShowVolumeTransferResponse
from huaweicloudsdkevs.v2.model.create_snapshot_option import CreateSnapshotOption
from huaweicloudsdkevs.v2.model.create_snapshot_request import CreateSnapshotRequest
from huaweicloudsdkevs.v2.model.create_snapshot_request_body import CreateSnapshotRequestBody
from huaweicloudsdkevs.v2.model.create_snapshot_response import CreateSnapshotResponse
from huaweicloudsdkevs.v2.model.create_volume_option import CreateVolumeOption
from huaweicloudsdkevs.v2.model.create_volume_request import CreateVolumeRequest
from huaweicloudsdkevs.v2.model.create_volume_request_body import CreateVolumeRequestBody
from huaweicloudsdkevs.v2.model.create_volume_response import CreateVolumeResponse
from huaweicloudsdkevs.v2.model.create_volume_scheduler_hints import CreateVolumeSchedulerHints
from huaweicloudsdkevs.v2.model.create_volume_transfer_detail import CreateVolumeTransferDetail
from huaweicloudsdkevs.v2.model.create_volume_transfer_option import CreateVolumeTransferOption
from huaweicloudsdkevs.v2.model.delete_snapshot_request import DeleteSnapshotRequest
from huaweicloudsdkevs.v2.model.delete_snapshot_response import DeleteSnapshotResponse
from huaweicloudsdkevs.v2.model.delete_tags_option import DeleteTagsOption
from huaweicloudsdkevs.v2.model.delete_volume_request import DeleteVolumeRequest
from huaweicloudsdkevs.v2.model.delete_volume_response import DeleteVolumeResponse
from huaweicloudsdkevs.v2.model.iops import Iops
from huaweicloudsdkevs.v2.model.job_entities import JobEntities
from huaweicloudsdkevs.v2.model.link import Link
from huaweicloudsdkevs.v2.model.list_snapshots_request import ListSnapshotsRequest
from huaweicloudsdkevs.v2.model.list_snapshots_response import ListSnapshotsResponse
from huaweicloudsdkevs.v2.model.list_versions_request import ListVersionsRequest
from huaweicloudsdkevs.v2.model.list_versions_response import ListVersionsResponse
from huaweicloudsdkevs.v2.model.list_volume_tags_request import ListVolumeTagsRequest
from huaweicloudsdkevs.v2.model.list_volume_tags_response import ListVolumeTagsResponse
from huaweicloudsdkevs.v2.model.list_volumes_by_tags_request import ListVolumesByTagsRequest
from huaweicloudsdkevs.v2.model.list_volumes_by_tags_request_body import ListVolumesByTagsRequestBody
from huaweicloudsdkevs.v2.model.list_volumes_by_tags_response import ListVolumesByTagsResponse
from huaweicloudsdkevs.v2.model.list_volumes_request import ListVolumesRequest
from huaweicloudsdkevs.v2.model.list_volumes_response import ListVolumesResponse
from huaweicloudsdkevs.v2.model.match import Match
from huaweicloudsdkevs.v2.model.media_types import MediaTypes
from huaweicloudsdkevs.v2.model.modify_volume_qo_s_option import ModifyVolumeQoSOption
from huaweicloudsdkevs.v2.model.modify_volume_qo_s_request import ModifyVolumeQoSRequest
from huaweicloudsdkevs.v2.model.modify_volume_qo_s_request_body import ModifyVolumeQoSRequestBody
from huaweicloudsdkevs.v2.model.modify_volume_qo_s_response import ModifyVolumeQoSResponse
from huaweicloudsdkevs.v2.model.os_extend import OsExtend
from huaweicloudsdkevs.v2.model.quota_detail import QuotaDetail
from huaweicloudsdkevs.v2.model.quota_detail_backup_gigabytes import QuotaDetailBackupGigabytes
from huaweicloudsdkevs.v2.model.quota_detail_backups import QuotaDetailBackups
from huaweicloudsdkevs.v2.model.quota_detail_gigabytes import QuotaDetailGigabytes
from huaweicloudsdkevs.v2.model.quota_detail_gigabytes_gpssd import QuotaDetailGigabytesGPSSD
from huaweicloudsdkevs.v2.model.quota_detail_gigabytes_sas import QuotaDetailGigabytesSAS
from huaweicloudsdkevs.v2.model.quota_detail_gigabytes_sata import QuotaDetailGigabytesSATA
from huaweicloudsdkevs.v2.model.quota_detail_gigabytes_ssd import QuotaDetailGigabytesSSD
from huaweicloudsdkevs.v2.model.quota_detail_per_volume_gigabytes import QuotaDetailPerVolumeGigabytes
from huaweicloudsdkevs.v2.model.quota_detail_snapshots import QuotaDetailSnapshots
from huaweicloudsdkevs.v2.model.quota_detail_snapshots_gpssd import QuotaDetailSnapshotsGPSSD
from huaweicloudsdkevs.v2.model.quota_detail_snapshots_sas import QuotaDetailSnapshotsSAS
from huaweicloudsdkevs.v2.model.quota_detail_snapshots_sata import QuotaDetailSnapshotsSATA
from huaweicloudsdkevs.v2.model.quota_detail_snapshots_ssd import QuotaDetailSnapshotsSSD
from huaweicloudsdkevs.v2.model.quota_detail_volumes import QuotaDetailVolumes
from huaweicloudsdkevs.v2.model.quota_detail_volumes_gpssd import QuotaDetailVolumesGPSSD
from huaweicloudsdkevs.v2.model.quota_detail_volumes_sas import QuotaDetailVolumesSAS
from huaweicloudsdkevs.v2.model.quota_detail_volumes_sata import QuotaDetailVolumesSATA
from huaweicloudsdkevs.v2.model.quota_detail_volumes_ssd import QuotaDetailVolumesSSD
from huaweicloudsdkevs.v2.model.quota_list import QuotaList
from huaweicloudsdkevs.v2.model.resize_volume_request import ResizeVolumeRequest
from huaweicloudsdkevs.v2.model.resize_volume_request_body import ResizeVolumeRequestBody
from huaweicloudsdkevs.v2.model.resize_volume_response import ResizeVolumeResponse
from huaweicloudsdkevs.v2.model.resource import Resource
from huaweicloudsdkevs.v2.model.retype_volume import RetypeVolume
from huaweicloudsdkevs.v2.model.retype_volume_request import RetypeVolumeRequest
from huaweicloudsdkevs.v2.model.retype_volume_request_body import RetypeVolumeRequestBody
from huaweicloudsdkevs.v2.model.retype_volume_response import RetypeVolumeResponse
from huaweicloudsdkevs.v2.model.rollback_info import RollbackInfo
from huaweicloudsdkevs.v2.model.rollback_snapshot_option import RollbackSnapshotOption
from huaweicloudsdkevs.v2.model.rollback_snapshot_request import RollbackSnapshotRequest
from huaweicloudsdkevs.v2.model.rollback_snapshot_request_body import RollbackSnapshotRequestBody
from huaweicloudsdkevs.v2.model.rollback_snapshot_response import RollbackSnapshotResponse
from huaweicloudsdkevs.v2.model.show_job_request import ShowJobRequest
from huaweicloudsdkevs.v2.model.show_job_response import ShowJobResponse
from huaweicloudsdkevs.v2.model.show_snapshot_request import ShowSnapshotRequest
from huaweicloudsdkevs.v2.model.show_snapshot_response import ShowSnapshotResponse
from huaweicloudsdkevs.v2.model.show_version_request import ShowVersionRequest
from huaweicloudsdkevs.v2.model.show_version_response import ShowVersionResponse
from huaweicloudsdkevs.v2.model.show_volume_request import ShowVolumeRequest
from huaweicloudsdkevs.v2.model.show_volume_response import ShowVolumeResponse
from huaweicloudsdkevs.v2.model.show_volume_tags_request import ShowVolumeTagsRequest
from huaweicloudsdkevs.v2.model.show_volume_tags_response import ShowVolumeTagsResponse
from huaweicloudsdkevs.v2.model.snapshot_details import SnapshotDetails
from huaweicloudsdkevs.v2.model.snapshot_list import SnapshotList
from huaweicloudsdkevs.v2.model.sub_job import SubJob
from huaweicloudsdkevs.v2.model.sub_job_entities import SubJobEntities
from huaweicloudsdkevs.v2.model.tag import Tag
from huaweicloudsdkevs.v2.model.tags_for_list_volumes import TagsForListVolumes
from huaweicloudsdkevs.v2.model.throughput import Throughput
from huaweicloudsdkevs.v2.model.unsubscribe_postpaid_volume_request import UnsubscribePostpaidVolumeRequest
from huaweicloudsdkevs.v2.model.unsubscribe_postpaid_volume_response import UnsubscribePostpaidVolumeResponse
from huaweicloudsdkevs.v2.model.unsubscribe_volume import UnsubscribeVolume
from huaweicloudsdkevs.v2.model.unsubscribe_volume_request_body import UnsubscribeVolumeRequestBody
from huaweicloudsdkevs.v2.model.unsubscribe_volume_response_body import UnsubscribeVolumeResponseBody
from huaweicloudsdkevs.v2.model.update_snapshot_option import UpdateSnapshotOption
from huaweicloudsdkevs.v2.model.update_snapshot_request import UpdateSnapshotRequest
from huaweicloudsdkevs.v2.model.update_snapshot_request_body import UpdateSnapshotRequestBody
from huaweicloudsdkevs.v2.model.update_snapshot_response import UpdateSnapshotResponse
from huaweicloudsdkevs.v2.model.update_volume_option import UpdateVolumeOption
from huaweicloudsdkevs.v2.model.update_volume_request import UpdateVolumeRequest
from huaweicloudsdkevs.v2.model.update_volume_request_body import UpdateVolumeRequestBody
from huaweicloudsdkevs.v2.model.update_volume_response import UpdateVolumeResponse
from huaweicloudsdkevs.v2.model.versions import Versions
from huaweicloudsdkevs.v2.model.volume_detail import VolumeDetail
from huaweicloudsdkevs.v2.model.volume_detail_for_tag import VolumeDetailForTag
from huaweicloudsdkevs.v2.model.volume_metadata import VolumeMetadata
from huaweicloudsdkevs.v2.model.volume_transfer import VolumeTransfer
from huaweicloudsdkevs.v2.model.volume_transfer_summary import VolumeTransferSummary
from huaweicloudsdkevs.v2.model.volume_type import VolumeType
from huaweicloudsdkevs.v2.model.volume_type_extra_specs import VolumeTypeExtraSpecs
from huaweicloudsdkevs.v2.model.zone_state import ZoneState
