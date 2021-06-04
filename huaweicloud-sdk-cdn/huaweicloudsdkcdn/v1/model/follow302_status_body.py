# coding: utf-8

import pprint
import re

import six





class Follow302StatusBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'follow_status': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'follow_status': 'follow_status'
    }

    def __init__(self, domain_id=None, follow_status=None):
        """Follow302StatusBody - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._follow_status = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if follow_status is not None:
            self.follow_status = follow_status

    @property
    def domain_id(self):
        """Gets the domain_id of this Follow302StatusBody.

        加速域名id。获取方法请参见查询加速域名。

        :return: The domain_id of this Follow302StatusBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Follow302StatusBody.

        加速域名id。获取方法请参见查询加速域名。

        :param domain_id: The domain_id of this Follow302StatusBody.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def follow_status(self):
        """Gets the follow_status of this Follow302StatusBody.

        follow302状态（\"off\"/\"on\"）

        :return: The follow_status of this Follow302StatusBody.
        :rtype: str
        """
        return self._follow_status

    @follow_status.setter
    def follow_status(self, follow_status):
        """Sets the follow_status of this Follow302StatusBody.

        follow302状态（\"off\"/\"on\"）

        :param follow_status: The follow_status of this Follow302StatusBody.
        :type: str
        """
        self._follow_status = follow_status

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
        if not isinstance(other, Follow302StatusBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
