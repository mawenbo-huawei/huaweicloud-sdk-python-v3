# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScaleOutPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'body': 'UpdateScaleOutPolicyReq'
    }

    attribute_map = {
        'id': 'id',
        'body': 'body'
    }

    def __init__(self, id=None, body=None):
        """UpdateScaleOutPolicyRequest

        The model defined in huaweicloud sdk

        :param id: 策略id
        :type id: str
        :param body: Body of the UpdateScaleOutPolicyRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateScaleOutPolicyReq`
        """
        
        

        self._id = None
        self._body = None
        self.discriminator = None

        self.id = id
        if body is not None:
            self.body = body

    @property
    def id(self):
        """Gets the id of this UpdateScaleOutPolicyRequest.

        策略id

        :return: The id of this UpdateScaleOutPolicyRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateScaleOutPolicyRequest.

        策略id

        :param id: The id of this UpdateScaleOutPolicyRequest.
        :type id: str
        """
        self._id = id

    @property
    def body(self):
        """Gets the body of this UpdateScaleOutPolicyRequest.

        :return: The body of this UpdateScaleOutPolicyRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScaleOutPolicyReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateScaleOutPolicyRequest.

        :param body: The body of this UpdateScaleOutPolicyRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateScaleOutPolicyReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateScaleOutPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
