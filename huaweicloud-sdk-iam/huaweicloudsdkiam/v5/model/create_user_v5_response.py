# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'User'
    }

    attribute_map = {
        'user': 'user'
    }

    def __init__(self, user=None):
        """CreateUserV5Response

        The model defined in huaweicloud sdk

        :param user: 
        :type user: :class:`huaweicloudsdkiam.v5.User`
        """
        
        super(CreateUserV5Response, self).__init__()

        self._user = None
        self.discriminator = None

        if user is not None:
            self.user = user

    @property
    def user(self):
        """Gets the user of this CreateUserV5Response.

        :return: The user of this CreateUserV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.User`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CreateUserV5Response.

        :param user: The user of this CreateUserV5Response.
        :type user: :class:`huaweicloudsdkiam.v5.User`
        """
        self._user = user

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
        if not isinstance(other, CreateUserV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
