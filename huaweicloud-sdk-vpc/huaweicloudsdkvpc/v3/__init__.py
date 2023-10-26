# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkvpc.v3.vpc_client import VpcClient
from huaweicloudsdkvpc.v3.vpc_async_client import VpcAsyncClient

from huaweicloudsdkvpc.v3.model.add_extend_cidr_option import AddExtendCidrOption
from huaweicloudsdkvpc.v3.model.add_firewall_rules_request import AddFirewallRulesRequest
from huaweicloudsdkvpc.v3.model.add_firewall_rules_request_body import AddFirewallRulesRequestBody
from huaweicloudsdkvpc.v3.model.add_firewall_rules_response import AddFirewallRulesResponse
from huaweicloudsdkvpc.v3.model.add_security_groups_request import AddSecurityGroupsRequest
from huaweicloudsdkvpc.v3.model.add_security_groups_request_body import AddSecurityGroupsRequestBody
from huaweicloudsdkvpc.v3.model.add_security_groups_response import AddSecurityGroupsResponse
from huaweicloudsdkvpc.v3.model.add_sources_to_traffic_mirror_session_request import AddSourcesToTrafficMirrorSessionRequest
from huaweicloudsdkvpc.v3.model.add_sources_to_traffic_mirror_session_request_body import AddSourcesToTrafficMirrorSessionRequestBody
from huaweicloudsdkvpc.v3.model.add_sources_to_traffic_mirror_session_response import AddSourcesToTrafficMirrorSessionResponse
from huaweicloudsdkvpc.v3.model.add_vpc_extend_cidr_request import AddVpcExtendCidrRequest
from huaweicloudsdkvpc.v3.model.add_vpc_extend_cidr_request_body import AddVpcExtendCidrRequestBody
from huaweicloudsdkvpc.v3.model.add_vpc_extend_cidr_response import AddVpcExtendCidrResponse
from huaweicloudsdkvpc.v3.model.address_group import AddressGroup
from huaweicloudsdkvpc.v3.model.allowed_address_pair import AllowedAddressPair
from huaweicloudsdkvpc.v3.model.associate_subnet_firewall_request import AssociateSubnetFirewallRequest
from huaweicloudsdkvpc.v3.model.associate_subnet_firewall_request_body import AssociateSubnetFirewallRequestBody
from huaweicloudsdkvpc.v3.model.associate_subnet_firewall_response import AssociateSubnetFirewallResponse
from huaweicloudsdkvpc.v3.model.batch_create_security_group_rules_option import BatchCreateSecurityGroupRulesOption
from huaweicloudsdkvpc.v3.model.batch_create_security_group_rules_request import BatchCreateSecurityGroupRulesRequest
from huaweicloudsdkvpc.v3.model.batch_create_security_group_rules_request_body import BatchCreateSecurityGroupRulesRequestBody
from huaweicloudsdkvpc.v3.model.batch_create_security_group_rules_response import BatchCreateSecurityGroupRulesResponse
from huaweicloudsdkvpc.v3.model.batch_create_sub_network_interface_option import BatchCreateSubNetworkInterfaceOption
from huaweicloudsdkvpc.v3.model.batch_create_sub_network_interface_request import BatchCreateSubNetworkInterfaceRequest
from huaweicloudsdkvpc.v3.model.batch_create_sub_network_interface_request_body import BatchCreateSubNetworkInterfaceRequestBody
from huaweicloudsdkvpc.v3.model.batch_create_sub_network_interface_response import BatchCreateSubNetworkInterfaceResponse
from huaweicloudsdkvpc.v3.model.cloud_resource import CloudResource
from huaweicloudsdkvpc.v3.model.create_address_group_option import CreateAddressGroupOption
from huaweicloudsdkvpc.v3.model.create_address_group_request import CreateAddressGroupRequest
from huaweicloudsdkvpc.v3.model.create_address_group_request_body import CreateAddressGroupRequestBody
from huaweicloudsdkvpc.v3.model.create_address_group_response import CreateAddressGroupResponse
from huaweicloudsdkvpc.v3.model.create_firewall_option import CreateFirewallOption
from huaweicloudsdkvpc.v3.model.create_firewall_request import CreateFirewallRequest
from huaweicloudsdkvpc.v3.model.create_firewall_request_body import CreateFirewallRequestBody
from huaweicloudsdkvpc.v3.model.create_firewall_response import CreateFirewallResponse
from huaweicloudsdkvpc.v3.model.create_security_group_option import CreateSecurityGroupOption
from huaweicloudsdkvpc.v3.model.create_security_group_request import CreateSecurityGroupRequest
from huaweicloudsdkvpc.v3.model.create_security_group_request_body import CreateSecurityGroupRequestBody
from huaweicloudsdkvpc.v3.model.create_security_group_response import CreateSecurityGroupResponse
from huaweicloudsdkvpc.v3.model.create_security_group_rule_option import CreateSecurityGroupRuleOption
from huaweicloudsdkvpc.v3.model.create_security_group_rule_request import CreateSecurityGroupRuleRequest
from huaweicloudsdkvpc.v3.model.create_security_group_rule_request_body import CreateSecurityGroupRuleRequestBody
from huaweicloudsdkvpc.v3.model.create_security_group_rule_response import CreateSecurityGroupRuleResponse
from huaweicloudsdkvpc.v3.model.create_sub_network_interface_option import CreateSubNetworkInterfaceOption
from huaweicloudsdkvpc.v3.model.create_sub_network_interface_request import CreateSubNetworkInterfaceRequest
from huaweicloudsdkvpc.v3.model.create_sub_network_interface_request_body import CreateSubNetworkInterfaceRequestBody
from huaweicloudsdkvpc.v3.model.create_sub_network_interface_response import CreateSubNetworkInterfaceResponse
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_option import CreateTrafficMirrorFilterOption
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_request import CreateTrafficMirrorFilterRequest
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_request_body import CreateTrafficMirrorFilterRequestBody
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_response import CreateTrafficMirrorFilterResponse
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_rule_option import CreateTrafficMirrorFilterRuleOption
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_rule_request import CreateTrafficMirrorFilterRuleRequest
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_rule_request_body import CreateTrafficMirrorFilterRuleRequestBody
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_filter_rule_response import CreateTrafficMirrorFilterRuleResponse
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_session_option import CreateTrafficMirrorSessionOption
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_session_request import CreateTrafficMirrorSessionRequest
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_session_request_body import CreateTrafficMirrorSessionRequestBody
from huaweicloudsdkvpc.v3.model.create_traffic_mirror_session_response import CreateTrafficMirrorSessionResponse
from huaweicloudsdkvpc.v3.model.create_vpc_option import CreateVpcOption
from huaweicloudsdkvpc.v3.model.create_vpc_request import CreateVpcRequest
from huaweicloudsdkvpc.v3.model.create_vpc_request_body import CreateVpcRequestBody
from huaweicloudsdkvpc.v3.model.create_vpc_response import CreateVpcResponse
from huaweicloudsdkvpc.v3.model.delete_address_group_request import DeleteAddressGroupRequest
from huaweicloudsdkvpc.v3.model.delete_address_group_response import DeleteAddressGroupResponse
from huaweicloudsdkvpc.v3.model.delete_firewall_request import DeleteFirewallRequest
from huaweicloudsdkvpc.v3.model.delete_firewall_response import DeleteFirewallResponse
from huaweicloudsdkvpc.v3.model.delete_ip_address_group_force_request import DeleteIpAddressGroupForceRequest
from huaweicloudsdkvpc.v3.model.delete_ip_address_group_force_response import DeleteIpAddressGroupForceResponse
from huaweicloudsdkvpc.v3.model.delete_security_group_request import DeleteSecurityGroupRequest
from huaweicloudsdkvpc.v3.model.delete_security_group_response import DeleteSecurityGroupResponse
from huaweicloudsdkvpc.v3.model.delete_security_group_rule_request import DeleteSecurityGroupRuleRequest
from huaweicloudsdkvpc.v3.model.delete_security_group_rule_response import DeleteSecurityGroupRuleResponse
from huaweicloudsdkvpc.v3.model.delete_sub_network_interface_request import DeleteSubNetworkInterfaceRequest
from huaweicloudsdkvpc.v3.model.delete_sub_network_interface_response import DeleteSubNetworkInterfaceResponse
from huaweicloudsdkvpc.v3.model.delete_traffic_mirror_filter_request import DeleteTrafficMirrorFilterRequest
from huaweicloudsdkvpc.v3.model.delete_traffic_mirror_filter_response import DeleteTrafficMirrorFilterResponse
from huaweicloudsdkvpc.v3.model.delete_traffic_mirror_filter_rule_request import DeleteTrafficMirrorFilterRuleRequest
from huaweicloudsdkvpc.v3.model.delete_traffic_mirror_filter_rule_response import DeleteTrafficMirrorFilterRuleResponse
from huaweicloudsdkvpc.v3.model.delete_traffic_mirror_session_request import DeleteTrafficMirrorSessionRequest
from huaweicloudsdkvpc.v3.model.delete_traffic_mirror_session_response import DeleteTrafficMirrorSessionResponse
from huaweicloudsdkvpc.v3.model.delete_vpc_request import DeleteVpcRequest
from huaweicloudsdkvpc.v3.model.delete_vpc_response import DeleteVpcResponse
from huaweicloudsdkvpc.v3.model.disassociate_subnet_firewall_request import DisassociateSubnetFirewallRequest
from huaweicloudsdkvpc.v3.model.disassociate_subnet_firewall_request_body import DisassociateSubnetFirewallRequestBody
from huaweicloudsdkvpc.v3.model.disassociate_subnet_firewall_response import DisassociateSubnetFirewallResponse
from huaweicloudsdkvpc.v3.model.firewall_association import FirewallAssociation
from huaweicloudsdkvpc.v3.model.firewall_detail import FirewallDetail
from huaweicloudsdkvpc.v3.model.firewall_insert_rule_item_option import FirewallInsertRuleItemOption
from huaweicloudsdkvpc.v3.model.firewall_insert_rule_option import FirewallInsertRuleOption
from huaweicloudsdkvpc.v3.model.firewall_remove_rule_item_option import FirewallRemoveRuleItemOption
from huaweicloudsdkvpc.v3.model.firewall_remove_rule_option import FirewallRemoveRuleOption
from huaweicloudsdkvpc.v3.model.firewall_rule_detail import FirewallRuleDetail
from huaweicloudsdkvpc.v3.model.firewall_update_rule_item_option import FirewallUpdateRuleItemOption
from huaweicloudsdkvpc.v3.model.firewall_update_rule_option import FirewallUpdateRuleOption
from huaweicloudsdkvpc.v3.model.insert_security_group_option import InsertSecurityGroupOption
from huaweicloudsdkvpc.v3.model.list_address_group_request import ListAddressGroupRequest
from huaweicloudsdkvpc.v3.model.list_address_group_response import ListAddressGroupResponse
from huaweicloudsdkvpc.v3.model.list_firewall_detail import ListFirewallDetail
from huaweicloudsdkvpc.v3.model.list_firewall_request import ListFirewallRequest
from huaweicloudsdkvpc.v3.model.list_firewall_response import ListFirewallResponse
from huaweicloudsdkvpc.v3.model.list_security_group_rules_request import ListSecurityGroupRulesRequest
from huaweicloudsdkvpc.v3.model.list_security_group_rules_response import ListSecurityGroupRulesResponse
from huaweicloudsdkvpc.v3.model.list_security_groups_request import ListSecurityGroupsRequest
from huaweicloudsdkvpc.v3.model.list_security_groups_response import ListSecurityGroupsResponse
from huaweicloudsdkvpc.v3.model.list_sub_network_interfaces_request import ListSubNetworkInterfacesRequest
from huaweicloudsdkvpc.v3.model.list_sub_network_interfaces_response import ListSubNetworkInterfacesResponse
from huaweicloudsdkvpc.v3.model.list_traffic_mirror_filter_rules_request import ListTrafficMirrorFilterRulesRequest
from huaweicloudsdkvpc.v3.model.list_traffic_mirror_filter_rules_response import ListTrafficMirrorFilterRulesResponse
from huaweicloudsdkvpc.v3.model.list_traffic_mirror_filters_request import ListTrafficMirrorFiltersRequest
from huaweicloudsdkvpc.v3.model.list_traffic_mirror_filters_response import ListTrafficMirrorFiltersResponse
from huaweicloudsdkvpc.v3.model.list_traffic_mirror_sessions_request import ListTrafficMirrorSessionsRequest
from huaweicloudsdkvpc.v3.model.list_traffic_mirror_sessions_response import ListTrafficMirrorSessionsResponse
from huaweicloudsdkvpc.v3.model.list_vpcs_request import ListVpcsRequest
from huaweicloudsdkvpc.v3.model.list_vpcs_response import ListVpcsResponse
from huaweicloudsdkvpc.v3.model.migrate_sub_network_interface_option import MigrateSubNetworkInterfaceOption
from huaweicloudsdkvpc.v3.model.migrate_sub_network_interface_request import MigrateSubNetworkInterfaceRequest
from huaweicloudsdkvpc.v3.model.migrate_sub_network_interface_request_body import MigrateSubNetworkInterfaceRequestBody
from huaweicloudsdkvpc.v3.model.migrate_sub_network_interface_response import MigrateSubNetworkInterfaceResponse
from huaweicloudsdkvpc.v3.model.page_info import PageInfo
from huaweicloudsdkvpc.v3.model.port import Port
from huaweicloudsdkvpc.v3.model.private_ip_info import PrivateIpInfo
from huaweicloudsdkvpc.v3.model.remove_extend_cidr_option import RemoveExtendCidrOption
from huaweicloudsdkvpc.v3.model.remove_firewall_rules_request import RemoveFirewallRulesRequest
from huaweicloudsdkvpc.v3.model.remove_firewall_rules_request_body import RemoveFirewallRulesRequestBody
from huaweicloudsdkvpc.v3.model.remove_firewall_rules_response import RemoveFirewallRulesResponse
from huaweicloudsdkvpc.v3.model.remove_security_group_option import RemoveSecurityGroupOption
from huaweicloudsdkvpc.v3.model.remove_security_groups_request import RemoveSecurityGroupsRequest
from huaweicloudsdkvpc.v3.model.remove_security_groups_request_body import RemoveSecurityGroupsRequestBody
from huaweicloudsdkvpc.v3.model.remove_security_groups_response import RemoveSecurityGroupsResponse
from huaweicloudsdkvpc.v3.model.remove_sources_from_traffic_mirror_session_request import RemoveSourcesFromTrafficMirrorSessionRequest
from huaweicloudsdkvpc.v3.model.remove_sources_from_traffic_mirror_session_request_body import RemoveSourcesFromTrafficMirrorSessionRequestBody
from huaweicloudsdkvpc.v3.model.remove_sources_from_traffic_mirror_session_response import RemoveSourcesFromTrafficMirrorSessionResponse
from huaweicloudsdkvpc.v3.model.remove_vpc_extend_cidr_request import RemoveVpcExtendCidrRequest
from huaweicloudsdkvpc.v3.model.remove_vpc_extend_cidr_request_body import RemoveVpcExtendCidrRequestBody
from huaweicloudsdkvpc.v3.model.remove_vpc_extend_cidr_response import RemoveVpcExtendCidrResponse
from huaweicloudsdkvpc.v3.model.resource_tag import ResourceTag
from huaweicloudsdkvpc.v3.model.security_group import SecurityGroup
from huaweicloudsdkvpc.v3.model.security_group_info import SecurityGroupInfo
from huaweicloudsdkvpc.v3.model.security_group_rule import SecurityGroupRule
from huaweicloudsdkvpc.v3.model.show_address_group_request import ShowAddressGroupRequest
from huaweicloudsdkvpc.v3.model.show_address_group_response import ShowAddressGroupResponse
from huaweicloudsdkvpc.v3.model.show_firewall_request import ShowFirewallRequest
from huaweicloudsdkvpc.v3.model.show_firewall_response import ShowFirewallResponse
from huaweicloudsdkvpc.v3.model.show_security_group_request import ShowSecurityGroupRequest
from huaweicloudsdkvpc.v3.model.show_security_group_response import ShowSecurityGroupResponse
from huaweicloudsdkvpc.v3.model.show_security_group_rule_request import ShowSecurityGroupRuleRequest
from huaweicloudsdkvpc.v3.model.show_security_group_rule_response import ShowSecurityGroupRuleResponse
from huaweicloudsdkvpc.v3.model.show_sub_network_interface_request import ShowSubNetworkInterfaceRequest
from huaweicloudsdkvpc.v3.model.show_sub_network_interface_response import ShowSubNetworkInterfaceResponse
from huaweicloudsdkvpc.v3.model.show_sub_network_interfaces_quantity_request import ShowSubNetworkInterfacesQuantityRequest
from huaweicloudsdkvpc.v3.model.show_sub_network_interfaces_quantity_response import ShowSubNetworkInterfacesQuantityResponse
from huaweicloudsdkvpc.v3.model.show_traffic_mirror_filter_request import ShowTrafficMirrorFilterRequest
from huaweicloudsdkvpc.v3.model.show_traffic_mirror_filter_response import ShowTrafficMirrorFilterResponse
from huaweicloudsdkvpc.v3.model.show_traffic_mirror_filter_rule_request import ShowTrafficMirrorFilterRuleRequest
from huaweicloudsdkvpc.v3.model.show_traffic_mirror_filter_rule_response import ShowTrafficMirrorFilterRuleResponse
from huaweicloudsdkvpc.v3.model.show_traffic_mirror_session_request import ShowTrafficMirrorSessionRequest
from huaweicloudsdkvpc.v3.model.show_traffic_mirror_session_response import ShowTrafficMirrorSessionResponse
from huaweicloudsdkvpc.v3.model.show_vpc_request import ShowVpcRequest
from huaweicloudsdkvpc.v3.model.show_vpc_response import ShowVpcResponse
from huaweicloudsdkvpc.v3.model.sub_network_interface import SubNetworkInterface
from huaweicloudsdkvpc.v3.model.tag import Tag
from huaweicloudsdkvpc.v3.model.traffic_mirror_filter import TrafficMirrorFilter
from huaweicloudsdkvpc.v3.model.traffic_mirror_filter_rule import TrafficMirrorFilterRule
from huaweicloudsdkvpc.v3.model.traffic_mirror_session import TrafficMirrorSession
from huaweicloudsdkvpc.v3.model.traffic_mirror_sources_option import TrafficMirrorSourcesOption
from huaweicloudsdkvpc.v3.model.update_address_group_option import UpdateAddressGroupOption
from huaweicloudsdkvpc.v3.model.update_address_group_request import UpdateAddressGroupRequest
from huaweicloudsdkvpc.v3.model.update_address_group_request_body import UpdateAddressGroupRequestBody
from huaweicloudsdkvpc.v3.model.update_address_group_response import UpdateAddressGroupResponse
from huaweicloudsdkvpc.v3.model.update_firewall_option import UpdateFirewallOption
from huaweicloudsdkvpc.v3.model.update_firewall_request import UpdateFirewallRequest
from huaweicloudsdkvpc.v3.model.update_firewall_request_body import UpdateFirewallRequestBody
from huaweicloudsdkvpc.v3.model.update_firewall_response import UpdateFirewallResponse
from huaweicloudsdkvpc.v3.model.update_firewall_rules_request import UpdateFirewallRulesRequest
from huaweicloudsdkvpc.v3.model.update_firewall_rules_request_body import UpdateFirewallRulesRequestBody
from huaweicloudsdkvpc.v3.model.update_firewall_rules_response import UpdateFirewallRulesResponse
from huaweicloudsdkvpc.v3.model.update_security_group_option import UpdateSecurityGroupOption
from huaweicloudsdkvpc.v3.model.update_security_group_request import UpdateSecurityGroupRequest
from huaweicloudsdkvpc.v3.model.update_security_group_request_body import UpdateSecurityGroupRequestBody
from huaweicloudsdkvpc.v3.model.update_security_group_response import UpdateSecurityGroupResponse
from huaweicloudsdkvpc.v3.model.update_sub_network_interface_option import UpdateSubNetworkInterfaceOption
from huaweicloudsdkvpc.v3.model.update_sub_network_interface_request import UpdateSubNetworkInterfaceRequest
from huaweicloudsdkvpc.v3.model.update_sub_network_interface_request_body import UpdateSubNetworkInterfaceRequestBody
from huaweicloudsdkvpc.v3.model.update_sub_network_interface_response import UpdateSubNetworkInterfaceResponse
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_option import UpdateTrafficMirrorFilterOption
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_request import UpdateTrafficMirrorFilterRequest
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_request_body import UpdateTrafficMirrorFilterRequestBody
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_response import UpdateTrafficMirrorFilterResponse
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_rule_option import UpdateTrafficMirrorFilterRuleOption
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_rule_request import UpdateTrafficMirrorFilterRuleRequest
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_rule_request_body import UpdateTrafficMirrorFilterRuleRequestBody
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_filter_rule_response import UpdateTrafficMirrorFilterRuleResponse
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_session_option import UpdateTrafficMirrorSessionOption
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_session_request import UpdateTrafficMirrorSessionRequest
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_session_request_body import UpdateTrafficMirrorSessionRequestBody
from huaweicloudsdkvpc.v3.model.update_traffic_mirror_session_response import UpdateTrafficMirrorSessionResponse
from huaweicloudsdkvpc.v3.model.update_vpc_option import UpdateVpcOption
from huaweicloudsdkvpc.v3.model.update_vpc_request import UpdateVpcRequest
from huaweicloudsdkvpc.v3.model.update_vpc_request_body import UpdateVpcRequestBody
from huaweicloudsdkvpc.v3.model.update_vpc_response import UpdateVpcResponse
from huaweicloudsdkvpc.v3.model.vpc import Vpc

