# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid'
    }

    def __init__(self, name=None, uid=None):
        """NodePoolMetadata - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._uid = None
        self.discriminator = None

        self.name = name
        if uid is not None:
            self.uid = uid

    @property
    def name(self):
        """Gets the name of this NodePoolMetadata.

        节点名池名称。  > 命名规则： > >  - 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-50位，且不能以中划线(-)结尾。 > >  - 不允许创建名为 DefaultPool 的节点池。

        :return: The name of this NodePoolMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodePoolMetadata.

        节点名池名称。  > 命名规则： > >  - 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-50位，且不能以中划线(-)结尾。 > >  - 不允许创建名为 DefaultPool 的节点池。

        :param name: The name of this NodePoolMetadata.
        :type: str
        """
        self._name = name

    @property
    def uid(self):
        """Gets the uid of this NodePoolMetadata.

        节点池的uid。创建成功后自动生成，填写无效

        :return: The uid of this NodePoolMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this NodePoolMetadata.

        节点池的uid。创建成功后自动生成，填写无效

        :param uid: The uid of this NodePoolMetadata.
        :type: str
        """
        self._uid = uid

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
        if not isinstance(other, NodePoolMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
