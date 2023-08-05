# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class AttachDiskRequest(JDCloudRequest):
    """
    云主机挂载硬盘，主机和云盘没有未完成的任务时才可挂载，一个主机上最多可挂载4块数据盘
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AttachDiskRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:attachDisk', 'POST', header, version)
        self.parameters = parameters


class AttachDiskParameters(object):

    def __init__(self, regionId, instanceId, diskId, ):
        """
        :param regionId: Region ID
        :param instanceId: Instance ID
        :param diskId: 云硬盘ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.diskId = diskId
        self.deviceName = None
        self.autoDelete = None

    def setDeviceName(self, deviceName):
        """
        :param deviceName: (Optional) 逻辑挂载点[vdb,vdc,vdd,vde,vdf,vdg,vdh]
        """
        self.deviceName = deviceName

    def setAutoDelete(self, autoDelete):
        """
        :param autoDelete: (Optional) 当删除主机时，是否自动关联删除此硬盘，默认False，只支持按配置计费
        """
        self.autoDelete = autoDelete

