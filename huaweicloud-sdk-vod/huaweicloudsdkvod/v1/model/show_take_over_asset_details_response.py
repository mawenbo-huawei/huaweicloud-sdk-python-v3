# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTakeOverAssetDetailsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'asset_status': 'str',
        'transcode_status': 'str',
        'base_info': 'BaseInfo',
        'transcode_info': 'TranscodeInfo'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_status': 'asset_status',
        'transcode_status': 'transcode_status',
        'base_info': 'base_info',
        'transcode_info': 'transcode_info'
    }

    def __init__(self, asset_id=None, asset_status=None, transcode_status=None, base_info=None, transcode_info=None):
        """ShowTakeOverAssetDetailsResponse - a model defined in huaweicloud sdk"""
        
        super(ShowTakeOverAssetDetailsResponse, self).__init__()

        self._asset_id = None
        self._asset_status = None
        self._transcode_status = None
        self._base_info = None
        self._transcode_info = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_status is not None:
            self.asset_status = asset_status
        if transcode_status is not None:
            self.transcode_status = transcode_status
        if base_info is not None:
            self.base_info = base_info
        if transcode_info is not None:
            self.transcode_info = transcode_info

    @property
    def asset_id(self):
        """Gets the asset_id of this ShowTakeOverAssetDetailsResponse.

        媒资ID。

        :return: The asset_id of this ShowTakeOverAssetDetailsResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ShowTakeOverAssetDetailsResponse.

        媒资ID。

        :param asset_id: The asset_id of this ShowTakeOverAssetDetailsResponse.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def asset_status(self):
        """Gets the asset_status of this ShowTakeOverAssetDetailsResponse.

        媒资状态。 - \"CREATING\"：上传中 - \"FAILED\"：上传失败 - \"CREATED\"：上传成功 - \"PUBLISHED\"：已发布 - \"DELETED\"：已删除

        :return: The asset_status of this ShowTakeOverAssetDetailsResponse.
        :rtype: str
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        """Sets the asset_status of this ShowTakeOverAssetDetailsResponse.

        媒资状态。 - \"CREATING\"：上传中 - \"FAILED\"：上传失败 - \"CREATED\"：上传成功 - \"PUBLISHED\"：已发布 - \"DELETED\"：已删除

        :param asset_status: The asset_status of this ShowTakeOverAssetDetailsResponse.
        :type: str
        """
        self._asset_status = asset_status

    @property
    def transcode_status(self):
        """Gets the transcode_status of this ShowTakeOverAssetDetailsResponse.

        转码状态。 - \"UN_TRANSCODE\"：未转码 - \"WAITING_TRANSCODE\"：等待转码，排队中 - \"TRANSCODING\"：转码中 - \"TRANSCODE_SUCCEED\"：转码成功 - \"TRANSCODE_FAILED\"：转码失败

        :return: The transcode_status of this ShowTakeOverAssetDetailsResponse.
        :rtype: str
        """
        return self._transcode_status

    @transcode_status.setter
    def transcode_status(self, transcode_status):
        """Sets the transcode_status of this ShowTakeOverAssetDetailsResponse.

        转码状态。 - \"UN_TRANSCODE\"：未转码 - \"WAITING_TRANSCODE\"：等待转码，排队中 - \"TRANSCODING\"：转码中 - \"TRANSCODE_SUCCEED\"：转码成功 - \"TRANSCODE_FAILED\"：转码失败

        :param transcode_status: The transcode_status of this ShowTakeOverAssetDetailsResponse.
        :type: str
        """
        self._transcode_status = transcode_status

    @property
    def base_info(self):
        """Gets the base_info of this ShowTakeOverAssetDetailsResponse.


        :return: The base_info of this ShowTakeOverAssetDetailsResponse.
        :rtype: BaseInfo
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this ShowTakeOverAssetDetailsResponse.


        :param base_info: The base_info of this ShowTakeOverAssetDetailsResponse.
        :type: BaseInfo
        """
        self._base_info = base_info

    @property
    def transcode_info(self):
        """Gets the transcode_info of this ShowTakeOverAssetDetailsResponse.


        :return: The transcode_info of this ShowTakeOverAssetDetailsResponse.
        :rtype: TranscodeInfo
        """
        return self._transcode_info

    @transcode_info.setter
    def transcode_info(self, transcode_info):
        """Sets the transcode_info of this ShowTakeOverAssetDetailsResponse.


        :param transcode_info: The transcode_info of this ShowTakeOverAssetDetailsResponse.
        :type: TranscodeInfo
        """
        self._transcode_info = transcode_info

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
        if not isinstance(other, ShowTakeOverAssetDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
