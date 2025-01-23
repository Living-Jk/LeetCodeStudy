# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:07
    @Author  : Yanjiakang
    @File    : lc141_环形链表.py
"""

from typing import Optional
from type.date_structure import ListNode


class Solution:
    # 方法1：哈希集合
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur_ptr = head
        node_set = set()

        # 遍历链表
        while cur_ptr != None:
            # 如果当前节点在集合中，说明有相同节点（有环）
            if cur_ptr in node_set:
                return True

            # 当前不在集合，就插入集合
            node_set.add(cur_ptr)
            # 向后遍历
            cur_ptr = cur_ptr.next

        # 如果能走出while，说明没有环
        return False

    # 方法2：快慢指针
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # 如果是空链表 or 只有一个节点，一定没环
        if head is None or head.next is None:
            return False

        # 创建快慢指针
        slow = head
        fast = head.next

        # 循环遍历
        while fast != None and fast.next != None:
            # 如果快慢指针指向同一节点，说明有环
            if fast == slow:
                return True

            # 否则向后移动指针
            slow = slow.next
            fast = fast.next.next

        # 如果走出循环，说明遇到了空节点，没有环
        return False

    # 方法2换个写法
    def hasCycle3(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while True:
            if fast is None or fast.next is None:
                return False

            fast, slow = fast.next.next, slow.next

            if fast == slow:
                return True
