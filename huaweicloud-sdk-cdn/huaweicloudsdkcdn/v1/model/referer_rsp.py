# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefererRsp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'referer_type': 'int',
        'referer_list': 'str',
        'include_empty': 'bool'
    }

    attribute_map = {
        'referer_type': 'referer_type',
        'referer_list': 'referer_list',
        'include_empty': 'include_empty'
    }

    def __init__(self, referer_type=None, referer_list=None, include_empty=None):
        """RefererRsp - a model defined in huaweicloud sdk"""
        
        

        self._referer_type = None
        self._referer_list = None
        self._include_empty = None
        self.discriminator = None

        if referer_type is not None:
            self.referer_type = referer_type
        if referer_list is not None:
            self.referer_list = referer_list
        if include_empty is not None:
            self.include_empty = include_empty

    @property
    def referer_type(self):
        """Gets the referer_type of this RefererRsp.

        Referer类型。取值：0代表不设置Referer过滤；1代表黑名单；2代表白名单。默认取值为0。

        :return: The referer_type of this RefererRsp.
        :rtype: int
        """
        return self._referer_type

    @referer_type.setter
    def referer_type(self, referer_type):
        """Sets the referer_type of this RefererRsp.

        Referer类型。取值：0代表不设置Referer过滤；1代表黑名单；2代表白名单。默认取值为0。

        :param referer_type: The referer_type of this RefererRsp.
        :type: int
        """
        self._referer_type = referer_type

    @property
    def referer_list(self):
        """Gets the referer_list of this RefererRsp.

        请输入域名或IP地址，以“;”进行分割，域名、IP地址可以混合输入，支持泛域名添加。输入的域名、IP地址总数不超过100个。当设置防盗链时，此项必填。

        :return: The referer_list of this RefererRsp.
        :rtype: str
        """
        return self._referer_list

    @referer_list.setter
    def referer_list(self, referer_list):
        """Sets the referer_list of this RefererRsp.

        请输入域名或IP地址，以“;”进行分割，域名、IP地址可以混合输入，支持泛域名添加。输入的域名、IP地址总数不超过100个。当设置防盗链时，此项必填。

        :param referer_list: The referer_list of this RefererRsp.
        :type: str
        """
        self._referer_list = referer_list

    @property
    def include_empty(self):
        """Gets the include_empty of this RefererRsp.

        是否包含空Referer。如果是黑名单并开启该选项，则表示无referer不允许访问。如果是白名单并开启该选项，则表示无referer允许访问。默认不包含。

        :return: The include_empty of this RefererRsp.
        :rtype: bool
        """
        return self._include_empty

    @include_empty.setter
    def include_empty(self, include_empty):
        """Sets the include_empty of this RefererRsp.

        是否包含空Referer。如果是黑名单并开启该选项，则表示无referer不允许访问。如果是白名单并开启该选项，则表示无referer允许访问。默认不包含。

        :param include_empty: The include_empty of this RefererRsp.
        :type: bool
        """
        self._include_empty = include_empty

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
        if not isinstance(other, RefererRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
