# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyRuleStatusRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'ruletype': 'str',
        'rule_id': 'str',
        'body': 'UpdateRuleStatusRequestBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'ruletype': 'ruletype',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, ruletype=None, rule_id=None, body=None):
        """UpdatePolicyRuleStatusRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_id = None
        self._ruletype = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        self.ruletype = ruletype
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        """Gets the policy_id of this UpdatePolicyRuleStatusRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :return: The policy_id of this UpdatePolicyRuleStatusRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this UpdatePolicyRuleStatusRequest.

        策略id（策略id从查询防护策略列表接口获取）

        :param policy_id: The policy_id of this UpdatePolicyRuleStatusRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def ruletype(self):
        """Gets the ruletype of this UpdatePolicyRuleStatusRequest.

        策略类型

        :return: The ruletype of this UpdatePolicyRuleStatusRequest.
        :rtype: str
        """
        return self._ruletype

    @ruletype.setter
    def ruletype(self, ruletype):
        """Sets the ruletype of this UpdatePolicyRuleStatusRequest.

        策略类型

        :param ruletype: The ruletype of this UpdatePolicyRuleStatusRequest.
        :type: str
        """
        self._ruletype = ruletype

    @property
    def rule_id(self):
        """Gets the rule_id of this UpdatePolicyRuleStatusRequest.

        规则id（根据不同的ruletype调用规则列表接口获取规则id）

        :return: The rule_id of this UpdatePolicyRuleStatusRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this UpdatePolicyRuleStatusRequest.

        规则id（根据不同的ruletype调用规则列表接口获取规则id）

        :param rule_id: The rule_id of this UpdatePolicyRuleStatusRequest.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        """Gets the body of this UpdatePolicyRuleStatusRequest.


        :return: The body of this UpdatePolicyRuleStatusRequest.
        :rtype: UpdateRuleStatusRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePolicyRuleStatusRequest.


        :param body: The body of this UpdatePolicyRuleStatusRequest.
        :type: UpdateRuleStatusRequestBody
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
        if not isinstance(other, UpdatePolicyRuleStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
