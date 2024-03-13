# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkdns.v2.model.alias_target import AliasTarget
from huaweicloudsdkdns.v2.model.associate_router_request import AssociateRouterRequest
from huaweicloudsdkdns.v2.model.associate_router_request_body import AssociateRouterRequestBody
from huaweicloudsdkdns.v2.model.associate_router_response import AssociateRouterResponse
from huaweicloudsdkdns.v2.model.batch_create_record_set_with_line import BatchCreateRecordSetWithLine
from huaweicloudsdkdns.v2.model.batch_create_tag_request import BatchCreateTagRequest
from huaweicloudsdkdns.v2.model.batch_create_tag_response import BatchCreateTagResponse
from huaweicloudsdkdns.v2.model.batch_delete_record_set_with_line_request import BatchDeleteRecordSetWithLineRequest
from huaweicloudsdkdns.v2.model.batch_delete_record_set_with_line_request_body import BatchDeleteRecordSetWithLineRequestBody
from huaweicloudsdkdns.v2.model.batch_delete_record_set_with_line_response import BatchDeleteRecordSetWithLineResponse
from huaweicloudsdkdns.v2.model.batch_hand_tags import BatchHandTags
from huaweicloudsdkdns.v2.model.batch_update_record_set import BatchUpdateRecordSet
from huaweicloudsdkdns.v2.model.batch_update_record_set_with_line_req import BatchUpdateRecordSetWithLineReq
from huaweicloudsdkdns.v2.model.batch_update_record_set_with_line_request import BatchUpdateRecordSetWithLineRequest
from huaweicloudsdkdns.v2.model.batch_update_record_set_with_line_response import BatchUpdateRecordSetWithLineResponse
from huaweicloudsdkdns.v2.model.create_custom_line_request import CreateCustomLineRequest
from huaweicloudsdkdns.v2.model.create_custom_line_response import CreateCustomLineResponse
from huaweicloudsdkdns.v2.model.create_custom_lines import CreateCustomLines
from huaweicloudsdkdns.v2.model.create_eip_record_set_request import CreateEipRecordSetRequest
from huaweicloudsdkdns.v2.model.create_eip_record_set_response import CreateEipRecordSetResponse
from huaweicloudsdkdns.v2.model.create_line_group_request import CreateLineGroupRequest
from huaweicloudsdkdns.v2.model.create_line_group_response import CreateLineGroupResponse
from huaweicloudsdkdns.v2.model.create_line_groups_req import CreateLineGroupsReq
from huaweicloudsdkdns.v2.model.create_line_groups_resp import CreateLineGroupsResp
from huaweicloudsdkdns.v2.model.create_private_zone_req import CreatePrivateZoneReq
from huaweicloudsdkdns.v2.model.create_private_zone_request import CreatePrivateZoneRequest
from huaweicloudsdkdns.v2.model.create_private_zone_response import CreatePrivateZoneResponse
from huaweicloudsdkdns.v2.model.create_ptr_req import CreatePtrReq
from huaweicloudsdkdns.v2.model.create_public_zone_req import CreatePublicZoneReq
from huaweicloudsdkdns.v2.model.create_public_zone_request import CreatePublicZoneRequest
from huaweicloudsdkdns.v2.model.create_public_zone_response import CreatePublicZoneResponse
from huaweicloudsdkdns.v2.model.create_r_set_batch_lines_req import CreateRSetBatchLinesReq
from huaweicloudsdkdns.v2.model.create_record_set_request import CreateRecordSetRequest
from huaweicloudsdkdns.v2.model.create_record_set_request_body import CreateRecordSetRequestBody
from huaweicloudsdkdns.v2.model.create_record_set_response import CreateRecordSetResponse
from huaweicloudsdkdns.v2.model.create_record_set_with_batch_lines_request import CreateRecordSetWithBatchLinesRequest
from huaweicloudsdkdns.v2.model.create_record_set_with_batch_lines_response import CreateRecordSetWithBatchLinesResponse
from huaweicloudsdkdns.v2.model.create_record_set_with_line_request import CreateRecordSetWithLineRequest
from huaweicloudsdkdns.v2.model.create_record_set_with_line_request_body import CreateRecordSetWithLineRequestBody
from huaweicloudsdkdns.v2.model.create_record_set_with_line_response import CreateRecordSetWithLineResponse
from huaweicloudsdkdns.v2.model.create_tag_req import CreateTagReq
from huaweicloudsdkdns.v2.model.create_tag_request import CreateTagRequest
from huaweicloudsdkdns.v2.model.create_tag_response import CreateTagResponse
from huaweicloudsdkdns.v2.model.delete_custom_line_request import DeleteCustomLineRequest
from huaweicloudsdkdns.v2.model.delete_custom_line_response import DeleteCustomLineResponse
from huaweicloudsdkdns.v2.model.delete_line_group_request import DeleteLineGroupRequest
from huaweicloudsdkdns.v2.model.delete_line_group_response import DeleteLineGroupResponse
from huaweicloudsdkdns.v2.model.delete_private_zone_request import DeletePrivateZoneRequest
from huaweicloudsdkdns.v2.model.delete_private_zone_response import DeletePrivateZoneResponse
from huaweicloudsdkdns.v2.model.delete_public_zone_request import DeletePublicZoneRequest
from huaweicloudsdkdns.v2.model.delete_public_zone_response import DeletePublicZoneResponse
from huaweicloudsdkdns.v2.model.delete_record_set_request import DeleteRecordSetRequest
from huaweicloudsdkdns.v2.model.delete_record_set_response import DeleteRecordSetResponse
from huaweicloudsdkdns.v2.model.delete_record_sets_request import DeleteRecordSetsRequest
from huaweicloudsdkdns.v2.model.delete_record_sets_response import DeleteRecordSetsResponse
from huaweicloudsdkdns.v2.model.delete_tag_request import DeleteTagRequest
from huaweicloudsdkdns.v2.model.delete_tag_response import DeleteTagResponse
from huaweicloudsdkdns.v2.model.disassociate_router_request import DisassociateRouterRequest
from huaweicloudsdkdns.v2.model.disassociate_router_response import DisassociateRouterResponse
from huaweicloudsdkdns.v2.model.disassociaterouter_request_body import DisassociaterouterRequestBody
from huaweicloudsdkdns.v2.model.domain_quota_response_quotas import DomainQuotaResponseQuotas
from huaweicloudsdkdns.v2.model.line import Line
from huaweicloudsdkdns.v2.model.links_item import LinksItem
from huaweicloudsdkdns.v2.model.list_api_versions_item import ListApiVersionsItem
from huaweicloudsdkdns.v2.model.list_api_versions_request import ListApiVersionsRequest
from huaweicloudsdkdns.v2.model.list_api_versions_response import ListApiVersionsResponse
from huaweicloudsdkdns.v2.model.list_custom_line_request import ListCustomLineRequest
from huaweicloudsdkdns.v2.model.list_custom_line_response import ListCustomLineResponse
from huaweicloudsdkdns.v2.model.list_line_groups_request import ListLineGroupsRequest
from huaweicloudsdkdns.v2.model.list_line_groups_response import ListLineGroupsResponse
from huaweicloudsdkdns.v2.model.list_name_servers_request import ListNameServersRequest
from huaweicloudsdkdns.v2.model.list_name_servers_response import ListNameServersResponse
from huaweicloudsdkdns.v2.model.list_private_zones_request import ListPrivateZonesRequest
from huaweicloudsdkdns.v2.model.list_private_zones_response import ListPrivateZonesResponse
from huaweicloudsdkdns.v2.model.list_ptr_records_floating_resp import ListPtrRecordsFloatingResp
from huaweicloudsdkdns.v2.model.list_ptr_records_request import ListPtrRecordsRequest
from huaweicloudsdkdns.v2.model.list_ptr_records_response import ListPtrRecordsResponse
from huaweicloudsdkdns.v2.model.list_public_zones_request import ListPublicZonesRequest
from huaweicloudsdkdns.v2.model.list_public_zones_response import ListPublicZonesResponse
from huaweicloudsdkdns.v2.model.list_record_sets import ListRecordSets
from huaweicloudsdkdns.v2.model.list_record_sets_by_zone_request import ListRecordSetsByZoneRequest
from huaweicloudsdkdns.v2.model.list_record_sets_by_zone_response import ListRecordSetsByZoneResponse
from huaweicloudsdkdns.v2.model.list_record_sets_request import ListRecordSetsRequest
from huaweicloudsdkdns.v2.model.list_record_sets_response import ListRecordSetsResponse
from huaweicloudsdkdns.v2.model.list_record_sets_with_line_request import ListRecordSetsWithLineRequest
from huaweicloudsdkdns.v2.model.list_record_sets_with_line_response import ListRecordSetsWithLineResponse
from huaweicloudsdkdns.v2.model.list_record_sets_with_tags import ListRecordSetsWithTags
from huaweicloudsdkdns.v2.model.list_tag_req import ListTagReq
from huaweicloudsdkdns.v2.model.list_tag_request import ListTagRequest
from huaweicloudsdkdns.v2.model.list_tag_response import ListTagResponse
from huaweicloudsdkdns.v2.model.list_tags_request import ListTagsRequest
from huaweicloudsdkdns.v2.model.list_tags_response import ListTagsResponse
from huaweicloudsdkdns.v2.model.match import Match
from huaweicloudsdkdns.v2.model.metadata import Metadata
from huaweicloudsdkdns.v2.model.name_servers_resp import NameServersResp
from huaweicloudsdkdns.v2.model.nameserver import Nameserver
from huaweicloudsdkdns.v2.model.ns_records import NsRecords
from huaweicloudsdkdns.v2.model.page_link import PageLink
from huaweicloudsdkdns.v2.model.private_name_server import PrivateNameServer
from huaweicloudsdkdns.v2.model.private_zone_resp import PrivateZoneResp
from huaweicloudsdkdns.v2.model.public_zone_resp import PublicZoneResp
from huaweicloudsdkdns.v2.model.query_record_set_with_line_and_tags_resp import QueryRecordSetWithLineAndTagsResp
from huaweicloudsdkdns.v2.model.query_record_set_with_line_resp import QueryRecordSetWithLineResp
from huaweicloudsdkdns.v2.model.resource_item import ResourceItem
from huaweicloudsdkdns.v2.model.restore_ptr_record_request import RestorePtrRecordRequest
from huaweicloudsdkdns.v2.model.restore_ptr_record_response import RestorePtrRecordResponse
from huaweicloudsdkdns.v2.model.restore_ptr_req import RestorePtrReq
from huaweicloudsdkdns.v2.model.router import Router
from huaweicloudsdkdns.v2.model.router_with_status import RouterWithStatus
from huaweicloudsdkdns.v2.model.set_record_sets_status_req import SetRecordSetsStatusReq
from huaweicloudsdkdns.v2.model.set_record_sets_status_request import SetRecordSetsStatusRequest
from huaweicloudsdkdns.v2.model.set_record_sets_status_response import SetRecordSetsStatusResponse
from huaweicloudsdkdns.v2.model.show_api_info_request import ShowApiInfoRequest
from huaweicloudsdkdns.v2.model.show_api_info_response import ShowApiInfoResponse
from huaweicloudsdkdns.v2.model.show_domain_quota_request import ShowDomainQuotaRequest
from huaweicloudsdkdns.v2.model.show_domain_quota_response import ShowDomainQuotaResponse
from huaweicloudsdkdns.v2.model.show_line_group_request import ShowLineGroupRequest
from huaweicloudsdkdns.v2.model.show_line_group_response import ShowLineGroupResponse
from huaweicloudsdkdns.v2.model.show_private_zone_name_server_request import ShowPrivateZoneNameServerRequest
from huaweicloudsdkdns.v2.model.show_private_zone_name_server_response import ShowPrivateZoneNameServerResponse
from huaweicloudsdkdns.v2.model.show_private_zone_request import ShowPrivateZoneRequest
from huaweicloudsdkdns.v2.model.show_private_zone_response import ShowPrivateZoneResponse
from huaweicloudsdkdns.v2.model.show_ptr_record_set_request import ShowPtrRecordSetRequest
from huaweicloudsdkdns.v2.model.show_ptr_record_set_response import ShowPtrRecordSetResponse
from huaweicloudsdkdns.v2.model.show_public_zone_name_server_request import ShowPublicZoneNameServerRequest
from huaweicloudsdkdns.v2.model.show_public_zone_name_server_response import ShowPublicZoneNameServerResponse
from huaweicloudsdkdns.v2.model.show_public_zone_request import ShowPublicZoneRequest
from huaweicloudsdkdns.v2.model.show_public_zone_response import ShowPublicZoneResponse
from huaweicloudsdkdns.v2.model.show_record_set_by_zone_request import ShowRecordSetByZoneRequest
from huaweicloudsdkdns.v2.model.show_record_set_by_zone_resp import ShowRecordSetByZoneResp
from huaweicloudsdkdns.v2.model.show_record_set_by_zone_response import ShowRecordSetByZoneResponse
from huaweicloudsdkdns.v2.model.show_record_set_request import ShowRecordSetRequest
from huaweicloudsdkdns.v2.model.show_record_set_response import ShowRecordSetResponse
from huaweicloudsdkdns.v2.model.show_record_set_with_line_request import ShowRecordSetWithLineRequest
from huaweicloudsdkdns.v2.model.show_record_set_with_line_response import ShowRecordSetWithLineResponse
from huaweicloudsdkdns.v2.model.show_resource_tag_request import ShowResourceTagRequest
from huaweicloudsdkdns.v2.model.show_resource_tag_response import ShowResourceTagResponse
from huaweicloudsdkdns.v2.model.tag import Tag
from huaweicloudsdkdns.v2.model.tag_values import TagValues
from huaweicloudsdkdns.v2.model.update_custom_line_request import UpdateCustomLineRequest
from huaweicloudsdkdns.v2.model.update_custom_line_response import UpdateCustomLineResponse
from huaweicloudsdkdns.v2.model.update_customs_line_req import UpdateCustomsLineReq
from huaweicloudsdkdns.v2.model.update_line_groups_body import UpdateLineGroupsBody
from huaweicloudsdkdns.v2.model.update_line_groups_request import UpdateLineGroupsRequest
from huaweicloudsdkdns.v2.model.update_line_groups_response import UpdateLineGroupsResponse
from huaweicloudsdkdns.v2.model.update_private_zone_info_req import UpdatePrivateZoneInfoReq
from huaweicloudsdkdns.v2.model.update_private_zone_request import UpdatePrivateZoneRequest
from huaweicloudsdkdns.v2.model.update_private_zone_response import UpdatePrivateZoneResponse
from huaweicloudsdkdns.v2.model.update_ptr_record_request import UpdatePtrRecordRequest
from huaweicloudsdkdns.v2.model.update_ptr_record_response import UpdatePtrRecordResponse
from huaweicloudsdkdns.v2.model.update_ptr_req import UpdatePtrReq
from huaweicloudsdkdns.v2.model.update_public_zone_info import UpdatePublicZoneInfo
from huaweicloudsdkdns.v2.model.update_public_zone_request import UpdatePublicZoneRequest
from huaweicloudsdkdns.v2.model.update_public_zone_response import UpdatePublicZoneResponse
from huaweicloudsdkdns.v2.model.update_public_zone_status_request import UpdatePublicZoneStatusRequest
from huaweicloudsdkdns.v2.model.update_public_zone_status_request_body import UpdatePublicZoneStatusRequestBody
from huaweicloudsdkdns.v2.model.update_public_zone_status_response import UpdatePublicZoneStatusResponse
from huaweicloudsdkdns.v2.model.update_record_set_req import UpdateRecordSetReq
from huaweicloudsdkdns.v2.model.update_record_set_request import UpdateRecordSetRequest
from huaweicloudsdkdns.v2.model.update_record_set_response import UpdateRecordSetResponse
from huaweicloudsdkdns.v2.model.update_record_sets_req import UpdateRecordSetsReq
from huaweicloudsdkdns.v2.model.update_record_sets_request import UpdateRecordSetsRequest
from huaweicloudsdkdns.v2.model.update_record_sets_response import UpdateRecordSetsResponse
from huaweicloudsdkdns.v2.model.values_item import ValuesItem
from huaweicloudsdkdns.v2.model.version_item import VersionItem
