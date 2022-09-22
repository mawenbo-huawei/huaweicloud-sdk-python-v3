# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskGroupDstNodeResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'region': 'str',
        'save_prefix': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'region': 'region',
        'save_prefix': 'save_prefix'
    }

    def __init__(self, bucket=None, region=None, save_prefix=None):
        """TaskGroupDstNodeResp

        The model defined in huaweicloud sdk

        :param bucket: 目的端桶的名称。
        :type bucket: str
        :param region: 目的端桶所处的区域。
        :type region: str
        :param save_prefix: 目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。
        :type save_prefix: str
        """
        
        

        self._bucket = None
        self._region = None
        self._save_prefix = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if region is not None:
            self.region = region
        if save_prefix is not None:
            self.save_prefix = save_prefix

    @property
    def bucket(self):
        """Gets the bucket of this TaskGroupDstNodeResp.

        目的端桶的名称。

        :return: The bucket of this TaskGroupDstNodeResp.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this TaskGroupDstNodeResp.

        目的端桶的名称。

        :param bucket: The bucket of this TaskGroupDstNodeResp.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def region(self):
        """Gets the region of this TaskGroupDstNodeResp.

        目的端桶所处的区域。

        :return: The region of this TaskGroupDstNodeResp.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TaskGroupDstNodeResp.

        目的端桶所处的区域。

        :param region: The region of this TaskGroupDstNodeResp.
        :type region: str
        """
        self._region = region

    @property
    def save_prefix(self):
        """Gets the save_prefix of this TaskGroupDstNodeResp.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :return: The save_prefix of this TaskGroupDstNodeResp.
        :rtype: str
        """
        return self._save_prefix

    @save_prefix.setter
    def save_prefix(self, save_prefix):
        """Sets the save_prefix of this TaskGroupDstNodeResp.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :param save_prefix: The save_prefix of this TaskGroupDstNodeResp.
        :type save_prefix: str
        """
        self._save_prefix = save_prefix

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
        if not isinstance(other, TaskGroupDstNodeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
