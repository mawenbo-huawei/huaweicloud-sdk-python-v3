# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'result': 'bool',
        'msg': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'msg': 'msg',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, result=None, msg=None, cluster_id=None):
        """CreateClusterResponse

        The model defined in huaweicloud sdk

        :param result: 操作结果。 - true：操作成功 - false：操作失败
        :type result: bool
        :param msg: 系统提示信息，可为空。
        :type msg: str
        :param cluster_id: 集群创建成功后系统返回的集群ID值。
        :type cluster_id: str
        """
        
        super(CreateClusterResponse, self).__init__()

        self._result = None
        self._msg = None
        self._cluster_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if msg is not None:
            self.msg = msg
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def result(self):
        """Gets the result of this CreateClusterResponse.

        操作结果。 - true：操作成功 - false：操作失败

        :return: The result of this CreateClusterResponse.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CreateClusterResponse.

        操作结果。 - true：操作成功 - false：操作失败

        :param result: The result of this CreateClusterResponse.
        :type result: bool
        """
        self._result = result

    @property
    def msg(self):
        """Gets the msg of this CreateClusterResponse.

        系统提示信息，可为空。

        :return: The msg of this CreateClusterResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this CreateClusterResponse.

        系统提示信息，可为空。

        :param msg: The msg of this CreateClusterResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateClusterResponse.

        集群创建成功后系统返回的集群ID值。

        :return: The cluster_id of this CreateClusterResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateClusterResponse.

        集群创建成功后系统返回的集群ID值。

        :param cluster_id: The cluster_id of this CreateClusterResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, CreateClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
