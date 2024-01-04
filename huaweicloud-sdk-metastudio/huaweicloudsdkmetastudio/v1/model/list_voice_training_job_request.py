# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVoiceTrainingJobRequest:

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
        'create_until': 'str',
        'create_since': 'str',
        'x_app_user_id': 'str',
        'state': 'str',
        'job_id': 'str',
        'voice_name': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'create_until': 'create_until',
        'create_since': 'create_since',
        'x_app_user_id': 'X-App-UserId',
        'state': 'state',
        'job_id': 'job_id',
        'voice_name': 'voice_name',
        'tag': 'tag'
    }

    def __init__(self, offset=None, limit=None, create_until=None, create_since=None, x_app_user_id=None, state=None, job_id=None, voice_name=None, tag=None):
        """ListVoiceTrainingJobRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。
        :type create_until: str
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。
        :type create_since: str
        :param x_app_user_id: 第三方用户ID。 &gt; *不允许输入中文。
        :type x_app_user_id: str
        :param state: 任务状态，默认所有状态。 可多个状态查询，使用英文逗号分隔。 如state&#x3D;FAILED,WAITING
        :type state: str
        :param job_id: 任务id。
        :type job_id: str
        :param voice_name: 声音名称。
        :type voice_name: str
        :param tag: 任务标签。
        :type tag: str
        """
        
        

        self._offset = None
        self._limit = None
        self._create_until = None
        self._create_since = None
        self._x_app_user_id = None
        self._state = None
        self._job_id = None
        self._voice_name = None
        self._tag = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if create_until is not None:
            self.create_until = create_until
        if create_since is not None:
            self.create_since = create_since
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if state is not None:
            self.state = state
        if job_id is not None:
            self.job_id = job_id
        if voice_name is not None:
            self.voice_name = voice_name
        if tag is not None:
            self.tag = tag

    @property
    def offset(self):
        """Gets the offset of this ListVoiceTrainingJobRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListVoiceTrainingJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVoiceTrainingJobRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListVoiceTrainingJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListVoiceTrainingJobRequest.

        每页显示的条目数量。

        :return: The limit of this ListVoiceTrainingJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVoiceTrainingJobRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListVoiceTrainingJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def create_until(self):
        """Gets the create_until of this ListVoiceTrainingJobRequest.

        过滤创建时间<=输入时间的记录。

        :return: The create_until of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        """Sets the create_until of this ListVoiceTrainingJobRequest.

        过滤创建时间<=输入时间的记录。

        :param create_until: The create_until of this ListVoiceTrainingJobRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def create_since(self):
        """Gets the create_since of this ListVoiceTrainingJobRequest.

        过滤创建时间>=输入时间的记录。

        :return: The create_since of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        """Sets the create_since of this ListVoiceTrainingJobRequest.

        过滤创建时间>=输入时间的记录。

        :param create_since: The create_since of this ListVoiceTrainingJobRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this ListVoiceTrainingJobRequest.

        第三方用户ID。 > *不允许输入中文。

        :return: The x_app_user_id of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this ListVoiceTrainingJobRequest.

        第三方用户ID。 > *不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListVoiceTrainingJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def state(self):
        """Gets the state of this ListVoiceTrainingJobRequest.

        任务状态，默认所有状态。 可多个状态查询，使用英文逗号分隔。 如state=FAILED,WAITING

        :return: The state of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListVoiceTrainingJobRequest.

        任务状态，默认所有状态。 可多个状态查询，使用英文逗号分隔。 如state=FAILED,WAITING

        :param state: The state of this ListVoiceTrainingJobRequest.
        :type state: str
        """
        self._state = state

    @property
    def job_id(self):
        """Gets the job_id of this ListVoiceTrainingJobRequest.

        任务id。

        :return: The job_id of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListVoiceTrainingJobRequest.

        任务id。

        :param job_id: The job_id of this ListVoiceTrainingJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def voice_name(self):
        """Gets the voice_name of this ListVoiceTrainingJobRequest.

        声音名称。

        :return: The voice_name of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        """Sets the voice_name of this ListVoiceTrainingJobRequest.

        声音名称。

        :param voice_name: The voice_name of this ListVoiceTrainingJobRequest.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def tag(self):
        """Gets the tag of this ListVoiceTrainingJobRequest.

        任务标签。

        :return: The tag of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListVoiceTrainingJobRequest.

        任务标签。

        :param tag: The tag of this ListVoiceTrainingJobRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ListVoiceTrainingJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
