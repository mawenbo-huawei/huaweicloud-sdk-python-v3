# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBizMetricResultData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'object'
    }

    attribute_map = {
        'value': 'value'
    }

    def __init__(self, value=None):
        """UpdateBizMetricResultData

        The model defined in huaweicloud sdk

        :param value: value，统一的返回结果的外层数据结构。
        :type value: object
        """
        
        

        self._value = None
        self.discriminator = None

        if value is not None:
            self.value = value

    @property
    def value(self):
        """Gets the value of this UpdateBizMetricResultData.

        value，统一的返回结果的外层数据结构。

        :return: The value of this UpdateBizMetricResultData.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateBizMetricResultData.

        value，统一的返回结果的外层数据结构。

        :param value: The value of this UpdateBizMetricResultData.
        :type value: object
        """
        self._value = value

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
        if not isinstance(other, UpdateBizMetricResultData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
