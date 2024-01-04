# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkmetastudio.v1.model.action_mark_item import ActionMarkItem
from huaweicloudsdkmetastudio.v1.model.animation_asset_meta import AnimationAssetMeta
from huaweicloudsdkmetastudio.v1.model.animation_config import AnimationConfig
from huaweicloudsdkmetastudio.v1.model.animation_item import AnimationItem
from huaweicloudsdkmetastudio.v1.model.asset_extra_meta import AssetExtraMeta
from huaweicloudsdkmetastudio.v1.model.asset_file_info import AssetFileInfo
from huaweicloudsdkmetastudio.v1.model.audit_result_admin_audit_result import AuditResultAdminAuditResult
from huaweicloudsdkmetastudio.v1.model.audit_result_system_audit_result import AuditResultSystemAuditResult
from huaweicloudsdkmetastudio.v1.model.audit_result_system_audit_result_errors import AuditResultSystemAuditResultErrors
from huaweicloudsdkmetastudio.v1.model.audition_file import AuditionFile
from huaweicloudsdkmetastudio.v1.model.background_config_info import BackgroundConfigInfo
from huaweicloudsdkmetastudio.v1.model.background_music_config import BackgroundMusicConfig
from huaweicloudsdkmetastudio.v1.model.business_card_image_config import BusinessCardImageConfig
from huaweicloudsdkmetastudio.v1.model.business_card_image_url import BusinessCardImageUrl
from huaweicloudsdkmetastudio.v1.model.business_card_text_config import BusinessCardTextConfig
from huaweicloudsdkmetastudio.v1.model.call_back_config import CallBackConfig
from huaweicloudsdkmetastudio.v1.model.cancel2_d_digital_human_video_request import Cancel2DDigitalHumanVideoRequest
from huaweicloudsdkmetastudio.v1.model.cancel2_d_digital_human_video_response import Cancel2DDigitalHumanVideoResponse
from huaweicloudsdkmetastudio.v1.model.cancel_photo_digital_human_video_request import CancelPhotoDigitalHumanVideoRequest
from huaweicloudsdkmetastudio.v1.model.cancel_photo_digital_human_video_response import CancelPhotoDigitalHumanVideoResponse
from huaweicloudsdkmetastudio.v1.model.check_text_language_request import CheckTextLanguageRequest
from huaweicloudsdkmetastudio.v1.model.check_text_language_response import CheckTextLanguageResponse
from huaweicloudsdkmetastudio.v1.model.comment_data import CommentData
from huaweicloudsdkmetastudio.v1.model.comment_log_info import CommentLogInfo
from huaweicloudsdkmetastudio.v1.model.commit_voice_training_job_request import CommitVoiceTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.commit_voice_training_job_response import CommitVoiceTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.component_info import ComponentInfo
from huaweicloudsdkmetastudio.v1.model.confirm_file_upload_request import ConfirmFileUploadRequest
from huaweicloudsdkmetastudio.v1.model.confirm_file_upload_request_body import ConfirmFileUploadRequestBody
from huaweicloudsdkmetastudio.v1.model.confirm_file_upload_response import ConfirmFileUploadResponse
from huaweicloudsdkmetastudio.v1.model.confirm_training_segment_request import ConfirmTrainingSegmentRequest
from huaweicloudsdkmetastudio.v1.model.confirm_training_segment_response import ConfirmTrainingSegmentResponse
from huaweicloudsdkmetastudio.v1.model.control_digital_human_live_req import ControlDigitalHumanLiveReq
from huaweicloudsdkmetastudio.v1.model.control_smart_live_req import ControlSmartLiveReq
from huaweicloudsdkmetastudio.v1.model.create2_d_digital_human_video_req import Create2DDigitalHumanVideoReq
from huaweicloudsdkmetastudio.v1.model.create2_d_digital_human_video_request import Create2DDigitalHumanVideoRequest
from huaweicloudsdkmetastudio.v1.model.create2_d_digital_human_video_response import Create2DDigitalHumanVideoResponse
from huaweicloudsdkmetastudio.v1.model.create2d_model_training_job_req import Create2dModelTrainingJobReq
from huaweicloudsdkmetastudio.v1.model.create2d_model_training_job_request import Create2dModelTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.create2d_model_training_job_response import Create2dModelTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.create_digital_asset_request import CreateDigitalAssetRequest
from huaweicloudsdkmetastudio.v1.model.create_digital_asset_request_body import CreateDigitalAssetRequestBody
from huaweicloudsdkmetastudio.v1.model.create_digital_asset_response import CreateDigitalAssetResponse
from huaweicloudsdkmetastudio.v1.model.create_digital_human_business_card_req import CreateDigitalHumanBusinessCardReq
from huaweicloudsdkmetastudio.v1.model.create_digital_human_business_card_request import CreateDigitalHumanBusinessCardRequest
from huaweicloudsdkmetastudio.v1.model.create_digital_human_business_card_response import CreateDigitalHumanBusinessCardResponse
from huaweicloudsdkmetastudio.v1.model.create_fas_req import CreateFASReq
from huaweicloudsdkmetastudio.v1.model.create_facial_animations_request import CreateFacialAnimationsRequest
from huaweicloudsdkmetastudio.v1.model.create_facial_animations_response import CreateFacialAnimationsResponse
from huaweicloudsdkmetastudio.v1.model.create_file_request import CreateFileRequest
from huaweicloudsdkmetastudio.v1.model.create_file_response import CreateFileResponse
from huaweicloudsdkmetastudio.v1.model.create_interaction_rule_group_request import CreateInteractionRuleGroupRequest
from huaweicloudsdkmetastudio.v1.model.create_interaction_rule_group_response import CreateInteractionRuleGroupResponse
from huaweicloudsdkmetastudio.v1.model.create_photo_detection_req import CreatePhotoDetectionReq
from huaweicloudsdkmetastudio.v1.model.create_photo_detection_request import CreatePhotoDetectionRequest
from huaweicloudsdkmetastudio.v1.model.create_photo_detection_response import CreatePhotoDetectionResponse
from huaweicloudsdkmetastudio.v1.model.create_photo_digital_human_video_req import CreatePhotoDigitalHumanVideoReq
from huaweicloudsdkmetastudio.v1.model.create_photo_digital_human_video_request import CreatePhotoDigitalHumanVideoRequest
from huaweicloudsdkmetastudio.v1.model.create_photo_digital_human_video_response import CreatePhotoDigitalHumanVideoResponse
from huaweicloudsdkmetastudio.v1.model.create_picture_modeling_by_url_job_request import CreatePictureModelingByUrlJobRequest
from huaweicloudsdkmetastudio.v1.model.create_picture_modeling_by_url_job_response import CreatePictureModelingByUrlJobResponse
from huaweicloudsdkmetastudio.v1.model.create_picture_modeling_job_request import CreatePictureModelingJobRequest
from huaweicloudsdkmetastudio.v1.model.create_picture_modeling_job_request_body import CreatePictureModelingJobRequestBody
from huaweicloudsdkmetastudio.v1.model.create_picture_modeling_job_response import CreatePictureModelingJobResponse
from huaweicloudsdkmetastudio.v1.model.create_smart_live_room_req import CreateSmartLiveRoomReq
from huaweicloudsdkmetastudio.v1.model.create_smart_live_room_request import CreateSmartLiveRoomRequest
from huaweicloudsdkmetastudio.v1.model.create_smart_live_room_response import CreateSmartLiveRoomResponse
from huaweicloudsdkmetastudio.v1.model.create_style_request_body import CreateStyleRequestBody
from huaweicloudsdkmetastudio.v1.model.create_ttsa_req import CreateTTSAReq
from huaweicloudsdkmetastudio.v1.model.create_training_advance_job_request import CreateTrainingAdvanceJobRequest
from huaweicloudsdkmetastudio.v1.model.create_training_advance_job_response import CreateTrainingAdvanceJobResponse
from huaweicloudsdkmetastudio.v1.model.create_training_basic_job_request import CreateTrainingBasicJobRequest
from huaweicloudsdkmetastudio.v1.model.create_training_basic_job_response import CreateTrainingBasicJobResponse
from huaweicloudsdkmetastudio.v1.model.create_training_job_req import CreateTrainingJobReq
from huaweicloudsdkmetastudio.v1.model.create_training_job_rsp_segment_uploading_url import CreateTrainingJobRspSegmentUploadingUrl
from huaweicloudsdkmetastudio.v1.model.create_training_middle_job_request import CreateTrainingMiddleJobRequest
from huaweicloudsdkmetastudio.v1.model.create_training_middle_job_response import CreateTrainingMiddleJobResponse
from huaweicloudsdkmetastudio.v1.model.create_tts_audition_request import CreateTtsAuditionRequest
from huaweicloudsdkmetastudio.v1.model.create_tts_audition_request_body import CreateTtsAuditionRequestBody
from huaweicloudsdkmetastudio.v1.model.create_tts_audition_response import CreateTtsAuditionResponse
from huaweicloudsdkmetastudio.v1.model.create_ttsa_request import CreateTtsaRequest
from huaweicloudsdkmetastudio.v1.model.create_ttsa_response import CreateTtsaResponse
from huaweicloudsdkmetastudio.v1.model.create_type import CreateType
from huaweicloudsdkmetastudio.v1.model.create_video_motion_capture_job_request import CreateVideoMotionCaptureJobRequest
from huaweicloudsdkmetastudio.v1.model.create_video_motion_capture_job_response import CreateVideoMotionCaptureJobResponse
from huaweicloudsdkmetastudio.v1.model.create_video_scripts_req import CreateVideoScriptsReq
from huaweicloudsdkmetastudio.v1.model.create_video_scripts_request import CreateVideoScriptsRequest
from huaweicloudsdkmetastudio.v1.model.create_video_scripts_response import CreateVideoScriptsResponse
from huaweicloudsdkmetastudio.v1.model.delete2d_model_training_job_request import Delete2dModelTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.delete2d_model_training_job_response import Delete2dModelTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.delete_asset_request import DeleteAssetRequest
from huaweicloudsdkmetastudio.v1.model.delete_asset_response import DeleteAssetResponse
from huaweicloudsdkmetastudio.v1.model.delete_digital_human_business_card_request import DeleteDigitalHumanBusinessCardRequest
from huaweicloudsdkmetastudio.v1.model.delete_digital_human_business_card_response import DeleteDigitalHumanBusinessCardResponse
from huaweicloudsdkmetastudio.v1.model.delete_file_request import DeleteFileRequest
from huaweicloudsdkmetastudio.v1.model.delete_file_response import DeleteFileResponse
from huaweicloudsdkmetastudio.v1.model.delete_interaction_rule_group_request import DeleteInteractionRuleGroupRequest
from huaweicloudsdkmetastudio.v1.model.delete_interaction_rule_group_response import DeleteInteractionRuleGroupResponse
from huaweicloudsdkmetastudio.v1.model.delete_smart_live_room_request import DeleteSmartLiveRoomRequest
from huaweicloudsdkmetastudio.v1.model.delete_smart_live_room_response import DeleteSmartLiveRoomResponse
from huaweicloudsdkmetastudio.v1.model.delete_video_script_request import DeleteVideoScriptRequest
from huaweicloudsdkmetastudio.v1.model.delete_video_script_response import DeleteVideoScriptResponse
from huaweicloudsdkmetastudio.v1.model.delete_voice_training_job_request import DeleteVoiceTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.delete_voice_training_job_response import DeleteVoiceTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.digital_asset_info import DigitalAssetInfo
from huaweicloudsdkmetastudio.v1.model.digital_asset_summary import DigitalAssetSummary
from huaweicloudsdkmetastudio.v1.model.digital_human_business_card_job_info import DigitalHumanBusinessCardJobInfo
from huaweicloudsdkmetastudio.v1.model.digital_human_modeling_job_info import DigitalHumanModelingJobInfo
from huaweicloudsdkmetastudio.v1.model.digital_human_video import DigitalHumanVideo
from huaweicloudsdkmetastudio.v1.model.emotion_config import EmotionConfig
from huaweicloudsdkmetastudio.v1.model.error_response import ErrorResponse
from huaweicloudsdkmetastudio.v1.model.execute2d_model_training_command_by_user_req import Execute2dModelTrainingCommandByUserReq
from huaweicloudsdkmetastudio.v1.model.execute2d_model_training_command_by_user_request import Execute2dModelTrainingCommandByUserRequest
from huaweicloudsdkmetastudio.v1.model.execute2d_model_training_command_by_user_response import Execute2dModelTrainingCommandByUserResponse
from huaweicloudsdkmetastudio.v1.model.execute_smart_live_command_request import ExecuteSmartLiveCommandRequest
from huaweicloudsdkmetastudio.v1.model.execute_smart_live_command_response import ExecuteSmartLiveCommandResponse
from huaweicloudsdkmetastudio.v1.model.execute_video_motion_capture_command_request import ExecuteVideoMotionCaptureCommandRequest
from huaweicloudsdkmetastudio.v1.model.execute_video_motion_capture_command_response import ExecuteVideoMotionCaptureCommandResponse
from huaweicloudsdkmetastudio.v1.model.files_create_req import FilesCreateReq
from huaweicloudsdkmetastudio.v1.model.hit_condition import HitCondition
from huaweicloudsdkmetastudio.v1.model.hit_condition_tag import HitConditionTag
from huaweicloudsdkmetastudio.v1.model.human_model2_d_asset_meta import HumanModel2DAssetMeta
from huaweicloudsdkmetastudio.v1.model.human_model_asset_meta import HumanModelAssetMeta
from huaweicloudsdkmetastudio.v1.model.human_model_meta_properties import HumanModelMetaProperties
from huaweicloudsdkmetastudio.v1.model.human_position2_d import HumanPosition2D
from huaweicloudsdkmetastudio.v1.model.human_size2_d import HumanSize2D
from huaweicloudsdkmetastudio.v1.model.image_layer_config import ImageLayerConfig
from huaweicloudsdkmetastudio.v1.model.inference_action_mark_info import InferenceActionMarkInfo
from huaweicloudsdkmetastudio.v1.model.inference_video_mark_info import InferenceVideoMarkInfo
from huaweicloudsdkmetastudio.v1.model.input_info import InputInfo
from huaweicloudsdkmetastudio.v1.model.interaction_rule_detail_info import InteractionRuleDetailInfo
from huaweicloudsdkmetastudio.v1.model.interaction_rule_group import InteractionRuleGroup
from huaweicloudsdkmetastudio.v1.model.interaction_rule_group_detail import InteractionRuleGroupDetail
from huaweicloudsdkmetastudio.v1.model.interaction_rule_info import InteractionRuleInfo
from huaweicloudsdkmetastudio.v1.model.job_state import JobState
from huaweicloudsdkmetastudio.v1.model.job_tag import JobTag
from huaweicloudsdkmetastudio.v1.model.job_type import JobType
from huaweicloudsdkmetastudio.v1.model.language_check_info_req import LanguageCheckInfoReq
from huaweicloudsdkmetastudio.v1.model.layer_config import LayerConfig
from huaweicloudsdkmetastudio.v1.model.layer_position_config import LayerPositionConfig
from huaweicloudsdkmetastudio.v1.model.layer_size_config import LayerSizeConfig
from huaweicloudsdkmetastudio.v1.model.list2d_model_training_job_request import List2dModelTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.list2d_model_training_job_response import List2dModelTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.list_asset_summary_request import ListAssetSummaryRequest
from huaweicloudsdkmetastudio.v1.model.list_asset_summary_response import ListAssetSummaryResponse
from huaweicloudsdkmetastudio.v1.model.list_asset_summarys_req import ListAssetSummarysReq
from huaweicloudsdkmetastudio.v1.model.list_assets_request import ListAssetsRequest
from huaweicloudsdkmetastudio.v1.model.list_assets_response import ListAssetsResponse
from huaweicloudsdkmetastudio.v1.model.list_digital_human_business_card_request import ListDigitalHumanBusinessCardRequest
from huaweicloudsdkmetastudio.v1.model.list_digital_human_business_card_response import ListDigitalHumanBusinessCardResponse
from huaweicloudsdkmetastudio.v1.model.list_digital_human_video_request import ListDigitalHumanVideoRequest
from huaweicloudsdkmetastudio.v1.model.list_digital_human_video_response import ListDigitalHumanVideoResponse
from huaweicloudsdkmetastudio.v1.model.list_facial_animations_data_request import ListFacialAnimationsDataRequest
from huaweicloudsdkmetastudio.v1.model.list_facial_animations_data_response import ListFacialAnimationsDataResponse
from huaweicloudsdkmetastudio.v1.model.list_interaction_rule_groups_request import ListInteractionRuleGroupsRequest
from huaweicloudsdkmetastudio.v1.model.list_interaction_rule_groups_response import ListInteractionRuleGroupsResponse
from huaweicloudsdkmetastudio.v1.model.list_picture_modeling_jobs_request import ListPictureModelingJobsRequest
from huaweicloudsdkmetastudio.v1.model.list_picture_modeling_jobs_response import ListPictureModelingJobsResponse
from huaweicloudsdkmetastudio.v1.model.list_smart_live_request import ListSmartLiveRequest
from huaweicloudsdkmetastudio.v1.model.list_smart_live_response import ListSmartLiveResponse
from huaweicloudsdkmetastudio.v1.model.list_smart_live_rooms_request import ListSmartLiveRoomsRequest
from huaweicloudsdkmetastudio.v1.model.list_smart_live_rooms_response import ListSmartLiveRoomsResponse
from huaweicloudsdkmetastudio.v1.model.list_styles_request import ListStylesRequest
from huaweicloudsdkmetastudio.v1.model.list_styles_response import ListStylesResponse
from huaweicloudsdkmetastudio.v1.model.list_ttsa_data_request import ListTtsaDataRequest
from huaweicloudsdkmetastudio.v1.model.list_ttsa_data_response import ListTtsaDataResponse
from huaweicloudsdkmetastudio.v1.model.list_ttsa_jobs_request import ListTtsaJobsRequest
from huaweicloudsdkmetastudio.v1.model.list_ttsa_jobs_response import ListTtsaJobsResponse
from huaweicloudsdkmetastudio.v1.model.list_video_motion_capture_jobs_request import ListVideoMotionCaptureJobsRequest
from huaweicloudsdkmetastudio.v1.model.list_video_motion_capture_jobs_response import ListVideoMotionCaptureJobsResponse
from huaweicloudsdkmetastudio.v1.model.list_video_scripts_request import ListVideoScriptsRequest
from huaweicloudsdkmetastudio.v1.model.list_video_scripts_response import ListVideoScriptsResponse
from huaweicloudsdkmetastudio.v1.model.list_voice_training_job_request import ListVoiceTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.list_voice_training_job_response import ListVoiceTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.live_audio_config import LiveAudioConfig
from huaweicloudsdkmetastudio.v1.model.live_event import LiveEvent
from huaweicloudsdkmetastudio.v1.model.live_event_call_back_config import LiveEventCallBackConfig
from huaweicloudsdkmetastudio.v1.model.live_event_report_request import LiveEventReportRequest
from huaweicloudsdkmetastudio.v1.model.live_event_report_response import LiveEventReportResponse
from huaweicloudsdkmetastudio.v1.model.live_shoot_script_item import LiveShootScriptItem
from huaweicloudsdkmetastudio.v1.model.live_video_script_info import LiveVideoScriptInfo
from huaweicloudsdkmetastudio.v1.model.live_warning_item import LiveWarningItem
from huaweicloudsdkmetastudio.v1.model.material_asset_meta import MaterialAssetMeta
from huaweicloudsdkmetastudio.v1.model.material_component_info import MaterialComponentInfo
from huaweicloudsdkmetastudio.v1.model.model_info import ModelInfo
from huaweicloudsdkmetastudio.v1.model.motion_item import MotionItem
from huaweicloudsdkmetastudio.v1.model.multipart_upload_info import MultipartUploadInfo
from huaweicloudsdkmetastudio.v1.model.operation_log_info import OperationLogInfo
from huaweicloudsdkmetastudio.v1.model.output_asset_config import OutputAssetConfig
from huaweicloudsdkmetastudio.v1.model.output_asset_info import OutputAssetInfo
from huaweicloudsdkmetastudio.v1.model.output_info import OutputInfo
from huaweicloudsdkmetastudio.v1.model.ppt_asset_meta import PPTAssetMeta
from huaweicloudsdkmetastudio.v1.model.ppt_page_info import PPTPageInfo
from huaweicloudsdkmetastudio.v1.model.photo_video_config import PhotoVideoConfig
from huaweicloudsdkmetastudio.v1.model.picture_modeling_by_url_req import PictureModelingByUrlReq
from huaweicloudsdkmetastudio.v1.model.picture_modeling_info import PictureModelingInfo
from huaweicloudsdkmetastudio.v1.model.play_policy import PlayPolicy
from huaweicloudsdkmetastudio.v1.model.rtc_room_info_list import RTCRoomInfoList
from huaweicloudsdkmetastudio.v1.model.rtc_user_info import RTCUserInfo
from huaweicloudsdkmetastudio.v1.model.reply_audio_info import ReplyAudioInfo
from huaweicloudsdkmetastudio.v1.model.report_live_event_req import ReportLiveEventReq
from huaweicloudsdkmetastudio.v1.model.restore_asset_request import RestoreAssetRequest
from huaweicloudsdkmetastudio.v1.model.restore_asset_response import RestoreAssetResponse
from huaweicloudsdkmetastudio.v1.model.review_config import ReviewConfig
from huaweicloudsdkmetastudio.v1.model.scene_asset_meta import SceneAssetMeta
from huaweicloudsdkmetastudio.v1.model.scene_component_info import SceneComponentInfo
from huaweicloudsdkmetastudio.v1.model.shared_config import SharedConfig
from huaweicloudsdkmetastudio.v1.model.shoot_script import ShootScript
from huaweicloudsdkmetastudio.v1.model.shoot_script_audio_file_item import ShootScriptAudioFileItem
from huaweicloudsdkmetastudio.v1.model.shoot_script_audio_files import ShootScriptAudioFiles
from huaweicloudsdkmetastudio.v1.model.shoot_script_detail import ShootScriptDetail
from huaweicloudsdkmetastudio.v1.model.shoot_script_item import ShootScriptItem
from huaweicloudsdkmetastudio.v1.model.shoot_script_item_base_info import ShootScriptItemBaseInfo
from huaweicloudsdkmetastudio.v1.model.shoot_script_show_item import ShootScriptShowItem
from huaweicloudsdkmetastudio.v1.model.show2_d_digital_human_video_request import Show2DDigitalHumanVideoRequest
from huaweicloudsdkmetastudio.v1.model.show2_d_digital_human_video_response import Show2DDigitalHumanVideoResponse
from huaweicloudsdkmetastudio.v1.model.show2d_model_training_job_request import Show2dModelTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.show2d_model_training_job_response import Show2dModelTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.show_asset_request import ShowAssetRequest
from huaweicloudsdkmetastudio.v1.model.show_asset_response import ShowAssetResponse
from huaweicloudsdkmetastudio.v1.model.show_digital_human_business_card_request import ShowDigitalHumanBusinessCardRequest
from huaweicloudsdkmetastudio.v1.model.show_digital_human_business_card_response import ShowDigitalHumanBusinessCardResponse
from huaweicloudsdkmetastudio.v1.model.show_job_audit_result_request import ShowJobAuditResultRequest
from huaweicloudsdkmetastudio.v1.model.show_job_audit_result_response import ShowJobAuditResultResponse
from huaweicloudsdkmetastudio.v1.model.show_job_uploading_address_request import ShowJobUploadingAddressRequest
from huaweicloudsdkmetastudio.v1.model.show_job_uploading_address_response import ShowJobUploadingAddressResponse
from huaweicloudsdkmetastudio.v1.model.show_job_uploading_address_rsp_package_url import ShowJobUploadingAddressRspPackageUrl
from huaweicloudsdkmetastudio.v1.model.show_job_uploading_address_rsp_segment_url import ShowJobUploadingAddressRspSegmentUrl
from huaweicloudsdkmetastudio.v1.model.show_photo_detection_request import ShowPhotoDetectionRequest
from huaweicloudsdkmetastudio.v1.model.show_photo_detection_response import ShowPhotoDetectionResponse
from huaweicloudsdkmetastudio.v1.model.show_photo_digital_human_video_request import ShowPhotoDigitalHumanVideoRequest
from huaweicloudsdkmetastudio.v1.model.show_photo_digital_human_video_response import ShowPhotoDigitalHumanVideoResponse
from huaweicloudsdkmetastudio.v1.model.show_picture_modeling_job_request import ShowPictureModelingJobRequest
from huaweicloudsdkmetastudio.v1.model.show_picture_modeling_job_response import ShowPictureModelingJobResponse
from huaweicloudsdkmetastudio.v1.model.show_smart_live_request import ShowSmartLiveRequest
from huaweicloudsdkmetastudio.v1.model.show_smart_live_response import ShowSmartLiveResponse
from huaweicloudsdkmetastudio.v1.model.show_smart_live_room_request import ShowSmartLiveRoomRequest
from huaweicloudsdkmetastudio.v1.model.show_smart_live_room_response import ShowSmartLiveRoomResponse
from huaweicloudsdkmetastudio.v1.model.show_training_segment_info_request import ShowTrainingSegmentInfoRequest
from huaweicloudsdkmetastudio.v1.model.show_training_segment_info_response import ShowTrainingSegmentInfoResponse
from huaweicloudsdkmetastudio.v1.model.show_tts_audition_file_request import ShowTtsAuditionFileRequest
from huaweicloudsdkmetastudio.v1.model.show_tts_audition_file_response import ShowTtsAuditionFileResponse
from huaweicloudsdkmetastudio.v1.model.show_video_motion_capture_job_request import ShowVideoMotionCaptureJobRequest
from huaweicloudsdkmetastudio.v1.model.show_video_motion_capture_job_response import ShowVideoMotionCaptureJobResponse
from huaweicloudsdkmetastudio.v1.model.show_video_script_request import ShowVideoScriptRequest
from huaweicloudsdkmetastudio.v1.model.show_video_script_response import ShowVideoScriptResponse
from huaweicloudsdkmetastudio.v1.model.show_voice_training_job_request import ShowVoiceTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.show_voice_training_job_response import ShowVoiceTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.smart_image_layer_config import SmartImageLayerConfig
from huaweicloudsdkmetastudio.v1.model.smart_layer_config import SmartLayerConfig
from huaweicloudsdkmetastudio.v1.model.smart_live_job import SmartLiveJob
from huaweicloudsdkmetastudio.v1.model.smart_live_room_base_info import SmartLiveRoomBaseInfo
from huaweicloudsdkmetastudio.v1.model.smart_video_layer_config import SmartVideoLayerConfig
from huaweicloudsdkmetastudio.v1.model.start_smart_live_req import StartSmartLiveReq
from huaweicloudsdkmetastudio.v1.model.start_smart_live_request import StartSmartLiveRequest
from huaweicloudsdkmetastudio.v1.model.start_smart_live_response import StartSmartLiveResponse
from huaweicloudsdkmetastudio.v1.model.stop_smart_live_request import StopSmartLiveRequest
from huaweicloudsdkmetastudio.v1.model.stop_smart_live_response import StopSmartLiveResponse
from huaweicloudsdkmetastudio.v1.model.stop_video_motion_capture_job_request import StopVideoMotionCaptureJobRequest
from huaweicloudsdkmetastudio.v1.model.stop_video_motion_capture_job_response import StopVideoMotionCaptureJobResponse
from huaweicloudsdkmetastudio.v1.model.style_asset_item import StyleAssetItem
from huaweicloudsdkmetastudio.v1.model.style_extra_meta import StyleExtraMeta
from huaweicloudsdkmetastudio.v1.model.style_info import StyleInfo
from huaweicloudsdkmetastudio.v1.model.subtitle_config import SubtitleConfig
from huaweicloudsdkmetastudio.v1.model.system_property import SystemProperty
from huaweicloudsdkmetastudio.v1.model.ttsa_job import TTSAJob
from huaweicloudsdkmetastudio.v1.model.text_config import TextConfig
from huaweicloudsdkmetastudio.v1.model.text_layer_config import TextLayerConfig
from huaweicloudsdkmetastudio.v1.model.training_job_basic_info import TrainingJobBasicInfo
from huaweicloudsdkmetastudio.v1.model.training_job_info import TrainingJobInfo
from huaweicloudsdkmetastudio.v1.model.trigger_process import TriggerProcess
from huaweicloudsdkmetastudio.v1.model.update2d_model_training_job_request import Update2dModelTrainingJobRequest
from huaweicloudsdkmetastudio.v1.model.update2d_model_training_job_response import Update2dModelTrainingJobResponse
from huaweicloudsdkmetastudio.v1.model.update_digital_asset_request import UpdateDigitalAssetRequest
from huaweicloudsdkmetastudio.v1.model.update_digital_asset_request_body import UpdateDigitalAssetRequestBody
from huaweicloudsdkmetastudio.v1.model.update_digital_asset_response import UpdateDigitalAssetResponse
from huaweicloudsdkmetastudio.v1.model.update_digital_human_business_card_request import UpdateDigitalHumanBusinessCardRequest
from huaweicloudsdkmetastudio.v1.model.update_digital_human_business_card_response import UpdateDigitalHumanBusinessCardResponse
from huaweicloudsdkmetastudio.v1.model.update_interaction_rule_group_request import UpdateInteractionRuleGroupRequest
from huaweicloudsdkmetastudio.v1.model.update_interaction_rule_group_response import UpdateInteractionRuleGroupResponse
from huaweicloudsdkmetastudio.v1.model.update_smart_live_room_request import UpdateSmartLiveRoomRequest
from huaweicloudsdkmetastudio.v1.model.update_smart_live_room_response import UpdateSmartLiveRoomResponse
from huaweicloudsdkmetastudio.v1.model.update_video_script_request import UpdateVideoScriptRequest
from huaweicloudsdkmetastudio.v1.model.update_video_script_response import UpdateVideoScriptResponse
from huaweicloudsdkmetastudio.v1.model.update_video_scripts_req import UpdateVideoScriptsReq
from huaweicloudsdkmetastudio.v1.model.video_config import VideoConfig
from huaweicloudsdkmetastudio.v1.model.video_layer_config import VideoLayerConfig
from huaweicloudsdkmetastudio.v1.model.video_motion_capture_info import VideoMotionCaptureInfo
from huaweicloudsdkmetastudio.v1.model.video_motion_capture_job_req import VideoMotionCaptureJobReq
from huaweicloudsdkmetastudio.v1.model.video_script_base_info import VideoScriptBaseInfo
from huaweicloudsdkmetastudio.v1.model.video_scripts_create_info import VideoScriptsCreateInfo
from huaweicloudsdkmetastudio.v1.model.video_scripts_show_info import VideoScriptsShowInfo
from huaweicloudsdkmetastudio.v1.model.video_scripts_simple_info import VideoScriptsSimpleInfo
from huaweicloudsdkmetastudio.v1.model.voice_config import VoiceConfig
from huaweicloudsdkmetastudio.v1.model.voice_model_asset_meta import VoiceModelAssetMeta
