# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransfersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_transfer_type': 'str',
        'log_group_name': 'str',
        'log_stream_name': 'str'
    }

    attribute_map = {
        'log_transfer_type': 'log_transfer_type',
        'log_group_name': 'log_group_name',
        'log_stream_name': 'log_stream_name'
    }

    def __init__(self, log_transfer_type=None, log_group_name=None, log_stream_name=None):
        r"""ListTransfersRequest

        The model defined in huaweicloud sdk

        :param log_transfer_type: 日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储
        :type log_transfer_type: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        """
        
        

        self._log_transfer_type = None
        self._log_group_name = None
        self._log_stream_name = None
        self.discriminator = None

        if log_transfer_type is not None:
            self.log_transfer_type = log_transfer_type
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name

    @property
    def log_transfer_type(self):
        r"""Gets the log_transfer_type of this ListTransfersRequest.

        日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储

        :return: The log_transfer_type of this ListTransfersRequest.
        :rtype: str
        """
        return self._log_transfer_type

    @log_transfer_type.setter
    def log_transfer_type(self, log_transfer_type):
        r"""Sets the log_transfer_type of this ListTransfersRequest.

        日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储

        :param log_transfer_type: The log_transfer_type of this ListTransfersRequest.
        :type log_transfer_type: str
        """
        self._log_transfer_type = log_transfer_type

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this ListTransfersRequest.

        日志组名称

        :return: The log_group_name of this ListTransfersRequest.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this ListTransfersRequest.

        日志组名称

        :param log_group_name: The log_group_name of this ListTransfersRequest.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this ListTransfersRequest.

        日志流名称

        :return: The log_stream_name of this ListTransfersRequest.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this ListTransfersRequest.

        日志流名称

        :param log_stream_name: The log_stream_name of this ListTransfersRequest.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

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
        if not isinstance(other, ListTransfersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
