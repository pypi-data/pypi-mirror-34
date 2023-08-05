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


class Disk(object):

    def __init__(self, diskId=None, az=None, name=None, description=None, diskType=None, diskSizeGB=None, status=None, attachments=None, snapshotId=None, createTime=None, charge=None):
        """
        :param diskId: (Optional) 云硬盘ID
        :param az: (Optional) 云硬盘所属AZ
        :param name: (Optional) 云硬盘名称
        :param description: (Optional) 云硬盘描述
        :param diskType: (Optional) 磁盘类型，取值为 ssd 或 premium-hdd
        :param diskSizeGB: (Optional) 磁盘大小，单位为 GiB
        :param status: (Optional) 云硬盘状态，取值为 creating、available、in-use、extending、restoring、deleting、deleted、error_create、error_delete、error_restore、error_extend 之一
        :param attachments: (Optional) 挂载信息
        :param snapshotId: (Optional) 创建该云硬盘的快照ID
        :param createTime: (Optional) 创建云硬盘时间
        :param charge: (Optional) 云硬盘计费配置信息
        """

        self.diskId = diskId
        self.az = az
        self.name = name
        self.description = description
        self.diskType = diskType
        self.diskSizeGB = diskSizeGB
        self.status = status
        self.attachments = attachments
        self.snapshotId = snapshotId
        self.createTime = createTime
        self.charge = charge
