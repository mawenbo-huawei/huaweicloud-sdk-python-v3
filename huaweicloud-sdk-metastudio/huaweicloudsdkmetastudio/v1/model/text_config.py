# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text': 'str'
    }

    attribute_map = {
        'text': 'text'
    }

    def __init__(self, text=None):
        """TextConfig

        The model defined in huaweicloud sdk

        :param text: 台词脚本。  支持两种模式，纯文本模式和标签模式。  ### 纯文本模式 纯文本模式，使用方法，如“大家好，我是人工智大家，是个虚拟主播”。  ### 标签模式 SSML标签的详细定义请参考[文本驱动SSML定义](metastudio_02_0038.xml)。
        :type text: str
        """
        
        

        self._text = None
        self.discriminator = None

        self.text = text

    @property
    def text(self):
        """Gets the text of this TextConfig.

        台词脚本。  支持两种模式，纯文本模式和标签模式。  ### 纯文本模式 纯文本模式，使用方法，如“大家好，我是人工智大家，是个虚拟主播”。  ### 标签模式 SSML标签的详细定义请参考[文本驱动SSML定义](metastudio_02_0038.xml)。

        :return: The text of this TextConfig.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextConfig.

        台词脚本。  支持两种模式，纯文本模式和标签模式。  ### 纯文本模式 纯文本模式，使用方法，如“大家好，我是人工智大家，是个虚拟主播”。  ### 标签模式 SSML标签的详细定义请参考[文本驱动SSML定义](metastudio_02_0038.xml)。

        :param text: The text of this TextConfig.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, TextConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
