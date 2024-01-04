# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetMessageOffsetWithEngineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'instance_id': 'str',
        'group': 'str',
        'body': 'ResetMessageOffsetReq'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'group': 'group',
        'body': 'body'
    }

    def __init__(self, engine=None, instance_id=None, group=None, body=None):
        """ResetMessageOffsetWithEngineRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎。
        :type engine: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param group: 消费组名称。
        :type group: str
        :param body: Body of the ResetMessageOffsetWithEngineRequest
        :type body: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetReq`
        """
        
        

        self._engine = None
        self._instance_id = None
        self._group = None
        self._body = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.group = group
        if body is not None:
            self.body = body

    @property
    def engine(self):
        """Gets the engine of this ResetMessageOffsetWithEngineRequest.

        引擎。

        :return: The engine of this ResetMessageOffsetWithEngineRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ResetMessageOffsetWithEngineRequest.

        引擎。

        :param engine: The engine of this ResetMessageOffsetWithEngineRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        """Gets the instance_id of this ResetMessageOffsetWithEngineRequest.

        实例ID。

        :return: The instance_id of this ResetMessageOffsetWithEngineRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ResetMessageOffsetWithEngineRequest.

        实例ID。

        :param instance_id: The instance_id of this ResetMessageOffsetWithEngineRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group(self):
        """Gets the group of this ResetMessageOffsetWithEngineRequest.

        消费组名称。

        :return: The group of this ResetMessageOffsetWithEngineRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ResetMessageOffsetWithEngineRequest.

        消费组名称。

        :param group: The group of this ResetMessageOffsetWithEngineRequest.
        :type group: str
        """
        self._group = group

    @property
    def body(self):
        """Gets the body of this ResetMessageOffsetWithEngineRequest.

        :return: The body of this ResetMessageOffsetWithEngineRequest.
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ResetMessageOffsetWithEngineRequest.

        :param body: The body of this ResetMessageOffsetWithEngineRequest.
        :type body: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetReq`
        """
        self._body = body

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
        if not isinstance(other, ResetMessageOffsetWithEngineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
