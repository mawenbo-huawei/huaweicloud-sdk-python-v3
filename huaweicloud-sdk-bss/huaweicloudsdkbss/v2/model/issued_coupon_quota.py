# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssuedCouponQuota:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'quota_id': 'str',
        'quota_type': 'int',
        'create_time': 'str',
        'last_update_time': 'str',
        'quota_value': 'float',
        'quota_status': 'int',
        'balance': 'float',
        'measure_id': 'int',
        'currency': 'str',
        'effective_time': 'str',
        'expire_time': 'str',
        'limit_infos': 'list[QuotaLimitInfo]',
        'indirect_partner_id': 'str',
        'indirect_partner_account_name': 'str',
        'indirect_partner_name': 'str',
        'parent_quota_id': 'str'
    }

    attribute_map = {
        'quota_id': 'quota_id',
        'quota_type': 'quota_type',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'quota_value': 'quota_value',
        'quota_status': 'quota_status',
        'balance': 'balance',
        'measure_id': 'measure_id',
        'currency': 'currency',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'limit_infos': 'limit_infos',
        'indirect_partner_id': 'indirect_partner_id',
        'indirect_partner_account_name': 'indirect_partner_account_name',
        'indirect_partner_name': 'indirect_partner_name',
        'parent_quota_id': 'parent_quota_id'
    }

    def __init__(self, quota_id=None, quota_type=None, create_time=None, last_update_time=None, quota_value=None, quota_status=None, balance=None, measure_id=None, currency=None, effective_time=None, expire_time=None, limit_infos=None, indirect_partner_id=None, indirect_partner_account_name=None, indirect_partner_name=None, parent_quota_id=None):
        """IssuedCouponQuota - a model defined in huaweicloud sdk"""
        
        

        self._quota_id = None
        self._quota_type = None
        self._create_time = None
        self._last_update_time = None
        self._quota_value = None
        self._quota_status = None
        self._balance = None
        self._measure_id = None
        self._currency = None
        self._effective_time = None
        self._expire_time = None
        self._limit_infos = None
        self._indirect_partner_id = None
        self._indirect_partner_account_name = None
        self._indirect_partner_name = None
        self._parent_quota_id = None
        self.discriminator = None

        if quota_id is not None:
            self.quota_id = quota_id
        if quota_type is not None:
            self.quota_type = quota_type
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if quota_value is not None:
            self.quota_value = quota_value
        if quota_status is not None:
            self.quota_status = quota_status
        if balance is not None:
            self.balance = balance
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if limit_infos is not None:
            self.limit_infos = limit_infos
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if indirect_partner_account_name is not None:
            self.indirect_partner_account_name = indirect_partner_account_name
        if indirect_partner_name is not None:
            self.indirect_partner_name = indirect_partner_name
        if parent_quota_id is not None:
            self.parent_quota_id = parent_quota_id

    @property
    def quota_id(self):
        """Gets the quota_id of this IssuedCouponQuota.

        已发放的代金券额度ID。

        :return: The quota_id of this IssuedCouponQuota.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this IssuedCouponQuota.

        已发放的代金券额度ID。

        :param quota_id: The quota_id of this IssuedCouponQuota.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def quota_type(self):
        """Gets the quota_type of this IssuedCouponQuota.

        额度类型： 0：代金券额度

        :return: The quota_type of this IssuedCouponQuota.
        :rtype: int
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        """Sets the quota_type of this IssuedCouponQuota.

        额度类型： 0：代金券额度

        :param quota_type: The quota_type of this IssuedCouponQuota.
        :type: int
        """
        self._quota_type = quota_type

    @property
    def create_time(self):
        """Gets the create_time of this IssuedCouponQuota.

        创建时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The create_time of this IssuedCouponQuota.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IssuedCouponQuota.

        创建时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param create_time: The create_time of this IssuedCouponQuota.
        :type: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this IssuedCouponQuota.

        最后一次更新时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The last_update_time of this IssuedCouponQuota.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this IssuedCouponQuota.

        最后一次更新时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param last_update_time: The last_update_time of this IssuedCouponQuota.
        :type: str
        """
        self._last_update_time = last_update_time

    @property
    def quota_value(self):
        """Gets the quota_value of this IssuedCouponQuota.

        代金券额度的值，精确到小数点后2位。

        :return: The quota_value of this IssuedCouponQuota.
        :rtype: float
        """
        return self._quota_value

    @quota_value.setter
    def quota_value(self, quota_value):
        """Sets the quota_value of this IssuedCouponQuota.

        代金券额度的值，精确到小数点后2位。

        :param quota_value: The quota_value of this IssuedCouponQuota.
        :type: float
        """
        self._quota_value = quota_value

    @property
    def quota_status(self):
        """Gets the quota_status of this IssuedCouponQuota.

        代金券额度的状态： 0：正常3：失效（包括过期失效和人工设置失效）4：额度调整中（伙伴可以查看该额度，但不能使用该额度发放代金券）5：冻结6：回收

        :return: The quota_status of this IssuedCouponQuota.
        :rtype: int
        """
        return self._quota_status

    @quota_status.setter
    def quota_status(self, quota_status):
        """Sets the quota_status of this IssuedCouponQuota.

        代金券额度的状态： 0：正常3：失效（包括过期失效和人工设置失效）4：额度调整中（伙伴可以查看该额度，但不能使用该额度发放代金券）5：冻结6：回收

        :param quota_status: The quota_status of this IssuedCouponQuota.
        :type: int
        """
        self._quota_status = quota_status

    @property
    def balance(self):
        """Gets the balance of this IssuedCouponQuota.

        剩余的代金券额度，精确到小数点后2位。

        :return: The balance of this IssuedCouponQuota.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this IssuedCouponQuota.

        剩余的代金券额度，精确到小数点后2位。

        :param balance: The balance of this IssuedCouponQuota.
        :type: float
        """
        self._balance = balance

    @property
    def measure_id(self):
        """Gets the measure_id of this IssuedCouponQuota.

        代金券额度的单位。 1：元。

        :return: The measure_id of this IssuedCouponQuota.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this IssuedCouponQuota.

        代金券额度的单位。 1：元。

        :param measure_id: The measure_id of this IssuedCouponQuota.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this IssuedCouponQuota.

        币种。 CNY：人民币

        :return: The currency of this IssuedCouponQuota.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IssuedCouponQuota.

        币种。 CNY：人民币

        :param currency: The currency of this IssuedCouponQuota.
        :type: str
        """
        self._currency = currency

    @property
    def effective_time(self):
        """Gets the effective_time of this IssuedCouponQuota.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The effective_time of this IssuedCouponQuota.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this IssuedCouponQuota.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param effective_time: The effective_time of this IssuedCouponQuota.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this IssuedCouponQuota.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this IssuedCouponQuota.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this IssuedCouponQuota.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this IssuedCouponQuota.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def limit_infos(self):
        """Gets the limit_infos of this IssuedCouponQuota.

        代金券额度上的限制属性，具体参见表3。

        :return: The limit_infos of this IssuedCouponQuota.
        :rtype: list[QuotaLimitInfo]
        """
        return self._limit_infos

    @limit_infos.setter
    def limit_infos(self, limit_infos):
        """Sets the limit_infos of this IssuedCouponQuota.

        代金券额度上的限制属性，具体参见表3。

        :param limit_infos: The limit_infos of this IssuedCouponQuota.
        :type: list[QuotaLimitInfo]
        """
        self._limit_infos = limit_infos

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this IssuedCouponQuota.

        精英服务商ID。

        :return: The indirect_partner_id of this IssuedCouponQuota.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this IssuedCouponQuota.

        精英服务商ID。

        :param indirect_partner_id: The indirect_partner_id of this IssuedCouponQuota.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def indirect_partner_account_name(self):
        """Gets the indirect_partner_account_name of this IssuedCouponQuota.

        精英服务商账号名。

        :return: The indirect_partner_account_name of this IssuedCouponQuota.
        :rtype: str
        """
        return self._indirect_partner_account_name

    @indirect_partner_account_name.setter
    def indirect_partner_account_name(self, indirect_partner_account_name):
        """Sets the indirect_partner_account_name of this IssuedCouponQuota.

        精英服务商账号名。

        :param indirect_partner_account_name: The indirect_partner_account_name of this IssuedCouponQuota.
        :type: str
        """
        self._indirect_partner_account_name = indirect_partner_account_name

    @property
    def indirect_partner_name(self):
        """Gets the indirect_partner_name of this IssuedCouponQuota.

        精英服务商名称。

        :return: The indirect_partner_name of this IssuedCouponQuota.
        :rtype: str
        """
        return self._indirect_partner_name

    @indirect_partner_name.setter
    def indirect_partner_name(self, indirect_partner_name):
        """Sets the indirect_partner_name of this IssuedCouponQuota.

        精英服务商名称。

        :param indirect_partner_name: The indirect_partner_name of this IssuedCouponQuota.
        :type: str
        """
        self._indirect_partner_name = indirect_partner_name

    @property
    def parent_quota_id(self):
        """Gets the parent_quota_id of this IssuedCouponQuota.

        父额度ID，即华为云伙伴能力中心用于发放给精英服务商代金券额度的额度ID。

        :return: The parent_quota_id of this IssuedCouponQuota.
        :rtype: str
        """
        return self._parent_quota_id

    @parent_quota_id.setter
    def parent_quota_id(self, parent_quota_id):
        """Sets the parent_quota_id of this IssuedCouponQuota.

        父额度ID，即华为云伙伴能力中心用于发放给精英服务商代金券额度的额度ID。

        :param parent_quota_id: The parent_quota_id of this IssuedCouponQuota.
        :type: str
        """
        self._parent_quota_id = parent_quota_id

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
        if not isinstance(other, IssuedCouponQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
