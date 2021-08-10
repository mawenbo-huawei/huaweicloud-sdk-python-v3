# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodToOnDemandReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'operation': 'str',
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'operation': 'operation',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, operation=None, resource_ids=None):
        """PeriodToOnDemandReq - a model defined in huaweicloud sdk"""
        
        

        self._operation = None
        self._resource_ids = None
        self.discriminator = None

        self.operation = operation
        self.resource_ids = resource_ids

    @property
    def operation(self):
        """Gets the operation of this PeriodToOnDemandReq.

        |参数名称：动作| |参数约束及描述：动作 动作SET_UP：设置CANCEL：取消|

        :return: The operation of this PeriodToOnDemandReq.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this PeriodToOnDemandReq.

        |参数名称：动作| |参数约束及描述：动作 动作SET_UP：设置CANCEL：取消|

        :param operation: The operation of this PeriodToOnDemandReq.
        :type: str
        """
        self._operation = operation

    @property
    def resource_ids(self):
        """Gets the resource_ids of this PeriodToOnDemandReq.

        |参数名称：资源ID| |参数约束以及描述：资源ID 资源ID。您可以调用“2.1-查询客户包年/包月资源列表”接口获取资源ID。只支持传入主资源ID，最多100个资源ID。设置的时候，主资源和对应的子资源一起转按需。哪些资源是主资源请根据“2.1-查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。|

        :return: The resource_ids of this PeriodToOnDemandReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this PeriodToOnDemandReq.

        |参数名称：资源ID| |参数约束以及描述：资源ID 资源ID。您可以调用“2.1-查询客户包年/包月资源列表”接口获取资源ID。只支持传入主资源ID，最多100个资源ID。设置的时候，主资源和对应的子资源一起转按需。哪些资源是主资源请根据“2.1-查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。|

        :param resource_ids: The resource_ids of this PeriodToOnDemandReq.
        :type: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, PeriodToOnDemandReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
