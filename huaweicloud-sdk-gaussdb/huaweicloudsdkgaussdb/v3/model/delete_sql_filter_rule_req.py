# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSqlFilterRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sql_filter_rules': 'list[DeleteNodeSqlFilterRuleInfo]'
    }

    attribute_map = {
        'sql_filter_rules': 'sql_filter_rules'
    }

    def __init__(self, sql_filter_rules=None):
        """DeleteSqlFilterRuleReq

        The model defined in huaweicloud sdk

        :param sql_filter_rules: 
        :type sql_filter_rules: list[:class:`huaweicloudsdkgaussdb.v3.DeleteNodeSqlFilterRuleInfo`]
        """
        
        

        self._sql_filter_rules = None
        self.discriminator = None

        self.sql_filter_rules = sql_filter_rules

    @property
    def sql_filter_rules(self):
        """Gets the sql_filter_rules of this DeleteSqlFilterRuleReq.


        :return: The sql_filter_rules of this DeleteSqlFilterRuleReq.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DeleteNodeSqlFilterRuleInfo`]
        """
        return self._sql_filter_rules

    @sql_filter_rules.setter
    def sql_filter_rules(self, sql_filter_rules):
        """Sets the sql_filter_rules of this DeleteSqlFilterRuleReq.


        :param sql_filter_rules: The sql_filter_rules of this DeleteSqlFilterRuleReq.
        :type sql_filter_rules: list[:class:`huaweicloudsdkgaussdb.v3.DeleteNodeSqlFilterRuleInfo`]
        """
        self._sql_filter_rules = sql_filter_rules

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
        if not isinstance(other, DeleteSqlFilterRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
