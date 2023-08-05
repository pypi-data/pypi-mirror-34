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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateDisksRequest(JDCloudRequest):
    """
    创建一块或多块云硬盘
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateDisksRequest, self).__init__(
            '/regions/{regionId}/disks', 'POST', header, version)
        self.parameters = parameters


class CreateDisksParameters(object):

    def __init__(self, regionId, diskSpec, maxCount, clientToken):
        """
        :param regionId: 地域ID
        :param diskSpec: 创建云硬盘规格
        :param maxCount: 购买实例数量；取值范围：[1,100]
        :param clientToken: 幂等性校验参数
        """

        self.regionId = regionId
        self.diskSpec = diskSpec
        self.maxCount = maxCount
        self.clientToken = clientToken

