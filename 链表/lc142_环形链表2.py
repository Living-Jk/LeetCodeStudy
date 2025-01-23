# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:09
    @Author  : Yanjiakang
    @File    : lc142_环形链表2.py
"""

from typing import Optional
from type.date_structure import ListNode


class Solution:
    # 方法1：哈希集合
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_ptr = head
        node_set = set()

        # 遍历链表
        while cur_ptr != None:
            # 如果当前节点在集合中，说明有相同节点（有环）
            if cur_ptr in node_set:
                return cur_ptr

            # 当前不在集合，就插入集合
            node_set.add(cur_ptr)
            # 向后遍历
            cur_ptr = cur_ptr.next

        # 如果能走出while，说明没有环
        return None

    # 方法2：快慢指针
    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针
        fast = slow = head

        while True:
            # 如果快指针走到None，说明没环，直接返回None
            if fast is None or fast.next is None:
                return None

            # 移动指针
            fast, slow = fast.next.next, slow.next
            # 如果相遇，跳出循环
            if fast == slow:
                break

        # 让fast从头节点开始，与slow同时向后移动，相遇节点即为环的入口节点
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

