# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNetworkInstanceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'network_instance': 'NetworkInstance',
        'request_id': 'str'
    }

    attribute_map = {
        'network_instance': 'network_instance',
        'request_id': 'request_id'
    }

    def __init__(self, network_instance=None, request_id=None):
        """UpdateNetworkInstanceResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateNetworkInstanceResponse, self).__init__()

        self._network_instance = None
        self._request_id = None
        self.discriminator = None

        if network_instance is not None:
            self.network_instance = network_instance
        if request_id is not None:
            self.request_id = request_id

    @property
    def network_instance(self):
        """Gets the network_instance of this UpdateNetworkInstanceResponse.


        :return: The network_instance of this UpdateNetworkInstanceResponse.
        :rtype: NetworkInstance
        """
        return self._network_instance

    @network_instance.setter
    def network_instance(self, network_instance):
        """Sets the network_instance of this UpdateNetworkInstanceResponse.


        :param network_instance: The network_instance of this UpdateNetworkInstanceResponse.
        :type: NetworkInstance
        """
        self._network_instance = network_instance

    @property
    def request_id(self):
        """Gets the request_id of this UpdateNetworkInstanceResponse.

        请求ID。

        :return: The request_id of this UpdateNetworkInstanceResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateNetworkInstanceResponse.

        请求ID。

        :param request_id: The request_id of this UpdateNetworkInstanceResponse.
        :type: str
        """
        self._request_id = request_id

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
        if not isinstance(other, UpdateNetworkInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
