# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubNetworkInterfaceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virsubnet_id': 'str',
        'vlan_id': 'str',
        'parent_id': 'str',
        'description': 'str',
        'ipv6_enable': 'bool',
        'private_ip_address': 'str',
        'ipv6_ip_address': 'str',
        'security_groups': 'list[str]',
        'project_id': 'str',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'instance_id': 'str',
        'instance_type': 'str',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'virsubnet_id': 'virsubnet_id',
        'vlan_id': 'vlan_id',
        'parent_id': 'parent_id',
        'description': 'description',
        'ipv6_enable': 'ipv6_enable',
        'private_ip_address': 'private_ip_address',
        'ipv6_ip_address': 'ipv6_ip_address',
        'security_groups': 'security_groups',
        'project_id': 'project_id',
        'allowed_address_pairs': 'allowed_address_pairs',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'tags': 'tags'
    }

    def __init__(self, virsubnet_id=None, vlan_id=None, parent_id=None, description=None, ipv6_enable=None, private_ip_address=None, ipv6_ip_address=None, security_groups=None, project_id=None, allowed_address_pairs=None, instance_id=None, instance_type=None, tags=None):
        """CreateSubNetworkInterfaceOption

        The model defined in huaweicloud sdk

        :param virsubnet_id: 功能说明：虚拟子网ID 取值范围：标准UUID
        :type virsubnet_id: str
        :param vlan_id: 功能说明：辅助弹性网卡的VLAN ID 取值范围：1-4094 约束：同一个宿主网络接口下唯一
        :type vlan_id: str
        :param parent_id: 功能说明：宿主网络接口的ID 取值范围：标准UUID 约束：必须是实际存在的端口ID
        :type parent_id: str
        :param description: 功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;” 
        :type description: str
        :param ipv6_enable: 功能说明：辅助弹性网卡是否启用ipv6地址 取值范围：true（开启)，false（关闭） 默认值：false
        :type ipv6_enable: bool
        :param private_ip_address: 功能说明：辅助弹性网卡的私有IPv4地址 取值范围：必须在虚拟子网的网段内，不填则随机在虚拟子网网段内随机分配
        :type private_ip_address: str
        :param ipv6_ip_address: 功能说明：辅助弹性网卡的IPv6地址 取值范围：不填则随机分配
        :type ipv6_ip_address: str
        :param security_groups: 功能说明：安全组的ID列表；例如：\&quot;security_groups\&quot;: [\&quot;a0608cbf-d047-4f54-8b28-cd7b59853fff\&quot;] 取值范围：默认值为系统默认安全组
        :type security_groups: list[str]
        :param project_id: 功能说明：辅助弹性网卡所属的项目ID 取值范围：标准UUID 约束：只有管理员有权限指定
        :type project_id: str
        :param allowed_address_pairs: 1. 扩展属性：IP/Mac对列表，allowed_address_pair参见“allowed_address_pair对象” 2. 使用说明: IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
        :param instance_id: 功能说明：辅助弹性网卡所属实例ID，例如RDS实例ID 约束： 1-64个字符
        :type instance_id: str
        :param instance_type: 功能说明：辅助弹性网卡所属实例类型，例如“RDS” 约束：1-64个字符
        :type instance_type: str
        :param tags: 辅助弹性网卡资源标签
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        
        

        self._virsubnet_id = None
        self._vlan_id = None
        self._parent_id = None
        self._description = None
        self._ipv6_enable = None
        self._private_ip_address = None
        self._ipv6_ip_address = None
        self._security_groups = None
        self._project_id = None
        self._allowed_address_pairs = None
        self._instance_id = None
        self._instance_type = None
        self._tags = None
        self.discriminator = None

        self.virsubnet_id = virsubnet_id
        if vlan_id is not None:
            self.vlan_id = vlan_id
        self.parent_id = parent_id
        if description is not None:
            self.description = description
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if ipv6_ip_address is not None:
            self.ipv6_ip_address = ipv6_ip_address
        if security_groups is not None:
            self.security_groups = security_groups
        if project_id is not None:
            self.project_id = project_id
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if tags is not None:
            self.tags = tags

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this CreateSubNetworkInterfaceOption.

        功能说明：虚拟子网ID 取值范围：标准UUID

        :return: The virsubnet_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this CreateSubNetworkInterfaceOption.

        功能说明：虚拟子网ID 取值范围：标准UUID

        :param virsubnet_id: The virsubnet_id of this CreateSubNetworkInterfaceOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的VLAN ID 取值范围：1-4094 约束：同一个宿主网络接口下唯一

        :return: The vlan_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的VLAN ID 取值范围：1-4094 约束：同一个宿主网络接口下唯一

        :param vlan_id: The vlan_id of this CreateSubNetworkInterfaceOption.
        :type vlan_id: str
        """
        self._vlan_id = vlan_id

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateSubNetworkInterfaceOption.

        功能说明：宿主网络接口的ID 取值范围：标准UUID 约束：必须是实际存在的端口ID

        :return: The parent_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateSubNetworkInterfaceOption.

        功能说明：宿主网络接口的ID 取值范围：标准UUID 约束：必须是实际存在的端口ID

        :param parent_id: The parent_id of this CreateSubNetworkInterfaceOption.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“<”和“>” 

        :return: The description of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“<”和“>” 

        :param description: The description of this CreateSubNetworkInterfaceOption.
        :type description: str
        """
        self._description = description

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡是否启用ipv6地址 取值范围：true（开启)，false（关闭） 默认值：false

        :return: The ipv6_enable of this CreateSubNetworkInterfaceOption.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡是否启用ipv6地址 取值范围：true（开启)，false（关闭） 默认值：false

        :param ipv6_enable: The ipv6_enable of this CreateSubNetworkInterfaceOption.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的私有IPv4地址 取值范围：必须在虚拟子网的网段内，不填则随机在虚拟子网网段内随机分配

        :return: The private_ip_address of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的私有IPv4地址 取值范围：必须在虚拟子网的网段内，不填则随机在虚拟子网网段内随机分配

        :param private_ip_address: The private_ip_address of this CreateSubNetworkInterfaceOption.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def ipv6_ip_address(self):
        """Gets the ipv6_ip_address of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的IPv6地址 取值范围：不填则随机分配

        :return: The ipv6_ip_address of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._ipv6_ip_address

    @ipv6_ip_address.setter
    def ipv6_ip_address(self, ipv6_ip_address):
        """Sets the ipv6_ip_address of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡的IPv6地址 取值范围：不填则随机分配

        :param ipv6_ip_address: The ipv6_ip_address of this CreateSubNetworkInterfaceOption.
        :type ipv6_ip_address: str
        """
        self._ipv6_ip_address = ipv6_ip_address

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateSubNetworkInterfaceOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 取值范围：默认值为系统默认安全组

        :return: The security_groups of this CreateSubNetworkInterfaceOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateSubNetworkInterfaceOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 取值范围：默认值为系统默认安全组

        :param security_groups: The security_groups of this CreateSubNetworkInterfaceOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def project_id(self):
        """Gets the project_id of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡所属的项目ID 取值范围：标准UUID 约束：只有管理员有权限指定

        :return: The project_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡所属的项目ID 取值范围：标准UUID 约束：只有管理员有权限指定

        :param project_id: The project_id of this CreateSubNetworkInterfaceOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this CreateSubNetworkInterfaceOption.

        1. 扩展属性：IP/Mac对列表，allowed_address_pair参见“allowed_address_pair对象” 2. 使用说明: IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。

        :return: The allowed_address_pairs of this CreateSubNetworkInterfaceOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this CreateSubNetworkInterfaceOption.

        1. 扩展属性：IP/Mac对列表，allowed_address_pair参见“allowed_address_pair对象” 2. 使用说明: IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。

        :param allowed_address_pairs: The allowed_address_pairs of this CreateSubNetworkInterfaceOption.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡所属实例ID，例如RDS实例ID 约束： 1-64个字符

        :return: The instance_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡所属实例ID，例如RDS实例ID 约束： 1-64个字符

        :param instance_id: The instance_id of this CreateSubNetworkInterfaceOption.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡所属实例类型，例如“RDS” 约束：1-64个字符

        :return: The instance_type of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this CreateSubNetworkInterfaceOption.

        功能说明：辅助弹性网卡所属实例类型，例如“RDS” 约束：1-64个字符

        :param instance_type: The instance_type of this CreateSubNetworkInterfaceOption.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def tags(self):
        """Gets the tags of this CreateSubNetworkInterfaceOption.

        辅助弹性网卡资源标签

        :return: The tags of this CreateSubNetworkInterfaceOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateSubNetworkInterfaceOption.

        辅助弹性网卡资源标签

        :param tags: The tags of this CreateSubNetworkInterfaceOption.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResourceTag`]
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
        if not isinstance(other, CreateSubNetworkInterfaceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
