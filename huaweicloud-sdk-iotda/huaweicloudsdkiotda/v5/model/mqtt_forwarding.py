# coding: utf-8

import pprint
import re

import six





class MqttForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'topic': 'str'
    }

    attribute_map = {
        'topic': 'topic'
    }

    def __init__(self, topic=None):
        """MqttForwarding - a model defined in huaweicloud sdk"""
        
        

        self._topic = None
        self.discriminator = None

        self.topic = topic

    @property
    def topic(self):
        """Gets the topic of this MqttForwarding.

        **参数说明**：用于接收满足规则条件数据的topic。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、斜杠（/）、连接符（-）的组合。

        :return: The topic of this MqttForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this MqttForwarding.

        **参数说明**：用于接收满足规则条件数据的topic。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、斜杠（/）、连接符（-）的组合。

        :param topic: The topic of this MqttForwarding.
        :type: str
        """
        self._topic = topic

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MqttForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
