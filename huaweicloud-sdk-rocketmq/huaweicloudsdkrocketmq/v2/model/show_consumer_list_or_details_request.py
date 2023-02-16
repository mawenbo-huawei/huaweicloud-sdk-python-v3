# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerListOrDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'group': 'str',
        'topic': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group': 'group',
        'topic': 'topic',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, group=None, topic=None, limit=None, offset=None):
        """ShowConsumerListOrDetailsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param group: 消费组名称。
        :type group: str
        :param topic: 待查询的topic，不指定时查询topic列表，指定时查询详情。
        :type topic: str
        :param limit: 当次查询返回的最大个数,默认值为10,取值范围为1~50。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._group = None
        self._topic = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group = group
        if topic is not None:
            self.topic = topic
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowConsumerListOrDetailsRequest.

        实例ID。

        :return: The instance_id of this ShowConsumerListOrDetailsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowConsumerListOrDetailsRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowConsumerListOrDetailsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        """Gets the group of this ShowConsumerListOrDetailsRequest.

        消费组名称。

        :return: The group of this ShowConsumerListOrDetailsRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ShowConsumerListOrDetailsRequest.

        消费组名称。

        :param group: The group of this ShowConsumerListOrDetailsRequest.
        :type group: str
        """
        self._group = group

    @property
    def topic(self):
        """Gets the topic of this ShowConsumerListOrDetailsRequest.

        待查询的topic，不指定时查询topic列表，指定时查询详情。

        :return: The topic of this ShowConsumerListOrDetailsRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowConsumerListOrDetailsRequest.

        待查询的topic，不指定时查询topic列表，指定时查询详情。

        :param topic: The topic of this ShowConsumerListOrDetailsRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def limit(self):
        """Gets the limit of this ShowConsumerListOrDetailsRequest.

        当次查询返回的最大个数,默认值为10,取值范围为1~50。

        :return: The limit of this ShowConsumerListOrDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowConsumerListOrDetailsRequest.

        当次查询返回的最大个数,默认值为10,取值范围为1~50。

        :param limit: The limit of this ShowConsumerListOrDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowConsumerListOrDetailsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ShowConsumerListOrDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowConsumerListOrDetailsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ShowConsumerListOrDetailsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowConsumerListOrDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
