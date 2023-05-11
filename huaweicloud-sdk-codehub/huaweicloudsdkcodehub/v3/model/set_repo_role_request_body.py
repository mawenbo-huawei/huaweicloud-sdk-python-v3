# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRepoRoleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'int'
    }

    attribute_map = {
        'role': 'role'
    }

    def __init__(self, role=None):
        """SetRepoRoleRequestBody

        The model defined in huaweicloud sdk

        :param role: 设置仓库的成员权限，取值范围：20 -&gt; 只读成员 30-&gt;普通成员，40-&gt;管理员
        :type role: int
        """
        
        

        self._role = None
        self.discriminator = None

        self.role = role

    @property
    def role(self):
        """Gets the role of this SetRepoRoleRequestBody.

        设置仓库的成员权限，取值范围：20 -> 只读成员 30->普通成员，40->管理员

        :return: The role of this SetRepoRoleRequestBody.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SetRepoRoleRequestBody.

        设置仓库的成员权限，取值范围：20 -> 只读成员 30->普通成员，40->管理员

        :param role: The role of this SetRepoRoleRequestBody.
        :type role: int
        """
        self._role = role

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
        if not isinstance(other, SetRepoRoleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
