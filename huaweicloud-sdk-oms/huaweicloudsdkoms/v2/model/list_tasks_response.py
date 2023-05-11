# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[TaskResp]',
        'count': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'count': 'count'
    }

    def __init__(self, tasks=None, count=None):
        """ListTasksResponse

        The model defined in huaweicloud sdk

        :param tasks: 查询的任务详情
        :type tasks: list[:class:`huaweicloudsdkoms.v2.TaskResp`]
        :param count: 满足查询条件的任务总数
        :type count: int
        """
        
        super(ListTasksResponse, self).__init__()

        self._tasks = None
        self._count = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if count is not None:
            self.count = count

    @property
    def tasks(self):
        """Gets the tasks of this ListTasksResponse.

        查询的任务详情

        :return: The tasks of this ListTasksResponse.
        :rtype: list[:class:`huaweicloudsdkoms.v2.TaskResp`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ListTasksResponse.

        查询的任务详情

        :param tasks: The tasks of this ListTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkoms.v2.TaskResp`]
        """
        self._tasks = tasks

    @property
    def count(self):
        """Gets the count of this ListTasksResponse.

        满足查询条件的任务总数

        :return: The count of this ListTasksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListTasksResponse.

        满足查询条件的任务总数

        :param count: The count of this ListTasksResponse.
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
        if not isinstance(other, ListTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
