# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkimage.v2.model.celebrity_recognition_req import CelebrityRecognitionReq
from huaweicloudsdkimage.v2.model.celebrity_recognition_result_body import CelebrityRecognitionResultBody
from huaweicloudsdkimage.v2.model.create_image_highresolution_matting_task_request import CreateImageHighresolutionMattingTaskRequest
from huaweicloudsdkimage.v2.model.create_image_highresolution_matting_task_response import CreateImageHighresolutionMattingTaskResponse
from huaweicloudsdkimage.v2.model.create_image_to_video_task_request import CreateImageToVideoTaskRequest
from huaweicloudsdkimage.v2.model.create_image_to_video_task_response import CreateImageToVideoTaskResponse
from huaweicloudsdkimage.v2.model.create_image_translate_task_request import CreateImageTranslateTaskRequest
from huaweicloudsdkimage.v2.model.create_image_translate_task_response import CreateImageTranslateTaskResponse
from huaweicloudsdkimage.v2.model.create_image_variation_task_request import CreateImageVariationTaskRequest
from huaweicloudsdkimage.v2.model.create_image_variation_task_request_body import CreateImageVariationTaskRequestBody
from huaweicloudsdkimage.v2.model.create_image_variation_task_response import CreateImageVariationTaskResponse
from huaweicloudsdkimage.v2.model.create_text_to_image_task_request import CreateTextToImageTaskRequest
from huaweicloudsdkimage.v2.model.create_text_to_image_task_request_body import CreateTextToImageTaskRequestBody
from huaweicloudsdkimage.v2.model.create_text_to_image_task_response import CreateTextToImageTaskResponse
from huaweicloudsdkimage.v2.model.create_video_cover_analysis_task_request import CreateVideoCoverAnalysisTaskRequest
from huaweicloudsdkimage.v2.model.create_video_cover_analysis_task_response import CreateVideoCoverAnalysisTaskResponse
from huaweicloudsdkimage.v2.model.create_video_cutting_task_request import CreateVideoCuttingTaskRequest
from huaweicloudsdkimage.v2.model.create_video_cutting_task_response import CreateVideoCuttingTaskResponse
from huaweicloudsdkimage.v2.model.create_video_shot_split_task_request import CreateVideoShotSplitTaskRequest
from huaweicloudsdkimage.v2.model.create_video_shot_split_task_response import CreateVideoShotSplitTaskResponse
from huaweicloudsdkimage.v2.model.create_video_split_task_request_body import CreateVideoSplitTaskRequestBody
from huaweicloudsdkimage.v2.model.create_video_summarization_analysis_task_request import CreateVideoSummarizationAnalysisTaskRequest
from huaweicloudsdkimage.v2.model.create_video_summarization_analysis_task_response import CreateVideoSummarizationAnalysisTaskResponse
from huaweicloudsdkimage.v2.model.create_video_synthesis_task_request import CreateVideoSynthesisTaskRequest
from huaweicloudsdkimage.v2.model.create_video_synthesis_task_response import CreateVideoSynthesisTaskResponse
from huaweicloudsdkimage.v2.model.create_video_translate_task_request import CreateVideoTranslateTaskRequest
from huaweicloudsdkimage.v2.model.create_video_translate_task_response import CreateVideoTranslateTaskResponse
from huaweicloudsdkimage.v2.model.image_description_req import ImageDescriptionReq
from huaweicloudsdkimage.v2.model.image_description_response_result import ImageDescriptionResponseResult
from huaweicloudsdkimage.v2.model.image_highresolution_matting_config import ImageHighresolutionMattingConfig
from huaweicloudsdkimage.v2.model.image_highresolution_matting_config_common import ImageHighresolutionMattingConfigCommon
from huaweicloudsdkimage.v2.model.image_highresolution_matting_inference import ImageHighresolutionMattingInference
from huaweicloudsdkimage.v2.model.image_highresolution_matting_request_body import ImageHighresolutionMattingRequestBody
from huaweicloudsdkimage.v2.model.image_main_object_detection_instance import ImageMainObjectDetectionInstance
from huaweicloudsdkimage.v2.model.image_main_object_detection_req import ImageMainObjectDetectionReq
from huaweicloudsdkimage.v2.model.image_media_tagging_det_instance import ImageMediaTaggingDetInstance
from huaweicloudsdkimage.v2.model.image_media_tagging_det_item_body import ImageMediaTaggingDetItemBody
from huaweicloudsdkimage.v2.model.image_media_tagging_det_item_body_i18n_tag import ImageMediaTaggingDetItemBodyI18nTag
from huaweicloudsdkimage.v2.model.image_media_tagging_det_req import ImageMediaTaggingDetReq
from huaweicloudsdkimage.v2.model.image_media_tagging_det_response_result import ImageMediaTaggingDetResponseResult
from huaweicloudsdkimage.v2.model.image_media_tagging_item_body import ImageMediaTaggingItemBody
from huaweicloudsdkimage.v2.model.image_media_tagging_item_body_i18n_tag import ImageMediaTaggingItemBodyI18nTag
from huaweicloudsdkimage.v2.model.image_media_tagging_item_body_i18n_type import ImageMediaTaggingItemBodyI18nType
from huaweicloudsdkimage.v2.model.image_media_tagging_req import ImageMediaTaggingReq
from huaweicloudsdkimage.v2.model.image_media_tagging_response_result import ImageMediaTaggingResponseResult
from huaweicloudsdkimage.v2.model.image_super_resolution_req import ImageSuperResolutionReq
from huaweicloudsdkimage.v2.model.image_super_resolution_response_result import ImageSuperResolutionResponseResult
from huaweicloudsdkimage.v2.model.image_tagging_instance import ImageTaggingInstance
from huaweicloudsdkimage.v2.model.image_tagging_item_body import ImageTaggingItemBody
from huaweicloudsdkimage.v2.model.image_tagging_item_body_i18n_tag import ImageTaggingItemBodyI18nTag
from huaweicloudsdkimage.v2.model.image_tagging_item_body_i18n_type import ImageTaggingItemBodyI18nType
from huaweicloudsdkimage.v2.model.image_tagging_req import ImageTaggingReq
from huaweicloudsdkimage.v2.model.image_tagging_response_result import ImageTaggingResponseResult
from huaweicloudsdkimage.v2.model.image_to_video_config import ImageToVideoConfig
from huaweicloudsdkimage.v2.model.image_to_video_config_common import ImageToVideoConfigCommon
from huaweicloudsdkimage.v2.model.image_to_video_inference import ImageToVideoInference
from huaweicloudsdkimage.v2.model.image_to_video_info import ImageToVideoInfo
from huaweicloudsdkimage.v2.model.image_to_video_request_body import ImageToVideoRequestBody
from huaweicloudsdkimage.v2.model.image_translate_config import ImageTranslateConfig
from huaweicloudsdkimage.v2.model.image_translate_config_common import ImageTranslateConfigCommon
from huaweicloudsdkimage.v2.model.image_translate_inference import ImageTranslateInference
from huaweicloudsdkimage.v2.model.image_translate_request_body import ImageTranslateRequestBody
from huaweicloudsdkimage.v2.model.image_variation_inference import ImageVariationInference
from huaweicloudsdkimage.v2.model.image_variation_task_config import ImageVariationTaskConfig
from huaweicloudsdkimage.v2.model.image_variation_task_config_common import ImageVariationTaskConfigCommon
from huaweicloudsdkimage.v2.model.image_wisedesign_crop_req import ImageWisedesignCropReq
from huaweicloudsdkimage.v2.model.image_wisedesign_crop_response_result import ImageWisedesignCropResponseResult
from huaweicloudsdkimage.v2.model.image_wisedesign_inpainting_req import ImageWisedesignInpaintingReq
from huaweicloudsdkimage.v2.model.image_wisedesign_inpainting_response_result import ImageWisedesignInpaintingResponseResult
from huaweicloudsdkimage.v2.model.recapture_detect_req import RecaptureDetectReq
from huaweicloudsdkimage.v2.model.recapture_detect_response_result import RecaptureDetectResponseResult
from huaweicloudsdkimage.v2.model.recapture_detect_response_result_detail import RecaptureDetectResponseResultDetail
from huaweicloudsdkimage.v2.model.run_celebrity_recognition_request import RunCelebrityRecognitionRequest
from huaweicloudsdkimage.v2.model.run_celebrity_recognition_response import RunCelebrityRecognitionResponse
from huaweicloudsdkimage.v2.model.run_delete_custom_tags_request import RunDeleteCustomTagsRequest
from huaweicloudsdkimage.v2.model.run_delete_custom_tags_response import RunDeleteCustomTagsResponse
from huaweicloudsdkimage.v2.model.run_image_description_request import RunImageDescriptionRequest
from huaweicloudsdkimage.v2.model.run_image_description_response import RunImageDescriptionResponse
from huaweicloudsdkimage.v2.model.run_image_main_object_detection_request import RunImageMainObjectDetectionRequest
from huaweicloudsdkimage.v2.model.run_image_main_object_detection_response import RunImageMainObjectDetectionResponse
from huaweicloudsdkimage.v2.model.run_image_media_tagging_det_request import RunImageMediaTaggingDetRequest
from huaweicloudsdkimage.v2.model.run_image_media_tagging_det_response import RunImageMediaTaggingDetResponse
from huaweicloudsdkimage.v2.model.run_image_media_tagging_request import RunImageMediaTaggingRequest
from huaweicloudsdkimage.v2.model.run_image_media_tagging_response import RunImageMediaTaggingResponse
from huaweicloudsdkimage.v2.model.run_image_super_resolution_request import RunImageSuperResolutionRequest
from huaweicloudsdkimage.v2.model.run_image_super_resolution_response import RunImageSuperResolutionResponse
from huaweicloudsdkimage.v2.model.run_image_tagging_request import RunImageTaggingRequest
from huaweicloudsdkimage.v2.model.run_image_tagging_response import RunImageTaggingResponse
from huaweicloudsdkimage.v2.model.run_image_wisedesign_crop_request import RunImageWisedesignCropRequest
from huaweicloudsdkimage.v2.model.run_image_wisedesign_crop_response import RunImageWisedesignCropResponse
from huaweicloudsdkimage.v2.model.run_image_wisedesign_inpainting_request import RunImageWisedesignInpaintingRequest
from huaweicloudsdkimage.v2.model.run_image_wisedesign_inpainting_response import RunImageWisedesignInpaintingResponse
from huaweicloudsdkimage.v2.model.run_query_custom_tags_request import RunQueryCustomTagsRequest
from huaweicloudsdkimage.v2.model.run_query_custom_tags_response import RunQueryCustomTagsResponse
from huaweicloudsdkimage.v2.model.run_recapture_detect_request import RunRecaptureDetectRequest
from huaweicloudsdkimage.v2.model.run_recapture_detect_response import RunRecaptureDetectResponse
from huaweicloudsdkimage.v2.model.show_image_highresolution_matting_task_request import ShowImageHighresolutionMattingTaskRequest
from huaweicloudsdkimage.v2.model.show_image_highresolution_matting_task_response import ShowImageHighresolutionMattingTaskResponse
from huaweicloudsdkimage.v2.model.show_image_to_video_task_request import ShowImageToVideoTaskRequest
from huaweicloudsdkimage.v2.model.show_image_to_video_task_response import ShowImageToVideoTaskResponse
from huaweicloudsdkimage.v2.model.show_image_translate_task_request import ShowImageTranslateTaskRequest
from huaweicloudsdkimage.v2.model.show_image_translate_task_response import ShowImageTranslateTaskResponse
from huaweicloudsdkimage.v2.model.show_image_variation_task_request import ShowImageVariationTaskRequest
from huaweicloudsdkimage.v2.model.show_image_variation_task_response import ShowImageVariationTaskResponse
from huaweicloudsdkimage.v2.model.show_text_to_image_task_request import ShowTextToImageTaskRequest
from huaweicloudsdkimage.v2.model.show_text_to_image_task_response import ShowTextToImageTaskResponse
from huaweicloudsdkimage.v2.model.show_video_cover_analysis_task_request import ShowVideoCoverAnalysisTaskRequest
from huaweicloudsdkimage.v2.model.show_video_cover_analysis_task_response import ShowVideoCoverAnalysisTaskResponse
from huaweicloudsdkimage.v2.model.show_video_cutting_task_request import ShowVideoCuttingTaskRequest
from huaweicloudsdkimage.v2.model.show_video_cutting_task_response import ShowVideoCuttingTaskResponse
from huaweicloudsdkimage.v2.model.show_video_shot_split_task_request import ShowVideoShotSplitTaskRequest
from huaweicloudsdkimage.v2.model.show_video_shot_split_task_response import ShowVideoShotSplitTaskResponse
from huaweicloudsdkimage.v2.model.show_video_summarization_analysis_task_request import ShowVideoSummarizationAnalysisTaskRequest
from huaweicloudsdkimage.v2.model.show_video_summarization_analysis_task_response import ShowVideoSummarizationAnalysisTaskResponse
from huaweicloudsdkimage.v2.model.show_video_synthesis_task_request import ShowVideoSynthesisTaskRequest
from huaweicloudsdkimage.v2.model.show_video_synthesis_task_response import ShowVideoSynthesisTaskResponse
from huaweicloudsdkimage.v2.model.show_video_translate_task_request import ShowVideoTranslateTaskRequest
from huaweicloudsdkimage.v2.model.show_video_translate_task_response import ShowVideoTranslateTaskResponse
from huaweicloudsdkimage.v2.model.summarization_analysis_config import SummarizationAnalysisConfig
from huaweicloudsdkimage.v2.model.summarization_analysis_config_common import SummarizationAnalysisConfigCommon
from huaweicloudsdkimage.v2.model.summarization_analysis_inference import SummarizationAnalysisInference
from huaweicloudsdkimage.v2.model.task_callback import TaskCallback
from huaweicloudsdkimage.v2.model.task_input import TaskInput
from huaweicloudsdkimage.v2.model.task_input_data import TaskInputData
from huaweicloudsdkimage.v2.model.task_output import TaskOutput
from huaweicloudsdkimage.v2.model.task_output_obs import TaskOutputObs
from huaweicloudsdkimage.v2.model.text_to_image_inference import TextToImageInference
from huaweicloudsdkimage.v2.model.text_to_image_task_config import TextToImageTaskConfig
from huaweicloudsdkimage.v2.model.text_to_image_task_config_common import TextToImageTaskConfigCommon
from huaweicloudsdkimage.v2.model.video_cover_analysis_config import VideoCoverAnalysisConfig
from huaweicloudsdkimage.v2.model.video_cover_analysis_config_common import VideoCoverAnalysisConfigCommon
from huaweicloudsdkimage.v2.model.video_cover_analysis_create_task_request_body import VideoCoverAnalysisCreateTaskRequestBody
from huaweicloudsdkimage.v2.model.video_cover_analysisinference import VideoCoverAnalysisinference
from huaweicloudsdkimage.v2.model.video_cutting_config import VideoCuttingConfig
from huaweicloudsdkimage.v2.model.video_cutting_config_common import VideoCuttingConfigCommon
from huaweicloudsdkimage.v2.model.video_cutting_inference import VideoCuttingInference
from huaweicloudsdkimage.v2.model.video_cutting_request_body import VideoCuttingRequestBody
from huaweicloudsdkimage.v2.model.video_segment_info import VideoSegmentInfo
from huaweicloudsdkimage.v2.model.video_split_task_input import VideoSplitTaskInput
from huaweicloudsdkimage.v2.model.video_split_task_input_data import VideoSplitTaskInputData
from huaweicloudsdkimage.v2.model.video_summarization_create_task_request_body import VideoSummarizationCreateTaskRequestBody
from huaweicloudsdkimage.v2.model.video_synthesis_config import VideoSynthesisConfig
from huaweicloudsdkimage.v2.model.video_synthesis_config_common import VideoSynthesisConfigCommon
from huaweicloudsdkimage.v2.model.video_synthesis_inference import VideoSynthesisInference
from huaweicloudsdkimage.v2.model.video_synthesis_info import VideoSynthesisInfo
from huaweicloudsdkimage.v2.model.video_synthesis_request_body import VideoSynthesisRequestBody
from huaweicloudsdkimage.v2.model.video_translate_config import VideoTranslateConfig
from huaweicloudsdkimage.v2.model.video_translate_config_common import VideoTranslateConfigCommon
from huaweicloudsdkimage.v2.model.video_translate_inference import VideoTranslateInference
from huaweicloudsdkimage.v2.model.video_translate_inference_rewrite_config import VideoTranslateInferenceRewriteConfig
from huaweicloudsdkimage.v2.model.video_translate_inference_rewrite_config_background import VideoTranslateInferenceRewriteConfigBackground
from huaweicloudsdkimage.v2.model.video_translate_inference_rewrite_config_stroke import VideoTranslateInferenceRewriteConfigStroke
from huaweicloudsdkimage.v2.model.video_translate_request_body import VideoTranslateRequestBody
