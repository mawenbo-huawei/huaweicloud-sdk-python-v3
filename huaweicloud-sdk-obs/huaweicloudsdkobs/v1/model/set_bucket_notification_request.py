# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketNotificationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SetBucketNotificationRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'notification': 'str',
        'body': 'SetBucketNotificationRequestBody'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'notification': 'notification',
        'body': 'body'
    }

    def __init__(self, date=None, bucket_name=None, notification=None, body=None):
        """SetBucketNotificationRequest

        The model defined in huaweicloud sdk

        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param bucket_name: 请求的桶名称。 
        :type bucket_name: str
        :param notification: notification表示请求桶的消息通知配置API。 
        :type notification: str
        :param body: Body of the SetBucketNotificationRequest
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequestBody`
        """
        
        

        self._date = None
        self._bucket_name = None
        self._notification = None
        self._body = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.notification = notification
        if body is not None:
            self.body = body

    @property
    def date(self):
        """Gets the date of this SetBucketNotificationRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this SetBucketNotificationRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this SetBucketNotificationRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this SetBucketNotificationRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        """Gets the bucket_name of this SetBucketNotificationRequest.

        请求的桶名称。 

        :return: The bucket_name of this SetBucketNotificationRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this SetBucketNotificationRequest.

        请求的桶名称。 

        :param bucket_name: The bucket_name of this SetBucketNotificationRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def notification(self):
        """Gets the notification of this SetBucketNotificationRequest.

        notification表示请求桶的消息通知配置API。 

        :return: The notification of this SetBucketNotificationRequest.
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this SetBucketNotificationRequest.

        notification表示请求桶的消息通知配置API。 

        :param notification: The notification of this SetBucketNotificationRequest.
        :type notification: str
        """
        self._notification = notification

    @property
    def body(self):
        """Gets the body of this SetBucketNotificationRequest.

        :return: The body of this SetBucketNotificationRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SetBucketNotificationRequest.

        :param body: The body of this SetBucketNotificationRequest.
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketNotificationRequestBody`
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
        if not isinstance(other, SetBucketNotificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
