# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CinderExportToImageRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'os_volume_upload_image': 'CinderExportToImageOption'
    }

    attribute_map = {
        'os_volume_upload_image': 'os-volume_upload_image'
    }

    def __init__(self, os_volume_upload_image=None):
        """CinderExportToImageRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._os_volume_upload_image = None
        self.discriminator = None

        self.os_volume_upload_image = os_volume_upload_image

    @property
    def os_volume_upload_image(self):
        """Gets the os_volume_upload_image of this CinderExportToImageRequestBody.


        :return: The os_volume_upload_image of this CinderExportToImageRequestBody.
        :rtype: CinderExportToImageOption
        """
        return self._os_volume_upload_image

    @os_volume_upload_image.setter
    def os_volume_upload_image(self, os_volume_upload_image):
        """Sets the os_volume_upload_image of this CinderExportToImageRequestBody.


        :param os_volume_upload_image: The os_volume_upload_image of this CinderExportToImageRequestBody.
        :type: CinderExportToImageOption
        """
        self._os_volume_upload_image = os_volume_upload_image

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
        if not isinstance(other, CinderExportToImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
