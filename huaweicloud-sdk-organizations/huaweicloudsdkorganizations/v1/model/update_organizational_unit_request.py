# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOrganizationalUnitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organizational_unit_id': 'str',
        'body': 'UpdateOrganizationalUnitReqBody'
    }

    attribute_map = {
        'organizational_unit_id': 'organizational_unit_id',
        'body': 'body'
    }

    def __init__(self, organizational_unit_id=None, body=None):
        """UpdateOrganizationalUnitRequest

        The model defined in huaweicloud sdk

        :param organizational_unit_id: 与组织单元关联的唯一标识符（ID）。
        :type organizational_unit_id: str
        :param body: Body of the UpdateOrganizationalUnitRequest
        :type body: :class:`huaweicloudsdkorganizations.v1.UpdateOrganizationalUnitReqBody`
        """
        
        

        self._organizational_unit_id = None
        self._body = None
        self.discriminator = None

        self.organizational_unit_id = organizational_unit_id
        if body is not None:
            self.body = body

    @property
    def organizational_unit_id(self):
        """Gets the organizational_unit_id of this UpdateOrganizationalUnitRequest.

        与组织单元关联的唯一标识符（ID）。

        :return: The organizational_unit_id of this UpdateOrganizationalUnitRequest.
        :rtype: str
        """
        return self._organizational_unit_id

    @organizational_unit_id.setter
    def organizational_unit_id(self, organizational_unit_id):
        """Sets the organizational_unit_id of this UpdateOrganizationalUnitRequest.

        与组织单元关联的唯一标识符（ID）。

        :param organizational_unit_id: The organizational_unit_id of this UpdateOrganizationalUnitRequest.
        :type organizational_unit_id: str
        """
        self._organizational_unit_id = organizational_unit_id

    @property
    def body(self):
        """Gets the body of this UpdateOrganizationalUnitRequest.

        :return: The body of this UpdateOrganizationalUnitRequest.
        :rtype: :class:`huaweicloudsdkorganizations.v1.UpdateOrganizationalUnitReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateOrganizationalUnitRequest.

        :param body: The body of this UpdateOrganizationalUnitRequest.
        :type body: :class:`huaweicloudsdkorganizations.v1.UpdateOrganizationalUnitReqBody`
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
        if not isinstance(other, UpdateOrganizationalUnitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
