# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSpecResponse:

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
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'subject': 'str',
        'category': 'str',
        'severity': 'str',
        'source_type': 'str',
        'name_space': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'display_name',
        'description': 'description',
        'subject': 'subject',
        'category': 'category',
        'severity': 'severity',
        'source_type': 'source_type',
        'name_space': 'name_space'
    }

    def __init__(self, id=None, name=None, display_name=None, description=None, subject=None, category=None, severity=None, source_type=None, name_space=None):
        """EventSpecResponse

        The model defined in huaweicloud sdk

        :param id: 事件配置ID
        :type id: str
        :param name: 事件配置定义名称
        :type name: str
        :param display_name: 事件配置显示名称
        :type display_name: str
        :param description: 事件配置描述
        :type description: str
        :param subject: 事件主题
        :type subject: str
        :param category: 事件类别
        :type category: str
        :param severity: 事件级别
        :type severity: str
        :param source_type: 事件源类型
        :type source_type: str
        :param name_space: 所属服务
        :type name_space: str
        """
        
        

        self._id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._subject = None
        self._category = None
        self._severity = None
        self._source_type = None
        self._name_space = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if subject is not None:
            self.subject = subject
        if category is not None:
            self.category = category
        if severity is not None:
            self.severity = severity
        if source_type is not None:
            self.source_type = source_type
        if name_space is not None:
            self.name_space = name_space

    @property
    def id(self):
        """Gets the id of this EventSpecResponse.

        事件配置ID

        :return: The id of this EventSpecResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventSpecResponse.

        事件配置ID

        :param id: The id of this EventSpecResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EventSpecResponse.

        事件配置定义名称

        :return: The name of this EventSpecResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventSpecResponse.

        事件配置定义名称

        :param name: The name of this EventSpecResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this EventSpecResponse.

        事件配置显示名称

        :return: The display_name of this EventSpecResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EventSpecResponse.

        事件配置显示名称

        :param display_name: The display_name of this EventSpecResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this EventSpecResponse.

        事件配置描述

        :return: The description of this EventSpecResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventSpecResponse.

        事件配置描述

        :param description: The description of this EventSpecResponse.
        :type description: str
        """
        self._description = description

    @property
    def subject(self):
        """Gets the subject of this EventSpecResponse.

        事件主题

        :return: The subject of this EventSpecResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EventSpecResponse.

        事件主题

        :param subject: The subject of this EventSpecResponse.
        :type subject: str
        """
        self._subject = subject

    @property
    def category(self):
        """Gets the category of this EventSpecResponse.

        事件类别

        :return: The category of this EventSpecResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EventSpecResponse.

        事件类别

        :param category: The category of this EventSpecResponse.
        :type category: str
        """
        self._category = category

    @property
    def severity(self):
        """Gets the severity of this EventSpecResponse.

        事件级别

        :return: The severity of this EventSpecResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this EventSpecResponse.

        事件级别

        :param severity: The severity of this EventSpecResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def source_type(self):
        """Gets the source_type of this EventSpecResponse.

        事件源类型

        :return: The source_type of this EventSpecResponse.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this EventSpecResponse.

        事件源类型

        :param source_type: The source_type of this EventSpecResponse.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def name_space(self):
        """Gets the name_space of this EventSpecResponse.

        所属服务

        :return: The name_space of this EventSpecResponse.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this EventSpecResponse.

        所属服务

        :param name_space: The name_space of this EventSpecResponse.
        :type name_space: str
        """
        self._name_space = name_space

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
        if not isinstance(other, EventSpecResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
