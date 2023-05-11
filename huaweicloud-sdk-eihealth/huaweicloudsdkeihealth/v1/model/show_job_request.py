# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_addition_info': 'str',
        'eihealth_project_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'x_addition_info': 'X-Addition-Info',
        'eihealth_project_id': 'eihealth_project_id',
        'job_id': 'job_id'
    }

    def __init__(self, x_addition_info=None, eihealth_project_id=None, job_id=None):
        """ShowJobRequest

        The model defined in huaweicloud sdk

        :param x_addition_info: 设置为LOG时，返回作业日志链接
        :type x_addition_info: str
        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param job_id: 作业id
        :type job_id: str
        """
        
        

        self._x_addition_info = None
        self._eihealth_project_id = None
        self._job_id = None
        self.discriminator = None

        if x_addition_info is not None:
            self.x_addition_info = x_addition_info
        self.eihealth_project_id = eihealth_project_id
        self.job_id = job_id

    @property
    def x_addition_info(self):
        """Gets the x_addition_info of this ShowJobRequest.

        设置为LOG时，返回作业日志链接

        :return: The x_addition_info of this ShowJobRequest.
        :rtype: str
        """
        return self._x_addition_info

    @x_addition_info.setter
    def x_addition_info(self, x_addition_info):
        """Sets the x_addition_info of this ShowJobRequest.

        设置为LOG时，返回作业日志链接

        :param x_addition_info: The x_addition_info of this ShowJobRequest.
        :type x_addition_info: str
        """
        self._x_addition_info = x_addition_info

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ShowJobRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ShowJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ShowJobRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ShowJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobRequest.

        作业id

        :return: The job_id of this ShowJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobRequest.

        作业id

        :param job_id: The job_id of this ShowJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ShowJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
