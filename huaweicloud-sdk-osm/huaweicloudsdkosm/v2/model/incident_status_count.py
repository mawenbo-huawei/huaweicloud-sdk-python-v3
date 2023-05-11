# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentStatusCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'count': 'int'
    }

    attribute_map = {
        'status': 'status',
        'count': 'count'
    }

    def __init__(self, status=None, count=None):
        """IncidentStatusCount

        The model defined in huaweicloud sdk

        :param status: 状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈
        :type status: int
        :param count: 数量
        :type count: int
        """
        
        

        self._status = None
        self._count = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if count is not None:
            self.count = count

    @property
    def status(self):
        """Gets the status of this IncidentStatusCount.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :return: The status of this IncidentStatusCount.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncidentStatusCount.

        状态 0：待受理 1：处理中 2：待确认结果 3：已完成 4：已撤销 12：无效 17： 待反馈

        :param status: The status of this IncidentStatusCount.
        :type status: int
        """
        self._status = status

    @property
    def count(self):
        """Gets the count of this IncidentStatusCount.

        数量

        :return: The count of this IncidentStatusCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this IncidentStatusCount.

        数量

        :param count: The count of this IncidentStatusCount.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, IncidentStatusCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
