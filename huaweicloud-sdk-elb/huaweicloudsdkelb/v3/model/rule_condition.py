# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleCondition:


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
        """RuleCondition - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        """Gets the key of this RuleCondition.

        匹配项的名称。[该字段固定为空字符串](tag:dt,dt_test,hcso_dt)  [匹配项的名称。  当type为HOST_NAME、PATH、METHOD、SOURCE_IP时，该字段固定为空字符串。  当type为HEADER时，key表示请求头参数的名称，value表示请求头参数的值。key的长度限制[1,40]，只允许包含字母、数字和-_。  当type为QUERY_STRING时，key表示查询参数的名称，value表示查询参数的值。key的长度限制为[1,128]，不支持空格，中括号，大括号，尖括号，反斜杠，双引号，'#'，'&'，'|'，'%'，'~'，字母区分大小写。](tag:hws,hws_hk,ocb,tlf,ctc,hcso,sbc,g42,tm,cmcc,hk-g42)

        :return: The key of this RuleCondition.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RuleCondition.

        匹配项的名称。[该字段固定为空字符串](tag:dt,dt_test,hcso_dt)  [匹配项的名称。  当type为HOST_NAME、PATH、METHOD、SOURCE_IP时，该字段固定为空字符串。  当type为HEADER时，key表示请求头参数的名称，value表示请求头参数的值。key的长度限制[1,40]，只允许包含字母、数字和-_。  当type为QUERY_STRING时，key表示查询参数的名称，value表示查询参数的值。key的长度限制为[1,128]，不支持空格，中括号，大括号，尖括号，反斜杠，双引号，'#'，'&'，'|'，'%'，'~'，字母区分大小写。](tag:hws,hws_hk,ocb,tlf,ctc,hcso,sbc,g42,tm,cmcc,hk-g42)

        :param key: The key of this RuleCondition.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this RuleCondition.

        匹配项的值。  当type为HOST_NAME时，key固定为空字符串，value表示域名的值。value长度[1，128]，字符串只能包含英文字母、数字、\"-\"、\".\"或\"*\"，必须以字母、数字或\"*\"开头，\"*\"只能出现在开头且必须以*.开始。  当type为PATH时，key固定为空字符串，value表示请求路径的值。value长度[1，128]。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%\\#&$.*+?,=!:|/()[]{}，且必须以\"/\"开头。  [当type为HEADER时，key表示请求头参数的名称，value表示请求头参数的值。value长度限制[1,128]，不支持空格，双引号，支持以下通配符：*（匹配0个或更多字符）和？（正好匹配1个字符）。  当type为QUERY_STRING时，key表示查询参数的名称，value表示查询参数的值。value长度限制为[1,128]，不支持空格，中括号，大括号，尖括号，反斜杠，双引号，'#'，'&'，'|'，'%'，'~'，字母区分大小写，支持通配符：*（匹配0个或更多字符）和？（正好匹配1个字符）  当type为METHOD时，key固定为空字符串，value表示请求方式。value取值范围为：GET, PUT, POST, DELETE, PATCH, HEAD, OPTIONS。  当type为SOURCE_IP时，key固定为空字符串，value表示请求源地址。value为CIDR格式，支持ipv4，ipv6。例如：192.168.0.2/32，2049::49/64。](tag:hws,hws_hk,ocb,tlf,ctc,hcso,sbc,g42,tm,cmcc,hk-g42)

        :return: The value of this RuleCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RuleCondition.

        匹配项的值。  当type为HOST_NAME时，key固定为空字符串，value表示域名的值。value长度[1，128]，字符串只能包含英文字母、数字、\"-\"、\".\"或\"*\"，必须以字母、数字或\"*\"开头，\"*\"只能出现在开头且必须以*.开始。  当type为PATH时，key固定为空字符串，value表示请求路径的值。value长度[1，128]。当转发规则的compare_type为STARTS_WITH、EQUAL_TO时，字符串只能包含英文字母、数字、_~';@^-%\\#&$.*+?,=!:|/()[]{}，且必须以\"/\"开头。  [当type为HEADER时，key表示请求头参数的名称，value表示请求头参数的值。value长度限制[1,128]，不支持空格，双引号，支持以下通配符：*（匹配0个或更多字符）和？（正好匹配1个字符）。  当type为QUERY_STRING时，key表示查询参数的名称，value表示查询参数的值。value长度限制为[1,128]，不支持空格，中括号，大括号，尖括号，反斜杠，双引号，'#'，'&'，'|'，'%'，'~'，字母区分大小写，支持通配符：*（匹配0个或更多字符）和？（正好匹配1个字符）  当type为METHOD时，key固定为空字符串，value表示请求方式。value取值范围为：GET, PUT, POST, DELETE, PATCH, HEAD, OPTIONS。  当type为SOURCE_IP时，key固定为空字符串，value表示请求源地址。value为CIDR格式，支持ipv4，ipv6。例如：192.168.0.2/32，2049::49/64。](tag:hws,hws_hk,ocb,tlf,ctc,hcso,sbc,g42,tm,cmcc,hk-g42)

        :param value: The value of this RuleCondition.
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
        if not isinstance(other, RuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
