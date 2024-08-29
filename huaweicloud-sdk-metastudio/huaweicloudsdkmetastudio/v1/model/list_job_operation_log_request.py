# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobOperationLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'job_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'job_id': 'job_id'
    }

    def __init__(self, offset=None, limit=None, job_id=None):
        """ListJobOperationLogRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param job_id: 任务id
        :type job_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._job_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.job_id = job_id

    @property
    def offset(self):
        """Gets the offset of this ListJobOperationLogRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListJobOperationLogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListJobOperationLogRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListJobOperationLogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListJobOperationLogRequest.

        每页显示的条目数量。

        :return: The limit of this ListJobOperationLogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListJobOperationLogRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListJobOperationLogRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def job_id(self):
        """Gets the job_id of this ListJobOperationLogRequest.

        任务id

        :return: The job_id of this ListJobOperationLogRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListJobOperationLogRequest.

        任务id

        :param job_id: The job_id of this ListJobOperationLogRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ListJobOperationLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
