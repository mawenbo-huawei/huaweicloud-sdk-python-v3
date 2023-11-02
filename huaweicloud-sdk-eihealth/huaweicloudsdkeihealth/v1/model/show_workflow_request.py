# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'show_param_detail': 'bool',
        'eihealth_project_id': 'str',
        'workflow_id': 'str'
    }

    attribute_map = {
        'show_param_detail': 'Show-Param-Detail',
        'eihealth_project_id': 'eihealth_project_id',
        'workflow_id': 'workflow_id'
    }

    def __init__(self, show_param_detail=None, eihealth_project_id=None, workflow_id=None):
        """ShowWorkflowRequest

        The model defined in huaweicloud sdk

        :param show_param_detail: 是否显示模板参数详情
        :type show_param_detail: bool
        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param workflow_id: 流程id
        :type workflow_id: str
        """
        
        

        self._show_param_detail = None
        self._eihealth_project_id = None
        self._workflow_id = None
        self.discriminator = None

        if show_param_detail is not None:
            self.show_param_detail = show_param_detail
        self.eihealth_project_id = eihealth_project_id
        self.workflow_id = workflow_id

    @property
    def show_param_detail(self):
        """Gets the show_param_detail of this ShowWorkflowRequest.

        是否显示模板参数详情

        :return: The show_param_detail of this ShowWorkflowRequest.
        :rtype: bool
        """
        return self._show_param_detail

    @show_param_detail.setter
    def show_param_detail(self, show_param_detail):
        """Sets the show_param_detail of this ShowWorkflowRequest.

        是否显示模板参数详情

        :param show_param_detail: The show_param_detail of this ShowWorkflowRequest.
        :type show_param_detail: bool
        """
        self._show_param_detail = show_param_detail

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ShowWorkflowRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ShowWorkflowRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ShowWorkflowRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ShowWorkflowRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ShowWorkflowRequest.

        流程id

        :return: The workflow_id of this ShowWorkflowRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ShowWorkflowRequest.

        流程id

        :param workflow_id: The workflow_id of this ShowWorkflowRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

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
        if not isinstance(other, ShowWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
