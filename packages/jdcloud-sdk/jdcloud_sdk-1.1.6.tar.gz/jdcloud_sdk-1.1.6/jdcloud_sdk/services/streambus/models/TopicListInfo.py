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


class TopicListInfo(object):

    def __init__(self, archived=None, createdTime=None, deleted=None, id=None, lifecycle=None, name=None, partitionNum=None, remark=None, shardNum=None, status=None, topicName=None, uid=None, updatedTime=None, userPin=None):
        """
        :param archived: (Optional) 是否归档（0：未归档，1：已归档）
        :param createdTime: (Optional) 创建topic的时间戳
        :param deleted: (Optional) topic是否已删除（0：未删除，1：删除）
        :param id: (Optional) topic的id值
        :param lifecycle: (Optional) 数据写入后的保留时间
        :param name: (Optional) 流数据总线中topic的名字
        :param partitionNum: (Optional) 对应kafka中的分区数
        :param remark: (Optional) 备注
        :param shardNum: (Optional) 流数据总线shard的数量
        :param status: (Optional) 0: 已创建, 1: 创建中
        :param topicName: (Optional) 对应kafka中的topic名字
        :param uid: (Optional) 对应kafka中的uid
        :param updatedTime: (Optional) 更新topic的时间戳
        :param userPin: (Optional) 用户的userPin
        """

        self.archived = archived
        self.createdTime = createdTime
        self.deleted = deleted
        self.id = id
        self.lifecycle = lifecycle
        self.name = name
        self.partitionNum = partitionNum
        self.remark = remark
        self.shardNum = shardNum
        self.status = status
        self.topicName = topicName
        self.uid = uid
        self.updatedTime = updatedTime
        self.userPin = userPin
