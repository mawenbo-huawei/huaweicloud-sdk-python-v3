# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfo:

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
        'links': 'list[Links]'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links'
    }

    def __init__(self, id=None, links=None):
        """FlavorInfo

        The model defined in huaweicloud sdk

        :param id: 规格ID
        :type id: str
        :param links: 规格相关信息快捷链接
        :type links: list[:class:`huaweicloudsdkbms.v1.Links`]
        """
        
        

        self._id = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this FlavorInfo.

        规格ID

        :return: The id of this FlavorInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlavorInfo.

        规格ID

        :param id: The id of this FlavorInfo.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this FlavorInfo.

        规格相关信息快捷链接

        :return: The links of this FlavorInfo.
        :rtype: list[:class:`huaweicloudsdkbms.v1.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FlavorInfo.

        规格相关信息快捷链接

        :param links: The links of this FlavorInfo.
        :type links: list[:class:`huaweicloudsdkbms.v1.Links`]
        """
        self._links = links

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
        if not isinstance(other, FlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
