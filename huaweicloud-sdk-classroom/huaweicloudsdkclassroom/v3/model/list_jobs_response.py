# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[JobCard]',
        'total': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'total': 'total'
    }

    def __init__(self, jobs=None, total=None):
        """ListJobsResponse

        The model defined in huaweicloud sdk

        :param jobs: 作业列表
        :type jobs: list[:class:`huaweicloudsdkclassroom.v3.JobCard`]
        :param total: 作业总数
        :type total: int
        """
        
        super(ListJobsResponse, self).__init__()

        self._jobs = None
        self._total = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if total is not None:
            self.total = total

    @property
    def jobs(self):
        """Gets the jobs of this ListJobsResponse.

        作业列表

        :return: The jobs of this ListJobsResponse.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.JobCard`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ListJobsResponse.

        作业列表

        :param jobs: The jobs of this ListJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkclassroom.v3.JobCard`]
        """
        self._jobs = jobs

    @property
    def total(self):
        """Gets the total of this ListJobsResponse.

        作业总数

        :return: The total of this ListJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListJobsResponse.

        作业总数

        :param total: The total of this ListJobsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
