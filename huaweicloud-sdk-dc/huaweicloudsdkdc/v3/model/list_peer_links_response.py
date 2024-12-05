# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPeerLinksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'peer_links': 'list[ExternalListPeerLinks]',
        'page_info': 'PageInfo',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'peer_links': 'peer_links',
        'page_info': 'page_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, peer_links=None, page_info=None, x_request_id=None):
        """ListPeerLinksResponse

        The model defined in huaweicloud sdk

        :param request_id: 
        :type request_id: str
        :param peer_links: 
        :type peer_links: list[:class:`huaweicloudsdkdc.v3.ExternalListPeerLinks`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListPeerLinksResponse, self).__init__()

        self._request_id = None
        self._peer_links = None
        self._page_info = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if peer_links is not None:
            self.peer_links = peer_links
        if page_info is not None:
            self.page_info = page_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        """Gets the request_id of this ListPeerLinksResponse.

        :return: The request_id of this ListPeerLinksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListPeerLinksResponse.

        :param request_id: The request_id of this ListPeerLinksResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def peer_links(self):
        """Gets the peer_links of this ListPeerLinksResponse.

        :return: The peer_links of this ListPeerLinksResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.ExternalListPeerLinks`]
        """
        return self._peer_links

    @peer_links.setter
    def peer_links(self, peer_links):
        """Sets the peer_links of this ListPeerLinksResponse.

        :param peer_links: The peer_links of this ListPeerLinksResponse.
        :type peer_links: list[:class:`huaweicloudsdkdc.v3.ExternalListPeerLinks`]
        """
        self._peer_links = peer_links

    @property
    def page_info(self):
        """Gets the page_info of this ListPeerLinksResponse.

        :return: The page_info of this ListPeerLinksResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPeerLinksResponse.

        :param page_info: The page_info of this ListPeerLinksResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListPeerLinksResponse.

        :return: The x_request_id of this ListPeerLinksResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListPeerLinksResponse.

        :param x_request_id: The x_request_id of this ListPeerLinksResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListPeerLinksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
