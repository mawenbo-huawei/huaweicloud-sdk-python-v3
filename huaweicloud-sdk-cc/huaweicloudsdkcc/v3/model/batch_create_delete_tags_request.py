# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateDeleteTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_type': 'str',
        'body': 'Tags'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, resource_id=None, resource_type=None, body=None):
        """BatchCreateDeleteTagsRequest

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_type: 资源类型: - cc: 云连接 - bwp: 带宽包
        :type resource_type: str
        :param body: Body of the BatchCreateDeleteTagsRequest
        :type body: :class:`huaweicloudsdkcc.v3.Tags`
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._body = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_type = resource_type
        if body is not None:
            self.body = body

    @property
    def resource_id(self):
        """Gets the resource_id of this BatchCreateDeleteTagsRequest.

        资源ID

        :return: The resource_id of this BatchCreateDeleteTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BatchCreateDeleteTagsRequest.

        资源ID

        :param resource_id: The resource_id of this BatchCreateDeleteTagsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this BatchCreateDeleteTagsRequest.

        资源类型: - cc: 云连接 - bwp: 带宽包

        :return: The resource_type of this BatchCreateDeleteTagsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BatchCreateDeleteTagsRequest.

        资源类型: - cc: 云连接 - bwp: 带宽包

        :param resource_type: The resource_type of this BatchCreateDeleteTagsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        """Gets the body of this BatchCreateDeleteTagsRequest.

        :return: The body of this BatchCreateDeleteTagsRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.Tags`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchCreateDeleteTagsRequest.

        :param body: The body of this BatchCreateDeleteTagsRequest.
        :type body: :class:`huaweicloudsdkcc.v3.Tags`
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
        if not isinstance(other, BatchCreateDeleteTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
