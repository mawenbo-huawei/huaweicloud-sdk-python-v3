# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOfficialTemplateResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_size': 'float',
        'items': 'list[TemplateList]'
    }

    attribute_map = {
        'total_size': 'total_size',
        'items': 'items'
    }

    def __init__(self, total_size=None, items=None):
        r"""ListOfficialTemplateResult

        The model defined in huaweicloud sdk

        :param total_size: 总数
        :type total_size: float
        :param items: 模版列表
        :type items: list[:class:`huaweicloudsdkcodeartsbuild.v3.TemplateList`]
        """
        
        

        self._total_size = None
        self._items = None
        self.discriminator = None

        if total_size is not None:
            self.total_size = total_size
        if items is not None:
            self.items = items

    @property
    def total_size(self):
        r"""Gets the total_size of this ListOfficialTemplateResult.

        总数

        :return: The total_size of this ListOfficialTemplateResult.
        :rtype: float
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListOfficialTemplateResult.

        总数

        :param total_size: The total_size of this ListOfficialTemplateResult.
        :type total_size: float
        """
        self._total_size = total_size

    @property
    def items(self):
        r"""Gets the items of this ListOfficialTemplateResult.

        模版列表

        :return: The items of this ListOfficialTemplateResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.TemplateList`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListOfficialTemplateResult.

        模版列表

        :param items: The items of this ListOfficialTemplateResult.
        :type items: list[:class:`huaweicloudsdkcodeartsbuild.v3.TemplateList`]
        """
        self._items = items

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
        if not isinstance(other, ListOfficialTemplateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
