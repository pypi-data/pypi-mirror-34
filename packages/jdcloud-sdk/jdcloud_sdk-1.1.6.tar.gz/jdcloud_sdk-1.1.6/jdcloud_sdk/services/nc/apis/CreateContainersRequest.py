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


class CreateContainersRequest(JDCloudRequest):
    """
    创建一台或多台指定配置的实例
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateContainersRequest, self).__init__(
            '/regions/{regionId}/containers', 'POST', header, version)
        self.parameters = parameters


class CreateContainersParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.containerSpec = None
        self.maxCount = None

    def setContainerSpec(self, containerSpec):
        """
        :param containerSpec: (Optional) 创建容器规格
        """
        self.containerSpec = containerSpec

    def setMaxCount(self, maxCount):
        """
        :param maxCount: (Optional) 购买实例数量；取值范围：[1,100]
        """
        self.maxCount = maxCount

