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


class DeleteTableRequest(JDCloudRequest):
    """
    删除数据表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteTableRequest, self).__init__(
            '/regions/{regionId}/dwTable/{tableName}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteTableParameters(object):

    def __init__(self, regionId, tableName, instanceName, databaseName):
        """
        :param regionId: 地域ID
        :param tableName: 数据表名
        :param instanceName: 实例名称
        :param databaseName: 数据库名称
        """

        self.regionId = regionId
        self.tableName = tableName
        self.instanceName = instanceName
        self.databaseName = databaseName

