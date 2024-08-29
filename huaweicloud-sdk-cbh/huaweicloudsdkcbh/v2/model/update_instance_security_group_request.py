# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceSecurityGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'body': 'ChangeInstanceSecurityGroups'
    }

    attribute_map = {
        'server_id': 'server_id',
        'body': 'body'
    }

    def __init__(self, server_id=None, body=None):
        """UpdateInstanceSecurityGroupRequest

        The model defined in huaweicloud sdk

        :param server_id: 云堡垒机实例ID，使用UUID格式表示。  获取方法详见用户指南里面的实例\&quot;查看实例详情\&quot;
        :type server_id: str
        :param body: Body of the UpdateInstanceSecurityGroupRequest
        :type body: :class:`huaweicloudsdkcbh.v2.ChangeInstanceSecurityGroups`
        """
        
        

        self._server_id = None
        self._body = None
        self.discriminator = None

        self.server_id = server_id
        if body is not None:
            self.body = body

    @property
    def server_id(self):
        """Gets the server_id of this UpdateInstanceSecurityGroupRequest.

        云堡垒机实例ID，使用UUID格式表示。  获取方法详见用户指南里面的实例\"查看实例详情\"

        :return: The server_id of this UpdateInstanceSecurityGroupRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this UpdateInstanceSecurityGroupRequest.

        云堡垒机实例ID，使用UUID格式表示。  获取方法详见用户指南里面的实例\"查看实例详情\"

        :param server_id: The server_id of this UpdateInstanceSecurityGroupRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def body(self):
        """Gets the body of this UpdateInstanceSecurityGroupRequest.

        :return: The body of this UpdateInstanceSecurityGroupRequest.
        :rtype: :class:`huaweicloudsdkcbh.v2.ChangeInstanceSecurityGroups`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateInstanceSecurityGroupRequest.

        :param body: The body of this UpdateInstanceSecurityGroupRequest.
        :type body: :class:`huaweicloudsdkcbh.v2.ChangeInstanceSecurityGroups`
        """
        self._body = body

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
        if not isinstance(other, UpdateInstanceSecurityGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
