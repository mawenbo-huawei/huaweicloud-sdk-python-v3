# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagValuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'values': 'list[str]',
        'page_info': 'PageInfoTagValues'
    }

    attribute_map = {
        'values': 'values',
        'page_info': 'page_info'
    }

    def __init__(self, values=None, page_info=None):
        """ListTagValuesResponse

        The model defined in huaweicloud sdk

        :param values: 查询到的标签值列表
        :type values: list[str]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfoTagValues`
        """
        
        super(ListTagValuesResponse, self).__init__()

        self._values = None
        self._page_info = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if page_info is not None:
            self.page_info = page_info

    @property
    def values(self):
        """Gets the values of this ListTagValuesResponse.

        查询到的标签值列表

        :return: The values of this ListTagValuesResponse.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ListTagValuesResponse.

        查询到的标签值列表

        :param values: The values of this ListTagValuesResponse.
        :type values: list[str]
        """
        self._values = values

    @property
    def page_info(self):
        """Gets the page_info of this ListTagValuesResponse.

        :return: The page_info of this ListTagValuesResponse.
        :rtype: :class:`huaweicloudsdktms.v1.PageInfoTagValues`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListTagValuesResponse.

        :param page_info: The page_info of this ListTagValuesResponse.
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfoTagValues`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListTagValuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
