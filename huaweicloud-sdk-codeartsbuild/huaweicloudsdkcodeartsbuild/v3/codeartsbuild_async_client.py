# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodeartsbuild'")


class CodeArtsBuildAsyncClient(Client):
    def __init__(self):
        super(CodeArtsBuildAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsbuild.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsBuildAsyncClient":
                raise TypeError("client type error, support client type is CodeArtsBuildAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_build_job_async(self, request):
        r"""创建构建任务

        创建构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobResponse`
        """
        http_info = self._create_build_job_http_info(request)
        return self._call_api(**http_info)

    def create_build_job_async_invoker(self, request):
        http_info = self._create_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBuildJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_templates_async(self, request):
        r"""创建构建模板

        创建构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemplates
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplatesResponse`
        """
        http_info = self._create_templates_http_info(request)
        return self._call_api(**http_info)

    def create_templates_async_invoker(self, request):
        http_info = self._create_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_templates_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/templates/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_build_job_async(self, request):
        r"""删除构建任务

        删除构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteBuildJobResponse`
        """
        http_info = self._delete_build_job_http_info(request)
        return self._call_api(**http_info)

    def delete_build_job_async_invoker(self, request):
        http_info = self._delete_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBuildJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_templates_async(self, request):
        r"""删除构建模板

        删除构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplates
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DeleteTemplatesResponse`
        """
        http_info = self._delete_templates_http_info(request)
        return self._call_api(**http_info)

    def delete_templates_async_invoker(self, request):
        http_info = self._delete_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_templates_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/templates/{uuid}/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_build_job_async(self, request):
        r"""禁用构建任务

        禁用构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DisableBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DisableBuildJobResponse`
        """
        http_info = self._disable_build_job_http_info(request)
        return self._call_api(**http_info)

    def disable_build_job_async_invoker(self, request):
        http_info = self._disable_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableBuildJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_notice_async(self, request):
        r"""取消通知

        取消通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableNotice
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DisableNoticeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DisableNoticeResponse`
        """
        http_info = self._disable_notice_http_info(request)
        return self._call_api(**http_info)

    def disable_notice_async_invoker(self, request):
        http_info = self._disable_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_notice_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/notice/{job_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableNoticeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'notice_type' in local_var_params:
            query_params.append(('notice_type', local_var_params['notice_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_build_log_async(self, request):
        r"""下载全量构建日志

        下载全量构建日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadBuildLog
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadBuildLogRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadBuildLogResponse`
        """
        http_info = self._download_build_log_http_info(request)
        return self._call_api(**http_info)

    def download_build_log_async_invoker(self, request):
        http_info = self._download_build_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_build_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{record_id}/download-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadBuildLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
        if 'log_level' in local_var_params:
            query_params.append(('log_level', local_var_params['log_level']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_keystore_async(self, request):
        r"""KeyStore文件下载

        下载指定租户下的KeyStore文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadKeystore
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadKeystoreRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadKeystoreResponse`
        """
        http_info = self._download_keystore_http_info(request)
        return self._call_api(**http_info)

    def download_keystore_async_invoker(self, request):
        http_info = self._download_keystore_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_keystore_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/keystore",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadKeystoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_real_time_log_async(self, request):
        r"""下载构建实时日志

        下载构建实时日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadRealTimeLog
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadRealTimeLogRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadRealTimeLogResponse`
        """
        http_info = self._download_real_time_log_http_info(request)
        return self._call_api(**http_info)

    def download_real_time_log_async_invoker(self, request):
        http_info = self._download_real_time_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_real_time_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/real-time-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadRealTimeLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'length' in local_var_params:
            query_params.append(('length', local_var_params['length']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_task_log_async(self, request):
        r"""下载构建步骤日志

        下载构建步骤日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadTaskLog
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadTaskLogRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadTaskLogResponse`
        """
        http_info = self._download_task_log_http_info(request)
        return self._call_api(**http_info)

    def download_task_log_async_invoker(self, request):
        http_info = self._download_task_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_task_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{record_id}/task-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadTaskLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'log_level' in local_var_params:
            query_params.append(('log_level', local_var_params['log_level']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_build_job_async(self, request):
        r"""恢复构建任务

        恢复构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.EnableBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.EnableBuildJobResponse`
        """
        http_info = self._enable_build_job_http_info(request)
        return self._call_api(**http_info)

    def enable_build_job_async_invoker(self, request):
        http_info = self._enable_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/recover",
            "request_type": request.__class__.__name__,
            "response_type": "EnableBuildJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_build_info_record_async(self, request):
        r"""获取任务构建记录列表

        获取任务构建记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuildInfoRecord
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordResponse`
        """
        http_info = self._list_build_info_record_http_info(request)
        return self._call_api(**http_info)

    def list_build_info_record_async_invoker(self, request):
        http_info = self._list_build_info_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_build_info_record_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/build-info-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListBuildInfoRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_build_info_record_by_job_id_async(self, request):
        r"""获取任务构建记录列表v1

        获取任务构建记录列表v1
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuildInfoRecordByJobId
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordByJobIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListBuildInfoRecordByJobIdResponse`
        """
        http_info = self._list_build_info_record_by_job_id_http_info(request)
        return self._call_api(**http_info)

    def list_build_info_record_by_job_id_async_invoker(self, request):
        http_info = self._list_build_info_record_by_job_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_build_info_record_by_job_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{job_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListBuildInfoRecordByJobIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_job_config_async(self, request):
        r"""获取构建任务详情

        获取构建任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobConfig
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListJobConfigRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListJobConfigResponse`
        """
        http_info = self._list_job_config_http_info(request)
        return self._call_api(**http_info)

    def list_job_config_async_invoker(self, request):
        http_info = self._list_job_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'get_all_params' in local_var_params:
            query_params.append(('get_all_params', local_var_params['get_all_params']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_notice_async(self, request):
        r"""查询通知

        查询通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotice
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListNoticeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListNoticeResponse`
        """
        http_info = self._list_notice_http_info(request)
        return self._call_api(**http_info)

    def list_notice_async_invoker(self, request):
        http_info = self._list_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notice_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/notice/{job_id}/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListNoticeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_official_template_async(self, request):
        r"""查询官方模版

        查询官方模版
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOfficialTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListOfficialTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListOfficialTemplateResponse`
        """
        http_info = self._list_official_template_http_info(request)
        return self._call_api(**http_info)

    def list_official_template_async_invoker(self, request):
        http_info = self._list_official_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_official_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/template/officialtemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListOfficialTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_jobs_async(self, request):
        r"""查询项目任务列表

        查询项目任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectJobs
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListProjectJobsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListProjectJobsResponse`
        """
        http_info = self._list_project_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_project_jobs_async_invoker(self, request):
        http_info = self._list_project_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{project_id}/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_order' in local_var_params:
            query_params.append(('sort_order', local_var_params['sort_order']))
        if 'creator_id' in local_var_params:
            query_params.append(('creator_id', local_var_params['creator_id']))
        if 'build_status' in local_var_params:
            query_params.append(('build_status', local_var_params['build_status']))
        if 'by_group' in local_var_params:
            query_params.append(('by_group', local_var_params['by_group']))
        if 'group_path_id' in local_var_params:
            query_params.append(('group_path_id', local_var_params['group_path_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_recycling_job_async(self, request):
        r"""查看回收站中删除的构建任务列表

        查看回收站中删除的构建任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecyclingJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecyclingJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListRecyclingJobResponse`
        """
        http_info = self._list_recycling_job_http_info(request)
        return self._call_api(**http_info)

    def list_recycling_job_async_invoker(self, request):
        http_info = self._list_recycling_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_recycling_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/recycling-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecyclingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_templates_async(self, request):
        r"""查询构建模板

        查询构建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_async_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/templates/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def run_job_async(self, request):
        r"""执行构建任务

        执行构建任务,可传自定义参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.RunJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.RunJobResponse`
        """
        http_info = self._run_job_http_info(request)
        return self._call_api(**http_info)

    def run_job_async_invoker(self, request):
        http_info = self._run_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/build",
            "request_type": request.__class__.__name__,
            "response_type": "RunJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_params_list_async(self, request):
        r"""编辑页获取参数类型的接口

        编辑页获取参数类型的接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildParamsList
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildParamsListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildParamsListResponse`
        """
        http_info = self._show_build_params_list_http_info(request)
        return self._call_api(**http_info)

    def show_build_params_list_async_invoker(self, request):
        http_info = self._show_build_params_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_params_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/build-params",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildParamsListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_record_async(self, request):
        r"""查询指定构建记录详情

        查询指定构建记录详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildRecord
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordResponse`
        """
        http_info = self._show_build_record_http_info(request)
        return self._call_api(**http_info)

    def show_build_record_async_invoker(self, request):
        http_info = self._show_build_record_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_record_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{record_id}/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_record_build_script_async(self, request):
        r"""获取构建记录的构建脚本

        获取构建记录的构建脚本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildRecordBuildScript
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordBuildScriptRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordBuildScriptResponse`
        """
        http_info = self._show_build_record_build_script_http_info(request)
        return self._call_api(**http_info)

    def show_build_record_build_script_async_invoker(self, request):
        http_info = self._show_build_record_build_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_record_build_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{record_id}/build-script",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildRecordBuildScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_build_record_full_stages_async(self, request):
        r"""获取任务各阶段信息

        获取任务各阶段信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuildRecordFullStages
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordFullStagesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowBuildRecordFullStagesResponse`
        """
        http_info = self._show_build_record_full_stages_http_info(request)
        return self._call_api(**http_info)

    def show_build_record_full_stages_async_invoker(self, request):
        http_info = self._show_build_record_full_stages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_build_record_full_stages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/record/{record_id}/full-stages",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuildRecordFullStagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []
        if 'cascade' in local_var_params:
            query_params.append(('cascade', local_var_params['cascade']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_history_details_async(self, request):
        r"""获取构建历史详情信息接口

        获取构建历史详情信息接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHistoryDetails
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowHistoryDetailsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowHistoryDetailsResponse`
        """
        http_info = self._show_history_details_http_info(request)
        return self._call_api(**http_info)

    def show_history_details_async_invoker(self, request):
        http_info = self._show_history_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_history_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_number}/history-details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_number' in local_var_params:
            path_params['build_number'] = local_var_params['build_number']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_image_template_list_async(self, request):
        r"""获取镜像模板列表

        获取镜像模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageTemplateList
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowImageTemplateListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowImageTemplateListResponse`
        """
        http_info = self._show_image_template_list_http_info(request)
        return self._call_api(**http_info)

    def show_image_template_list_async_invoker(self, request):
        http_info = self._show_image_template_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_image_template_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/image/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageTemplateListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_build_success_ratio_async(self, request):
        r"""查询构建成功率

        查询构建成功率
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobBuildSuccessRatio
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildSuccessRatioRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildSuccessRatioResponse`
        """
        http_info = self._show_job_build_success_ratio_http_info(request)
        return self._call_api(**http_info)

    def show_job_build_success_ratio_async_invoker(self, request):
        http_info = self._show_job_build_success_ratio_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_build_success_ratio_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/ratio",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobBuildSuccessRatioResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))
        if 'branch' in local_var_params:
            query_params.append(('branch', local_var_params['branch']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_build_time_async(self, request):
        r"""洞察构建时长

        洞察构建时长
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobBuildTime
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildTimeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildTimeResponse`
        """
        http_info = self._show_job_build_time_http_info(request)
        return self._call_api(**http_info)

    def show_job_build_time_async_invoker(self, request):
        http_info = self._show_job_build_time_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_build_time_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/time",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobBuildTimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))
        if 'branch' in local_var_params:
            query_params.append(('branch', local_var_params['branch']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_config_async(self, request):
        r"""获取构建任务详情

        获取构建任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobConfig
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigResponse`
        """
        http_info = self._show_job_config_http_info(request)
        return self._call_api(**http_info)

    def show_job_config_async_invoker(self, request):
        http_info = self._show_job_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'get_all_params' in local_var_params:
            query_params.append(('get_all_params', local_var_params['get_all_params']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_config_diff_async(self, request):
        r"""获取构建任务配置的对比差异

        获取构建任务配置的对比差异
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobConfigDiff
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigDiffRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobConfigDiffResponse`
        """
        http_info = self._show_job_config_diff_http_info(request)
        return self._call_api(**http_info)

    def show_job_config_diff_async_invoker(self, request):
        http_info = self._show_job_config_diff_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_config_diff_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/diff",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobConfigDiffResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'revisedl_no' in local_var_params:
            query_params.append(('revisedl_no', local_var_params['revisedl_no']))
        if 'original_no' in local_var_params:
            query_params.append(('original_no', local_var_params['original_no']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_info_async(self, request):
        r"""查看构建任务构建信息

        查看构建任务构建信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobInfoResponse`
        """
        http_info = self._show_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_job_info_async_invoker(self, request):
        http_info = self._show_job_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_list_by_project_id_async(self, request):
        r"""查看项目下用户的构建任务列表

        查看项目下用户的构建任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobListByProjectId
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobListByProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobListByProjectIdResponse`
        """
        http_info = self._show_job_list_by_project_id_http_info(request)
        return self._call_api(**http_info)

    def show_job_list_by_project_id_async_invoker(self, request):
        http_info = self._show_job_list_by_project_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_list_by_project_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobListByProjectIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_role_permission_async(self, request):
        r"""获取构建任务的角色权限矩阵信息

        获取构建任务的角色权限矩阵信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobRolePermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobRolePermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobRolePermissionResponse`
        """
        http_info = self._show_job_role_permission_http_info(request)
        return self._call_api(**http_info)

    def show_job_role_permission_async_invoker(self, request):
        http_info = self._show_job_role_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_role_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/permission/role",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobRolePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_status_async(self, request):
        r"""查看任务运行状态

        查看任务运行状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobStatus
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobStatusResponse`
        """
        http_info = self._show_job_status_http_info(request)
        return self._call_api(**http_info)

    def show_job_status_async_invoker(self, request):
        http_info = self._show_job_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_success_ratio_async(self, request):
        r"""根据开始时间和结束时间查看构建任务的构建成功率

        根据开始时间和结束时间查看构建任务的构建成功率
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobSuccessRatio
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSuccessRatioRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSuccessRatioResponse`
        """
        http_info = self._show_job_success_ratio_http_info(request)
        return self._call_api(**http_info)

    def show_job_success_ratio_async_invoker(self, request):
        http_info = self._show_job_success_ratio_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_success_ratio_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/success-ratio",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobSuccessRatioResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_job_system_parameters_async(self, request):
        r"""查看系统预定义参数

        查看系统预定义参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobSystemParameters
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSystemParametersRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowJobSystemParametersResponse`
        """
        http_info = self._show_job_system_parameters_http_info(request)
        return self._call_api(**http_info)

    def show_job_system_parameters_async_invoker(self, request):
        http_info = self._show_job_system_parameters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_system_parameters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/system-parameters",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobSystemParametersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_last_history_async(self, request):
        r"""查询指定代码仓库最近一次成功的构建历史

        查询指定代码仓库最近一次成功的构建历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLastHistory
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowLastHistoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowLastHistoryResponse`
        """
        http_info = self._show_last_history_http_info(request)
        return self._call_api(**http_info)

    def show_last_history_async_invoker(self, request):
        http_info = self._show_last_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_last_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{project_id}/last-history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLastHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_list_history_async(self, request):
        r"""查看构建任务的构建历史列表

        查看构建任务的构建历史列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListHistory
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListHistoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListHistoryResponse`
        """
        http_info = self._show_list_history_http_info(request)
        return self._call_api(**http_info)

    def show_list_history_async_invoker(self, request):
        http_info = self._show_list_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_list_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_list_period_history_async(self, request):
        r"""根据开始时间和结束时间查看构建任务的构建历史列表

        根据开始时间和结束时间查看构建任务的构建历史列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListPeriodHistory
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListPeriodHistoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowListPeriodHistoryResponse`
        """
        http_info = self._show_list_period_history_http_info(request)
        return self._call_api(**http_info)

    def show_list_period_history_async_invoker(self, request):
        http_info = self._show_list_period_history_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_list_period_history_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/period-history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowListPeriodHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_output_info_async(self, request):
        r"""获取构建产物详情信息

        获取构建产物详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOutputInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowOutputInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowOutputInfoResponse`
        """
        http_info = self._show_output_info_http_info(request)
        return self._call_api(**http_info)

    def show_output_info_async_invoker(self, request):
        http_info = self._show_output_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_output_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/output-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOutputInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_permission_async(self, request):
        r"""获取用户权限

        获取用户权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectPermission
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowProjectPermissionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowProjectPermissionResponse`
        """
        http_info = self._show_project_permission_http_info(request)
        return self._call_api(**http_info)

    def show_project_permission_async_invoker(self, request):
        http_info = self._show_project_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/domain/user-permission",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_record_detail_async(self, request):
        r"""获取构建记录信息

        获取构建记录信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordDetail
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordDetailResponse`
        """
        http_info = self._show_record_detail_http_info(request)
        return self._call_api(**http_info)

    def show_record_detail_async_invoker(self, request):
        http_info = self._show_record_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/jobs/{job_id}/{build_no}/record-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_report_summary_async(self, request):
        r"""获取覆盖率接口

        获取覆盖率接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReportSummary
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummaryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowReportSummaryResponse`
        """
        http_info = self._show_report_summary_http_info(request)
        return self._call_api(**http_info)

    def show_report_summary_async_invoker(self, request):
        http_info = self._show_report_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_report_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/report/{job_id}/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'build_no' in local_var_params:
            query_params.append(('build_no', local_var_params['build_no']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_running_status_async(self, request):
        r"""查看任务是否在构建

        查看任务是否在构建
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRunningStatus
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRunningStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRunningStatusResponse`
        """
        http_info = self._show_running_status_http_info(request)
        return self._call_api(**http_info)

    def show_running_status_async_invoker(self, request):
        http_info = self._show_running_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_running_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/{job_id}/running-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRunningStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_yaml_template_async(self, request):
        r"""获取代码化构建默认模板

        获取代码化构建默认模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowYamlTemplate
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowYamlTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowYamlTemplateResponse`
        """
        http_info = self._show_yaml_template_http_info(request)
        return self._call_api(**http_info)

    def show_yaml_template_async_invoker(self, request):
        http_info = self._show_yaml_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_yaml_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/template/{job_id}/default-template",
            "request_type": request.__class__.__name__,
            "response_type": "ShowYamlTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'default_host' in local_var_params:
            query_params.append(('default_host', local_var_params['default_host']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_build_job_async(self, request):
        r"""停止构建任务

        停止构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.StopBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.StopBuildJobResponse`
        """
        http_info = self._stop_build_job_http_info(request)
        return self._call_api(**http_info)

    def stop_build_job_async_invoker(self, request):
        http_info = self._stop_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopBuildJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_build_job_async(self, request):
        r"""更新构建任务

        更新构建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBuildJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateBuildJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateBuildJobResponse`
        """
        http_info = self._update_build_job_http_info(request)
        return self._call_api(**http_info)

    def update_build_job_async_invoker(self, request):
        http_info = self._update_build_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_build_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBuildJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_notice_async(self, request):
        r"""更新通知

        更新通知
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotice
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateNoticeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.UpdateNoticeResponse`
        """
        http_info = self._update_notice_http_info(request)
        return self._call_api(**http_info)

    def update_notice_async_invoker(self, request):
        http_info = self._update_notice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notice_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/notice/{job_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNoticeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_log_by_record_id_async(self, request):
        r"""下载构建日志(待下线)

        下载构建日志(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadLogByRecordId
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadLogByRecordIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DownloadLogByRecordIdResponse`
        """
        http_info = self._download_log_by_record_id_http_info(request)
        return self._call_api(**http_info)

    def download_log_by_record_id_async_invoker(self, request):
        http_info = self._download_log_by_record_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_log_by_record_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{record_id}/download-log",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadLogByRecordIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'record_id' in local_var_params:
            path_params['record_id'] = local_var_params['record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_flow_graph_async(self, request):
        r"""获取构建记录的有向无环图(待下线)

        获取构建记录的有向无环图(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlowGraph
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowFlowGraphRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowFlowGraphResponse`
        """
        http_info = self._show_flow_graph_http_info(request)
        return self._call_api(**http_info)

    def show_flow_graph_async_invoker(self, request):
        http_info = self._show_flow_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flow_graph_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{build_flow_record_id}/flow-graph",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'build_flow_record_id' in local_var_params:
            path_params['build_flow_record_id'] = local_var_params['build_flow_record_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_record_info_async(self, request):
        r"""获取构建记录信息(待下线)

        获取构建记录信息(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordInfo
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ShowRecordInfoResponse`
        """
        http_info = self._show_record_info_http_info(request)
        return self._call_api(**http_info)

    def show_record_info_async_invoker(self, request):
        http_info = self._show_record_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_record_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/jobs/{job_id}/{build_no}/record-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'build_no' in local_var_params:
            path_params['build_no'] = local_var_params['build_no']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_job_async(self, request):
        r"""停止构建任务(待下线)

        停止构建任务(待下线)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkcodeartsbuild.v3.StopJobRequest`
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.StopJobResponse`
        """
        http_info = self._stop_job_http_info(request)
        return self._call_api(**http_info)

    def stop_job_async_invoker(self, request):
        http_info = self._stop_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/jobs/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	        async_request=True)
