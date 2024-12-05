# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalListGlobalDcGateways:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'global_center_network_id': 'str',
        'site_network_id': 'str',
        'cloud_connection_id': 'str',
        'bgp_asn': 'int',
        'region_id': 'str',
        'location_name': 'str',
        'address_family': 'str',
        'locales': 'Locale',
        'current_peer_link_count': 'int',
        'available_peer_link_count': 'int',
        'admin_state_up': 'bool',
        'status': 'str',
        'reason': 'str',
        'created_time': 'datetime',
        'updated_time': 'datetime',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'global_center_network_id': 'global_center_network_id',
        'site_network_id': 'site_network_id',
        'cloud_connection_id': 'cloud_connection_id',
        'bgp_asn': 'bgp_asn',
        'region_id': 'region_id',
        'location_name': 'location_name',
        'address_family': 'address_family',
        'locales': 'locales',
        'current_peer_link_count': 'current_peer_link_count',
        'available_peer_link_count': 'available_peer_link_count',
        'admin_state_up': 'admin_state_up',
        'status': 'status',
        'reason': 'reason',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'tags': 'tags'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, enterprise_project_id=None, global_center_network_id=None, site_network_id=None, cloud_connection_id=None, bgp_asn=None, region_id=None, location_name=None, address_family=None, locales=None, current_peer_link_count=None, available_peer_link_count=None, admin_state_up=None, status=None, reason=None, created_time=None, updated_time=None, tags=None):
        """ExternalListGlobalDcGateways

        The model defined in huaweicloud sdk

        :param id: 唯一ID
        :type id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param name: 名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param global_center_network_id: 全球中心网络ID
        :type global_center_network_id: str
        :param site_network_id: 站点网络ID
        :type site_network_id: str
        :param cloud_connection_id: 云连接ID
        :type cloud_connection_id: str
        :param bgp_asn: BGP模式的AS号
        :type bgp_asn: int
        :param region_id: 局点ID
        :type region_id: str
        :param location_name: 位置名称
        :type location_name: str
        :param address_family: 地址簇
        :type address_family: str
        :param locales: 
        :type locales: :class:`huaweicloudsdkdc.v3.Locale`
        :param current_peer_link_count: 当前对等体数量
        :type current_peer_link_count: int
        :param available_peer_link_count: 有效对等体数量
        :type available_peer_link_count: int
        :param admin_state_up: 是否冻结： true-是，false-否
        :type admin_state_up: bool
        :param status: 状态： ACTIVE-正常，ERROR-异常
        :type status: str
        :param reason: 失败原因
        :type reason: str
        :param created_time: 创建时间
        :type created_time: datetime
        :param updated_time: 修改时间
        :type updated_time: datetime
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._global_center_network_id = None
        self._site_network_id = None
        self._cloud_connection_id = None
        self._bgp_asn = None
        self._region_id = None
        self._location_name = None
        self._address_family = None
        self._locales = None
        self._current_peer_link_count = None
        self._available_peer_link_count = None
        self._admin_state_up = None
        self._status = None
        self._reason = None
        self._created_time = None
        self._updated_time = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if global_center_network_id is not None:
            self.global_center_network_id = global_center_network_id
        if site_network_id is not None:
            self.site_network_id = site_network_id
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if region_id is not None:
            self.region_id = region_id
        if location_name is not None:
            self.location_name = location_name
        if address_family is not None:
            self.address_family = address_family
        if locales is not None:
            self.locales = locales
        if current_peer_link_count is not None:
            self.current_peer_link_count = current_peer_link_count
        if available_peer_link_count is not None:
            self.available_peer_link_count = available_peer_link_count
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this ExternalListGlobalDcGateways.

        唯一ID

        :return: The id of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalListGlobalDcGateways.

        唯一ID

        :param id: The id of this ExternalListGlobalDcGateways.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ExternalListGlobalDcGateways.

        租户ID

        :return: The tenant_id of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ExternalListGlobalDcGateways.

        租户ID

        :param tenant_id: The tenant_id of this ExternalListGlobalDcGateways.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this ExternalListGlobalDcGateways.

        名称

        :return: The name of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalListGlobalDcGateways.

        名称

        :param name: The name of this ExternalListGlobalDcGateways.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ExternalListGlobalDcGateways.

        描述信息

        :return: The description of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalListGlobalDcGateways.

        描述信息

        :param description: The description of this ExternalListGlobalDcGateways.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ExternalListGlobalDcGateways.

        企业项目ID

        :return: The enterprise_project_id of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ExternalListGlobalDcGateways.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ExternalListGlobalDcGateways.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def global_center_network_id(self):
        """Gets the global_center_network_id of this ExternalListGlobalDcGateways.

        全球中心网络ID

        :return: The global_center_network_id of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._global_center_network_id

    @global_center_network_id.setter
    def global_center_network_id(self, global_center_network_id):
        """Sets the global_center_network_id of this ExternalListGlobalDcGateways.

        全球中心网络ID

        :param global_center_network_id: The global_center_network_id of this ExternalListGlobalDcGateways.
        :type global_center_network_id: str
        """
        self._global_center_network_id = global_center_network_id

    @property
    def site_network_id(self):
        """Gets the site_network_id of this ExternalListGlobalDcGateways.

        站点网络ID

        :return: The site_network_id of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._site_network_id

    @site_network_id.setter
    def site_network_id(self, site_network_id):
        """Sets the site_network_id of this ExternalListGlobalDcGateways.

        站点网络ID

        :param site_network_id: The site_network_id of this ExternalListGlobalDcGateways.
        :type site_network_id: str
        """
        self._site_network_id = site_network_id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this ExternalListGlobalDcGateways.

        云连接ID

        :return: The cloud_connection_id of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this ExternalListGlobalDcGateways.

        云连接ID

        :param cloud_connection_id: The cloud_connection_id of this ExternalListGlobalDcGateways.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def bgp_asn(self):
        """Gets the bgp_asn of this ExternalListGlobalDcGateways.

        BGP模式的AS号

        :return: The bgp_asn of this ExternalListGlobalDcGateways.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        """Sets the bgp_asn of this ExternalListGlobalDcGateways.

        BGP模式的AS号

        :param bgp_asn: The bgp_asn of this ExternalListGlobalDcGateways.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def region_id(self):
        """Gets the region_id of this ExternalListGlobalDcGateways.

        局点ID

        :return: The region_id of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ExternalListGlobalDcGateways.

        局点ID

        :param region_id: The region_id of this ExternalListGlobalDcGateways.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def location_name(self):
        """Gets the location_name of this ExternalListGlobalDcGateways.

        位置名称

        :return: The location_name of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this ExternalListGlobalDcGateways.

        位置名称

        :param location_name: The location_name of this ExternalListGlobalDcGateways.
        :type location_name: str
        """
        self._location_name = location_name

    @property
    def address_family(self):
        """Gets the address_family of this ExternalListGlobalDcGateways.

        地址簇

        :return: The address_family of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this ExternalListGlobalDcGateways.

        地址簇

        :param address_family: The address_family of this ExternalListGlobalDcGateways.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def locales(self):
        """Gets the locales of this ExternalListGlobalDcGateways.

        :return: The locales of this ExternalListGlobalDcGateways.
        :rtype: :class:`huaweicloudsdkdc.v3.Locale`
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """Sets the locales of this ExternalListGlobalDcGateways.

        :param locales: The locales of this ExternalListGlobalDcGateways.
        :type locales: :class:`huaweicloudsdkdc.v3.Locale`
        """
        self._locales = locales

    @property
    def current_peer_link_count(self):
        """Gets the current_peer_link_count of this ExternalListGlobalDcGateways.

        当前对等体数量

        :return: The current_peer_link_count of this ExternalListGlobalDcGateways.
        :rtype: int
        """
        return self._current_peer_link_count

    @current_peer_link_count.setter
    def current_peer_link_count(self, current_peer_link_count):
        """Sets the current_peer_link_count of this ExternalListGlobalDcGateways.

        当前对等体数量

        :param current_peer_link_count: The current_peer_link_count of this ExternalListGlobalDcGateways.
        :type current_peer_link_count: int
        """
        self._current_peer_link_count = current_peer_link_count

    @property
    def available_peer_link_count(self):
        """Gets the available_peer_link_count of this ExternalListGlobalDcGateways.

        有效对等体数量

        :return: The available_peer_link_count of this ExternalListGlobalDcGateways.
        :rtype: int
        """
        return self._available_peer_link_count

    @available_peer_link_count.setter
    def available_peer_link_count(self, available_peer_link_count):
        """Sets the available_peer_link_count of this ExternalListGlobalDcGateways.

        有效对等体数量

        :param available_peer_link_count: The available_peer_link_count of this ExternalListGlobalDcGateways.
        :type available_peer_link_count: int
        """
        self._available_peer_link_count = available_peer_link_count

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ExternalListGlobalDcGateways.

        是否冻结： true-是，false-否

        :return: The admin_state_up of this ExternalListGlobalDcGateways.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ExternalListGlobalDcGateways.

        是否冻结： true-是，false-否

        :param admin_state_up: The admin_state_up of this ExternalListGlobalDcGateways.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def status(self):
        """Gets the status of this ExternalListGlobalDcGateways.

        状态： ACTIVE-正常，ERROR-异常

        :return: The status of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExternalListGlobalDcGateways.

        状态： ACTIVE-正常，ERROR-异常

        :param status: The status of this ExternalListGlobalDcGateways.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        """Gets the reason of this ExternalListGlobalDcGateways.

        失败原因

        :return: The reason of this ExternalListGlobalDcGateways.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ExternalListGlobalDcGateways.

        失败原因

        :param reason: The reason of this ExternalListGlobalDcGateways.
        :type reason: str
        """
        self._reason = reason

    @property
    def created_time(self):
        """Gets the created_time of this ExternalListGlobalDcGateways.

        创建时间

        :return: The created_time of this ExternalListGlobalDcGateways.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ExternalListGlobalDcGateways.

        创建时间

        :param created_time: The created_time of this ExternalListGlobalDcGateways.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ExternalListGlobalDcGateways.

        修改时间

        :return: The updated_time of this ExternalListGlobalDcGateways.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ExternalListGlobalDcGateways.

        修改时间

        :param updated_time: The updated_time of this ExternalListGlobalDcGateways.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def tags(self):
        """Gets the tags of this ExternalListGlobalDcGateways.

        标签

        :return: The tags of this ExternalListGlobalDcGateways.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ExternalListGlobalDcGateways.

        标签

        :param tags: The tags of this ExternalListGlobalDcGateways.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalListGlobalDcGateways):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
