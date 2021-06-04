# coding: utf-8

import pprint
import re

import six





class TagOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, key=None, values=None):
        """TagOption - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        self.key = key
        self.values = values

    @property
    def key(self):
        """Gets the key of this TagOption.

        标签键。最大长度36个unicode字符，key不能为空或者空字符串，不能为空格，校验和使用之前先排除前后半角空格。搜索时不对该参数做字符集校验。

        :return: The key of this TagOption.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TagOption.

        标签键。最大长度36个unicode字符，key不能为空或者空字符串，不能为空格，校验和使用之前先排除前后半角空格。搜索时不对该参数做字符集校验。

        :param key: The key of this TagOption.
        :type: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this TagOption.

        标签值列表。最大长度43个unicode字符，不能为空格，校验和使用之前先排除前后半角空格。如果values为空列表，则表示查询任意value。value之间为或的关系。

        :return: The values of this TagOption.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TagOption.

        标签值列表。最大长度43个unicode字符，不能为空格，校验和使用之前先排除前后半角空格。如果values为空列表，则表示查询任意value。value之间为或的关系。

        :param values: The values of this TagOption.
        :type: list[str]
        """
        self._values = values

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
        if not isinstance(other, TagOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
