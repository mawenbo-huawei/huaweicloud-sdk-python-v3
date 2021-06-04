# coding: utf-8

import pprint
import re

import six





class ShowHistoryTasksRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'status': 'str',
        'start_date': 'int',
        'end_date': 'int',
        'order_field': 'str',
        'order_type': 'str',
        'user_domain_id': 'str',
        'file_type': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'status': 'status',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'order_field': 'order_field',
        'order_type': 'order_type',
        'user_domain_id': 'user_domain_id',
        'file_type': 'file_type',
        'task_id': 'task_id'
    }

    def __init__(self, enterprise_project_id=None, page_size=None, page_number=None, status=None, start_date=None, end_date=None, order_field=None, order_type=None, user_domain_id=None, file_type=None, task_id=None):
        """ShowHistoryTasksRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._page_size = None
        self._page_number = None
        self._status = None
        self._start_date = None
        self._end_date = None
        self._order_field = None
        self._order_type = None
        self._user_domain_id = None
        self._file_type = None
        self._task_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if status is not None:
            self.status = status
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if order_field is not None:
            self.order_field = order_field
        if order_type is not None:
            self.order_type = order_type
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id
        if file_type is not None:
            self.file_type = file_type
        if task_id is not None:
            self.task_id = task_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowHistoryTasksRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :return: The enterprise_project_id of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowHistoryTasksRequest.

        当用户开启企业项目功能时，该参数生效，表示资源所属企业项目，不传表示默认项目。

        :param enterprise_project_id: The enterprise_project_id of this ShowHistoryTasksRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page_size(self):
        """Gets the page_size of this ShowHistoryTasksRequest.

        单页最大数量，取值范围为1-10000。

        :return: The page_size of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowHistoryTasksRequest.

        单页最大数量，取值范围为1-10000。

        :param page_size: The page_size of this ShowHistoryTasksRequest.
        :type: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ShowHistoryTasksRequest.

        当前查询第几页，取值范围为1-65535。

        :return: The page_number of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ShowHistoryTasksRequest.

        当前查询第几页，取值范围为1-65535。

        :param page_number: The page_number of this ShowHistoryTasksRequest.
        :type: int
        """
        self._page_number = page_number

    @property
    def status(self):
        """Gets the status of this ShowHistoryTasksRequest.

        任务状态。 task_inprocess 表示任务处理中，task_done表示任务完成。

        :return: The status of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHistoryTasksRequest.

        任务状态。 task_inprocess 表示任务处理中，task_done表示任务完成。

        :param status: The status of this ShowHistoryTasksRequest.
        :type: str
        """
        self._status = status

    @property
    def start_date(self):
        """Gets the start_date of this ShowHistoryTasksRequest.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The start_date of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ShowHistoryTasksRequest.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param start_date: The start_date of this ShowHistoryTasksRequest.
        :type: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ShowHistoryTasksRequest.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The end_date of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ShowHistoryTasksRequest.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param end_date: The end_date of this ShowHistoryTasksRequest.
        :type: int
        """
        self._end_date = end_date

    @property
    def order_field(self):
        """Gets the order_field of this ShowHistoryTasksRequest.

        用来排序的字段，支持的字段有“task_type”，“total”，“processing”， “succeed”，“failed”，“create_time”。order_field和order_type必须同时传值。

        :return: The order_field of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        """Sets the order_field of this ShowHistoryTasksRequest.

        用来排序的字段，支持的字段有“task_type”，“total”，“processing”， “succeed”，“failed”，“create_time”。order_field和order_type必须同时传值。

        :param order_field: The order_field of this ShowHistoryTasksRequest.
        :type: str
        """
        self._order_field = order_field

    @property
    def order_type(self):
        """Gets the order_type of this ShowHistoryTasksRequest.

        desc 或者asc。

        :return: The order_type of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this ShowHistoryTasksRequest.

        desc 或者asc。

        :param order_type: The order_type of this ShowHistoryTasksRequest.
        :type: str
        """
        self._order_type = order_type

    @property
    def user_domain_id(self):
        """Gets the user_domain_id of this ShowHistoryTasksRequest.

        指定用户的域id。

        :return: The user_domain_id of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        """Sets the user_domain_id of this ShowHistoryTasksRequest.

        指定用户的域id。

        :param user_domain_id: The user_domain_id of this ShowHistoryTasksRequest.
        :type: str
        """
        self._user_domain_id = user_domain_id

    @property
    def file_type(self):
        """Gets the file_type of this ShowHistoryTasksRequest.

        默认是文件file。file：文件,directory：目录。

        :return: The file_type of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ShowHistoryTasksRequest.

        默认是文件file。file：文件,directory：目录。

        :param file_type: The file_type of this ShowHistoryTasksRequest.
        :type: str
        """
        self._file_type = file_type

    @property
    def task_id(self):
        """Gets the task_id of this ShowHistoryTasksRequest.

        任务id。

        :return: The task_id of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowHistoryTasksRequest.

        任务id。

        :param task_id: The task_id of this ShowHistoryTasksRequest.
        :type: str
        """
        self._task_id = task_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowHistoryTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
