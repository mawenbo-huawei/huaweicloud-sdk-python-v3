# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagsMultiValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, key=None, values=None):
        """TagsMultiValue

        The model defined in huaweicloud sdk

        :param key: 资源标签键。最大长度36个unicode字符。key不能为空。（搜索时不对此参数做校验）。最多为10个，不能为空或者空字符串。且不能重复。
        :type key: str
        :param values: 资源标签值列表，每个值最大长度43个unicode字符，每个key下最多为10个，同一个key中values不能重复。  “*”为系统保留字符，如果value是以“*”开头表示按照“*”后面的值全模糊匹配。不能只传入“*”。 如果values为空列表但不可缺省，则表示any_value（查询任意value）。value之间为或的关系
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        self.key = key
        self.values = values

    @property
    def key(self):
        """Gets the key of this TagsMultiValue.

        资源标签键。最大长度36个unicode字符。key不能为空。（搜索时不对此参数做校验）。最多为10个，不能为空或者空字符串。且不能重复。

        :return: The key of this TagsMultiValue.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TagsMultiValue.

        资源标签键。最大长度36个unicode字符。key不能为空。（搜索时不对此参数做校验）。最多为10个，不能为空或者空字符串。且不能重复。

        :param key: The key of this TagsMultiValue.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this TagsMultiValue.

        资源标签值列表，每个值最大长度43个unicode字符，每个key下最多为10个，同一个key中values不能重复。  “*”为系统保留字符，如果value是以“*”开头表示按照“*”后面的值全模糊匹配。不能只传入“*”。 如果values为空列表但不可缺省，则表示any_value（查询任意value）。value之间为或的关系

        :return: The values of this TagsMultiValue.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TagsMultiValue.

        资源标签值列表，每个值最大长度43个unicode字符，每个key下最多为10个，同一个key中values不能重复。  “*”为系统保留字符，如果value是以“*”开头表示按照“*”后面的值全模糊匹配。不能只传入“*”。 如果values为空列表但不可缺省，则表示any_value（查询任意value）。value之间为或的关系

        :param values: The values of this TagsMultiValue.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, TagsMultiValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
