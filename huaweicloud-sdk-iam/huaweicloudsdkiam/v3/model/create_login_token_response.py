# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoginTokenResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'logintoken': 'LoginToken',
        'x_subject_login_token': 'str'
    }

    attribute_map = {
        'logintoken': 'logintoken',
        'x_subject_login_token': 'X-Subject-LoginToken'
    }

    def __init__(self, logintoken=None, x_subject_login_token=None):
        """CreateLoginTokenResponse - a model defined in huaweicloud sdk"""
        
        super(CreateLoginTokenResponse, self).__init__()

        self._logintoken = None
        self._x_subject_login_token = None
        self.discriminator = None

        if logintoken is not None:
            self.logintoken = logintoken
        if x_subject_login_token is not None:
            self.x_subject_login_token = x_subject_login_token

    @property
    def logintoken(self):
        """Gets the logintoken of this CreateLoginTokenResponse.


        :return: The logintoken of this CreateLoginTokenResponse.
        :rtype: LoginToken
        """
        return self._logintoken

    @logintoken.setter
    def logintoken(self, logintoken):
        """Sets the logintoken of this CreateLoginTokenResponse.


        :param logintoken: The logintoken of this CreateLoginTokenResponse.
        :type: LoginToken
        """
        self._logintoken = logintoken

    @property
    def x_subject_login_token(self):
        """Gets the x_subject_login_token of this CreateLoginTokenResponse.


        :return: The x_subject_login_token of this CreateLoginTokenResponse.
        :rtype: str
        """
        return self._x_subject_login_token

    @x_subject_login_token.setter
    def x_subject_login_token(self, x_subject_login_token):
        """Sets the x_subject_login_token of this CreateLoginTokenResponse.


        :param x_subject_login_token: The x_subject_login_token of this CreateLoginTokenResponse.
        :type: str
        """
        self._x_subject_login_token = x_subject_login_token

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
        if not isinstance(other, CreateLoginTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
