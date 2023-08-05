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


class DescribeCacheInstancesRequest(JDCloudRequest):
    """
    查询缓存Redis实例列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCacheInstancesRequest, self).__init__(
            '/regions/{regionId}/cacheInstance', 'GET', header, version)
        self.parameters = parameters


class DescribeCacheInstancesParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None
        self.sorts = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为20；取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) cacheInstanceId -实例Id，精确匹配，支持多个
cacheInstanceName - 实例名称，模糊匹配，支持单个
cacheInstanceStatus - redis状态，精确匹配，支持多个(running：运行，error：错误，creating：创建中，changing：变配中，deleting：删除中)

        """
        self.filters = filters

    def setSorts(self, sorts):
        """
        :param sorts: (Optional) createTime - 创建时间(asc：正序，desc：倒序)

        """
        self.sorts = sorts

