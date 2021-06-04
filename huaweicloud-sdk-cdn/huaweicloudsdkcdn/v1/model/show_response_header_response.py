# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowResponseHeaderResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'headers': 'HeaderMap'
    }

    attribute_map = {
        'headers': 'headers'
    }

    def __init__(self, headers=None):
        """ShowResponseHeaderResponse - a model defined in huaweicloud sdk"""
        
        super(ShowResponseHeaderResponse, self).__init__()

        self._headers = None
        self.discriminator = None

        if headers is not None:
            self.headers = headers

    @property
    def headers(self):
        """Gets the headers of this ShowResponseHeaderResponse.


        :return: The headers of this ShowResponseHeaderResponse.
        :rtype: HeaderMap
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ShowResponseHeaderResponse.


        :param headers: The headers of this ShowResponseHeaderResponse.
        :type: HeaderMap
        """
        self._headers = headers

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
        if not isinstance(other, ShowResponseHeaderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
