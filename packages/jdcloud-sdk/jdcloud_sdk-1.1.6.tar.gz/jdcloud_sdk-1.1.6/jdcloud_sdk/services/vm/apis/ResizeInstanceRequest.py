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


class ResizeInstanceRequest(JDCloudRequest):
    """
    "云主机变更实例规格，需要关机操作"
"16年创建的云盘做系统盘的主机，一代与二代实例类型不允许相互调整"
"本地盘做系统盘的主机，一代与二代实例类型不允许相互调整"
"ag中的主机，一代与二代实例类型不允许相互调整"
"变更后实例规格的网卡数量限制，要支持当前主机的网卡数量，如不支持，需要缷载网卡后再变更实例规格"

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ResizeInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:resizeInstance', 'POST', header, version)
        self.parameters = parameters


class ResizeInstanceParameters(object):

    def __init__(self, regionId, instanceId, instanceType):
        """
        :param regionId: Region ID
        :param instanceId: Instance ID
        :param instanceType: 实例规格
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.instanceType = instanceType

