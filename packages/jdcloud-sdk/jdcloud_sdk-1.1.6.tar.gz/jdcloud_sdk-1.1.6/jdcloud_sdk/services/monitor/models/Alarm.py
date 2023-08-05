# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class Alarm(object):

    def __init__(self, calculation=None, contactGroups=None, contactPersons=None, createTime=None, enabled=None, id=None, metric=None, metricName=None, noticePeriod=None, noticeTime=None, operation=None, period=None, region=None, resourceId=None, serviceCode=None, status=None, tag=None, threshold=None, times=None, value=None):
        """
        :param calculation: (Optional) 统计方法：平均值=avg、最大值=max、最小值=min
        :param contactGroups: (Optional) 通知的联系组，如 [“联系组1”,”联系组2”]
        :param contactPersons: (Optional) 通知的联系人，如 [“联系人1”,”联系人2”]
        :param createTime: (Optional) 创建时间
        :param enabled: (Optional) 启用禁用 1启用，0禁用
        :param id: (Optional) 规则id
        :param metric: (Optional) 监控项
        :param metricName: (Optional) 规则id监控项名称
        :param noticePeriod: (Optional) 通知周期 单位：小时
        :param noticeTime: (Optional) 报警的时间  , 查询正在报警规则时该字段有效
        :param operation: (Optional) >=、>、<、<=、==、！=
        :param period: (Optional) 统计周期（单位：分钟）
        :param region: (Optional) 地域信息
        :param resourceId: (Optional) 此规则所应用的资源id
        :param serviceCode: (Optional) 报警规则对应的产品
        :param status: (Optional) 监控项状态:1正常，2告警，4数据不足
        :param tag: (Optional) 监控项附属信息
        :param threshold: (Optional) 阈值
        :param times: (Optional) 连续多少次后报警
        :param value: (Optional) 报警值 , 查询正在报警规则时该字段有效
        """

        self.calculation = calculation
        self.contactGroups = contactGroups
        self.contactPersons = contactPersons
        self.createTime = createTime
        self.enabled = enabled
        self.id = id
        self.metric = metric
        self.metricName = metricName
        self.noticePeriod = noticePeriod
        self.noticeTime = noticeTime
        self.operation = operation
        self.period = period
        self.region = region
        self.resourceId = resourceId
        self.serviceCode = serviceCode
        self.status = status
        self.tag = tag
        self.threshold = threshold
        self.times = times
        self.value = value
