# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkcfw.v1.model.add_address_items_info_dto import AddAddressItemsInfoDto
from huaweicloudsdkcfw.v1.model.add_address_items_info_dto_address_items import AddAddressItemsInfoDtoAddressItems
from huaweicloudsdkcfw.v1.model.add_address_items_using_post_request import AddAddressItemsUsingPostRequest
from huaweicloudsdkcfw.v1.model.add_address_items_using_post_response import AddAddressItemsUsingPostResponse
from huaweicloudsdkcfw.v1.model.add_address_set_dto import AddAddressSetDto
from huaweicloudsdkcfw.v1.model.add_address_set_info_using_post_request import AddAddressSetInfoUsingPostRequest
from huaweicloudsdkcfw.v1.model.add_address_set_info_using_post_response import AddAddressSetInfoUsingPostResponse
from huaweicloudsdkcfw.v1.model.add_black_white_list_dto import AddBlackWhiteListDto
from huaweicloudsdkcfw.v1.model.add_black_white_list_using_post_request import AddBlackWhiteListUsingPostRequest
from huaweicloudsdkcfw.v1.model.add_black_white_list_using_post_response import AddBlackWhiteListUsingPostResponse
from huaweicloudsdkcfw.v1.model.add_rule_acl_dto import AddRuleAclDto
from huaweicloudsdkcfw.v1.model.add_rule_acl_dto_rules import AddRuleAclDtoRules
from huaweicloudsdkcfw.v1.model.add_rule_acl_using_post_request import AddRuleAclUsingPostRequest
from huaweicloudsdkcfw.v1.model.add_rule_acl_using_post_response import AddRuleAclUsingPostResponse
from huaweicloudsdkcfw.v1.model.add_service_items_using_post_request_body import AddServiceItemsUsingPOSTRequestBody
from huaweicloudsdkcfw.v1.model.add_service_items_using_post_request_body_service_items import AddServiceItemsUsingPOSTRequestBodyServiceItems
from huaweicloudsdkcfw.v1.model.add_service_items_using_post_request import AddServiceItemsUsingPostRequest
from huaweicloudsdkcfw.v1.model.add_service_items_using_post_response import AddServiceItemsUsingPostResponse
from huaweicloudsdkcfw.v1.model.add_service_set_using_post_request_body import AddServiceSetUsingPOSTRequestBody
from huaweicloudsdkcfw.v1.model.add_service_set_using_post_request import AddServiceSetUsingPostRequest
from huaweicloudsdkcfw.v1.model.add_service_set_using_post_response import AddServiceSetUsingPostResponse
from huaweicloudsdkcfw.v1.model.address_item_list_response_dto_data import AddressItemListResponseDTOData
from huaweicloudsdkcfw.v1.model.address_item_list_response_dto_data_records import AddressItemListResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.address_items import AddressItems
from huaweicloudsdkcfw.v1.model.address_set_detail_response_dto_data import AddressSetDetailResponseDTOData
from huaweicloudsdkcfw.v1.model.address_set_list_response_dto_data import AddressSetListResponseDTOData
from huaweicloudsdkcfw.v1.model.address_set_list_response_dto_data_records import AddressSetListResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.black_white_list_response_data import BlackWhiteListResponseData
from huaweicloudsdkcfw.v1.model.black_white_list_response_data_records import BlackWhiteListResponseDataRecords
from huaweicloudsdkcfw.v1.model.change_ew_protect_status_request import ChangeEwProtectStatusRequest
from huaweicloudsdkcfw.v1.model.change_ew_protect_status_response import ChangeEwProtectStatusResponse
from huaweicloudsdkcfw.v1.model.change_ips_protect_mode_using_post_request import ChangeIpsProtectModeUsingPostRequest
from huaweicloudsdkcfw.v1.model.change_ips_protect_mode_using_post_response import ChangeIpsProtectModeUsingPostResponse
from huaweicloudsdkcfw.v1.model.change_ips_switch_using_post_request import ChangeIpsSwitchUsingPostRequest
from huaweicloudsdkcfw.v1.model.change_ips_switch_using_post_response import ChangeIpsSwitchUsingPostResponse
from huaweicloudsdkcfw.v1.model.change_protect_eip_request import ChangeProtectEipRequest
from huaweicloudsdkcfw.v1.model.change_protect_eip_response import ChangeProtectEipResponse
from huaweicloudsdkcfw.v1.model.change_protect_status_request_body import ChangeProtectStatusRequestBody
from huaweicloudsdkcfw.v1.model.clear_access_log_rule_hit_counts_dto import ClearAccessLogRuleHitCountsDto
from huaweicloudsdkcfw.v1.model.common_response_dto_data import CommonResponseDTOData
from huaweicloudsdkcfw.v1.model.count_eips_request import CountEipsRequest
from huaweicloudsdkcfw.v1.model.count_eips_response import CountEipsResponse
from huaweicloudsdkcfw.v1.model.delete_acl_rule_count_request import DeleteAclRuleCountRequest
from huaweicloudsdkcfw.v1.model.delete_acl_rule_count_response import DeleteAclRuleCountResponse
from huaweicloudsdkcfw.v1.model.delete_address_item_using_delete_request import DeleteAddressItemUsingDeleteRequest
from huaweicloudsdkcfw.v1.model.delete_address_item_using_delete_response import DeleteAddressItemUsingDeleteResponse
from huaweicloudsdkcfw.v1.model.delete_address_set_info_using_delete_request import DeleteAddressSetInfoUsingDeleteRequest
from huaweicloudsdkcfw.v1.model.delete_address_set_info_using_delete_response import DeleteAddressSetInfoUsingDeleteResponse
from huaweicloudsdkcfw.v1.model.delete_black_white_list_using_delete_request import DeleteBlackWhiteListUsingDeleteRequest
from huaweicloudsdkcfw.v1.model.delete_black_white_list_using_delete_response import DeleteBlackWhiteListUsingDeleteResponse
from huaweicloudsdkcfw.v1.model.delete_rule_acl_using_delete_request import DeleteRuleAclUsingDeleteRequest
from huaweicloudsdkcfw.v1.model.delete_rule_acl_using_delete_response import DeleteRuleAclUsingDeleteResponse
from huaweicloudsdkcfw.v1.model.delete_service_item_using_delete_request import DeleteServiceItemUsingDeleteRequest
from huaweicloudsdkcfw.v1.model.delete_service_item_using_delete_response import DeleteServiceItemUsingDeleteResponse
from huaweicloudsdkcfw.v1.model.delete_service_set_using_delete_request import DeleteServiceSetUsingDeleteRequest
from huaweicloudsdkcfw.v1.model.delete_service_set_using_delete_response import DeleteServiceSetUsingDeleteResponse
from huaweicloudsdkcfw.v1.model.dns_servers_response_dto import DnsServersResponseDTO
from huaweicloudsdkcfw.v1.model.eip_count_resp_data import EipCountRespData
from huaweicloudsdkcfw.v1.model.eip_operate_protect_req import EipOperateProtectReq
from huaweicloudsdkcfw.v1.model.eip_operate_protect_req_ip_infos import EipOperateProtectReqIpInfos
from huaweicloudsdkcfw.v1.model.eip_resource import EipResource
from huaweicloudsdkcfw.v1.model.eip_response_data import EipResponseData
from huaweicloudsdkcfw.v1.model.er_instance import ErInstance
from huaweicloudsdkcfw.v1.model.ew_protect_resource_info import EwProtectResourceInfo
from huaweicloudsdkcfw.v1.model.firewall_instance_resource import FirewallInstanceResource
from huaweicloudsdkcfw.v1.model.flavor import Flavor
from huaweicloudsdkcfw.v1.model.get_east_west_firewall_response_body import GetEastWestFirewallResponseBody
from huaweicloudsdkcfw.v1.model.get_firewall_instance_data import GetFirewallInstanceData
from huaweicloudsdkcfw.v1.model.get_firewall_instance_response_record import GetFirewallInstanceResponseRecord
from huaweicloudsdkcfw.v1.model.http_query_cfw_access_controller_logs_response_dto_data import HttpQueryCfwAccessControllerLogsResponseDTOData
from huaweicloudsdkcfw.v1.model.http_query_cfw_access_controller_logs_response_dto_data_records import HttpQueryCfwAccessControllerLogsResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.http_query_cfw_attack_logs_response_dto_data import HttpQueryCfwAttackLogsResponseDTOData
from huaweicloudsdkcfw.v1.model.http_query_cfw_attack_logs_response_dto_data_records import HttpQueryCfwAttackLogsResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.http_query_cfw_flow_logs_response_dto_data import HttpQueryCfwFlowLogsResponseDTOData
from huaweicloudsdkcfw.v1.model.http_query_cfw_flow_logs_response_dto_data_records import HttpQueryCfwFlowLogsResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.id_object import IdObject
from huaweicloudsdkcfw.v1.model.ips_protect_dto import IpsProtectDTO
from huaweicloudsdkcfw.v1.model.ips_protect_mode_object import IpsProtectModeObject
from huaweicloudsdkcfw.v1.model.ips_switch_dto import IpsSwitchDTO
from huaweicloudsdkcfw.v1.model.ips_switch_response_dto import IpsSwitchResponseDTO
from huaweicloudsdkcfw.v1.model.list_access_control_logs_request import ListAccessControlLogsRequest
from huaweicloudsdkcfw.v1.model.list_access_control_logs_response import ListAccessControlLogsResponse
from huaweicloudsdkcfw.v1.model.list_address_items_using_get_request import ListAddressItemsUsingGetRequest
from huaweicloudsdkcfw.v1.model.list_address_items_using_get_response import ListAddressItemsUsingGetResponse
from huaweicloudsdkcfw.v1.model.list_address_set_detail_using_get_request import ListAddressSetDetailUsingGetRequest
from huaweicloudsdkcfw.v1.model.list_address_set_detail_using_get_response import ListAddressSetDetailUsingGetResponse
from huaweicloudsdkcfw.v1.model.list_address_set_list_using_get_request import ListAddressSetListUsingGetRequest
from huaweicloudsdkcfw.v1.model.list_address_set_list_using_get_response import ListAddressSetListUsingGetResponse
from huaweicloudsdkcfw.v1.model.list_attack_logs_request import ListAttackLogsRequest
from huaweicloudsdkcfw.v1.model.list_attack_logs_response import ListAttackLogsResponse
from huaweicloudsdkcfw.v1.model.list_black_white_lists_using_get_request import ListBlackWhiteListsUsingGetRequest
from huaweicloudsdkcfw.v1.model.list_black_white_lists_using_get_response import ListBlackWhiteListsUsingGetResponse
from huaweicloudsdkcfw.v1.model.list_dns_servers_request import ListDnsServersRequest
from huaweicloudsdkcfw.v1.model.list_dns_servers_response import ListDnsServersResponse
from huaweicloudsdkcfw.v1.model.list_east_west_firewall_request import ListEastWestFirewallRequest
from huaweicloudsdkcfw.v1.model.list_east_west_firewall_response import ListEastWestFirewallResponse
from huaweicloudsdkcfw.v1.model.list_eip_resources_request import ListEipResourcesRequest
from huaweicloudsdkcfw.v1.model.list_eip_resources_response import ListEipResourcesResponse
from huaweicloudsdkcfw.v1.model.list_firewall_using_get_request import ListFirewallUsingGetRequest
from huaweicloudsdkcfw.v1.model.list_firewall_using_get_response import ListFirewallUsingGetResponse
from huaweicloudsdkcfw.v1.model.list_flow_logs_request import ListFlowLogsRequest
from huaweicloudsdkcfw.v1.model.list_flow_logs_response import ListFlowLogsResponse
from huaweicloudsdkcfw.v1.model.list_ips_protect_mode_using_post_request import ListIpsProtectModeUsingPostRequest
from huaweicloudsdkcfw.v1.model.list_ips_protect_mode_using_post_response import ListIpsProtectModeUsingPostResponse
from huaweicloudsdkcfw.v1.model.list_ips_switch_status_using_get_request import ListIpsSwitchStatusUsingGetRequest
from huaweicloudsdkcfw.v1.model.list_ips_switch_status_using_get_response import ListIpsSwitchStatusUsingGetResponse
from huaweicloudsdkcfw.v1.model.list_parse_domain_details_request import ListParseDomainDetailsRequest
from huaweicloudsdkcfw.v1.model.list_parse_domain_details_response import ListParseDomainDetailsResponse
from huaweicloudsdkcfw.v1.model.list_rule_acl_using_put_request import ListRuleAclUsingPutRequest
from huaweicloudsdkcfw.v1.model.list_rule_acl_using_put_response import ListRuleAclUsingPutResponse
from huaweicloudsdkcfw.v1.model.list_rule_acls_using_get_request import ListRuleAclsUsingGetRequest
from huaweicloudsdkcfw.v1.model.list_rule_acls_using_get_response import ListRuleAclsUsingGetResponse
from huaweicloudsdkcfw.v1.model.list_rule_hit_count_dto import ListRuleHitCountDto
from huaweicloudsdkcfw.v1.model.list_rule_hit_count_request import ListRuleHitCountRequest
from huaweicloudsdkcfw.v1.model.list_rule_hit_count_response import ListRuleHitCountResponse
from huaweicloudsdkcfw.v1.model.list_service_items_details_request import ListServiceItemsDetailsRequest
from huaweicloudsdkcfw.v1.model.list_service_items_details_response import ListServiceItemsDetailsResponse
from huaweicloudsdkcfw.v1.model.list_service_set_details_request import ListServiceSetDetailsRequest
from huaweicloudsdkcfw.v1.model.list_service_set_details_response import ListServiceSetDetailsResponse
from huaweicloudsdkcfw.v1.model.list_service_set_request import ListServiceSetRequest
from huaweicloudsdkcfw.v1.model.list_service_set_response import ListServiceSetResponse
from huaweicloudsdkcfw.v1.model.list_vpc_protects_request import ListVpcProtectsRequest
from huaweicloudsdkcfw.v1.model.list_vpc_protects_response import ListVpcProtectsResponse
from huaweicloudsdkcfw.v1.model.order_rule_acl_dto import OrderRuleAclDto
from huaweicloudsdkcfw.v1.model.packet import Packet
from huaweicloudsdkcfw.v1.model.packet_message import PacketMessage
from huaweicloudsdkcfw.v1.model.protect_object_vo import ProtectObjectVO
from huaweicloudsdkcfw.v1.model.rule_acl_list_response_dto_data import RuleAclListResponseDTOData
from huaweicloudsdkcfw.v1.model.rule_acl_list_response_dto_data_records import RuleAclListResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.rule_address_dto import RuleAddressDto
from huaweicloudsdkcfw.v1.model.rule_hit_count_object import RuleHitCountObject
from huaweicloudsdkcfw.v1.model.rule_hit_count_records import RuleHitCountRecords
from huaweicloudsdkcfw.v1.model.rule_id import RuleId
from huaweicloudsdkcfw.v1.model.rule_id_list import RuleIdList
from huaweicloudsdkcfw.v1.model.rule_service_dto import RuleServiceDto
from huaweicloudsdkcfw.v1.model.service_item_ids import ServiceItemIds
from huaweicloudsdkcfw.v1.model.service_item_list_response_dto_data import ServiceItemListResponseDtoData
from huaweicloudsdkcfw.v1.model.service_item_list_response_dto_data_records import ServiceItemListResponseDtoDataRecords
from huaweicloudsdkcfw.v1.model.service_set import ServiceSet
from huaweicloudsdkcfw.v1.model.service_set_detail_response_dto import ServiceSetDetailResponseDto
from huaweicloudsdkcfw.v1.model.service_set_records import ServiceSetRecords
from huaweicloudsdkcfw.v1.model.subnet_info import SubnetInfo
from huaweicloudsdkcfw.v1.model.success_rsp_data import SuccessRspData
from huaweicloudsdkcfw.v1.model.tag import Tag
from huaweicloudsdkcfw.v1.model.update_address_set_dto import UpdateAddressSetDto
from huaweicloudsdkcfw.v1.model.update_address_set_info_using_put_request import UpdateAddressSetInfoUsingPutRequest
from huaweicloudsdkcfw.v1.model.update_address_set_info_using_put_response import UpdateAddressSetInfoUsingPutResponse
from huaweicloudsdkcfw.v1.model.update_black_white_list_dto import UpdateBlackWhiteListDto
from huaweicloudsdkcfw.v1.model.update_black_white_list_using_put_request import UpdateBlackWhiteListUsingPutRequest
from huaweicloudsdkcfw.v1.model.update_black_white_list_using_put_response import UpdateBlackWhiteListUsingPutResponse
from huaweicloudsdkcfw.v1.model.update_dns_servers_request import UpdateDnsServersRequest
from huaweicloudsdkcfw.v1.model.update_dns_servers_request_body import UpdateDnsServersRequestBody
from huaweicloudsdkcfw.v1.model.update_dns_servers_request_body_dns_server import UpdateDnsServersRequestBodyDnsServer
from huaweicloudsdkcfw.v1.model.update_dns_servers_response import UpdateDnsServersResponse
from huaweicloudsdkcfw.v1.model.update_rule_acl_dto import UpdateRuleAclDto
from huaweicloudsdkcfw.v1.model.update_rule_acl_using_put_request import UpdateRuleAclUsingPutRequest
from huaweicloudsdkcfw.v1.model.update_rule_acl_using_put_response import UpdateRuleAclUsingPutResponse
from huaweicloudsdkcfw.v1.model.update_service_set_using_put_request_body import UpdateServiceSetUsingPUTRequestBody
from huaweicloudsdkcfw.v1.model.update_service_set_using_put_request import UpdateServiceSetUsingPutRequest
from huaweicloudsdkcfw.v1.model.update_service_set_using_put_response import UpdateServiceSetUsingPutResponse
from huaweicloudsdkcfw.v1.model.vpc_protects_vo import VPCProtectsVo
from huaweicloudsdkcfw.v1.model.vpc_attachment_detail import VpcAttachmentDetail
from huaweicloudsdkcfw.v1.model.vpc_detail import VpcDetail
