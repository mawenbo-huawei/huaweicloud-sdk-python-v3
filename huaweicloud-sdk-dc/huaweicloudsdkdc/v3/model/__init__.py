# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkdc.v3.model.add_gdgw_route_action import AddGdgwRouteAction
from huaweicloudsdkdc.v3.model.address_body import AddressBody
from huaweicloudsdkdc.v3.model.address_family import AddressFamily
from huaweicloudsdkdc.v3.model.band_width_info import BandWidthInfo
from huaweicloudsdkdc.v3.model.bandwidth_info_external import BandwidthInfoExternal
from huaweicloudsdkdc.v3.model.base_add_route_action import BaseAddRouteAction
from huaweicloudsdkdc.v3.model.base_delete_route_action import BaseDeleteRouteAction
from huaweicloudsdkdc.v3.model.batch_create_resource_tags_request import BatchCreateResourceTagsRequest
from huaweicloudsdkdc.v3.model.batch_create_resource_tags_response import BatchCreateResourceTagsResponse
from huaweicloudsdkdc.v3.model.batch_operate_resource_tags_request_body import BatchOperateResourceTagsRequestBody
from huaweicloudsdkdc.v3.model.bind_global_eips_request import BindGlobalEipsRequest
from huaweicloudsdkdc.v3.model.bind_global_eips_response import BindGlobalEipsResponse
from huaweicloudsdkdc.v3.model.binding_geip_body import BindingGeipBody
from huaweicloudsdkdc.v3.model.common_routetable import CommonRoutetable
from huaweicloudsdkdc.v3.model.connect_gateway_response import ConnectGatewayResponse
from huaweicloudsdkdc.v3.model.create_binding_geip_request_body import CreateBindingGeipRequestBody
from huaweicloudsdkdc.v3.model.create_connect_gateway import CreateConnectGateway
from huaweicloudsdkdc.v3.model.create_connect_gateway_request import CreateConnectGatewayRequest
from huaweicloudsdkdc.v3.model.create_connect_gateway_request_body import CreateConnectGatewayRequestBody
from huaweicloudsdkdc.v3.model.create_connect_gateway_response import CreateConnectGatewayResponse
from huaweicloudsdkdc.v3.model.create_external_peer_link_request_body import CreateExternalPeerLinkRequestBody
from huaweicloudsdkdc.v3.model.create_external_peer_link_request_body_peer_link import CreateExternalPeerLinkRequestBodyPeerLink
from huaweicloudsdkdc.v3.model.create_external_peer_link_request_body_peer_link_peer_site import CreateExternalPeerLinkRequestBodyPeerLinkPeerSite
from huaweicloudsdkdc.v3.model.create_global_dc_gateway import CreateGlobalDcGateway
from huaweicloudsdkdc.v3.model.create_global_dc_gateway_entry import CreateGlobalDcGatewayEntry
from huaweicloudsdkdc.v3.model.create_global_dc_gateway_request import CreateGlobalDcGatewayRequest
from huaweicloudsdkdc.v3.model.create_global_dc_gateway_request_body import CreateGlobalDcGatewayRequestBody
from huaweicloudsdkdc.v3.model.create_global_dc_gateway_response import CreateGlobalDcGatewayResponse
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect import CreateHostedDirectConnect
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect_request import CreateHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect_request_body import CreateHostedDirectConnectRequestBody
from huaweicloudsdkdc.v3.model.create_hosted_direct_connect_response import CreateHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.create_peer_link_request import CreatePeerLinkRequest
from huaweicloudsdkdc.v3.model.create_peer_link_response import CreatePeerLinkResponse
from huaweicloudsdkdc.v3.model.create_resource_tag_request import CreateResourceTagRequest
from huaweicloudsdkdc.v3.model.create_resource_tag_request_body import CreateResourceTagRequestBody
from huaweicloudsdkdc.v3.model.create_resource_tag_response import CreateResourceTagResponse
from huaweicloudsdkdc.v3.model.create_switchover_test import CreateSwitchoverTest
from huaweicloudsdkdc.v3.model.create_switchover_test_request_body import CreateSwitchoverTestRequestBody
from huaweicloudsdkdc.v3.model.create_unbinding_geip_request_body import CreateUnbindingGeipRequestBody
from huaweicloudsdkdc.v3.model.create_vif_peer import CreateVifPeer
from huaweicloudsdkdc.v3.model.create_vif_peer_request import CreateVifPeerRequest
from huaweicloudsdkdc.v3.model.create_vif_peer_request_body import CreateVifPeerRequestBody
from huaweicloudsdkdc.v3.model.create_vif_peer_response import CreateVifPeerResponse
from huaweicloudsdkdc.v3.model.create_virtual_gateway import CreateVirtualGateway
from huaweicloudsdkdc.v3.model.create_virtual_gateway_request import CreateVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.create_virtual_gateway_request_body import CreateVirtualGatewayRequestBody
from huaweicloudsdkdc.v3.model.create_virtual_gateway_response import CreateVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.create_virtual_interface import CreateVirtualInterface
from huaweicloudsdkdc.v3.model.create_virtual_interface_request import CreateVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.create_virtual_interface_request_body import CreateVirtualInterfaceRequestBody
from huaweicloudsdkdc.v3.model.create_virtual_interface_response import CreateVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.delete_connect_gateway_request import DeleteConnectGatewayRequest
from huaweicloudsdkdc.v3.model.delete_connect_gateway_response import DeleteConnectGatewayResponse
from huaweicloudsdkdc.v3.model.delete_direct_connect_request import DeleteDirectConnectRequest
from huaweicloudsdkdc.v3.model.delete_direct_connect_response import DeleteDirectConnectResponse
from huaweicloudsdkdc.v3.model.delete_gdgw_route_action import DeleteGdgwRouteAction
from huaweicloudsdkdc.v3.model.delete_global_dc_gateway_request import DeleteGlobalDcGatewayRequest
from huaweicloudsdkdc.v3.model.delete_global_dc_gateway_response import DeleteGlobalDcGatewayResponse
from huaweicloudsdkdc.v3.model.delete_hosted_direct_connect_request import DeleteHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.delete_hosted_direct_connect_response import DeleteHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.delete_peer_link_request import DeletePeerLinkRequest
from huaweicloudsdkdc.v3.model.delete_peer_link_response import DeletePeerLinkResponse
from huaweicloudsdkdc.v3.model.delete_resource_tag_request import DeleteResourceTagRequest
from huaweicloudsdkdc.v3.model.delete_resource_tag_response import DeleteResourceTagResponse
from huaweicloudsdkdc.v3.model.delete_vif_peer_request import DeleteVifPeerRequest
from huaweicloudsdkdc.v3.model.delete_vif_peer_response import DeleteVifPeerResponse
from huaweicloudsdkdc.v3.model.delete_virtual_gateway_request import DeleteVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.delete_virtual_gateway_response import DeleteVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.delete_virtual_interface_request import DeleteVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.delete_virtual_interface_response import DeleteVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.direct_connect import DirectConnect
from huaweicloudsdkdc.v3.model.direct_connect_location_entry import DirectConnectLocationEntry
from huaweicloudsdkdc.v3.model.external_create_peer_link import ExternalCreatePeerLink
from huaweicloudsdkdc.v3.model.external_update_peer_link import ExternalUpdatePeerLink
from huaweicloudsdkdc.v3.model.gdgw_route_table_request import GdgwRouteTableRequest
from huaweicloudsdkdc.v3.model.global_dc_gateway_entry import GlobalDcGatewayEntry
from huaweicloudsdkdc.v3.model.global_dc_gateway_status import GlobalDcGatewayStatus
from huaweicloudsdkdc.v3.model.hosted_direct_connect import HostedDirectConnect
from huaweicloudsdkdc.v3.model.info import Info
from huaweicloudsdkdc.v3.model.list_binding_geip import ListBindingGeip
from huaweicloudsdkdc.v3.model.list_connect_gateways_request import ListConnectGatewaysRequest
from huaweicloudsdkdc.v3.model.list_connect_gateways_response import ListConnectGatewaysResponse
from huaweicloudsdkdc.v3.model.list_direct_connect_locations_request import ListDirectConnectLocationsRequest
from huaweicloudsdkdc.v3.model.list_direct_connect_locations_response import ListDirectConnectLocationsResponse
from huaweicloudsdkdc.v3.model.list_direct_connects_request import ListDirectConnectsRequest
from huaweicloudsdkdc.v3.model.list_direct_connects_response import ListDirectConnectsResponse
from huaweicloudsdkdc.v3.model.list_gdgw_route_tables_request import ListGdgwRouteTablesRequest
from huaweicloudsdkdc.v3.model.list_gdgw_route_tables_response import ListGdgwRouteTablesResponse
from huaweicloudsdkdc.v3.model.list_global_dc_gateways_request import ListGlobalDcGatewaysRequest
from huaweicloudsdkdc.v3.model.list_global_dc_gateways_response import ListGlobalDcGatewaysResponse
from huaweicloudsdkdc.v3.model.list_global_eips_request import ListGlobalEipsRequest
from huaweicloudsdkdc.v3.model.list_global_eips_response import ListGlobalEipsResponse
from huaweicloudsdkdc.v3.model.list_hosted_direct_connects_request import ListHostedDirectConnectsRequest
from huaweicloudsdkdc.v3.model.list_hosted_direct_connects_response import ListHostedDirectConnectsResponse
from huaweicloudsdkdc.v3.model.list_peer_links_request import ListPeerLinksRequest
from huaweicloudsdkdc.v3.model.list_peer_links_response import ListPeerLinksResponse
from huaweicloudsdkdc.v3.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkdc.v3.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkdc.v3.model.list_switchover_test_records_request import ListSwitchoverTestRecordsRequest
from huaweicloudsdkdc.v3.model.list_switchover_test_records_response import ListSwitchoverTestRecordsResponse
from huaweicloudsdkdc.v3.model.list_tag_resource_instances_request import ListTagResourceInstancesRequest
from huaweicloudsdkdc.v3.model.list_tag_resource_instances_request_body import ListTagResourceInstancesRequestBody
from huaweicloudsdkdc.v3.model.list_tag_resource_instances_response import ListTagResourceInstancesResponse
from huaweicloudsdkdc.v3.model.list_virtual_gateways_request import ListVirtualGatewaysRequest
from huaweicloudsdkdc.v3.model.list_virtual_gateways_response import ListVirtualGatewaysResponse
from huaweicloudsdkdc.v3.model.list_virtual_interfaces_request import ListVirtualInterfacesRequest
from huaweicloudsdkdc.v3.model.list_virtual_interfaces_response import ListVirtualInterfacesResponse
from huaweicloudsdkdc.v3.model.locales_body import LocalesBody
from huaweicloudsdkdc.v3.model.match import Match
from huaweicloudsdkdc.v3.model.page_info import PageInfo
from huaweicloudsdkdc.v3.model.peer_link_entry import PeerLinkEntry
from huaweicloudsdkdc.v3.model.peer_link_status import PeerLinkStatus
from huaweicloudsdkdc.v3.model.peer_site import PeerSite
from huaweicloudsdkdc.v3.model.peer_site_external import PeerSiteExternal
from huaweicloudsdkdc.v3.model.provider_response_body import ProviderResponseBody
from huaweicloudsdkdc.v3.model.provider_value_body import ProviderValueBody
from huaweicloudsdkdc.v3.model.resource import Resource
from huaweicloudsdkdc.v3.model.route_description import RouteDescription
from huaweicloudsdkdc.v3.model.route_destination import RouteDestination
from huaweicloudsdkdc.v3.model.route_next_hop import RouteNextHop
from huaweicloudsdkdc.v3.model.route_type_of_gdgw import RouteTypeOfGdgw
from huaweicloudsdkdc.v3.model.show_connect_gateway_request import ShowConnectGatewayRequest
from huaweicloudsdkdc.v3.model.show_connect_gateway_response import ShowConnectGatewayResponse
from huaweicloudsdkdc.v3.model.show_direct_connect_location_request import ShowDirectConnectLocationRequest
from huaweicloudsdkdc.v3.model.show_direct_connect_location_response import ShowDirectConnectLocationResponse
from huaweicloudsdkdc.v3.model.show_direct_connect_request import ShowDirectConnectRequest
from huaweicloudsdkdc.v3.model.show_direct_connect_response import ShowDirectConnectResponse
from huaweicloudsdkdc.v3.model.show_gdgw_routetable import ShowGdgwRoutetable
from huaweicloudsdkdc.v3.model.show_global_dc_gateway_request import ShowGlobalDcGatewayRequest
from huaweicloudsdkdc.v3.model.show_global_dc_gateway_response import ShowGlobalDcGatewayResponse
from huaweicloudsdkdc.v3.model.show_hosted_direct_connect_request import ShowHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.show_hosted_direct_connect_response import ShowHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.show_peer_link_request import ShowPeerLinkRequest
from huaweicloudsdkdc.v3.model.show_peer_link_response import ShowPeerLinkResponse
from huaweicloudsdkdc.v3.model.show_quotas_request import ShowQuotasRequest
from huaweicloudsdkdc.v3.model.show_quotas_response import ShowQuotasResponse
from huaweicloudsdkdc.v3.model.show_quotas_response_body_quotas import ShowQuotasResponseBodyQuotas
from huaweicloudsdkdc.v3.model.show_resource_tag_request import ShowResourceTagRequest
from huaweicloudsdkdc.v3.model.show_resource_tag_response import ShowResourceTagResponse
from huaweicloudsdkdc.v3.model.show_virtual_gateway_request import ShowVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.show_virtual_gateway_response import ShowVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.show_virtual_interface_request import ShowVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.show_virtual_interface_response import ShowVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.switchover_test_record import SwitchoverTestRecord
from huaweicloudsdkdc.v3.model.switchover_test_request import SwitchoverTestRequest
from huaweicloudsdkdc.v3.model.switchover_test_response import SwitchoverTestResponse
from huaweicloudsdkdc.v3.model.tag import Tag
from huaweicloudsdkdc.v3.model.tags import Tags
from huaweicloudsdkdc.v3.model.tenant_id_def import TenantIdDef
from huaweicloudsdkdc.v3.model.unbind_global_eips_request import UnbindGlobalEipsRequest
from huaweicloudsdkdc.v3.model.unbind_global_eips_response import UnbindGlobalEipsResponse
from huaweicloudsdkdc.v3.model.unbinding_geip_body import UnbindingGeipBody
from huaweicloudsdkdc.v3.model.update_connect_gateway import UpdateConnectGateway
from huaweicloudsdkdc.v3.model.update_connect_gateway_request import UpdateConnectGatewayRequest
from huaweicloudsdkdc.v3.model.update_connect_gateway_request_body import UpdateConnectGatewayRequestBody
from huaweicloudsdkdc.v3.model.update_connect_gateway_response import UpdateConnectGatewayResponse
from huaweicloudsdkdc.v3.model.update_direct_connect import UpdateDirectConnect
from huaweicloudsdkdc.v3.model.update_direct_connect_request import UpdateDirectConnectRequest
from huaweicloudsdkdc.v3.model.update_direct_connect_request_body import UpdateDirectConnectRequestBody
from huaweicloudsdkdc.v3.model.update_direct_connect_response import UpdateDirectConnectResponse
from huaweicloudsdkdc.v3.model.update_external_peer_link_request_body import UpdateExternalPeerLinkRequestBody
from huaweicloudsdkdc.v3.model.update_external_peer_link_request_body_peer_link import UpdateExternalPeerLinkRequestBodyPeerLink
from huaweicloudsdkdc.v3.model.update_gdgw_route_table_request import UpdateGdgwRouteTableRequest
from huaweicloudsdkdc.v3.model.update_gdgw_route_table_response import UpdateGdgwRouteTableResponse
from huaweicloudsdkdc.v3.model.update_gdgw_routetable_request_body import UpdateGdgwRoutetableRequestBody
from huaweicloudsdkdc.v3.model.update_global_dc_gateway import UpdateGlobalDcGateway
from huaweicloudsdkdc.v3.model.update_global_dc_gateway_request import UpdateGlobalDcGatewayRequest
from huaweicloudsdkdc.v3.model.update_global_dc_gateway_request_body import UpdateGlobalDcGatewayRequestBody
from huaweicloudsdkdc.v3.model.update_global_dc_gateway_response import UpdateGlobalDcGatewayResponse
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect import UpdateHostedDirectConnect
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect_request import UpdateHostedDirectConnectRequest
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect_request_body import UpdateHostedDirectConnectRequestBody
from huaweicloudsdkdc.v3.model.update_hosted_direct_connect_response import UpdateHostedDirectConnectResponse
from huaweicloudsdkdc.v3.model.update_peer_link_request import UpdatePeerLinkRequest
from huaweicloudsdkdc.v3.model.update_peer_link_response import UpdatePeerLinkResponse
from huaweicloudsdkdc.v3.model.update_route_action import UpdateRouteAction
from huaweicloudsdkdc.v3.model.update_vif_peer import UpdateVifPeer
from huaweicloudsdkdc.v3.model.update_vif_peer_request import UpdateVifPeerRequest
from huaweicloudsdkdc.v3.model.update_vif_peer_request_body import UpdateVifPeerRequestBody
from huaweicloudsdkdc.v3.model.update_vif_peer_response import UpdateVifPeerResponse
from huaweicloudsdkdc.v3.model.update_virtual_gateway import UpdateVirtualGateway
from huaweicloudsdkdc.v3.model.update_virtual_gateway_request import UpdateVirtualGatewayRequest
from huaweicloudsdkdc.v3.model.update_virtual_gateway_request_body import UpdateVirtualGatewayRequestBody
from huaweicloudsdkdc.v3.model.update_virtual_gateway_response import UpdateVirtualGatewayResponse
from huaweicloudsdkdc.v3.model.update_virtual_interface import UpdateVirtualInterface
from huaweicloudsdkdc.v3.model.update_virtual_interface_request import UpdateVirtualInterfaceRequest
from huaweicloudsdkdc.v3.model.update_virtual_interface_request_body import UpdateVirtualInterfaceRequestBody
from huaweicloudsdkdc.v3.model.update_virtual_interface_response import UpdateVirtualInterfaceResponse
from huaweicloudsdkdc.v3.model.vif_extend_attribute import VifExtendAttribute
from huaweicloudsdkdc.v3.model.vif_peer import VifPeer
from huaweicloudsdkdc.v3.model.virtual_gateway import VirtualGateway
from huaweicloudsdkdc.v3.model.virtual_interface import VirtualInterface
