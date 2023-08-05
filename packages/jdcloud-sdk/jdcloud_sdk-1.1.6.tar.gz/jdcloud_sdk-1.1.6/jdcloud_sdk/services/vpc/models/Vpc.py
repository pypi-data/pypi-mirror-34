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


class Vpc(object):

    def __init__(self, vpcId=None, addressPrefix=None, description=None, vpcName=None, aclIds=None, routeTableIds=None, subnets=None, createdTime=None):
        """
        :param vpcId: (Optional) Vpc的Id
        :param addressPrefix: (Optional) 如果为空，则不限制网段，如果不为空，10.0.0.0/8、172.16.0.0/12和192.168.0.0/16及它们包含的子网，且子网掩码长度为16-28之间
        :param description: (Optional) VPC 描述，取值范围：1~120个字符
        :param vpcName: (Optional) 私有网络名称，取值范围：1-60个中文、英文大小写的字母、数字和下划线分隔符
        :param aclIds: (Optional) 
        :param routeTableIds: (Optional) 
        :param subnets: (Optional) 私有网络包含的子网列表
        :param createdTime: (Optional) vpc创建时间
        """

        self.vpcId = vpcId
        self.addressPrefix = addressPrefix
        self.description = description
        self.vpcName = vpcName
        self.aclIds = aclIds
        self.routeTableIds = routeTableIds
        self.subnets = subnets
        self.createdTime = createdTime
