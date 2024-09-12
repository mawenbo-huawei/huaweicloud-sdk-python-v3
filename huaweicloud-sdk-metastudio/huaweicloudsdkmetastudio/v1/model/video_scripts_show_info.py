# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoScriptsShowInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_name': 'str',
        'script_description': 'str',
        'view_mode': 'str',
        'model_asset_id': 'str',
        'model_asset_type': 'str',
        'voice_config': 'VoiceConfig',
        'video_config': 'VideoConfig',
        'scene_asset_id': 'str',
        'priv_data': 'str',
        'background_music_config': 'BackgroundMusicConfig',
        'review_config': 'ReviewConfig',
        'shoot_scripts': 'list[ShootScriptShowItem]'
    }

    attribute_map = {
        'script_name': 'script_name',
        'script_description': 'script_description',
        'view_mode': 'view_mode',
        'model_asset_id': 'model_asset_id',
        'model_asset_type': 'model_asset_type',
        'voice_config': 'voice_config',
        'video_config': 'video_config',
        'scene_asset_id': 'scene_asset_id',
        'priv_data': 'priv_data',
        'background_music_config': 'background_music_config',
        'review_config': 'review_config',
        'shoot_scripts': 'shoot_scripts'
    }

    def __init__(self, script_name=None, script_description=None, view_mode=None, model_asset_id=None, model_asset_type=None, voice_config=None, video_config=None, scene_asset_id=None, priv_data=None, background_music_config=None, review_config=None, shoot_scripts=None):
        """VideoScriptsShowInfo

        The model defined in huaweicloud sdk

        :param script_name: **参数解释**： 剧本名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度1-256位。 **默认取值**： 不涉及。
        :type script_name: str
        :param script_description: **参数解释**： 剧本描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。
        :type script_description: str
        :param view_mode: **参数解释**： 横竖屏类型。 **约束限制**： 不涉及。 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL：竖屏。
        :type view_mode: str
        :param model_asset_id: **参数解释**： 数字人模型资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及
        :type model_asset_id: str
        :param model_asset_type: **参数解释**： 数字人模型类型。 **约束限制**： 不涉及 **取值范围**： * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人  **默认取值**： 不涉及
        :type model_asset_type: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param scene_asset_id: **参数解释**： 场景资产ID。 **约束限制**： 分身数字人视频制作不需要填写该参数。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及
        :type scene_asset_id: str
        :param priv_data: **参数解释**： 私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192位 **默认取值**： 不涉及
        :type priv_data: str
        :param background_music_config: 
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param shoot_scripts: 拍摄脚本列表。
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptShowItem`]
        """
        
        

        self._script_name = None
        self._script_description = None
        self._view_mode = None
        self._model_asset_id = None
        self._model_asset_type = None
        self._voice_config = None
        self._video_config = None
        self._scene_asset_id = None
        self._priv_data = None
        self._background_music_config = None
        self._review_config = None
        self._shoot_scripts = None
        self.discriminator = None

        if script_name is not None:
            self.script_name = script_name
        if script_description is not None:
            self.script_description = script_description
        if view_mode is not None:
            self.view_mode = view_mode
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if model_asset_type is not None:
            self.model_asset_type = model_asset_type
        if voice_config is not None:
            self.voice_config = voice_config
        if video_config is not None:
            self.video_config = video_config
        if scene_asset_id is not None:
            self.scene_asset_id = scene_asset_id
        if priv_data is not None:
            self.priv_data = priv_data
        if background_music_config is not None:
            self.background_music_config = background_music_config
        if review_config is not None:
            self.review_config = review_config
        if shoot_scripts is not None:
            self.shoot_scripts = shoot_scripts

    @property
    def script_name(self):
        """Gets the script_name of this VideoScriptsShowInfo.

        **参数解释**： 剧本名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度1-256位。 **默认取值**： 不涉及。

        :return: The script_name of this VideoScriptsShowInfo.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this VideoScriptsShowInfo.

        **参数解释**： 剧本名称。 **约束限制**： 不涉及。 **取值范围**： 只能使用中英文字符，字符长度1-256位。 **默认取值**： 不涉及。

        :param script_name: The script_name of this VideoScriptsShowInfo.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_description(self):
        """Gets the script_description of this VideoScriptsShowInfo.

        **参数解释**： 剧本描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。

        :return: The script_description of this VideoScriptsShowInfo.
        :rtype: str
        """
        return self._script_description

    @script_description.setter
    def script_description(self, script_description):
        """Sets the script_description of this VideoScriptsShowInfo.

        **参数解释**： 剧本描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。

        :param script_description: The script_description of this VideoScriptsShowInfo.
        :type script_description: str
        """
        self._script_description = script_description

    @property
    def view_mode(self):
        """Gets the view_mode of this VideoScriptsShowInfo.

        **参数解释**： 横竖屏类型。 **约束限制**： 不涉及。 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL：竖屏。

        :return: The view_mode of this VideoScriptsShowInfo.
        :rtype: str
        """
        return self._view_mode

    @view_mode.setter
    def view_mode(self, view_mode):
        """Sets the view_mode of this VideoScriptsShowInfo.

        **参数解释**： 横竖屏类型。 **约束限制**： 不涉及。 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL：竖屏。

        :param view_mode: The view_mode of this VideoScriptsShowInfo.
        :type view_mode: str
        """
        self._view_mode = view_mode

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this VideoScriptsShowInfo.

        **参数解释**： 数字人模型资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及

        :return: The model_asset_id of this VideoScriptsShowInfo.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this VideoScriptsShowInfo.

        **参数解释**： 数字人模型资产ID。 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及

        :param model_asset_id: The model_asset_id of this VideoScriptsShowInfo.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def model_asset_type(self):
        """Gets the model_asset_type of this VideoScriptsShowInfo.

        **参数解释**： 数字人模型类型。 **约束限制**： 不涉及 **取值范围**： * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人  **默认取值**： 不涉及

        :return: The model_asset_type of this VideoScriptsShowInfo.
        :rtype: str
        """
        return self._model_asset_type

    @model_asset_type.setter
    def model_asset_type(self, model_asset_type):
        """Sets the model_asset_type of this VideoScriptsShowInfo.

        **参数解释**： 数字人模型类型。 **约束限制**： 不涉及 **取值范围**： * HUMAN_MODEL_2D：分身数字人 * HUMAN_MODEL_3D：3D数字人  **默认取值**： 不涉及

        :param model_asset_type: The model_asset_type of this VideoScriptsShowInfo.
        :type model_asset_type: str
        """
        self._model_asset_type = model_asset_type

    @property
    def voice_config(self):
        """Gets the voice_config of this VideoScriptsShowInfo.

        :return: The voice_config of this VideoScriptsShowInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this VideoScriptsShowInfo.

        :param voice_config: The voice_config of this VideoScriptsShowInfo.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def video_config(self):
        """Gets the video_config of this VideoScriptsShowInfo.

        :return: The video_config of this VideoScriptsShowInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this VideoScriptsShowInfo.

        :param video_config: The video_config of this VideoScriptsShowInfo.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def scene_asset_id(self):
        """Gets the scene_asset_id of this VideoScriptsShowInfo.

        **参数解释**： 场景资产ID。 **约束限制**： 分身数字人视频制作不需要填写该参数。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :return: The scene_asset_id of this VideoScriptsShowInfo.
        :rtype: str
        """
        return self._scene_asset_id

    @scene_asset_id.setter
    def scene_asset_id(self, scene_asset_id):
        """Sets the scene_asset_id of this VideoScriptsShowInfo.

        **参数解释**： 场景资产ID。 **约束限制**： 分身数字人视频制作不需要填写该参数。 **取值范围**： 字符长度0-64位 **默认取值**： 不涉及

        :param scene_asset_id: The scene_asset_id of this VideoScriptsShowInfo.
        :type scene_asset_id: str
        """
        self._scene_asset_id = scene_asset_id

    @property
    def priv_data(self):
        """Gets the priv_data of this VideoScriptsShowInfo.

        **参数解释**： 私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192位 **默认取值**： 不涉及

        :return: The priv_data of this VideoScriptsShowInfo.
        :rtype: str
        """
        return self._priv_data

    @priv_data.setter
    def priv_data(self, priv_data):
        """Sets the priv_data of this VideoScriptsShowInfo.

        **参数解释**： 私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192位 **默认取值**： 不涉及

        :param priv_data: The priv_data of this VideoScriptsShowInfo.
        :type priv_data: str
        """
        self._priv_data = priv_data

    @property
    def background_music_config(self):
        """Gets the background_music_config of this VideoScriptsShowInfo.

        :return: The background_music_config of this VideoScriptsShowInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        return self._background_music_config

    @background_music_config.setter
    def background_music_config(self, background_music_config):
        """Sets the background_music_config of this VideoScriptsShowInfo.

        :param background_music_config: The background_music_config of this VideoScriptsShowInfo.
        :type background_music_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundMusicConfig`
        """
        self._background_music_config = background_music_config

    @property
    def review_config(self):
        """Gets the review_config of this VideoScriptsShowInfo.

        :return: The review_config of this VideoScriptsShowInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        """Sets the review_config of this VideoScriptsShowInfo.

        :param review_config: The review_config of this VideoScriptsShowInfo.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def shoot_scripts(self):
        """Gets the shoot_scripts of this VideoScriptsShowInfo.

        拍摄脚本列表。

        :return: The shoot_scripts of this VideoScriptsShowInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptShowItem`]
        """
        return self._shoot_scripts

    @shoot_scripts.setter
    def shoot_scripts(self, shoot_scripts):
        """Sets the shoot_scripts of this VideoScriptsShowInfo.

        拍摄脚本列表。

        :param shoot_scripts: The shoot_scripts of this VideoScriptsShowInfo.
        :type shoot_scripts: list[:class:`huaweicloudsdkmetastudio.v1.ShootScriptShowItem`]
        """
        self._shoot_scripts = shoot_scripts

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
        if not isinstance(other, VideoScriptsShowInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
