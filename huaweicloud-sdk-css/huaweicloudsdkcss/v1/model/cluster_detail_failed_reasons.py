# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDetailFailedReasons:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_msg': 'errorMsg'
    }

    def __init__(self, error_code=None, error_msg=None):
        """ClusterDetailFailedReasons

        The model defined in huaweicloud sdk

        :param error_code: 错误码。  - CSS.6000：表示集群创建失败。 - CSS.6001：表示集群扩容失败。 - CSS.6002：表示集群重启失败。 - CSS.6004：表示集群节点创建失败。 - CSS.6005：表示服务初始化失败。
        :type error_code: str
        :param error_msg: 详细错误信息。
        :type error_msg: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this ClusterDetailFailedReasons.

        错误码。  - CSS.6000：表示集群创建失败。 - CSS.6001：表示集群扩容失败。 - CSS.6002：表示集群重启失败。 - CSS.6004：表示集群节点创建失败。 - CSS.6005：表示服务初始化失败。

        :return: The error_code of this ClusterDetailFailedReasons.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ClusterDetailFailedReasons.

        错误码。  - CSS.6000：表示集群创建失败。 - CSS.6001：表示集群扩容失败。 - CSS.6002：表示集群重启失败。 - CSS.6004：表示集群节点创建失败。 - CSS.6005：表示服务初始化失败。

        :param error_code: The error_code of this ClusterDetailFailedReasons.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ClusterDetailFailedReasons.

        详细错误信息。

        :return: The error_msg of this ClusterDetailFailedReasons.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ClusterDetailFailedReasons.

        详细错误信息。

        :param error_msg: The error_msg of this ClusterDetailFailedReasons.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ClusterDetailFailedReasons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
