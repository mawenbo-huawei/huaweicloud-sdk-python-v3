# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPoolsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pools': 'list[PoolResp]'
    }

    attribute_map = {
        'pools': 'pools'
    }

    def __init__(self, pools=None):
        """ListPoolsResponse - a model defined in huaweicloud sdk"""
        
        super(ListPoolsResponse, self).__init__()

        self._pools = None
        self.discriminator = None

        if pools is not None:
            self.pools = pools

    @property
    def pools(self):
        """Gets the pools of this ListPoolsResponse.

        后端云服务器对象组列表

        :return: The pools of this ListPoolsResponse.
        :rtype: list[PoolResp]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this ListPoolsResponse.

        后端云服务器对象组列表

        :param pools: The pools of this ListPoolsResponse.
        :type: list[PoolResp]
        """
        self._pools = pools

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
