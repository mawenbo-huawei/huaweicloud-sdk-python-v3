# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowValueListResponse(SdkResponse):

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
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'values': 'list[str]',
        'producer': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'values': 'values',
        'producer': 'producer',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, name=None, type=None, description=None, values=None, producer=None, timestamp=None):
        """ShowValueListResponse

        The model defined in huaweicloud sdk

        :param id: 引用表id
        :type id: str
        :param name: 引用表名称
        :type name: str
        :param type: 引用表类型
        :type type: str
        :param description: 引用表描述
        :type description: str
        :param values: 引用表的值
        :type values: list[str]
        :param producer: 引用表来源：  - 1:表示来源于用户手动创建  - 2:表示来源于智能访问控制自动创建
        :type producer: int
        :param timestamp: 创建规则的时间，格式为13位毫秒时间戳
        :type timestamp: int
        """
        
        super(ShowValueListResponse, self).__init__()

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._values = None
        self._producer = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if values is not None:
            self.values = values
        if producer is not None:
            self.producer = producer
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this ShowValueListResponse.

        引用表id

        :return: The id of this ShowValueListResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowValueListResponse.

        引用表id

        :param id: The id of this ShowValueListResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowValueListResponse.

        引用表名称

        :return: The name of this ShowValueListResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowValueListResponse.

        引用表名称

        :param name: The name of this ShowValueListResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ShowValueListResponse.

        引用表类型

        :return: The type of this ShowValueListResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowValueListResponse.

        引用表类型

        :param type: The type of this ShowValueListResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this ShowValueListResponse.

        引用表描述

        :return: The description of this ShowValueListResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowValueListResponse.

        引用表描述

        :param description: The description of this ShowValueListResponse.
        :type description: str
        """
        self._description = description

    @property
    def values(self):
        """Gets the values of this ShowValueListResponse.

        引用表的值

        :return: The values of this ShowValueListResponse.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ShowValueListResponse.

        引用表的值

        :param values: The values of this ShowValueListResponse.
        :type values: list[str]
        """
        self._values = values

    @property
    def producer(self):
        """Gets the producer of this ShowValueListResponse.

        引用表来源：  - 1:表示来源于用户手动创建  - 2:表示来源于智能访问控制自动创建

        :return: The producer of this ShowValueListResponse.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this ShowValueListResponse.

        引用表来源：  - 1:表示来源于用户手动创建  - 2:表示来源于智能访问控制自动创建

        :param producer: The producer of this ShowValueListResponse.
        :type producer: int
        """
        self._producer = producer

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowValueListResponse.

        创建规则的时间，格式为13位毫秒时间戳

        :return: The timestamp of this ShowValueListResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowValueListResponse.

        创建规则的时间，格式为13位毫秒时间戳

        :param timestamp: The timestamp of this ShowValueListResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, ShowValueListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
