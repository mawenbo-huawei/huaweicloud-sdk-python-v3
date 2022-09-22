# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMeetingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'user_uuid': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str',
        'body': 'RestScheduleConfDTO'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'user_uuid': 'userUUID',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id',
        'body': 'body'
    }

    def __init__(self, conference_id=None, user_uuid=None, x_authorization_type=None, x_site_id=None, body=None):
        """UpdateMeetingRequest

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。 &gt; 创建会议时返回的conferenceID。不是vmrConferenceID。 
        :type conference_id: str
        :param user_uuid: 用户的UUID。 &gt; 该参数将废弃，请勿使用。 
        :type user_uuid: str
        :param x_authorization_type: 标识是否为第三方portal过来的请求。 &gt; 该参数将废弃，请勿使用。 
        :type x_authorization_type: str
        :param x_site_id: 用于区分到哪个HCSO站点鉴权。 &gt; 该参数将废弃，请勿使用。 
        :type x_site_id: str
        :param body: Body of the UpdateMeetingRequest
        :type body: :class:`huaweicloudsdkmeeting.v1.RestScheduleConfDTO`
        """
        
        

        self._conference_id = None
        self._user_uuid = None
        self._x_authorization_type = None
        self._x_site_id = None
        self._body = None
        self.discriminator = None

        self.conference_id = conference_id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id
        if body is not None:
            self.body = body

    @property
    def conference_id(self):
        """Gets the conference_id of this UpdateMeetingRequest.

        会议ID。 > 创建会议时返回的conferenceID。不是vmrConferenceID。 

        :return: The conference_id of this UpdateMeetingRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this UpdateMeetingRequest.

        会议ID。 > 创建会议时返回的conferenceID。不是vmrConferenceID。 

        :param conference_id: The conference_id of this UpdateMeetingRequest.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this UpdateMeetingRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。 

        :return: The user_uuid of this UpdateMeetingRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this UpdateMeetingRequest.

        用户的UUID。 > 该参数将废弃，请勿使用。 

        :param user_uuid: The user_uuid of this UpdateMeetingRequest.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this UpdateMeetingRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :return: The x_authorization_type of this UpdateMeetingRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this UpdateMeetingRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :param x_authorization_type: The x_authorization_type of this UpdateMeetingRequest.
        :type x_authorization_type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this UpdateMeetingRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :return: The x_site_id of this UpdateMeetingRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this UpdateMeetingRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :param x_site_id: The x_site_id of this UpdateMeetingRequest.
        :type x_site_id: str
        """
        self._x_site_id = x_site_id

    @property
    def body(self):
        """Gets the body of this UpdateMeetingRequest.


        :return: The body of this UpdateMeetingRequest.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RestScheduleConfDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateMeetingRequest.


        :param body: The body of this UpdateMeetingRequest.
        :type body: :class:`huaweicloudsdkmeeting.v1.RestScheduleConfDTO`
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
        if not isinstance(other, UpdateMeetingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
