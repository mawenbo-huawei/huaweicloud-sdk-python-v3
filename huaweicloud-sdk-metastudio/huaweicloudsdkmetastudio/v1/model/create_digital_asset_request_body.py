# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDigitalAssetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_name': 'str',
        'asset_description': 'str',
        'asset_type': 'str',
        'asset_owner': 'str',
        'is_need_generate_cover': 'bool',
        'review_config': 'ReviewConfig',
        'tags': 'list[str]',
        'asset_extra_meta': 'AssetExtraMeta',
        'system_properties': 'list[SystemProperty]'
    }

    attribute_map = {
        'asset_name': 'asset_name',
        'asset_description': 'asset_description',
        'asset_type': 'asset_type',
        'asset_owner': 'asset_owner',
        'is_need_generate_cover': 'is_need_generate_cover',
        'review_config': 'review_config',
        'tags': 'tags',
        'asset_extra_meta': 'asset_extra_meta',
        'system_properties': 'system_properties'
    }

    def __init__(self, asset_name=None, asset_description=None, asset_type=None, asset_owner=None, is_need_generate_cover=None, review_config=None, tags=None, asset_extra_meta=None, system_properties=None):
        """CreateDigitalAssetRequestBody

        The model defined in huaweicloud sdk

        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_description: 资产描述。
        :type asset_description: str
        :param asset_type: 资产类型。  公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  3D数字人资产： * HUMAN_MODEL：3D数字人模型 * SCENE：场景模型 * ANIMATION：动作动画 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型
        :type asset_type: str
        :param asset_owner: 项目ID。 &gt; * 仅管理员帐号可设置此参数。
        :type asset_owner: str
        :param is_need_generate_cover: 是否需要资产库生成封面图片。 &gt; * 当前支持自动生成封面图片的资产类型包括VIDEO。
        :type is_need_generate_cover: bool
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param tags: 标签列表。
        :type tags: list[str]
        :param asset_extra_meta: 
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        :param system_properties: 设置系统属性。
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        
        

        self._asset_name = None
        self._asset_description = None
        self._asset_type = None
        self._asset_owner = None
        self._is_need_generate_cover = None
        self._review_config = None
        self._tags = None
        self._asset_extra_meta = None
        self._system_properties = None
        self.discriminator = None

        self.asset_name = asset_name
        if asset_description is not None:
            self.asset_description = asset_description
        self.asset_type = asset_type
        if asset_owner is not None:
            self.asset_owner = asset_owner
        if is_need_generate_cover is not None:
            self.is_need_generate_cover = is_need_generate_cover
        if review_config is not None:
            self.review_config = review_config
        if tags is not None:
            self.tags = tags
        if asset_extra_meta is not None:
            self.asset_extra_meta = asset_extra_meta
        if system_properties is not None:
            self.system_properties = system_properties

    @property
    def asset_name(self):
        """Gets the asset_name of this CreateDigitalAssetRequestBody.

        资产名称。

        :return: The asset_name of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this CreateDigitalAssetRequestBody.

        资产名称。

        :param asset_name: The asset_name of this CreateDigitalAssetRequestBody.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_description(self):
        """Gets the asset_description of this CreateDigitalAssetRequestBody.

        资产描述。

        :return: The asset_description of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        """Sets the asset_description of this CreateDigitalAssetRequestBody.

        资产描述。

        :param asset_description: The asset_description of this CreateDigitalAssetRequestBody.
        :type asset_description: str
        """
        self._asset_description = asset_description

    @property
    def asset_type(self):
        """Gets the asset_type of this CreateDigitalAssetRequestBody.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  3D数字人资产： * HUMAN_MODEL：3D数字人模型 * SCENE：场景模型 * ANIMATION：动作动画 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型

        :return: The asset_type of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this CreateDigitalAssetRequestBody.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板  3D数字人资产： * HUMAN_MODEL：3D数字人模型 * SCENE：场景模型 * ANIMATION：动作动画 * MATERIAL：风格化素材 * NORMAL_MODEL: 普通模型

        :param asset_type: The asset_type of this CreateDigitalAssetRequestBody.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_owner(self):
        """Gets the asset_owner of this CreateDigitalAssetRequestBody.

        项目ID。 > * 仅管理员帐号可设置此参数。

        :return: The asset_owner of this CreateDigitalAssetRequestBody.
        :rtype: str
        """
        return self._asset_owner

    @asset_owner.setter
    def asset_owner(self, asset_owner):
        """Sets the asset_owner of this CreateDigitalAssetRequestBody.

        项目ID。 > * 仅管理员帐号可设置此参数。

        :param asset_owner: The asset_owner of this CreateDigitalAssetRequestBody.
        :type asset_owner: str
        """
        self._asset_owner = asset_owner

    @property
    def is_need_generate_cover(self):
        """Gets the is_need_generate_cover of this CreateDigitalAssetRequestBody.

        是否需要资产库生成封面图片。 > * 当前支持自动生成封面图片的资产类型包括VIDEO。

        :return: The is_need_generate_cover of this CreateDigitalAssetRequestBody.
        :rtype: bool
        """
        return self._is_need_generate_cover

    @is_need_generate_cover.setter
    def is_need_generate_cover(self, is_need_generate_cover):
        """Sets the is_need_generate_cover of this CreateDigitalAssetRequestBody.

        是否需要资产库生成封面图片。 > * 当前支持自动生成封面图片的资产类型包括VIDEO。

        :param is_need_generate_cover: The is_need_generate_cover of this CreateDigitalAssetRequestBody.
        :type is_need_generate_cover: bool
        """
        self._is_need_generate_cover = is_need_generate_cover

    @property
    def review_config(self):
        """Gets the review_config of this CreateDigitalAssetRequestBody.

        :return: The review_config of this CreateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        """Sets the review_config of this CreateDigitalAssetRequestBody.

        :param review_config: The review_config of this CreateDigitalAssetRequestBody.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def tags(self):
        """Gets the tags of this CreateDigitalAssetRequestBody.

        标签列表。

        :return: The tags of this CreateDigitalAssetRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDigitalAssetRequestBody.

        标签列表。

        :param tags: The tags of this CreateDigitalAssetRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def asset_extra_meta(self):
        """Gets the asset_extra_meta of this CreateDigitalAssetRequestBody.

        :return: The asset_extra_meta of this CreateDigitalAssetRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        return self._asset_extra_meta

    @asset_extra_meta.setter
    def asset_extra_meta(self, asset_extra_meta):
        """Sets the asset_extra_meta of this CreateDigitalAssetRequestBody.

        :param asset_extra_meta: The asset_extra_meta of this CreateDigitalAssetRequestBody.
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.AssetExtraMeta`
        """
        self._asset_extra_meta = asset_extra_meta

    @property
    def system_properties(self):
        """Gets the system_properties of this CreateDigitalAssetRequestBody.

        设置系统属性。

        :return: The system_properties of this CreateDigitalAssetRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        """Sets the system_properties of this CreateDigitalAssetRequestBody.

        设置系统属性。

        :param system_properties: The system_properties of this CreateDigitalAssetRequestBody.
        :type system_properties: list[:class:`huaweicloudsdkmetastudio.v1.SystemProperty`]
        """
        self._system_properties = system_properties

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
        if not isinstance(other, CreateDigitalAssetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
