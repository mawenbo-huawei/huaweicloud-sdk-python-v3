# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_repo_auth': 'str',
        'namespace': 'str',
        'project': 'str'
    }

    attribute_map = {
        'x_repo_auth': 'X-Repo-Auth',
        'namespace': 'namespace',
        'project': 'project'
    }

    def __init__(self, x_repo_auth=None, namespace=None, project=None):
        """ListTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_repo_auth = None
        self._namespace = None
        self._project = None
        self.discriminator = None

        self.x_repo_auth = x_repo_auth
        self.namespace = namespace
        self.project = project

    @property
    def x_repo_auth(self):
        """Gets the x_repo_auth of this ListTagsRequest.

        授权名称。

        :return: The x_repo_auth of this ListTagsRequest.
        :rtype: str
        """
        return self._x_repo_auth

    @x_repo_auth.setter
    def x_repo_auth(self, x_repo_auth):
        """Sets the x_repo_auth of this ListTagsRequest.

        授权名称。

        :param x_repo_auth: The x_repo_auth of this ListTagsRequest.
        :type: str
        """
        self._x_repo_auth = x_repo_auth

    @property
    def namespace(self):
        """Gets the namespace of this ListTagsRequest.

        组织ID。

        :return: The namespace of this ListTagsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListTagsRequest.

        组织ID。

        :param namespace: The namespace of this ListTagsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def project(self):
        """Gets the project of this ListTagsRequest.

        仓库项目ID，如果含有“/”，需要将“/”替换为“:”。

        :return: The project of this ListTagsRequest.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ListTagsRequest.

        仓库项目ID，如果含有“/”，需要将“/”替换为“:”。

        :param project: The project of this ListTagsRequest.
        :type: str
        """
        self._project = project

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
        if not isinstance(other, ListTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
