# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditlogPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keep_days': 'int'
    }

    attribute_map = {
        'keep_days': 'keep_days'
    }

    def __init__(self, keep_days=None):
        """ShowAuditlogPolicyResponse - a model defined in huaweicloud sdk"""
        
        super(ShowAuditlogPolicyResponse, self).__init__()

        self._keep_days = None
        self.discriminator = None

        if keep_days is not None:
            self.keep_days = keep_days

    @property
    def keep_days(self):
        """Gets the keep_days of this ShowAuditlogPolicyResponse.

        审计日志保存天数，取值范围0~732。0表示关闭审计日志策略。

        :return: The keep_days of this ShowAuditlogPolicyResponse.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this ShowAuditlogPolicyResponse.

        审计日志保存天数，取值范围0~732。0表示关闭审计日志策略。

        :param keep_days: The keep_days of this ShowAuditlogPolicyResponse.
        :type: int
        """
        self._keep_days = keep_days

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
        if not isinstance(other, ShowAuditlogPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
