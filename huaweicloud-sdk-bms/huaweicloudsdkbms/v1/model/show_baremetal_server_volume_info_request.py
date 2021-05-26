# coding: utf-8

import pprint
import re

import six





class ShowBaremetalServerVolumeInfoRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_id': 'str'
    }

    attribute_map = {
        'server_id': 'server_id'
    }

    def __init__(self, server_id=None):
        """ShowBaremetalServerVolumeInfoRequest - a model defined in huaweicloud sdk"""
        
        

        self._server_id = None
        self.discriminator = None

        self.server_id = server_id

    @property
    def server_id(self):
        """Gets the server_id of this ShowBaremetalServerVolumeInfoRequest.

        裸金属服务器ID。可以从裸金属服务器控制台查询，或者通过调用7.3.4-查询裸金属服务器列表（OpenStack原生）API获取。

        :return: The server_id of this ShowBaremetalServerVolumeInfoRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ShowBaremetalServerVolumeInfoRequest.

        裸金属服务器ID。可以从裸金属服务器控制台查询，或者通过调用7.3.4-查询裸金属服务器列表（OpenStack原生）API获取。

        :param server_id: The server_id of this ShowBaremetalServerVolumeInfoRequest.
        :type: str
        """
        self._server_id = server_id

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
        if not isinstance(other, ShowBaremetalServerVolumeInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
