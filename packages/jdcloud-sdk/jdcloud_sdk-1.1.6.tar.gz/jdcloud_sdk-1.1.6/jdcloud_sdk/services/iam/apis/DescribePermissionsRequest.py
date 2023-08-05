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


class DescribePermissionsRequest(JDCloudRequest):
    """
    查询策略列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribePermissionsRequest, self).__init__(
            '/regions/{regionId}/permissions', 'GET', header, version)
        self.parameters = parameters


class DescribePermissionsParameters(object):

    def __init__(self, regionId, pageNumber, pageSize, queryType):
        """
        :param regionId: Region ID
        :param pageNumber: 页码
        :param pageSize: 每页显示数目
        :param queryType: 权限类型,0-全部，1-系统权限，2-自定义权限
        """

        self.regionId = regionId
        self.pageNumber = pageNumber
        self.pageSize = pageSize
        self.keyword = None
        self.queryType = queryType

    def setKeyword(self, keyword):
        """
        :param keyword: (Optional) 关键字
        """
        self.keyword = keyword

