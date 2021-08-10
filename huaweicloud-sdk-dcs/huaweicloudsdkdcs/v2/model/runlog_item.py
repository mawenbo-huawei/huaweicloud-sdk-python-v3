# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunlogItem:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'file_name': 'str',
        'status': 'str',
        'time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'status': 'status',
        'time': 'time'
    }

    def __init__(self, id=None, file_name=None, status=None, time=None):
        """RunlogItem - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._file_name = None
        self._status = None
        self._time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if status is not None:
            self.status = status
        if time is not None:
            self.time = time

    @property
    def id(self):
        """Gets the id of this RunlogItem.

        日志的唯一标识

        :return: The id of this RunlogItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunlogItem.

        日志的唯一标识

        :param id: The id of this RunlogItem.
        :type: str
        """
        self._id = id

    @property
    def file_name(self):
        """Gets the file_name of this RunlogItem.

        运行日志文件名

        :return: The file_name of this RunlogItem.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this RunlogItem.

        运行日志文件名

        :param file_name: The file_name of this RunlogItem.
        :type: str
        """
        self._file_name = file_name

    @property
    def status(self):
        """Gets the status of this RunlogItem.

        获取运行日志状态

        :return: The status of this RunlogItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunlogItem.

        获取运行日志状态

        :param status: The status of this RunlogItem.
        :type: str
        """
        self._status = status

    @property
    def time(self):
        """Gets the time of this RunlogItem.

        运行日志采集的日期，格式为\"yyyy-MM-dd\"

        :return: The time of this RunlogItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this RunlogItem.

        运行日志采集的日期，格式为\"yyyy-MM-dd\"

        :param time: The time of this RunlogItem.
        :type: str
        """
        self._time = time

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
        if not isinstance(other, RunlogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
