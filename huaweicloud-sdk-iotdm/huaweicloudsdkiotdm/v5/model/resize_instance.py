# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'Flavor',
        'is_auto_pay': 'bool',
        'delay': 'bool'
    }

    attribute_map = {
        'flavor': 'flavor',
        'is_auto_pay': 'is_auto_pay',
        'delay': 'delay'
    }

    def __init__(self, flavor=None, is_auto_pay=None, delay=None):
        """ResizeInstance

        The model defined in huaweicloud sdk

        :param flavor: 
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        :param is_auto_pay: **参数说明**：修改包年/包月实例的规格时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。 **取值范围**：true - 自动支付，从账户余额自动扣费; false - 默认值，只提交订单不支付。[需要客户参考[\&quot;支付包年/包月产品订单\&quot;](https://support.huaweicloud.com/api-bpconsole/api_order_00016.html#section0)进行支付，或者在华为云官网页面使用进行支付。](tag:hws) 
        :type is_auto_pay: bool
        :param delay: **参数说明**：是否延时变更设备实例的计费信息。约束：如需延时变更，需要先设置实例的变更时间窗。 **取值范围**： - true：延迟变更，规格变更任务将在指定的变更时间窗内执行。 - false：立即变更，规格变更任务将立即执行。 
        :type delay: bool
        """
        
        

        self._flavor = None
        self._is_auto_pay = None
        self._delay = None
        self.discriminator = None

        self.flavor = flavor
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if delay is not None:
            self.delay = delay

    @property
    def flavor(self):
        """Gets the flavor of this ResizeInstance.

        :return: The flavor of this ResizeInstance.
        :rtype: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ResizeInstance.

        :param flavor: The flavor of this ResizeInstance.
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        self._flavor = flavor

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ResizeInstance.

        **参数说明**：修改包年/包月实例的规格时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。 **取值范围**：true - 自动支付，从账户余额自动扣费; false - 默认值，只提交订单不支付。[需要客户参考[\"支付包年/包月产品订单\"](https://support.huaweicloud.com/api-bpconsole/api_order_00016.html#section0)进行支付，或者在华为云官网页面使用进行支付。](tag:hws) 

        :return: The is_auto_pay of this ResizeInstance.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ResizeInstance.

        **参数说明**：修改包年/包月实例的规格时可指定，表示是否自动从客户的账户中支付，此字段不影响自动续订的支付方式。 **取值范围**：true - 自动支付，从账户余额自动扣费; false - 默认值，只提交订单不支付。[需要客户参考[\"支付包年/包月产品订单\"](https://support.huaweicloud.com/api-bpconsole/api_order_00016.html#section0)进行支付，或者在华为云官网页面使用进行支付。](tag:hws) 

        :param is_auto_pay: The is_auto_pay of this ResizeInstance.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def delay(self):
        """Gets the delay of this ResizeInstance.

        **参数说明**：是否延时变更设备实例的计费信息。约束：如需延时变更，需要先设置实例的变更时间窗。 **取值范围**： - true：延迟变更，规格变更任务将在指定的变更时间窗内执行。 - false：立即变更，规格变更任务将立即执行。 

        :return: The delay of this ResizeInstance.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this ResizeInstance.

        **参数说明**：是否延时变更设备实例的计费信息。约束：如需延时变更，需要先设置实例的变更时间窗。 **取值范围**： - true：延迟变更，规格变更任务将在指定的变更时间窗内执行。 - false：立即变更，规格变更任务将立即执行。 

        :param delay: The delay of this ResizeInstance.
        :type delay: bool
        """
        self._delay = delay

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
        if not isinstance(other, ResizeInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
