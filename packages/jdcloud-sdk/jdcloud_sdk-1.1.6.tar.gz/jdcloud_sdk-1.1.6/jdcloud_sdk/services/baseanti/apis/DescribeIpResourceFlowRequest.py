# coding=utf8

# Copyright 2018 JDCLOUD.COM
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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeIpResourceFlowRequest(JDCloudRequest):
    """
    查询公网Ip的监控流量
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeIpResourceFlowRequest, self).__init__(
            '/regions/{regionId}/ipResources/{ip}/monitorFlow', 'GET', header, version)
        self.parameters = parameters


class DescribeIpResourceFlowParameters(object):

    def __init__(self, regionId, ip, ):
        """
        :param regionId: Region ID
        :param ip: 公网ip
        """

        self.regionId = regionId
        self.ip = ip
        self.endTime = None

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询的结束时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ssZ
        """
        self.endTime = endTime

