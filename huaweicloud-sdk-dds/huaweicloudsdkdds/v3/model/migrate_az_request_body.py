# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateAzRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'target_azs': 'str'
    }

    attribute_map = {
        'target_azs': 'target_azs'
    }

    def __init__(self, target_azs=None):
        """MigrateAzRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._target_azs = None
        self.discriminator = None

        self.target_azs = target_azs

    @property
    def target_azs(self):
        """Gets the target_azs of this MigrateAzRequestBody.

        迁移到的目标单az或者多az，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The target_azs of this MigrateAzRequestBody.
        :rtype: str
        """
        return self._target_azs

    @target_azs.setter
    def target_azs(self, target_azs):
        """Sets the target_azs of this MigrateAzRequestBody.

        迁移到的目标单az或者多az，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param target_azs: The target_azs of this MigrateAzRequestBody.
        :type: str
        """
        self._target_azs = target_azs

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
        if not isinstance(other, MigrateAzRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
