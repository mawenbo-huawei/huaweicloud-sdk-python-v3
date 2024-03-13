# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFindingsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'analyzer_id': 'str',
        'body': 'UpdateFindingsReqBody'
    }

    attribute_map = {
        'analyzer_id': 'analyzer_id',
        'body': 'body'
    }

    def __init__(self, analyzer_id=None, body=None):
        """UpdateFindingsRequest

        The model defined in huaweicloud sdk

        :param analyzer_id: 分析器的唯一标识符。
        :type analyzer_id: str
        :param body: Body of the UpdateFindingsRequest
        :type body: :class:`huaweicloudsdkiamaccessanalyzer.v1.UpdateFindingsReqBody`
        """
        
        

        self._analyzer_id = None
        self._body = None
        self.discriminator = None

        self.analyzer_id = analyzer_id
        if body is not None:
            self.body = body

    @property
    def analyzer_id(self):
        """Gets the analyzer_id of this UpdateFindingsRequest.

        分析器的唯一标识符。

        :return: The analyzer_id of this UpdateFindingsRequest.
        :rtype: str
        """
        return self._analyzer_id

    @analyzer_id.setter
    def analyzer_id(self, analyzer_id):
        """Sets the analyzer_id of this UpdateFindingsRequest.

        分析器的唯一标识符。

        :param analyzer_id: The analyzer_id of this UpdateFindingsRequest.
        :type analyzer_id: str
        """
        self._analyzer_id = analyzer_id

    @property
    def body(self):
        """Gets the body of this UpdateFindingsRequest.

        :return: The body of this UpdateFindingsRequest.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.UpdateFindingsReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateFindingsRequest.

        :param body: The body of this UpdateFindingsRequest.
        :type body: :class:`huaweicloudsdkiamaccessanalyzer.v1.UpdateFindingsReqBody`
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
        if not isinstance(other, UpdateFindingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
