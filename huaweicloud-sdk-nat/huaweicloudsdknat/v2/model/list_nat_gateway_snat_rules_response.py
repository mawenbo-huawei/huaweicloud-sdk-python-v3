# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNatGatewaySnatRulesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'snat_rules': 'list[NatGatewaySnatRuleResponseBody]'
    }

    attribute_map = {
        'snat_rules': 'snat_rules'
    }

    def __init__(self, snat_rules=None):
        """ListNatGatewaySnatRulesResponse - a model defined in huaweicloud sdk"""
        
        super(ListNatGatewaySnatRulesResponse, self).__init__()

        self._snat_rules = None
        self.discriminator = None

        if snat_rules is not None:
            self.snat_rules = snat_rules

    @property
    def snat_rules(self):
        """Gets the snat_rules of this ListNatGatewaySnatRulesResponse.

        查询SNAT规则列表的响应体。

        :return: The snat_rules of this ListNatGatewaySnatRulesResponse.
        :rtype: list[NatGatewaySnatRuleResponseBody]
        """
        return self._snat_rules

    @snat_rules.setter
    def snat_rules(self, snat_rules):
        """Sets the snat_rules of this ListNatGatewaySnatRulesResponse.

        查询SNAT规则列表的响应体。

        :param snat_rules: The snat_rules of this ListNatGatewaySnatRulesResponse.
        :type: list[NatGatewaySnatRuleResponseBody]
        """
        self._snat_rules = snat_rules

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
        if not isinstance(other, ListNatGatewaySnatRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
