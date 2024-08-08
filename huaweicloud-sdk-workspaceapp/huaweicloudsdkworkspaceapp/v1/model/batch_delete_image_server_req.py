# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteImageServerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[str]',
        'recursive': 'bool'
    }

    attribute_map = {
        'items': 'items',
        'recursive': 'recursive'
    }

    def __init__(self, items=None, recursive=None):
        """BatchDeleteImageServerReq

        The model defined in huaweicloud sdk

        :param items: 批量唯一标识请求列表，一次请求数量区间 [1, 20]
        :type items: list[str]
        :param recursive: 是否同时删除镜像实例关联资源： **⚠ 警告: 关联资源删除，对应的应用将不可用** * &#x60;true&#x60; 同时删除关联资源，包括APS服务器组，APS服务器，应用组相关资源。镜像产物相关信息保留。 * &#x60;false&#x60; 只删除镜像实例记录，保留关联资源。
        :type recursive: bool
        """
        
        

        self._items = None
        self._recursive = None
        self.discriminator = None

        self.items = items
        if recursive is not None:
            self.recursive = recursive

    @property
    def items(self):
        """Gets the items of this BatchDeleteImageServerReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 20]

        :return: The items of this BatchDeleteImageServerReq.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this BatchDeleteImageServerReq.

        批量唯一标识请求列表，一次请求数量区间 [1, 20]

        :param items: The items of this BatchDeleteImageServerReq.
        :type items: list[str]
        """
        self._items = items

    @property
    def recursive(self):
        """Gets the recursive of this BatchDeleteImageServerReq.

        是否同时删除镜像实例关联资源： **⚠ 警告: 关联资源删除，对应的应用将不可用** * `true` 同时删除关联资源，包括APS服务器组，APS服务器，应用组相关资源。镜像产物相关信息保留。 * `false` 只删除镜像实例记录，保留关联资源。

        :return: The recursive of this BatchDeleteImageServerReq.
        :rtype: bool
        """
        return self._recursive

    @recursive.setter
    def recursive(self, recursive):
        """Sets the recursive of this BatchDeleteImageServerReq.

        是否同时删除镜像实例关联资源： **⚠ 警告: 关联资源删除，对应的应用将不可用** * `true` 同时删除关联资源，包括APS服务器组，APS服务器，应用组相关资源。镜像产物相关信息保留。 * `false` 只删除镜像实例记录，保留关联资源。

        :param recursive: The recursive of this BatchDeleteImageServerReq.
        :type recursive: bool
        """
        self._recursive = recursive

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
        if not isinstance(other, BatchDeleteImageServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
