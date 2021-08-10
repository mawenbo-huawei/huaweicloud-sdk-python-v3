# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyFunctionCreate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'invocation_type': 'str',
        'version': 'str',
        'timeout': 'int',
        'effect_mode': 'str',
        'name': 'str',
        'backend_params': 'list[BackendParamBase]',
        'conditions': 'list[ApiConditionBase]',
        'authorizer_id': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'invocation_type': 'invocation_type',
        'version': 'version',
        'timeout': 'timeout',
        'effect_mode': 'effect_mode',
        'name': 'name',
        'backend_params': 'backend_params',
        'conditions': 'conditions',
        'authorizer_id': 'authorizer_id'
    }

    def __init__(self, function_urn=None, invocation_type=None, version=None, timeout=None, effect_mode=None, name=None, backend_params=None, conditions=None, authorizer_id=None):
        """ApiPolicyFunctionCreate - a model defined in huaweicloud sdk"""
        
        

        self._function_urn = None
        self._invocation_type = None
        self._version = None
        self._timeout = None
        self._effect_mode = None
        self._name = None
        self._backend_params = None
        self._conditions = None
        self._authorizer_id = None
        self.discriminator = None

        self.function_urn = function_urn
        self.invocation_type = invocation_type
        if version is not None:
            self.version = version
        if timeout is not None:
            self.timeout = timeout
        self.effect_mode = effect_mode
        self.name = name
        if backend_params is not None:
            self.backend_params = backend_params
        self.conditions = conditions
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id

    @property
    def function_urn(self):
        """Gets the function_urn of this ApiPolicyFunctionCreate.

        函数URN

        :return: The function_urn of this ApiPolicyFunctionCreate.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ApiPolicyFunctionCreate.

        函数URN

        :param function_urn: The function_urn of this ApiPolicyFunctionCreate.
        :type: str
        """
        self._function_urn = function_urn

    @property
    def invocation_type(self):
        """Gets the invocation_type of this ApiPolicyFunctionCreate.

        调用类型 - async： 异步 - sync：同步

        :return: The invocation_type of this ApiPolicyFunctionCreate.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        """Sets the invocation_type of this ApiPolicyFunctionCreate.

        调用类型 - async： 异步 - sync：同步

        :param invocation_type: The invocation_type of this ApiPolicyFunctionCreate.
        :type: str
        """
        self._invocation_type = invocation_type

    @property
    def version(self):
        """Gets the version of this ApiPolicyFunctionCreate.

        版本。字符长度不超过64

        :return: The version of this ApiPolicyFunctionCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiPolicyFunctionCreate.

        版本。字符长度不超过64

        :param version: The version of this ApiPolicyFunctionCreate.
        :type: str
        """
        self._version = version

    @property
    def timeout(self):
        """Gets the timeout of this ApiPolicyFunctionCreate.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :return: The timeout of this ApiPolicyFunctionCreate.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ApiPolicyFunctionCreate.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :param timeout: The timeout of this ApiPolicyFunctionCreate.
        :type: int
        """
        self._timeout = timeout

    @property
    def effect_mode(self):
        """Gets the effect_mode of this ApiPolicyFunctionCreate.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :return: The effect_mode of this ApiPolicyFunctionCreate.
        :rtype: str
        """
        return self._effect_mode

    @effect_mode.setter
    def effect_mode(self, effect_mode):
        """Sets the effect_mode of this ApiPolicyFunctionCreate.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :param effect_mode: The effect_mode of this ApiPolicyFunctionCreate.
        :type: str
        """
        self._effect_mode = effect_mode

    @property
    def name(self):
        """Gets the name of this ApiPolicyFunctionCreate.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :return: The name of this ApiPolicyFunctionCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPolicyFunctionCreate.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :param name: The name of this ApiPolicyFunctionCreate.
        :type: str
        """
        self._name = name

    @property
    def backend_params(self):
        """Gets the backend_params of this ApiPolicyFunctionCreate.

        后端参数列表

        :return: The backend_params of this ApiPolicyFunctionCreate.
        :rtype: list[BackendParamBase]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        """Sets the backend_params of this ApiPolicyFunctionCreate.

        后端参数列表

        :param backend_params: The backend_params of this ApiPolicyFunctionCreate.
        :type: list[BackendParamBase]
        """
        self._backend_params = backend_params

    @property
    def conditions(self):
        """Gets the conditions of this ApiPolicyFunctionCreate.

        策略条件列表

        :return: The conditions of this ApiPolicyFunctionCreate.
        :rtype: list[ApiConditionBase]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ApiPolicyFunctionCreate.

        策略条件列表

        :param conditions: The conditions of this ApiPolicyFunctionCreate.
        :type: list[ApiConditionBase]
        """
        self._conditions = conditions

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiPolicyFunctionCreate.

        后端自定义认证对象的ID

        :return: The authorizer_id of this ApiPolicyFunctionCreate.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiPolicyFunctionCreate.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this ApiPolicyFunctionCreate.
        :type: str
        """
        self._authorizer_id = authorizer_id

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
        if not isinstance(other, ApiPolicyFunctionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
