# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePublicipOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'description': 'str',
        'associate_instance_type': 'str',
        'associate_instance_id': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'description': 'description',
        'associate_instance_type': 'associate_instance_type',
        'associate_instance_id': 'associate_instance_id'
    }

    def __init__(self, alias=None, description=None, associate_instance_type=None, associate_instance_id=None):
        """UpdatePublicipOption

        The model defined in huaweicloud sdk

        :param alias: 功能说明：公网IP的名称。
        :type alias: str
        :param description: 功能说明：公网IP的描述信息 取值范围：0-256长度的字符串，不支持特殊字符&lt;&gt;
        :type description: str
        :param associate_instance_type: 功能说明：端口所属实例类型 取值范围：PORT、NATGW、VPN、ELB、null 约束：associate_instance_type和associate_instance_id都不为空时表示绑定实例。 约束：associate_instance_type和associate_instance_id都为null时表示解绑实例，通过APIE调用需要切换为文本输入方式输入null值，可参考解绑请求实例。 约束：双栈公网IP不允许修改绑定的实例。
        :type associate_instance_type: str
        :param associate_instance_id: 功能说明：端口所属实例ID，例如RDS实例ID 约束：associate_instance_type和associate_instance_id都不为空时表示绑定实例。 约束：associate_instance_type和associate_instance_id都为null时表示解绑实例，通过APIE调用需要切换为文本输入方式输入null值，可参考解绑请求实例。 约束：双栈公网IP不允许修改绑定的实例。
        :type associate_instance_id: str
        """
        
        

        self._alias = None
        self._description = None
        self._associate_instance_type = None
        self._associate_instance_id = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description
        if associate_instance_type is not None:
            self.associate_instance_type = associate_instance_type
        if associate_instance_id is not None:
            self.associate_instance_id = associate_instance_id

    @property
    def alias(self):
        """Gets the alias of this UpdatePublicipOption.

        功能说明：公网IP的名称。

        :return: The alias of this UpdatePublicipOption.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this UpdatePublicipOption.

        功能说明：公网IP的名称。

        :param alias: The alias of this UpdatePublicipOption.
        :type alias: str
        """
        self._alias = alias

    @property
    def description(self):
        """Gets the description of this UpdatePublicipOption.

        功能说明：公网IP的描述信息 取值范围：0-256长度的字符串，不支持特殊字符<>

        :return: The description of this UpdatePublicipOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePublicipOption.

        功能说明：公网IP的描述信息 取值范围：0-256长度的字符串，不支持特殊字符<>

        :param description: The description of this UpdatePublicipOption.
        :type description: str
        """
        self._description = description

    @property
    def associate_instance_type(self):
        """Gets the associate_instance_type of this UpdatePublicipOption.

        功能说明：端口所属实例类型 取值范围：PORT、NATGW、VPN、ELB、null 约束：associate_instance_type和associate_instance_id都不为空时表示绑定实例。 约束：associate_instance_type和associate_instance_id都为null时表示解绑实例，通过APIE调用需要切换为文本输入方式输入null值，可参考解绑请求实例。 约束：双栈公网IP不允许修改绑定的实例。

        :return: The associate_instance_type of this UpdatePublicipOption.
        :rtype: str
        """
        return self._associate_instance_type

    @associate_instance_type.setter
    def associate_instance_type(self, associate_instance_type):
        """Sets the associate_instance_type of this UpdatePublicipOption.

        功能说明：端口所属实例类型 取值范围：PORT、NATGW、VPN、ELB、null 约束：associate_instance_type和associate_instance_id都不为空时表示绑定实例。 约束：associate_instance_type和associate_instance_id都为null时表示解绑实例，通过APIE调用需要切换为文本输入方式输入null值，可参考解绑请求实例。 约束：双栈公网IP不允许修改绑定的实例。

        :param associate_instance_type: The associate_instance_type of this UpdatePublicipOption.
        :type associate_instance_type: str
        """
        self._associate_instance_type = associate_instance_type

    @property
    def associate_instance_id(self):
        """Gets the associate_instance_id of this UpdatePublicipOption.

        功能说明：端口所属实例ID，例如RDS实例ID 约束：associate_instance_type和associate_instance_id都不为空时表示绑定实例。 约束：associate_instance_type和associate_instance_id都为null时表示解绑实例，通过APIE调用需要切换为文本输入方式输入null值，可参考解绑请求实例。 约束：双栈公网IP不允许修改绑定的实例。

        :return: The associate_instance_id of this UpdatePublicipOption.
        :rtype: str
        """
        return self._associate_instance_id

    @associate_instance_id.setter
    def associate_instance_id(self, associate_instance_id):
        """Sets the associate_instance_id of this UpdatePublicipOption.

        功能说明：端口所属实例ID，例如RDS实例ID 约束：associate_instance_type和associate_instance_id都不为空时表示绑定实例。 约束：associate_instance_type和associate_instance_id都为null时表示解绑实例，通过APIE调用需要切换为文本输入方式输入null值，可参考解绑请求实例。 约束：双栈公网IP不允许修改绑定的实例。

        :param associate_instance_id: The associate_instance_id of this UpdatePublicipOption.
        :type associate_instance_id: str
        """
        self._associate_instance_id = associate_instance_id

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
        if not isinstance(other, UpdatePublicipOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
