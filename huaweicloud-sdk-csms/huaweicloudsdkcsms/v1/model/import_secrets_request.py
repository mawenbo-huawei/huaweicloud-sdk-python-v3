# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportSecretsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secrets': 'list[CreateSecretRequestBody]',
        'total': 'int'
    }

    attribute_map = {
        'secrets': 'secrets',
        'total': 'total'
    }

    def __init__(self, secrets=None, total=None):
        """ImportSecretsRequest

        The model defined in huaweicloud sdk

        :param secrets: 批量创建凭据参数
        :type secrets: list[:class:`huaweicloudsdkcsms.v1.CreateSecretRequestBody`]
        :param total: 导入数据条数
        :type total: int
        """
        
        

        self._secrets = None
        self._total = None
        self.discriminator = None

        self.secrets = secrets
        self.total = total

    @property
    def secrets(self):
        """Gets the secrets of this ImportSecretsRequest.

        批量创建凭据参数

        :return: The secrets of this ImportSecretsRequest.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.CreateSecretRequestBody`]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this ImportSecretsRequest.

        批量创建凭据参数

        :param secrets: The secrets of this ImportSecretsRequest.
        :type secrets: list[:class:`huaweicloudsdkcsms.v1.CreateSecretRequestBody`]
        """
        self._secrets = secrets

    @property
    def total(self):
        """Gets the total of this ImportSecretsRequest.

        导入数据条数

        :return: The total of this ImportSecretsRequest.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ImportSecretsRequest.

        导入数据条数

        :param total: The total of this ImportSecretsRequest.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ImportSecretsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
