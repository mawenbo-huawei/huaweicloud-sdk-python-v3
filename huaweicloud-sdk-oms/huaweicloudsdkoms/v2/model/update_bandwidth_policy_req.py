# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBandwidthPolicyReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidth_policy': 'list[BandwidthPolicyDto]'
    }

    attribute_map = {
        'bandwidth_policy': 'bandwidth_policy'
    }

    def __init__(self, bandwidth_policy=None):
        """UpdateBandwidthPolicyReq - a model defined in huaweicloud sdk"""
        
        

        self._bandwidth_policy = None
        self.discriminator = None

        self.bandwidth_policy = bandwidth_policy

    @property
    def bandwidth_policy(self):
        """Gets the bandwidth_policy of this UpdateBandwidthPolicyReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :return: The bandwidth_policy of this UpdateBandwidthPolicyReq.
        :rtype: list[BandwidthPolicyDto]
        """
        return self._bandwidth_policy

    @bandwidth_policy.setter
    def bandwidth_policy(self, bandwidth_policy):
        """Sets the bandwidth_policy of this UpdateBandwidthPolicyReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :param bandwidth_policy: The bandwidth_policy of this UpdateBandwidthPolicyReq.
        :type: list[BandwidthPolicyDto]
        """
        self._bandwidth_policy = bandwidth_policy

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
        if not isinstance(other, UpdateBandwidthPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
