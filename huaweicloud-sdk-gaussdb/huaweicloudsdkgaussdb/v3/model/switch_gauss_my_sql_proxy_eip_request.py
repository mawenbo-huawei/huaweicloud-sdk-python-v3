# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchGaussMySqlProxyEipRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'proxy_id': 'str',
        'body': 'SwitchGaussMySqlProxyEipRequestBody'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'proxy_id': 'proxy_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, instance_id=None, proxy_id=None, body=None):
        r"""SwitchGaussMySqlProxyEipRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: 实例ID，此参数是实例的唯一标识。只能由英文字母、数字组成，后缀为in07，长度为36个字符。
        :type instance_id: str
        :param proxy_id: 数据库代理ID，此参数是代理的唯一标识。只能由英文字母、数字组成，后缀为po01，长度为36个字符。
        :type proxy_id: str
        :param body: Body of the SwitchGaussMySqlProxyEipRequest
        :type body: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxyEipRequestBody`
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._proxy_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.proxy_id = proxy_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this SwitchGaussMySqlProxyEipRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this SwitchGaussMySqlProxyEipRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this SwitchGaussMySqlProxyEipRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this SwitchGaussMySqlProxyEipRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SwitchGaussMySqlProxyEipRequest.

        实例ID，此参数是实例的唯一标识。只能由英文字母、数字组成，后缀为in07，长度为36个字符。

        :return: The instance_id of this SwitchGaussMySqlProxyEipRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SwitchGaussMySqlProxyEipRequest.

        实例ID，此参数是实例的唯一标识。只能由英文字母、数字组成，后缀为in07，长度为36个字符。

        :param instance_id: The instance_id of this SwitchGaussMySqlProxyEipRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this SwitchGaussMySqlProxyEipRequest.

        数据库代理ID，此参数是代理的唯一标识。只能由英文字母、数字组成，后缀为po01，长度为36个字符。

        :return: The proxy_id of this SwitchGaussMySqlProxyEipRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this SwitchGaussMySqlProxyEipRequest.

        数据库代理ID，此参数是代理的唯一标识。只能由英文字母、数字组成，后缀为po01，长度为36个字符。

        :param proxy_id: The proxy_id of this SwitchGaussMySqlProxyEipRequest.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def body(self):
        r"""Gets the body of this SwitchGaussMySqlProxyEipRequest.

        :return: The body of this SwitchGaussMySqlProxyEipRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxyEipRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SwitchGaussMySqlProxyEipRequest.

        :param body: The body of this SwitchGaussMySqlProxyEipRequest.
        :type body: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxyEipRequestBody`
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
        if not isinstance(other, SwitchGaussMySqlProxyEipRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
