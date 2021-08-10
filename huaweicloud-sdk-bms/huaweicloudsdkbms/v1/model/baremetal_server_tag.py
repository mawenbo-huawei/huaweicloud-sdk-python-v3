# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaremetalServerTag:


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
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        """BaremetalServerTag - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        """Gets the key of this BaremetalServerTag.

        键。  - 最大长度127个unicode字符。  - key不能为空。

        :return: The key of this BaremetalServerTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this BaremetalServerTag.

        键。  - 最大长度127个unicode字符。  - key不能为空。

        :param key: The key of this BaremetalServerTag.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this BaremetalServerTag.

        值列表。  - 最多10个value。  - value不允许重复。  - 每个值最大长度255个unicode字符。  - 如果values为空则表示any_value。  - value之间为或的关系。

        :return: The value of this BaremetalServerTag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BaremetalServerTag.

        值列表。  - 最多10个value。  - value不允许重复。  - 每个值最大长度255个unicode字符。  - 如果values为空则表示any_value。  - value之间为或的关系。

        :param value: The value of this BaremetalServerTag.
        :type: str
        """
        self._value = value

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
        if not isinstance(other, BaremetalServerTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
