# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkcbh.v2.model.agency_authorize_info import AgencyAuthorizeInfo
from huaweicloudsdkcbh.v2.model.authorize_csms_and_kms_request_body import AuthorizeCsmsAndKmsRequestBody
from huaweicloudsdkcbh.v2.model.availability_zones import AvailabilityZones
from huaweicloudsdkcbh.v2.model.batch_create_instance_tag_request import BatchCreateInstanceTagRequest
from huaweicloudsdkcbh.v2.model.batch_create_instance_tag_response import BatchCreateInstanceTagResponse
from huaweicloudsdkcbh.v2.model.cbh_instances import CBHInstances
from huaweicloudsdkcbh.v2.model.cbs_get_resource_id_tags import CbsGetResourceIdTags
from huaweicloudsdkcbh.v2.model.cbs_get_spec_info import CbsGetSpecInfo
from huaweicloudsdkcbh.v2.model.change_instance_request_body import ChangeInstanceRequestBody
from huaweicloudsdkcbh.v2.model.change_instance_security_groups import ChangeInstanceSecurityGroups
from huaweicloudsdkcbh.v2.model.common_cbh_request_body import CommonCbhRequestBody
from huaweicloudsdkcbh.v2.model.count_instances_by_tag_request import CountInstancesByTagRequest
from huaweicloudsdkcbh.v2.model.count_instances_by_tag_response import CountInstancesByTagResponse
from huaweicloudsdkcbh.v2.model.create_instance_body import CreateInstanceBody
from huaweicloudsdkcbh.v2.model.create_instance_request import CreateInstanceRequest
from huaweicloudsdkcbh.v2.model.create_instance_response import CreateInstanceResponse
from huaweicloudsdkcbh.v2.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkcbh.v2.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkcbh.v2.model.install_instance_eip_request import InstallInstanceEipRequest
from huaweicloudsdkcbh.v2.model.install_instance_eip_response import InstallInstanceEipResponse
from huaweicloudsdkcbh.v2.model.instance_detail import InstanceDetail
from huaweicloudsdkcbh.v2.model.instance_detail_az_info import InstanceDetailAzInfo
from huaweicloudsdkcbh.v2.model.instance_detail_ha_info import InstanceDetailHaInfo
from huaweicloudsdkcbh.v2.model.instance_detail_network import InstanceDetailNetwork
from huaweicloudsdkcbh.v2.model.instance_detail_resource_info import InstanceDetailResourceInfo
from huaweicloudsdkcbh.v2.model.instance_detail_status_info import InstanceDetailStatusInfo
from huaweicloudsdkcbh.v2.model.is_auto_pay import IsAutoPay
from huaweicloudsdkcbh.v2.model.list_available_zones_request import ListAvailableZonesRequest
from huaweicloudsdkcbh.v2.model.list_available_zones_response import ListAvailableZonesResponse
from huaweicloudsdkcbh.v2.model.list_cbh_by_tags_request_body import ListCBHByTagsRequestBody
from huaweicloudsdkcbh.v2.model.list_instances_by_tag_request import ListInstancesByTagRequest
from huaweicloudsdkcbh.v2.model.list_instances_by_tag_response import ListInstancesByTagResponse
from huaweicloudsdkcbh.v2.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkcbh.v2.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkcbh.v2.model.list_specifications_request import ListSpecificationsRequest
from huaweicloudsdkcbh.v2.model.list_specifications_response import ListSpecificationsResponse
from huaweicloudsdkcbh.v2.model.list_tags_request import ListTagsRequest
from huaweicloudsdkcbh.v2.model.list_tags_response import ListTagsResponse
from huaweicloudsdkcbh.v2.model.login_instance_request import LoginInstanceRequest
from huaweicloudsdkcbh.v2.model.login_instance_response import LoginInstanceResponse
from huaweicloudsdkcbh.v2.model.match import Match
from huaweicloudsdkcbh.v2.model.network_info_create import NetworkInfoCreate
from huaweicloudsdkcbh.v2.model.operate_eip_request_body import OperateEipRequestBody
from huaweicloudsdkcbh.v2.model.reboot_cbh_request_body import RebootCbhRequestBody
from huaweicloudsdkcbh.v2.model.reboot_instance_request import RebootInstanceRequest
from huaweicloudsdkcbh.v2.model.reboot_instance_response import RebootInstanceResponse
from huaweicloudsdkcbh.v2.model.register_authorization_request import RegisterAuthorizationRequest
from huaweicloudsdkcbh.v2.model.register_authorization_response import RegisterAuthorizationResponse
from huaweicloudsdkcbh.v2.model.reset_instance_login_method_request import ResetInstanceLoginMethodRequest
from huaweicloudsdkcbh.v2.model.reset_instance_login_method_response import ResetInstanceLoginMethodResponse
from huaweicloudsdkcbh.v2.model.reset_instance_password_request import ResetInstancePasswordRequest
from huaweicloudsdkcbh.v2.model.reset_instance_password_response import ResetInstancePasswordResponse
from huaweicloudsdkcbh.v2.model.reset_password import ResetPassword
from huaweicloudsdkcbh.v2.model.resize_instance_request import ResizeInstanceRequest
from huaweicloudsdkcbh.v2.model.resize_instance_response import ResizeInstanceResponse
from huaweicloudsdkcbh.v2.model.resource_tag import ResourceTag
from huaweicloudsdkcbh.v2.model.resources import Resources
from huaweicloudsdkcbh.v2.model.rollback_instance_request import RollbackInstanceRequest
from huaweicloudsdkcbh.v2.model.rollback_instance_request_body import RollbackInstanceRequestBody
from huaweicloudsdkcbh.v2.model.rollback_instance_response import RollbackInstanceResponse
from huaweicloudsdkcbh.v2.model.security_group import SecurityGroup
from huaweicloudsdkcbh.v2.model.show_authorization_request import ShowAuthorizationRequest
from huaweicloudsdkcbh.v2.model.show_authorization_response import ShowAuthorizationResponse
from huaweicloudsdkcbh.v2.model.show_ecs_quota_request import ShowEcsQuotaRequest
from huaweicloudsdkcbh.v2.model.show_ecs_quota_response import ShowEcsQuotaResponse
from huaweicloudsdkcbh.v2.model.show_instance_status_request import ShowInstanceStatusRequest
from huaweicloudsdkcbh.v2.model.show_instance_status_response import ShowInstanceStatusResponse
from huaweicloudsdkcbh.v2.model.show_instance_tags_request import ShowInstanceTagsRequest
from huaweicloudsdkcbh.v2.model.show_instance_tags_response import ShowInstanceTagsResponse
from huaweicloudsdkcbh.v2.model.show_om_url_request import ShowOmUrlRequest
from huaweicloudsdkcbh.v2.model.show_om_url_response import ShowOmUrlResponse
from huaweicloudsdkcbh.v2.model.show_quota_request import ShowQuotaRequest
from huaweicloudsdkcbh.v2.model.show_quota_response import ShowQuotaResponse
from huaweicloudsdkcbh.v2.model.start_instance_request import StartInstanceRequest
from huaweicloudsdkcbh.v2.model.start_instance_response import StartInstanceResponse
from huaweicloudsdkcbh.v2.model.stop_instance_request import StopInstanceRequest
from huaweicloudsdkcbh.v2.model.stop_instance_response import StopInstanceResponse
from huaweicloudsdkcbh.v2.model.tags import Tags
from huaweicloudsdkcbh.v2.model.uninstall_instance_eip_request import UninstallInstanceEipRequest
from huaweicloudsdkcbh.v2.model.uninstall_instance_eip_response import UninstallInstanceEipResponse
from huaweicloudsdkcbh.v2.model.update_instance_security_group_request import UpdateInstanceSecurityGroupRequest
from huaweicloudsdkcbh.v2.model.update_instance_security_group_response import UpdateInstanceSecurityGroupResponse
from huaweicloudsdkcbh.v2.model.upgrade_cbh_request_body import UpgradeCbhRequestBody
from huaweicloudsdkcbh.v2.model.upgrade_instance_request import UpgradeInstanceRequest
from huaweicloudsdkcbh.v2.model.upgrade_instance_response import UpgradeInstanceResponse
