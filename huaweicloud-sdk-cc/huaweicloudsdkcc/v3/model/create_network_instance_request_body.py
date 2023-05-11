# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNetworkInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_instance': 'CreateNetworkInstance'
    }

    attribute_map = {
        'network_instance': 'network_instance'
    }

    def __init__(self, network_instance=None):
        """CreateNetworkInstanceRequestBody

        The model defined in huaweicloud sdk

        :param network_instance: 
        :type network_instance: :class:`huaweicloudsdkcc.v3.CreateNetworkInstance`
        """
        
        

        self._network_instance = None
        self.discriminator = None

        self.network_instance = network_instance

    @property
    def network_instance(self):
        """Gets the network_instance of this CreateNetworkInstanceRequestBody.

        :return: The network_instance of this CreateNetworkInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkcc.v3.CreateNetworkInstance`
        """
        return self._network_instance

    @network_instance.setter
    def network_instance(self, network_instance):
        """Sets the network_instance of this CreateNetworkInstanceRequestBody.

        :param network_instance: The network_instance of this CreateNetworkInstanceRequestBody.
        :type network_instance: :class:`huaweicloudsdkcc.v3.CreateNetworkInstance`
        """
        self._network_instance = network_instance

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
        if not isinstance(other, CreateNetworkInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
