# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:10
    @Author  : Yanjiakang
    @File    : lc206_反转链表.py
"""

from typing import Optional
from type.date_structure import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 空链表或者只有一个节点，直接返回原链表
        if head is None or head.next is None:
            return head

        # 前后指针
        prev = None
        cur = head

        # 循环遍历，直到最后一个节点
        while cur != None:
            # 先保存后指针节点，防止链表中断
            next = cur.next
            # 将后指针的next指向前指针
            cur.next = prev
            # 向后遍历
            prev = cur
            cur = next

        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            cur.next, prev, cur, = prev, cur, cur.next

        return prev
