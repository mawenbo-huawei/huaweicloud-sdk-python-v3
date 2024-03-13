# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalEipDomainTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'total_count': 'int',
        'tags': 'list[GeipTags]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'total_count': 'total_count',
        'tags': 'tags',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, total_count=None, tags=None, x_request_id=None):
        """ListGlobalEipDomainTagsResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的编号
        :type request_id: str
        :param total_count: 当前列表中资源数量。
        :type total_count: int
        :param tags: tag列表信息
        :type tags: list[:class:`huaweicloudsdkgeip.v3.GeipTags`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListGlobalEipDomainTagsResponse, self).__init__()

        self._request_id = None
        self._total_count = None
        self._tags = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if total_count is not None:
            self.total_count = total_count
        if tags is not None:
            self.tags = tags
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        """Gets the request_id of this ListGlobalEipDomainTagsResponse.

        本次请求的编号

        :return: The request_id of this ListGlobalEipDomainTagsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListGlobalEipDomainTagsResponse.

        本次请求的编号

        :param request_id: The request_id of this ListGlobalEipDomainTagsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total_count(self):
        """Gets the total_count of this ListGlobalEipDomainTagsResponse.

        当前列表中资源数量。

        :return: The total_count of this ListGlobalEipDomainTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListGlobalEipDomainTagsResponse.

        当前列表中资源数量。

        :param total_count: The total_count of this ListGlobalEipDomainTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def tags(self):
        """Gets the tags of this ListGlobalEipDomainTagsResponse.

        tag列表信息

        :return: The tags of this ListGlobalEipDomainTagsResponse.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.GeipTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListGlobalEipDomainTagsResponse.

        tag列表信息

        :param tags: The tags of this ListGlobalEipDomainTagsResponse.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.GeipTags`]
        """
        self._tags = tags

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListGlobalEipDomainTagsResponse.

        :return: The x_request_id of this ListGlobalEipDomainTagsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListGlobalEipDomainTagsResponse.

        :param x_request_id: The x_request_id of this ListGlobalEipDomainTagsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListGlobalEipDomainTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
