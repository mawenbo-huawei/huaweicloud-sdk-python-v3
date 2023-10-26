# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkcc.v3.model.apply_central_network_policy_request import ApplyCentralNetworkPolicyRequest
from huaweicloudsdkcc.v3.model.apply_central_network_policy_response import ApplyCentralNetworkPolicyResponse
from huaweicloudsdkcc.v3.model.approved_state_enum import ApprovedStateEnum
from huaweicloudsdkcc.v3.model.area_id_def import AreaIdDef
from huaweicloudsdkcc.v3.model.asn import Asn
from huaweicloudsdkcc.v3.model.associate_bandwidth_package import AssociateBandwidthPackage
from huaweicloudsdkcc.v3.model.associate_bandwidth_package_request import AssociateBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.associate_bandwidth_package_request_body import AssociateBandwidthPackageRequestBody
from huaweicloudsdkcc.v3.model.associate_bandwidth_package_response import AssociateBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.associate_er_instance_document import AssociateErInstanceDocument
from huaweicloudsdkcc.v3.model.associate_er_table_document import AssociateErTableDocument
from huaweicloudsdkcc.v3.model.attachment_instance_id import AttachmentInstanceId
from huaweicloudsdkcc.v3.model.attachment_instance_type import AttachmentInstanceType
from huaweicloudsdkcc.v3.model.attachment_instance_type_enum import AttachmentInstanceTypeEnum
from huaweicloudsdkcc.v3.model.authorisation import Authorisation
from huaweicloudsdkcc.v3.model.bandwidth_package import BandwidthPackage
from huaweicloudsdkcc.v3.model.bandwidth_package_id import BandwidthPackageId
from huaweicloudsdkcc.v3.model.bandwidth_size import BandwidthSize
from huaweicloudsdkcc.v3.model.bandwidth_size_define import BandwidthSizeDefine
from huaweicloudsdkcc.v3.model.bandwidth_type import BandwidthType
from huaweicloudsdkcc.v3.model.bandwidth_type_enum import BandwidthTypeEnum
from huaweicloudsdkcc.v3.model.billing_mode import BillingMode
from huaweicloudsdkcc.v3.model.billing_mode_enum import BillingModeEnum
from huaweicloudsdkcc.v3.model.central_network import CentralNetwork
from huaweicloudsdkcc.v3.model.central_network_attachment import CentralNetworkAttachment
from huaweicloudsdkcc.v3.model.central_network_attachment_specification_value_info import CentralNetworkAttachmentSpecificationValueInfo
from huaweicloudsdkcc.v3.model.central_network_capability import CentralNetworkCapability
from huaweicloudsdkcc.v3.model.central_network_capability_enum import CentralNetworkCapabilityEnum
from huaweicloudsdkcc.v3.model.central_network_connection import CentralNetworkConnection
from huaweicloudsdkcc.v3.model.central_network_connection_info import CentralNetworkConnectionInfo
from huaweicloudsdkcc.v3.model.central_network_connection_state import CentralNetworkConnectionState
from huaweicloudsdkcc.v3.model.central_network_connection_state_enum import CentralNetworkConnectionStateEnum
from huaweicloudsdkcc.v3.model.central_network_element_change import CentralNetworkElementChange
from huaweicloudsdkcc.v3.model.central_network_er_instance import CentralNetworkErInstance
from huaweicloudsdkcc.v3.model.central_network_gdgw_attachment import CentralNetworkGdgwAttachment
from huaweicloudsdkcc.v3.model.central_network_id import CentralNetworkId
from huaweicloudsdkcc.v3.model.central_network_plane import CentralNetworkPlane
from huaweicloudsdkcc.v3.model.central_network_plane_document import CentralNetworkPlaneDocument
from huaweicloudsdkcc.v3.model.central_network_plane_id import CentralNetworkPlaneId
from huaweicloudsdkcc.v3.model.central_network_policy import CentralNetworkPolicy
from huaweicloudsdkcc.v3.model.central_network_policy_document import CentralNetworkPolicyDocument
from huaweicloudsdkcc.v3.model.central_network_policy_state import CentralNetworkPolicyState
from huaweicloudsdkcc.v3.model.central_network_policy_state_enum import CentralNetworkPolicyStateEnum
from huaweicloudsdkcc.v3.model.central_network_quota import CentralNetworkQuota
from huaweicloudsdkcc.v3.model.central_network_quota_key import CentralNetworkQuotaKey
from huaweicloudsdkcc.v3.model.central_network_quota_key_enum import CentralNetworkQuotaKeyEnum
from huaweicloudsdkcc.v3.model.central_network_state import CentralNetworkState
from huaweicloudsdkcc.v3.model.central_network_state_enum import CentralNetworkStateEnum
from huaweicloudsdkcc.v3.model.cloud_connection import CloudConnection
from huaweicloudsdkcc.v3.model.cloud_connection_id import CloudConnectionId
from huaweicloudsdkcc.v3.model.cloud_connection_quota import CloudConnectionQuota
from huaweicloudsdkcc.v3.model.cloud_connection_route import CloudConnectionRoute
from huaweicloudsdkcc.v3.model.connection_point import ConnectionPoint
from huaweicloudsdkcc.v3.model.connection_point_pair import ConnectionPointPair
from huaweicloudsdkcc.v3.model.connection_point_type_enum import ConnectionPointTypeEnum
from huaweicloudsdkcc.v3.model.connection_type import ConnectionType
from huaweicloudsdkcc.v3.model.connection_type_enum import ConnectionTypeEnum
from huaweicloudsdkcc.v3.model.create_authorisation import CreateAuthorisation
from huaweicloudsdkcc.v3.model.create_authorisation_request import CreateAuthorisationRequest
from huaweicloudsdkcc.v3.model.create_authorisation_request_body import CreateAuthorisationRequestBody
from huaweicloudsdkcc.v3.model.create_authorisation_response import CreateAuthorisationResponse
from huaweicloudsdkcc.v3.model.create_bandwidth_package import CreateBandwidthPackage
from huaweicloudsdkcc.v3.model.create_bandwidth_package_request import CreateBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.create_bandwidth_package_request_body import CreateBandwidthPackageRequestBody
from huaweicloudsdkcc.v3.model.create_bandwidth_package_response import CreateBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.create_central_network import CreateCentralNetwork
from huaweicloudsdkcc.v3.model.create_central_network_gdgw_attachment import CreateCentralNetworkGdgwAttachment
from huaweicloudsdkcc.v3.model.create_central_network_gdgw_attachment_request import CreateCentralNetworkGdgwAttachmentRequest
from huaweicloudsdkcc.v3.model.create_central_network_gdgw_attachment_request_body import CreateCentralNetworkGdgwAttachmentRequestBody
from huaweicloudsdkcc.v3.model.create_central_network_gdgw_attachment_response import CreateCentralNetworkGdgwAttachmentResponse
from huaweicloudsdkcc.v3.model.create_central_network_policy_request import CreateCentralNetworkPolicyRequest
from huaweicloudsdkcc.v3.model.create_central_network_policy_request_body import CreateCentralNetworkPolicyRequestBody
from huaweicloudsdkcc.v3.model.create_central_network_policy_response import CreateCentralNetworkPolicyResponse
from huaweicloudsdkcc.v3.model.create_central_network_request import CreateCentralNetworkRequest
from huaweicloudsdkcc.v3.model.create_central_network_request_body import CreateCentralNetworkRequestBody
from huaweicloudsdkcc.v3.model.create_central_network_response import CreateCentralNetworkResponse
from huaweicloudsdkcc.v3.model.create_cloud_connection import CreateCloudConnection
from huaweicloudsdkcc.v3.model.create_cloud_connection_request import CreateCloudConnectionRequest
from huaweicloudsdkcc.v3.model.create_cloud_connection_request_body import CreateCloudConnectionRequestBody
from huaweicloudsdkcc.v3.model.create_cloud_connection_response import CreateCloudConnectionResponse
from huaweicloudsdkcc.v3.model.create_inter_region_bandwidth import CreateInterRegionBandwidth
from huaweicloudsdkcc.v3.model.create_inter_region_bandwidth_request import CreateInterRegionBandwidthRequest
from huaweicloudsdkcc.v3.model.create_inter_region_bandwidth_request_body import CreateInterRegionBandwidthRequestBody
from huaweicloudsdkcc.v3.model.create_inter_region_bandwidth_response import CreateInterRegionBandwidthResponse
from huaweicloudsdkcc.v3.model.create_network_instance import CreateNetworkInstance
from huaweicloudsdkcc.v3.model.create_network_instance_request import CreateNetworkInstanceRequest
from huaweicloudsdkcc.v3.model.create_network_instance_request_body import CreateNetworkInstanceRequestBody
from huaweicloudsdkcc.v3.model.create_network_instance_response import CreateNetworkInstanceResponse
from huaweicloudsdkcc.v3.model.created_at import CreatedAt
from huaweicloudsdkcc.v3.model.delete_authorisation_request import DeleteAuthorisationRequest
from huaweicloudsdkcc.v3.model.delete_authorisation_response import DeleteAuthorisationResponse
from huaweicloudsdkcc.v3.model.delete_bandwidth_package_request import DeleteBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.delete_bandwidth_package_response import DeleteBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.delete_central_network_attachment_request import DeleteCentralNetworkAttachmentRequest
from huaweicloudsdkcc.v3.model.delete_central_network_attachment_response import DeleteCentralNetworkAttachmentResponse
from huaweicloudsdkcc.v3.model.delete_central_network_policy_request import DeleteCentralNetworkPolicyRequest
from huaweicloudsdkcc.v3.model.delete_central_network_policy_response import DeleteCentralNetworkPolicyResponse
from huaweicloudsdkcc.v3.model.delete_central_network_request import DeleteCentralNetworkRequest
from huaweicloudsdkcc.v3.model.delete_central_network_response import DeleteCentralNetworkResponse
from huaweicloudsdkcc.v3.model.delete_cloud_connection_request import DeleteCloudConnectionRequest
from huaweicloudsdkcc.v3.model.delete_cloud_connection_response import DeleteCloudConnectionResponse
from huaweicloudsdkcc.v3.model.delete_inter_region_bandwidth_request import DeleteInterRegionBandwidthRequest
from huaweicloudsdkcc.v3.model.delete_inter_region_bandwidth_response import DeleteInterRegionBandwidthResponse
from huaweicloudsdkcc.v3.model.delete_network_instance_request import DeleteNetworkInstanceRequest
from huaweicloudsdkcc.v3.model.delete_network_instance_response import DeleteNetworkInstanceResponse
from huaweicloudsdkcc.v3.model.description import Description
from huaweicloudsdkcc.v3.model.disassociate_bandwidth_package import DisassociateBandwidthPackage
from huaweicloudsdkcc.v3.model.disassociate_bandwidth_package_request import DisassociateBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.disassociate_bandwidth_package_request_body import DisassociateBandwidthPackageRequestBody
from huaweicloudsdkcc.v3.model.disassociate_bandwidth_package_response import DisassociateBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.document_template_version import DocumentTemplateVersion
from huaweicloudsdkcc.v3.model.document_template_version_enum import DocumentTemplateVersionEnum
from huaweicloudsdkcc.v3.model.domain_id import DomainId
from huaweicloudsdkcc.v3.model.domain_id_def import DomainIdDef
from huaweicloudsdkcc.v3.model.enterprise_project_id import EnterpriseProjectId
from huaweicloudsdkcc.v3.model.enterprise_router_attachment_id import EnterpriseRouterAttachmentId
from huaweicloudsdkcc.v3.model.enterprise_router_id import EnterpriseRouterId
from huaweicloudsdkcc.v3.model.enterprise_router_project_id import EnterpriseRouterProjectId
from huaweicloudsdkcc.v3.model.enterprise_router_region_id import EnterpriseRouterRegionId
from huaweicloudsdkcc.v3.model.enterprise_router_table_id import EnterpriseRouterTableId
from huaweicloudsdkcc.v3.model.global_connection_bandwidth_id import GlobalConnectionBandwidthId
from huaweicloudsdkcc.v3.model.global_dc_gateway_id import GlobalDcGatewayId
from huaweicloudsdkcc.v3.model.global_dc_gateway_peer_link_id import GlobalDcGatewayPeerLinkId
from huaweicloudsdkcc.v3.model.hosted_cloud_enum import HostedCloudEnum
from huaweicloudsdkcc.v3.model.instance_domain_id import InstanceDomainId
from huaweicloudsdkcc.v3.model.instance_id import InstanceId
from huaweicloudsdkcc.v3.model.inter_region import InterRegion
from huaweicloudsdkcc.v3.model.inter_region_bandwidth import InterRegionBandwidth
from huaweicloudsdkcc.v3.model.is_frozen import IsFrozen
from huaweicloudsdkcc.v3.model.list_authorisations_request import ListAuthorisationsRequest
from huaweicloudsdkcc.v3.model.list_authorisations_response import ListAuthorisationsResponse
from huaweicloudsdkcc.v3.model.list_bandwidth_package_tags_request import ListBandwidthPackageTagsRequest
from huaweicloudsdkcc.v3.model.list_bandwidth_package_tags_response import ListBandwidthPackageTagsResponse
from huaweicloudsdkcc.v3.model.list_bandwidth_packages_by_tags_request import ListBandwidthPackagesByTagsRequest
from huaweicloudsdkcc.v3.model.list_bandwidth_packages_by_tags_request_body import ListBandwidthPackagesByTagsRequestBody
from huaweicloudsdkcc.v3.model.list_bandwidth_packages_by_tags_response import ListBandwidthPackagesByTagsResponse
from huaweicloudsdkcc.v3.model.list_bandwidth_packages_request import ListBandwidthPackagesRequest
from huaweicloudsdkcc.v3.model.list_bandwidth_packages_response import ListBandwidthPackagesResponse
from huaweicloudsdkcc.v3.model.list_central_network_attachments_request import ListCentralNetworkAttachmentsRequest
from huaweicloudsdkcc.v3.model.list_central_network_attachments_response import ListCentralNetworkAttachmentsResponse
from huaweicloudsdkcc.v3.model.list_central_network_capabilities_request import ListCentralNetworkCapabilitiesRequest
from huaweicloudsdkcc.v3.model.list_central_network_capabilities_response import ListCentralNetworkCapabilitiesResponse
from huaweicloudsdkcc.v3.model.list_central_network_connections_request import ListCentralNetworkConnectionsRequest
from huaweicloudsdkcc.v3.model.list_central_network_connections_response import ListCentralNetworkConnectionsResponse
from huaweicloudsdkcc.v3.model.list_central_network_gdgw_attachments_request import ListCentralNetworkGdgwAttachmentsRequest
from huaweicloudsdkcc.v3.model.list_central_network_gdgw_attachments_response import ListCentralNetworkGdgwAttachmentsResponse
from huaweicloudsdkcc.v3.model.list_central_network_policies_request import ListCentralNetworkPoliciesRequest
from huaweicloudsdkcc.v3.model.list_central_network_policies_response import ListCentralNetworkPoliciesResponse
from huaweicloudsdkcc.v3.model.list_central_network_policy_change_set_request import ListCentralNetworkPolicyChangeSetRequest
from huaweicloudsdkcc.v3.model.list_central_network_policy_change_set_response import ListCentralNetworkPolicyChangeSetResponse
from huaweicloudsdkcc.v3.model.list_central_network_quotas_request import ListCentralNetworkQuotasRequest
from huaweicloudsdkcc.v3.model.list_central_network_quotas_response import ListCentralNetworkQuotasResponse
from huaweicloudsdkcc.v3.model.list_central_network_tags_request import ListCentralNetworkTagsRequest
from huaweicloudsdkcc.v3.model.list_central_network_tags_response import ListCentralNetworkTagsResponse
from huaweicloudsdkcc.v3.model.list_central_networks_request import ListCentralNetworksRequest
from huaweicloudsdkcc.v3.model.list_central_networks_response import ListCentralNetworksResponse
from huaweicloudsdkcc.v3.model.list_cloud_connection_quotas_request import ListCloudConnectionQuotasRequest
from huaweicloudsdkcc.v3.model.list_cloud_connection_quotas_response import ListCloudConnectionQuotasResponse
from huaweicloudsdkcc.v3.model.list_cloud_connection_routes_request import ListCloudConnectionRoutesRequest
from huaweicloudsdkcc.v3.model.list_cloud_connection_routes_response import ListCloudConnectionRoutesResponse
from huaweicloudsdkcc.v3.model.list_cloud_connection_tags_request import ListCloudConnectionTagsRequest
from huaweicloudsdkcc.v3.model.list_cloud_connection_tags_response import ListCloudConnectionTagsResponse
from huaweicloudsdkcc.v3.model.list_cloud_connections_by_tags_request import ListCloudConnectionsByTagsRequest
from huaweicloudsdkcc.v3.model.list_cloud_connections_by_tags_request_body import ListCloudConnectionsByTagsRequestBody
from huaweicloudsdkcc.v3.model.list_cloud_connections_by_tags_response import ListCloudConnectionsByTagsResponse
from huaweicloudsdkcc.v3.model.list_cloud_connections_request import ListCloudConnectionsRequest
from huaweicloudsdkcc.v3.model.list_cloud_connections_response import ListCloudConnectionsResponse
from huaweicloudsdkcc.v3.model.list_inter_region_bandwidths_request import ListInterRegionBandwidthsRequest
from huaweicloudsdkcc.v3.model.list_inter_region_bandwidths_response import ListInterRegionBandwidthsResponse
from huaweicloudsdkcc.v3.model.list_network_instances_request import ListNetworkInstancesRequest
from huaweicloudsdkcc.v3.model.list_network_instances_response import ListNetworkInstancesResponse
from huaweicloudsdkcc.v3.model.list_permissions_request import ListPermissionsRequest
from huaweicloudsdkcc.v3.model.list_permissions_response import ListPermissionsResponse
from huaweicloudsdkcc.v3.model.list_response_body import ListResponseBody
from huaweicloudsdkcc.v3.model.local_area_id import LocalAreaId
from huaweicloudsdkcc.v3.model.multivalued_tag import MultivaluedTag
from huaweicloudsdkcc.v3.model.name import Name
from huaweicloudsdkcc.v3.model.name_def import NameDef
from huaweicloudsdkcc.v3.model.network_instance import NetworkInstance
from huaweicloudsdkcc.v3.model.next_marker import NextMarker
from huaweicloudsdkcc.v3.model.non_required_name import NonRequiredName
from huaweicloudsdkcc.v3.model.page_info import PageInfo
from huaweicloudsdkcc.v3.model.permission import Permission
from huaweicloudsdkcc.v3.model.plane_id import PlaneId
from huaweicloudsdkcc.v3.model.previous_marker import PreviousMarker
from huaweicloudsdkcc.v3.model.project_id import ProjectId
from huaweicloudsdkcc.v3.model.project_id_def import ProjectIdDef
from huaweicloudsdkcc.v3.model.quota_limit import QuotaLimit
from huaweicloudsdkcc.v3.model.quota_unit import QuotaUnit
from huaweicloudsdkcc.v3.model.quota_used import QuotaUsed
from huaweicloudsdkcc.v3.model.region_id import RegionId
from huaweicloudsdkcc.v3.model.region_id_def import RegionIdDef
from huaweicloudsdkcc.v3.model.remote_area_id import RemoteAreaId
from huaweicloudsdkcc.v3.model.request_id import RequestId
from huaweicloudsdkcc.v3.model.resource_id import ResourceId
from huaweicloudsdkcc.v3.model.resource_type import ResourceType
from huaweicloudsdkcc.v3.model.show_bandwidth_package_request import ShowBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.show_bandwidth_package_response import ShowBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.show_central_network_gdgw_attachment_request import ShowCentralNetworkGdgwAttachmentRequest
from huaweicloudsdkcc.v3.model.show_central_network_gdgw_attachment_response import ShowCentralNetworkGdgwAttachmentResponse
from huaweicloudsdkcc.v3.model.show_central_network_request import ShowCentralNetworkRequest
from huaweicloudsdkcc.v3.model.show_central_network_response import ShowCentralNetworkResponse
from huaweicloudsdkcc.v3.model.show_cloud_connection_request import ShowCloudConnectionRequest
from huaweicloudsdkcc.v3.model.show_cloud_connection_response import ShowCloudConnectionResponse
from huaweicloudsdkcc.v3.model.show_cloud_connection_routes_request import ShowCloudConnectionRoutesRequest
from huaweicloudsdkcc.v3.model.show_cloud_connection_routes_response import ShowCloudConnectionRoutesResponse
from huaweicloudsdkcc.v3.model.show_inter_region_bandwidth_request import ShowInterRegionBandwidthRequest
from huaweicloudsdkcc.v3.model.show_inter_region_bandwidth_response import ShowInterRegionBandwidthResponse
from huaweicloudsdkcc.v3.model.show_network_instance_request import ShowNetworkInstanceRequest
from huaweicloudsdkcc.v3.model.show_network_instance_response import ShowNetworkInstanceResponse
from huaweicloudsdkcc.v3.model.site_code import SiteCode
from huaweicloudsdkcc.v3.model.site_code_def import SiteCodeDef
from huaweicloudsdkcc.v3.model.sort_dir import SortDir
from huaweicloudsdkcc.v3.model.spec_code import SpecCode
from huaweicloudsdkcc.v3.model.tag import Tag
from huaweicloudsdkcc.v3.model.tag_bandwidth_package_request import TagBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.tag_bandwidth_package_request_body import TagBandwidthPackageRequestBody
from huaweicloudsdkcc.v3.model.tag_bandwidth_package_response import TagBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.tag_central_network_request import TagCentralNetworkRequest
from huaweicloudsdkcc.v3.model.tag_central_network_request_body import TagCentralNetworkRequestBody
from huaweicloudsdkcc.v3.model.tag_central_network_response import TagCentralNetworkResponse
from huaweicloudsdkcc.v3.model.tag_cloud_connection_request import TagCloudConnectionRequest
from huaweicloudsdkcc.v3.model.tag_cloud_connection_request_body import TagCloudConnectionRequestBody
from huaweicloudsdkcc.v3.model.tag_cloud_connection_response import TagCloudConnectionResponse
from huaweicloudsdkcc.v3.model.tag_key import TagKey
from huaweicloudsdkcc.v3.model.tag_value import TagValue
from huaweicloudsdkcc.v3.model.tags import Tags
from huaweicloudsdkcc.v3.model.uuid_def import UUIDDef
from huaweicloudsdkcc.v3.model.uuid_identifier import UUIDIdentifier
from huaweicloudsdkcc.v3.model.untag_bandwidth_package_request import UntagBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.untag_bandwidth_package_request_body import UntagBandwidthPackageRequestBody
from huaweicloudsdkcc.v3.model.untag_bandwidth_package_response import UntagBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.untag_central_network_request import UntagCentralNetworkRequest
from huaweicloudsdkcc.v3.model.untag_central_network_request_body import UntagCentralNetworkRequestBody
from huaweicloudsdkcc.v3.model.untag_central_network_response import UntagCentralNetworkResponse
from huaweicloudsdkcc.v3.model.untag_cloud_connection_request import UntagCloudConnectionRequest
from huaweicloudsdkcc.v3.model.untag_cloud_connection_request_body import UntagCloudConnectionRequestBody
from huaweicloudsdkcc.v3.model.untag_cloud_connection_response import UntagCloudConnectionResponse
from huaweicloudsdkcc.v3.model.update_authorisation import UpdateAuthorisation
from huaweicloudsdkcc.v3.model.update_authorisation_request import UpdateAuthorisationRequest
from huaweicloudsdkcc.v3.model.update_authorisation_request_body import UpdateAuthorisationRequestBody
from huaweicloudsdkcc.v3.model.update_authorisation_response import UpdateAuthorisationResponse
from huaweicloudsdkcc.v3.model.update_bandwidth_package import UpdateBandwidthPackage
from huaweicloudsdkcc.v3.model.update_bandwidth_package_request import UpdateBandwidthPackageRequest
from huaweicloudsdkcc.v3.model.update_bandwidth_package_request_body import UpdateBandwidthPackageRequestBody
from huaweicloudsdkcc.v3.model.update_bandwidth_package_response import UpdateBandwidthPackageResponse
from huaweicloudsdkcc.v3.model.update_central_network import UpdateCentralNetwork
from huaweicloudsdkcc.v3.model.update_central_network_connection import UpdateCentralNetworkConnection
from huaweicloudsdkcc.v3.model.update_central_network_connection_request import UpdateCentralNetworkConnectionRequest
from huaweicloudsdkcc.v3.model.update_central_network_connection_request_body import UpdateCentralNetworkConnectionRequestBody
from huaweicloudsdkcc.v3.model.update_central_network_connection_response import UpdateCentralNetworkConnectionResponse
from huaweicloudsdkcc.v3.model.update_central_network_gdgw_attachment import UpdateCentralNetworkGdgwAttachment
from huaweicloudsdkcc.v3.model.update_central_network_gdgw_attachment_request import UpdateCentralNetworkGdgwAttachmentRequest
from huaweicloudsdkcc.v3.model.update_central_network_gdgw_attachment_request_body import UpdateCentralNetworkGdgwAttachmentRequestBody
from huaweicloudsdkcc.v3.model.update_central_network_gdgw_attachment_response import UpdateCentralNetworkGdgwAttachmentResponse
from huaweicloudsdkcc.v3.model.update_central_network_request import UpdateCentralNetworkRequest
from huaweicloudsdkcc.v3.model.update_central_network_request_body import UpdateCentralNetworkRequestBody
from huaweicloudsdkcc.v3.model.update_central_network_response import UpdateCentralNetworkResponse
from huaweicloudsdkcc.v3.model.update_cloud_connection import UpdateCloudConnection
from huaweicloudsdkcc.v3.model.update_cloud_connection_request import UpdateCloudConnectionRequest
from huaweicloudsdkcc.v3.model.update_cloud_connection_request_body import UpdateCloudConnectionRequestBody
from huaweicloudsdkcc.v3.model.update_cloud_connection_response import UpdateCloudConnectionResponse
from huaweicloudsdkcc.v3.model.update_inter_region_bandwidth import UpdateInterRegionBandwidth
from huaweicloudsdkcc.v3.model.update_inter_region_bandwidth_request import UpdateInterRegionBandwidthRequest
from huaweicloudsdkcc.v3.model.update_inter_region_bandwidth_request_body import UpdateInterRegionBandwidthRequestBody
from huaweicloudsdkcc.v3.model.update_inter_region_bandwidth_response import UpdateInterRegionBandwidthResponse
from huaweicloudsdkcc.v3.model.update_network_instance import UpdateNetworkInstance
from huaweicloudsdkcc.v3.model.update_network_instance_request import UpdateNetworkInstanceRequest
from huaweicloudsdkcc.v3.model.update_network_instance_request_body import UpdateNetworkInstanceRequestBody
from huaweicloudsdkcc.v3.model.update_network_instance_response import UpdateNetworkInstanceResponse
from huaweicloudsdkcc.v3.model.updated_at import UpdatedAt
from huaweicloudsdkcc.v3.model.version import Version
from huaweicloudsdkcc.v3.model.version_def import VersionDef
