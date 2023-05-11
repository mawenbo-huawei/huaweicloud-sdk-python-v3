# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobExercisesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'source_from': 'str',
        'source_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'source_from': 'source_from',
        'source_id': 'source_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, job_id=None, source_from=None, source_id=None, offset=None, limit=None):
        """ShowJobExercisesRequest

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: str
        :param source_from: 作业来源于课堂或课程。 取值范围： classroom:课堂作业 course:课程作业
        :type source_from: str
        :param source_id: 课堂ID或者课程ID。
        :type source_id: str
        :param offset: 信息记录的起始编号
        :type offset: int
        :param limit: 每页包含的信息记录数
        :type limit: int
        """
        
        

        self._job_id = None
        self._source_from = None
        self._source_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.job_id = job_id
        self.source_from = source_from
        self.source_id = source_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobExercisesRequest.

        作业ID。

        :return: The job_id of this ShowJobExercisesRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobExercisesRequest.

        作业ID。

        :param job_id: The job_id of this ShowJobExercisesRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def source_from(self):
        """Gets the source_from of this ShowJobExercisesRequest.

        作业来源于课堂或课程。 取值范围： classroom:课堂作业 course:课程作业

        :return: The source_from of this ShowJobExercisesRequest.
        :rtype: str
        """
        return self._source_from

    @source_from.setter
    def source_from(self, source_from):
        """Sets the source_from of this ShowJobExercisesRequest.

        作业来源于课堂或课程。 取值范围： classroom:课堂作业 course:课程作业

        :param source_from: The source_from of this ShowJobExercisesRequest.
        :type source_from: str
        """
        self._source_from = source_from

    @property
    def source_id(self):
        """Gets the source_id of this ShowJobExercisesRequest.

        课堂ID或者课程ID。

        :return: The source_id of this ShowJobExercisesRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ShowJobExercisesRequest.

        课堂ID或者课程ID。

        :param source_id: The source_id of this ShowJobExercisesRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def offset(self):
        """Gets the offset of this ShowJobExercisesRequest.

        信息记录的起始编号

        :return: The offset of this ShowJobExercisesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowJobExercisesRequest.

        信息记录的起始编号

        :param offset: The offset of this ShowJobExercisesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowJobExercisesRequest.

        每页包含的信息记录数

        :return: The limit of this ShowJobExercisesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowJobExercisesRequest.

        每页包含的信息记录数

        :param limit: The limit of this ShowJobExercisesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowJobExercisesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
