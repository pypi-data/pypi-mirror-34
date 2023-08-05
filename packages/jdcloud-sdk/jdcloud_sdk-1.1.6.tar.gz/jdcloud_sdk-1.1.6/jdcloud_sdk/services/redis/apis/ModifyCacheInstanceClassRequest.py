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


class ModifyCacheInstanceClassRequest(JDCloudRequest):
    """
    变更缓存Redis实例配置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyCacheInstanceClassRequest, self).__init__(
            '/regions/{regionId}/cacheInstance/{cacheInstanceId}:modifyCacheInstanceClass', 'POST', header, version)
        self.parameters = parameters


class ModifyCacheInstanceClassParameters(object):

    def __init__(self, regionId, cacheInstanceId, cacheInstanceClass):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstanceId: 缓存Redis实例ID
        :param cacheInstanceClass: 变更后的缓存Redis&lt;a href&#x3D;&quot;https://www.jdcloud.com/help/detail/411/isCatalog/1&quot;&gt;实例规格代码&lt;/a&gt;
        """

        self.regionId = regionId
        self.cacheInstanceId = cacheInstanceId
        self.cacheInstanceClass = cacheInstanceClass

