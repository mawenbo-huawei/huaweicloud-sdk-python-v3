# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentQueryResponseRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'DocumentQueryResponseRequestParamsData',
        'event_type': 'str',
        'image_categories': 'list[str]',
        'text_categories': 'list[str]',
        'video_image_categories': 'list[str]',
        'audio_categories': 'list[str]',
        'param_callback': 'str'
    }

    attribute_map = {
        'data': 'data',
        'event_type': 'event_type',
        'image_categories': 'image_categories',
        'text_categories': 'text_categories',
        'video_image_categories': 'video_image_categories',
        'audio_categories': 'audio_categories',
        'param_callback': 'callback'
    }

    def __init__(self, data=None, event_type=None, image_categories=None, text_categories=None, video_image_categories=None, audio_categories=None, param_callback=None):
        """DocumentQueryResponseRequestParams

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseRequestParamsData`
        :param event_type: 创建作业时传的event_type参数
        :type event_type: str
        :param image_categories: 创建作业时传的image_categories参数
        :type image_categories: list[str]
        :param text_categories: 创建作业时传的text_categories参数
        :type text_categories: list[str]
        :param video_image_categories: 创建作业时传的video_image_categories参数
        :type video_image_categories: list[str]
        :param audio_categories: 创建作业时传的audio_categories参数
        :type audio_categories: list[str]
        :param param_callback: 创建作业时传的callback参数
        :type param_callback: str
        """
        
        

        self._data = None
        self._event_type = None
        self._image_categories = None
        self._text_categories = None
        self._video_image_categories = None
        self._audio_categories = None
        self._param_callback = None
        self.discriminator = None

        self.data = data
        self.event_type = event_type
        if image_categories is not None:
            self.image_categories = image_categories
        if text_categories is not None:
            self.text_categories = text_categories
        if video_image_categories is not None:
            self.video_image_categories = video_image_categories
        if audio_categories is not None:
            self.audio_categories = audio_categories
        if param_callback is not None:
            self.param_callback = param_callback

    @property
    def data(self):
        """Gets the data of this DocumentQueryResponseRequestParams.

        :return: The data of this DocumentQueryResponseRequestParams.
        :rtype: :class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseRequestParamsData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DocumentQueryResponseRequestParams.

        :param data: The data of this DocumentQueryResponseRequestParams.
        :type data: :class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseRequestParamsData`
        """
        self._data = data

    @property
    def event_type(self):
        """Gets the event_type of this DocumentQueryResponseRequestParams.

        创建作业时传的event_type参数

        :return: The event_type of this DocumentQueryResponseRequestParams.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this DocumentQueryResponseRequestParams.

        创建作业时传的event_type参数

        :param event_type: The event_type of this DocumentQueryResponseRequestParams.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def image_categories(self):
        """Gets the image_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的image_categories参数

        :return: The image_categories of this DocumentQueryResponseRequestParams.
        :rtype: list[str]
        """
        return self._image_categories

    @image_categories.setter
    def image_categories(self, image_categories):
        """Sets the image_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的image_categories参数

        :param image_categories: The image_categories of this DocumentQueryResponseRequestParams.
        :type image_categories: list[str]
        """
        self._image_categories = image_categories

    @property
    def text_categories(self):
        """Gets the text_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的text_categories参数

        :return: The text_categories of this DocumentQueryResponseRequestParams.
        :rtype: list[str]
        """
        return self._text_categories

    @text_categories.setter
    def text_categories(self, text_categories):
        """Sets the text_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的text_categories参数

        :param text_categories: The text_categories of this DocumentQueryResponseRequestParams.
        :type text_categories: list[str]
        """
        self._text_categories = text_categories

    @property
    def video_image_categories(self):
        """Gets the video_image_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的video_image_categories参数

        :return: The video_image_categories of this DocumentQueryResponseRequestParams.
        :rtype: list[str]
        """
        return self._video_image_categories

    @video_image_categories.setter
    def video_image_categories(self, video_image_categories):
        """Sets the video_image_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的video_image_categories参数

        :param video_image_categories: The video_image_categories of this DocumentQueryResponseRequestParams.
        :type video_image_categories: list[str]
        """
        self._video_image_categories = video_image_categories

    @property
    def audio_categories(self):
        """Gets the audio_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的audio_categories参数

        :return: The audio_categories of this DocumentQueryResponseRequestParams.
        :rtype: list[str]
        """
        return self._audio_categories

    @audio_categories.setter
    def audio_categories(self, audio_categories):
        """Sets the audio_categories of this DocumentQueryResponseRequestParams.

        创建作业时传的audio_categories参数

        :param audio_categories: The audio_categories of this DocumentQueryResponseRequestParams.
        :type audio_categories: list[str]
        """
        self._audio_categories = audio_categories

    @property
    def param_callback(self):
        """Gets the param_callback of this DocumentQueryResponseRequestParams.

        创建作业时传的callback参数

        :return: The param_callback of this DocumentQueryResponseRequestParams.
        :rtype: str
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        """Sets the param_callback of this DocumentQueryResponseRequestParams.

        创建作业时传的callback参数

        :param param_callback: The param_callback of this DocumentQueryResponseRequestParams.
        :type param_callback: str
        """
        self._param_callback = param_callback

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
        if not isinstance(other, DocumentQueryResponseRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
