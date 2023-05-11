# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[Tag]',
        'total': 'int'
    }

    attribute_map = {
        'tags': 'tags',
        'total': 'total'
    }

    def __init__(self, tags=None, total=None):
        """TagList

        The model defined in huaweicloud sdk

        :param tags: 指定仓库的标签列表
        :type tags: list[:class:`huaweicloudsdkcodehub.v3.Tag`]
        :param total: 指定仓库的标签总数
        :type total: int
        """
        
        

        self._tags = None
        self._total = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if total is not None:
            self.total = total

    @property
    def tags(self):
        """Gets the tags of this TagList.

        指定仓库的标签列表

        :return: The tags of this TagList.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TagList.

        指定仓库的标签列表

        :param tags: The tags of this TagList.
        :type tags: list[:class:`huaweicloudsdkcodehub.v3.Tag`]
        """
        self._tags = tags

    @property
    def total(self):
        """Gets the total of this TagList.

        指定仓库的标签总数

        :return: The total of this TagList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TagList.

        指定仓库的标签总数

        :param total: The total of this TagList.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, TagList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
