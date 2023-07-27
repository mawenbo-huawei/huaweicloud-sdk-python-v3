# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkgaussdbforopengauss.v3.model.add_instance_tags_request import AddInstanceTagsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.add_instance_tags_response import AddInstanceTagsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.add_tags_request_body import AddTagsRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.allow_db_privileges_request import AllowDbPrivilegesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.allow_db_privileges_response import AllowDbPrivilegesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.applied_histories_result import AppliedHistoriesResult
from huaweicloudsdkgaussdbforopengauss.v3.model.apply_configuration_request_body import ApplyConfigurationRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.attach_eip_request import AttachEipRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.attach_eip_response import AttachEipResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.available_flavor_info_result import AvailableFlavorInfoResult
from huaweicloudsdkgaussdbforopengauss.v3.model.backup_info import BackupInfo
from huaweicloudsdkgaussdbforopengauss.v3.model.backup_policy import BackupPolicy
from huaweicloudsdkgaussdbforopengauss.v3.model.backup_policy_error_response import BackupPolicyErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.backups import Backups
from huaweicloudsdkgaussdbforopengauss.v3.model.backups_result import BackupsResult
from huaweicloudsdkgaussdbforopengauss.v3.model.bind_eip_request_body import BindEIPRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.binded_eip_result import BindedEipResult
from huaweicloudsdkgaussdbforopengauss.v3.model.components import Components
from huaweicloudsdkgaussdbforopengauss.v3.model.configuration_parameter import ConfigurationParameter
from huaweicloudsdkgaussdbforopengauss.v3.model.configuration_result import ConfigurationResult
from huaweicloudsdkgaussdbforopengauss.v3.model.configuration_summary import ConfigurationSummary
from huaweicloudsdkgaussdbforopengauss.v3.model.copy_configuration_request import CopyConfigurationRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.copy_configuration_response import CopyConfigurationResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_configuration_template_request import CreateConfigurationTemplateRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_configuration_template_request_body import CreateConfigurationTemplateRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.create_configuration_template_response import CreateConfigurationTemplateResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_database_request import CreateDatabaseRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_database_response import CreateDatabaseResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_database_schemas_request import CreateDatabaseSchemasRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_database_schemas_response import CreateDatabaseSchemasResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_db_instance_request import CreateDbInstanceRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_db_instance_response import CreateDbInstanceResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_db_user_request import CreateDbUserRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_db_user_response import CreateDbUserResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_instance_request import CreateInstanceRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_instance_resp_item import CreateInstanceRespItem
from huaweicloudsdkgaussdbforopengauss.v3.model.create_instance_response import CreateInstanceResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_manual_backup_request import CreateManualBackupRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_manual_backup_request_body import CreateManualBackupRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.create_manual_backup_response import CreateManualBackupResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.create_restore_instance_request import CreateRestoreInstanceRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.create_restore_instance_response import CreateRestoreInstanceResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.data_stroe_error_response import DataStroeErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.datastore_option import DatastoreOption
from huaweicloudsdkgaussdbforopengauss.v3.model.datastores_result import DatastoresResult
from huaweicloudsdkgaussdbforopengauss.v3.model.db_user_pwd_request import DbUserPwdRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_backup_error_response import DeleteBackupErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_configuration_request import DeleteConfigurationRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_configuration_response import DeleteConfigurationResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_job_request import DeleteJobRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_job_response import DeleteJobResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_manual_backup_request import DeleteManualBackupRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.delete_manual_backup_response import DeleteManualBackupResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.download_backup_error_response import DownloadBackupErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.download_backup_request import DownloadBackupRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.download_backup_response import DownloadBackupResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.download_object import DownloadObject
from huaweicloudsdkgaussdbforopengauss.v3.model.eps_quotas_option import EpsQuotasOption
from huaweicloudsdkgaussdbforopengauss.v3.model.flavor import Flavor
from huaweicloudsdkgaussdbforopengauss.v3.model.flavor_error_response import FlavorErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.flavor_result import FlavorResult
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_database_for_creation import GaussDBforOpenDatabaseForCreation
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_create_schema_req import GaussDBforOpenGaussCreateSchemaReq
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_database_for_list_schema import GaussDBforOpenGaussDatabaseForListSchema
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_database_schema_req import GaussDBforOpenGaussDatabaseSchemaReq
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_grant_request import GaussDBforOpenGaussGrantRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_list_database import GaussDBforOpenGaussListDatabase
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_user_for_creation import GaussDBforOpenGaussUserForCreation
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_user_for_list import GaussDBforOpenGaussUserForList
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_user_for_list_attributes import GaussDBforOpenGaussUserForListAttributes
from huaweicloudsdkgaussdbforopengauss.v3.model.gauss_d_bfor_open_gauss_user_with_privilege import GaussDBforOpenGaussUserWithPrivilege
from huaweicloudsdkgaussdbforopengauss.v3.model.get_restore_time_response_restore_time import GetRestoreTimeResponseRestoreTime
from huaweicloudsdkgaussdbforopengauss.v3.model.instance_info_result import InstanceInfoResult
from huaweicloudsdkgaussdbforopengauss.v3.model.instances_list_result import InstancesListResult
from huaweicloudsdkgaussdbforopengauss.v3.model.instances_result import InstancesResult
from huaweicloudsdkgaussdbforopengauss.v3.model.job_detail import JobDetail
from huaweicloudsdkgaussdbforopengauss.v3.model.job_instance_info import JobInstanceInfo
from huaweicloudsdkgaussdbforopengauss.v3.model.list_applicable_instances_request import ListApplicableInstancesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_applicable_instances_response import ListApplicableInstancesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_applied_histories_request import ListAppliedHistoriesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_applied_histories_response import ListAppliedHistoriesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_available_flavors_request import ListAvailableFlavorsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_available_flavors_response import ListAvailableFlavorsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_backups_request import ListBackupsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_backups_response import ListBackupsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_binded_eips_request import ListBindedEipsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_binded_eips_response import ListBindedEipsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_component_infos_request import ListComponentInfosRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_component_infos_response import ListComponentInfosResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_configurations_diff_request import ListConfigurationsDiffRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_configurations_diff_response import ListConfigurationsDiffResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_configurations_request import ListConfigurationsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_configurations_response import ListConfigurationsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_database_schemas_request import ListDatabaseSchemasRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_database_schemas_response import ListDatabaseSchemasResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_databases_request import ListDatabasesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_databases_response import ListDatabasesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_datastore import ListDatastore
from huaweicloudsdkgaussdbforopengauss.v3.model.list_datastores_request import ListDatastoresRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_datastores_response import ListDatastoresResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_db_backups_request import ListDbBackupsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_db_backups_response import ListDbBackupsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_db_flavors_request import ListDbFlavorsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_db_flavors_response import ListDbFlavorsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_db_users_request import ListDbUsersRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_db_users_response import ListDbUsersResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_diff_details_result import ListDiffDetailsResult
from huaweicloudsdkgaussdbforopengauss.v3.model.list_eps_quotas_request import ListEpsQuotasRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_eps_quotas_response import ListEpsQuotasResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_flavor_info import ListFlavorInfo
from huaweicloudsdkgaussdbforopengauss.v3.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_gauss_db_datastores_request import ListGaussDbDatastoresRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_gauss_db_datastores_response import ListGaussDbDatastoresResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_ha import ListHa
from huaweicloudsdkgaussdbforopengauss.v3.model.list_ha_result import ListHaResult
from huaweicloudsdkgaussdbforopengauss.v3.model.list_history_operations_request import ListHistoryOperationsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_history_operations_response import ListHistoryOperationsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_history_operations_result import ListHistoryOperationsResult
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instance_response import ListInstanceResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instance_result import ListInstanceResult
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instance_tags_request import ListInstanceTagsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instance_tags_response import ListInstanceTagsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instances_details_request import ListInstancesDetailsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instances_details_response import ListInstancesDetailsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_param_group_templates_request import ListParamGroupTemplatesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_param_group_templates_response import ListParamGroupTemplatesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_predefined_tags_request import ListPredefinedTagsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_predefined_tags_response import ListPredefinedTagsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_quota_result import ListQuotaResult
from huaweicloudsdkgaussdbforopengauss.v3.model.list_recycle_instances_request import ListRecycleInstancesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_recycle_instances_response import ListRecycleInstancesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_restorable_instances_request import ListRestorableInstancesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_restorable_instances_response import ListRestorableInstancesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_restore_times_request import ListRestoreTimesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_restore_times_response import ListRestoreTimesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_storage_types_request import ListStorageTypesRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_storage_types_response import ListStorageTypesResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_tasks_request import ListTasksRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.list_tasks_response import ListTasksResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.list_volume import ListVolume
from huaweicloudsdkgaussdbforopengauss.v3.model.modify_eps_quota_request import ModifyEpsQuotaRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.modify_eps_quota_request_body import ModifyEpsQuotaRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.modify_eps_quota_response import ModifyEpsQuotaResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.node_result import NodeResult
from huaweicloudsdkgaussdbforopengauss.v3.model.nodes import Nodes
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_backup_strategy import OpenGaussBackupStrategy
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_backup_strategy_for_list_response import OpenGaussBackupStrategyForListResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_backup_strategy_for_response import OpenGaussBackupStrategyForResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_charge_info import OpenGaussChargeInfo
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_charge_info_list_response import OpenGaussChargeInfoListResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_charge_info_response import OpenGaussChargeInfoResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_coordinators import OpenGaussCoordinators
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_datastore import OpenGaussDatastore
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_datastore_option import OpenGaussDatastoreOption
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_datastore_response import OpenGaussDatastoreResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_datastore_result import OpenGaussDatastoreResult
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_enlarge_volume import OpenGaussEnlargeVolume
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_error_response import OpenGaussErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_expand_cluster import OpenGaussExpandCluster
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_ha import OpenGaussHa
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_ha_option import OpenGaussHaOption
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_ha_response import OpenGaussHaResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_ha_result import OpenGaussHaResult
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_instance_action_request import OpenGaussInstanceActionRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_instance_request import OpenGaussInstanceRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_instance_request_body import OpenGaussInstanceRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_instance_response import OpenGaussInstanceResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_instance_result import OpenGaussInstanceResult
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_modify_instance_configuration_request import OpenGaussModifyInstanceConfigurationRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_resize_request import OpenGaussResizeRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_shard import OpenGaussShard
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_volume import OpenGaussVolume
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_volume_response import OpenGaussVolumeResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.open_gauss_volume_result import OpenGaussVolumeResult
from huaweicloudsdkgaussdbforopengauss.v3.model.opengauss_restore_instance_request import OpengaussRestoreInstanceRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.para_error_response import ParaErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.para_error_response_body import ParaErrorResponseBody
from huaweicloudsdkgaussdbforopengauss.v3.model.para_group_parameter_result import ParaGroupParameterResult
from huaweicloudsdkgaussdbforopengauss.v3.model.param_group_copy_request_body import ParamGroupCopyRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.param_group_diff_request_body import ParamGroupDiffRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.project_quotas_result import ProjectQuotasResult
from huaweicloudsdkgaussdbforopengauss.v3.model.pwd_reset_request import PwdResetRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.recycle_instances_detail_result import RecycleInstancesDetailResult
from huaweicloudsdkgaussdbforopengauss.v3.model.recycle_policy import RecyclePolicy
from huaweicloudsdkgaussdbforopengauss.v3.model.recycle_policy_request_body import RecyclePolicyRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.reset_configuration_request import ResetConfigurationRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.reset_configuration_response import ResetConfigurationResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.reset_pwd_request import ResetPwdRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.reset_pwd_response import ResetPwdResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.resize_instance_flavor_request import ResizeInstanceFlavorRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.resize_instance_flavor_response import ResizeInstanceFlavorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.resource_error_response import ResourceErrorResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.resource_result import ResourceResult
from huaweicloudsdkgaussdbforopengauss.v3.model.restart_instance_request import RestartInstanceRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.restart_instance_response import RestartInstanceResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.restore_point import RestorePoint
from huaweicloudsdkgaussdbforopengauss.v3.model.run_instance_action_request import RunInstanceActionRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.run_instance_action_response import RunInstanceActionResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.set_backup_policy_request import SetBackupPolicyRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.set_backup_policy_request_body import SetBackupPolicyRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.set_backup_policy_response import SetBackupPolicyResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.set_db_user_pwd_request import SetDbUserPwdRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.set_db_user_pwd_response import SetDbUserPwdResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.set_recycle_policy_request import SetRecyclePolicyRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.set_recycle_policy_response import SetRecyclePolicyResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.shards import Shards
from huaweicloudsdkgaussdbforopengauss.v3.model.show_backup_policy import ShowBackupPolicy
from huaweicloudsdkgaussdbforopengauss.v3.model.show_backup_policy_request import ShowBackupPolicyRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_backup_policy_response import ShowBackupPolicyResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_balance_status_request import ShowBalanceStatusRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_balance_status_response import ShowBalanceStatusResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_configuration_detail_request import ShowConfigurationDetailRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_configuration_detail_response import ShowConfigurationDetailResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_deployment_form_request import ShowDeploymentFormRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_deployment_form_response import ShowDeploymentFormResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_configuration_request import ShowInstanceConfigurationRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_configuration_response import ShowInstanceConfigurationResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_disk_request import ShowInstanceDiskRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_disk_response import ShowInstanceDiskResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_param_group_request import ShowInstanceParamGroupRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_param_group_response import ShowInstanceParamGroupResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_snapshot_request import ShowInstanceSnapshotRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_instance_snapshot_response import ShowInstanceSnapshotResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_job_detail_request import ShowJobDetailRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_job_detail_response import ShowJobDetailResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_project_quotas_request import ShowProjectQuotasRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_project_quotas_response import ShowProjectQuotasResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_recycle_policy_request import ShowRecyclePolicyRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_recycle_policy_response import ShowRecyclePolicyResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.show_ssl_cert_download_link_request import ShowSslCertDownloadLinkRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.show_ssl_cert_download_link_response import ShowSslCertDownloadLinkResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.storage import Storage
from huaweicloudsdkgaussdbforopengauss.v3.model.switch_configuration_request import SwitchConfigurationRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.switch_configuration_response import SwitchConfigurationResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.switch_shard_request import SwitchShardRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.switch_shard_request_body import SwitchShardRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.switch_shard_response import SwitchShardResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.tag_result import TagResult
from huaweicloudsdkgaussdbforopengauss.v3.model.tags_option import TagsOption
from huaweicloudsdkgaussdbforopengauss.v3.model.tags_result import TagsResult
from huaweicloudsdkgaussdbforopengauss.v3.model.task_detail_result import TaskDetailResult
from huaweicloudsdkgaussdbforopengauss.v3.model.update_instance_configuration_request import UpdateInstanceConfigurationRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.update_instance_configuration_response import UpdateInstanceConfigurationResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.update_instance_name_request import UpdateInstanceNameRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.update_instance_name_response import UpdateInstanceNameResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.update_name_request_body import UpdateNameRequestBody
from huaweicloudsdkgaussdbforopengauss.v3.model.validate_para_group_name_request import ValidateParaGroupNameRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.validate_para_group_name_response import ValidateParaGroupNameResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.validate_weak_password_request import ValidateWeakPasswordRequest
from huaweicloudsdkgaussdbforopengauss.v3.model.validate_weak_password_response import ValidateWeakPasswordResponse
from huaweicloudsdkgaussdbforopengauss.v3.model.weak_password_request_body import WeakPasswordRequestBody
