# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkvod.v1.model.asset_details import AssetDetails
from huaweicloudsdkvod.v1.model.asset_info import AssetInfo
from huaweicloudsdkvod.v1.model.asset_process_req import AssetProcessReq
from huaweicloudsdkvod.v1.model.asset_review_req import AssetReviewReq
from huaweicloudsdkvod.v1.model.asset_summary import AssetSummary
from huaweicloudsdkvod.v1.model.audio_info import AudioInfo
from huaweicloudsdkvod.v1.model.audio_template_info import AudioTemplateInfo
from huaweicloudsdkvod.v1.model.base_info import BaseInfo
from huaweicloudsdkvod.v1.model.cancel_asset_transcode_task_request import CancelAssetTranscodeTaskRequest
from huaweicloudsdkvod.v1.model.cancel_asset_transcode_task_response import CancelAssetTranscodeTaskResponse
from huaweicloudsdkvod.v1.model.cancel_extract_audio_task_request import CancelExtractAudioTaskRequest
from huaweicloudsdkvod.v1.model.cancel_extract_audio_task_response import CancelExtractAudioTaskResponse
from huaweicloudsdkvod.v1.model.cdn_log import CdnLog
from huaweicloudsdkvod.v1.model.check_md5_duplication_request import CheckMd5DuplicationRequest
from huaweicloudsdkvod.v1.model.check_md5_duplication_response import CheckMd5DuplicationResponse
from huaweicloudsdkvod.v1.model.common import Common
from huaweicloudsdkvod.v1.model.common_info import CommonInfo
from huaweicloudsdkvod.v1.model.confirm_asset_upload_req import ConfirmAssetUploadReq
from huaweicloudsdkvod.v1.model.confirm_asset_upload_request import ConfirmAssetUploadRequest
from huaweicloudsdkvod.v1.model.confirm_asset_upload_response import ConfirmAssetUploadResponse
from huaweicloudsdkvod.v1.model.confirm_image_upload_req import ConfirmImageUploadReq
from huaweicloudsdkvod.v1.model.confirm_image_upload_request import ConfirmImageUploadRequest
from huaweicloudsdkvod.v1.model.confirm_image_upload_response import ConfirmImageUploadResponse
from huaweicloudsdkvod.v1.model.cover_info import CoverInfo
from huaweicloudsdkvod.v1.model.create_asset_by_file_upload_req import CreateAssetByFileUploadReq
from huaweicloudsdkvod.v1.model.create_asset_by_file_upload_request import CreateAssetByFileUploadRequest
from huaweicloudsdkvod.v1.model.create_asset_by_file_upload_response import CreateAssetByFileUploadResponse
from huaweicloudsdkvod.v1.model.create_asset_category_request import CreateAssetCategoryRequest
from huaweicloudsdkvod.v1.model.create_asset_category_response import CreateAssetCategoryResponse
from huaweicloudsdkvod.v1.model.create_asset_process_task_request import CreateAssetProcessTaskRequest
from huaweicloudsdkvod.v1.model.create_asset_process_task_response import CreateAssetProcessTaskResponse
from huaweicloudsdkvod.v1.model.create_asset_review_task_request import CreateAssetReviewTaskRequest
from huaweicloudsdkvod.v1.model.create_asset_review_task_response import CreateAssetReviewTaskResponse
from huaweicloudsdkvod.v1.model.create_category_req import CreateCategoryReq
from huaweicloudsdkvod.v1.model.create_extract_audio_task_request import CreateExtractAudioTaskRequest
from huaweicloudsdkvod.v1.model.create_extract_audio_task_response import CreateExtractAudioTaskResponse
from huaweicloudsdkvod.v1.model.create_preheating_asset_req import CreatePreheatingAssetReq
from huaweicloudsdkvod.v1.model.create_preheating_asset_request import CreatePreheatingAssetRequest
from huaweicloudsdkvod.v1.model.create_preheating_asset_response import CreatePreheatingAssetResponse
from huaweicloudsdkvod.v1.model.create_take_over_task_req import CreateTakeOverTaskReq
from huaweicloudsdkvod.v1.model.create_take_over_task_request import CreateTakeOverTaskRequest
from huaweicloudsdkvod.v1.model.create_take_over_task_response import CreateTakeOverTaskResponse
from huaweicloudsdkvod.v1.model.create_template_group_collection_request import CreateTemplateGroupCollectionRequest
from huaweicloudsdkvod.v1.model.create_template_group_collection_response import CreateTemplateGroupCollectionResponse
from huaweicloudsdkvod.v1.model.create_template_group_request import CreateTemplateGroupRequest
from huaweicloudsdkvod.v1.model.create_template_group_response import CreateTemplateGroupResponse
from huaweicloudsdkvod.v1.model.create_transcode_template import CreateTranscodeTemplate
from huaweicloudsdkvod.v1.model.create_transcode_template_request import CreateTranscodeTemplateRequest
from huaweicloudsdkvod.v1.model.create_transcode_template_response import CreateTranscodeTemplateResponse
from huaweicloudsdkvod.v1.model.create_watermark_template_req import CreateWatermarkTemplateReq
from huaweicloudsdkvod.v1.model.create_watermark_template_request import CreateWatermarkTemplateRequest
from huaweicloudsdkvod.v1.model.create_watermark_template_response import CreateWatermarkTemplateResponse
from huaweicloudsdkvod.v1.model.delete_asset_category_request import DeleteAssetCategoryRequest
from huaweicloudsdkvod.v1.model.delete_asset_category_response import DeleteAssetCategoryResponse
from huaweicloudsdkvod.v1.model.delete_assets_request import DeleteAssetsRequest
from huaweicloudsdkvod.v1.model.delete_assets_response import DeleteAssetsResponse
from huaweicloudsdkvod.v1.model.delete_result import DeleteResult
from huaweicloudsdkvod.v1.model.delete_template_group_collection_request import DeleteTemplateGroupCollectionRequest
from huaweicloudsdkvod.v1.model.delete_template_group_collection_response import DeleteTemplateGroupCollectionResponse
from huaweicloudsdkvod.v1.model.delete_template_group_request import DeleteTemplateGroupRequest
from huaweicloudsdkvod.v1.model.delete_template_group_response import DeleteTemplateGroupResponse
from huaweicloudsdkvod.v1.model.delete_transcode_template_request import DeleteTranscodeTemplateRequest
from huaweicloudsdkvod.v1.model.delete_transcode_template_response import DeleteTranscodeTemplateResponse
from huaweicloudsdkvod.v1.model.delete_watermark_template_request import DeleteWatermarkTemplateRequest
from huaweicloudsdkvod.v1.model.delete_watermark_template_response import DeleteWatermarkTemplateResponse
from huaweicloudsdkvod.v1.model.extract_audio_task_req import ExtractAudioTaskReq
from huaweicloudsdkvod.v1.model.file_addr import FileAddr
from huaweicloudsdkvod.v1.model.list_asset_category_request import ListAssetCategoryRequest
from huaweicloudsdkvod.v1.model.list_asset_category_response import ListAssetCategoryResponse
from huaweicloudsdkvod.v1.model.list_asset_list_request import ListAssetListRequest
from huaweicloudsdkvod.v1.model.list_asset_list_response import ListAssetListResponse
from huaweicloudsdkvod.v1.model.list_domain_logs_request import ListDomainLogsRequest
from huaweicloudsdkvod.v1.model.list_domain_logs_response import ListDomainLogsResponse
from huaweicloudsdkvod.v1.model.list_take_over_task_request import ListTakeOverTaskRequest
from huaweicloudsdkvod.v1.model.list_take_over_task_response import ListTakeOverTaskResponse
from huaweicloudsdkvod.v1.model.list_template_group_collection_request import ListTemplateGroupCollectionRequest
from huaweicloudsdkvod.v1.model.list_template_group_collection_response import ListTemplateGroupCollectionResponse
from huaweicloudsdkvod.v1.model.list_template_group_request import ListTemplateGroupRequest
from huaweicloudsdkvod.v1.model.list_template_group_response import ListTemplateGroupResponse
from huaweicloudsdkvod.v1.model.list_top_statistics_request import ListTopStatisticsRequest
from huaweicloudsdkvod.v1.model.list_top_statistics_response import ListTopStatisticsResponse
from huaweicloudsdkvod.v1.model.list_transcode_template_request import ListTranscodeTemplateRequest
from huaweicloudsdkvod.v1.model.list_transcode_template_response import ListTranscodeTemplateResponse
from huaweicloudsdkvod.v1.model.list_watermark_template_request import ListWatermarkTemplateRequest
from huaweicloudsdkvod.v1.model.list_watermark_template_response import ListWatermarkTemplateResponse
from huaweicloudsdkvod.v1.model.meta_data import MetaData
from huaweicloudsdkvod.v1.model.modify_template_group_collection import ModifyTemplateGroupCollection
from huaweicloudsdkvod.v1.model.modify_trans_template import ModifyTransTemplate
from huaweicloudsdkvod.v1.model.modify_trans_template_group import ModifyTransTemplateGroup
from huaweicloudsdkvod.v1.model.output import Output
from huaweicloudsdkvod.v1.model.parameter import Parameter
from huaweicloudsdkvod.v1.model.picture_review_ret import PictureReviewRet
from huaweicloudsdkvod.v1.model.play_info import PlayInfo
from huaweicloudsdkvod.v1.model.preheating_result import PreheatingResult
from huaweicloudsdkvod.v1.model.publish_asset_from_obs_req import PublishAssetFromObsReq
from huaweicloudsdkvod.v1.model.publish_asset_from_obs_request import PublishAssetFromObsRequest
from huaweicloudsdkvod.v1.model.publish_asset_from_obs_response import PublishAssetFromObsResponse
from huaweicloudsdkvod.v1.model.publish_asset_req import PublishAssetReq
from huaweicloudsdkvod.v1.model.publish_assets_request import PublishAssetsRequest
from huaweicloudsdkvod.v1.model.publish_assets_response import PublishAssetsResponse
from huaweicloudsdkvod.v1.model.quality_info import QualityInfo
from huaweicloudsdkvod.v1.model.quality_info_list import QualityInfoList
from huaweicloudsdkvod.v1.model.query_category_rsp import QueryCategoryRsp
from huaweicloudsdkvod.v1.model.review import Review
from huaweicloudsdkvod.v1.model.review_detail import ReviewDetail
from huaweicloudsdkvod.v1.model.review_info import ReviewInfo
from huaweicloudsdkvod.v1.model.show_asset_cipher_request import ShowAssetCipherRequest
from huaweicloudsdkvod.v1.model.show_asset_cipher_response import ShowAssetCipherResponse
from huaweicloudsdkvod.v1.model.show_asset_detail_request import ShowAssetDetailRequest
from huaweicloudsdkvod.v1.model.show_asset_detail_response import ShowAssetDetailResponse
from huaweicloudsdkvod.v1.model.show_asset_meta_request import ShowAssetMetaRequest
from huaweicloudsdkvod.v1.model.show_asset_meta_response import ShowAssetMetaResponse
from huaweicloudsdkvod.v1.model.show_asset_temp_authority_request import ShowAssetTempAuthorityRequest
from huaweicloudsdkvod.v1.model.show_asset_temp_authority_response import ShowAssetTempAuthorityResponse
from huaweicloudsdkvod.v1.model.show_cdn_statistics_request import ShowCdnStatisticsRequest
from huaweicloudsdkvod.v1.model.show_cdn_statistics_response import ShowCdnStatisticsResponse
from huaweicloudsdkvod.v1.model.show_preheating_asset_request import ShowPreheatingAssetRequest
from huaweicloudsdkvod.v1.model.show_preheating_asset_response import ShowPreheatingAssetResponse
from huaweicloudsdkvod.v1.model.show_take_over_asset_details_request import ShowTakeOverAssetDetailsRequest
from huaweicloudsdkvod.v1.model.show_take_over_asset_details_response import ShowTakeOverAssetDetailsResponse
from huaweicloudsdkvod.v1.model.show_take_over_task_details_request import ShowTakeOverTaskDetailsRequest
from huaweicloudsdkvod.v1.model.show_take_over_task_details_response import ShowTakeOverTaskDetailsResponse
from huaweicloudsdkvod.v1.model.show_vod_statistics_request import ShowVodStatisticsRequest
from huaweicloudsdkvod.v1.model.show_vod_statistics_response import ShowVodStatisticsResponse
from huaweicloudsdkvod.v1.model.subtitle import Subtitle
from huaweicloudsdkvod.v1.model.subtitle_info import SubtitleInfo
from huaweicloudsdkvod.v1.model.take_over_task import TakeOverTask
from huaweicloudsdkvod.v1.model.template_group import TemplateGroup
from huaweicloudsdkvod.v1.model.template_group_collection import TemplateGroupCollection
from huaweicloudsdkvod.v1.model.text_review_ret import TextReviewRet
from huaweicloudsdkvod.v1.model.thumbnail import Thumbnail
from huaweicloudsdkvod.v1.model.thumbnail_info import ThumbnailInfo
from huaweicloudsdkvod.v1.model.thumbnail_rsp import ThumbnailRsp
from huaweicloudsdkvod.v1.model.top_url import TopUrl
from huaweicloudsdkvod.v1.model.trans_template_group import TransTemplateGroup
from huaweicloudsdkvod.v1.model.trans_template_group_collection import TransTemplateGroupCollection
from huaweicloudsdkvod.v1.model.trans_template_rsp import TransTemplateRsp
from huaweicloudsdkvod.v1.model.transcode_info import TranscodeInfo
from huaweicloudsdkvod.v1.model.unpublish_assets_request import UnpublishAssetsRequest
from huaweicloudsdkvod.v1.model.unpublish_assets_response import UnpublishAssetsResponse
from huaweicloudsdkvod.v1.model.update_asset_category_request import UpdateAssetCategoryRequest
from huaweicloudsdkvod.v1.model.update_asset_category_response import UpdateAssetCategoryResponse
from huaweicloudsdkvod.v1.model.update_asset_meta_req import UpdateAssetMetaReq
from huaweicloudsdkvod.v1.model.update_asset_meta_request import UpdateAssetMetaRequest
from huaweicloudsdkvod.v1.model.update_asset_meta_response import UpdateAssetMetaResponse
from huaweicloudsdkvod.v1.model.update_asset_request import UpdateAssetRequest
from huaweicloudsdkvod.v1.model.update_asset_response import UpdateAssetResponse
from huaweicloudsdkvod.v1.model.update_bucket_authorized_req import UpdateBucketAuthorizedReq
from huaweicloudsdkvod.v1.model.update_bucket_authorized_request import UpdateBucketAuthorizedRequest
from huaweicloudsdkvod.v1.model.update_bucket_authorized_response import UpdateBucketAuthorizedResponse
from huaweicloudsdkvod.v1.model.update_category_req import UpdateCategoryReq
from huaweicloudsdkvod.v1.model.update_cover_by_thumbnail_req import UpdateCoverByThumbnailReq
from huaweicloudsdkvod.v1.model.update_cover_by_thumbnail_request import UpdateCoverByThumbnailRequest
from huaweicloudsdkvod.v1.model.update_cover_by_thumbnail_response import UpdateCoverByThumbnailResponse
from huaweicloudsdkvod.v1.model.update_template_group_collection_request import UpdateTemplateGroupCollectionRequest
from huaweicloudsdkvod.v1.model.update_template_group_collection_response import UpdateTemplateGroupCollectionResponse
from huaweicloudsdkvod.v1.model.update_template_group_request import UpdateTemplateGroupRequest
from huaweicloudsdkvod.v1.model.update_template_group_response import UpdateTemplateGroupResponse
from huaweicloudsdkvod.v1.model.update_transcode_template_request import UpdateTranscodeTemplateRequest
from huaweicloudsdkvod.v1.model.update_transcode_template_response import UpdateTranscodeTemplateResponse
from huaweicloudsdkvod.v1.model.update_watermark_template_req import UpdateWatermarkTemplateReq
from huaweicloudsdkvod.v1.model.update_watermark_template_request import UpdateWatermarkTemplateRequest
from huaweicloudsdkvod.v1.model.update_watermark_template_response import UpdateWatermarkTemplateResponse
from huaweicloudsdkvod.v1.model.upload_asset import UploadAsset
from huaweicloudsdkvod.v1.model.upload_asset_req import UploadAssetReq
from huaweicloudsdkvod.v1.model.upload_meta_data_by_url import UploadMetaDataByUrl
from huaweicloudsdkvod.v1.model.upload_meta_data_by_url_req import UploadMetaDataByUrlReq
from huaweicloudsdkvod.v1.model.upload_meta_data_by_url_request import UploadMetaDataByUrlRequest
from huaweicloudsdkvod.v1.model.upload_meta_data_by_url_response import UploadMetaDataByUrlResponse
from huaweicloudsdkvod.v1.model.video_info import VideoInfo
from huaweicloudsdkvod.v1.model.video_template_info import VideoTemplateInfo
from huaweicloudsdkvod.v1.model.video_type_ref import VideoTypeRef
from huaweicloudsdkvod.v1.model.vod_sample_data import VodSampleData
from huaweicloudsdkvod.v1.model.watermark_template import WatermarkTemplate
