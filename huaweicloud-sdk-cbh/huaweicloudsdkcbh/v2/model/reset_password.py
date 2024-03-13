# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPassword:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'server_id': 'object'
    }

    attribute_map = {
        'new_password': 'new_password',
        'server_id': 'server_id'
    }

    def __init__(self, new_password=None, server_id=None):
        """ResetPassword

        The model defined in huaweicloud sdk

        :param new_password: admin用户修改后的新密码，8-32位，大写字母、小写字母、数字和特殊字符。
        :type new_password: str
        :param server_id: 
        :type server_id: object
        """
        
        

        self._new_password = None
        self._server_id = None
        self.discriminator = None

        self.new_password = new_password
        self.server_id = server_id

    @property
    def new_password(self):
        """Gets the new_password of this ResetPassword.

        admin用户修改后的新密码，8-32位，大写字母、小写字母、数字和特殊字符。

        :return: The new_password of this ResetPassword.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ResetPassword.

        admin用户修改后的新密码，8-32位，大写字母、小写字母、数字和特殊字符。

        :param new_password: The new_password of this ResetPassword.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def server_id(self):
        """Gets the server_id of this ResetPassword.

        :return: The server_id of this ResetPassword.
        :rtype: object
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ResetPassword.

        :param server_id: The server_id of this ResetPassword.
        :type server_id: object
        """
        self._server_id = server_id

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
        if not isinstance(other, ResetPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
