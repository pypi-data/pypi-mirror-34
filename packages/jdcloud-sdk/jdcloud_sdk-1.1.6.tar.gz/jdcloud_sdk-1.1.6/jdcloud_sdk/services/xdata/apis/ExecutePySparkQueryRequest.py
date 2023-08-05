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


class ExecutePySparkQueryRequest(JDCloudRequest):
    """
    执行PySpark脚本
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExecutePySparkQueryRequest, self).__init__(
            '/regions/{regionId}/dwQuery:executePySparkQuery', 'POST', header, version)
        self.parameters = parameters


class ExecutePySparkQueryParameters(object):

    def __init__(self, regionId, script, userName, instanceName, ):
        """
        :param regionId: 地域ID
        :param script: PySpark脚本
        :param userName: 用户名称
        :param instanceName: 实例名称
        """

        self.regionId = regionId
        self.script = script
        self.userName = userName
        self.instanceName = instanceName
        self.instanceOwnerName = None
        self.scriptType = None

    def setInstanceOwnerName(self, instanceOwnerName):
        """
        :param instanceOwnerName: (Optional) 实例拥有者名称
        """
        self.instanceOwnerName = instanceOwnerName

    def setScriptType(self, scriptType):
        """
        :param scriptType: (Optional) 脚本类型名称
        """
        self.scriptType = scriptType

