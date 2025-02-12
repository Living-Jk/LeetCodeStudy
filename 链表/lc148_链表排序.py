# -*- coding: utf-8 -*-
"""
    @Time    : 2/11/25 15:10
    @Author  : Yanjiakang
    @File    : lc148_链表排序.py
"""

from typing import Optional
from type.date_structure import ListNode
from common.method import list_to_linked_list, linked_list_to_list


class Solution:
    # 方法一：顺序表排序
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head  # 处理空链表

        node_list = []  # 顺序表，存放(val, 节点地址)元组元素
        cur = head

        while cur:
            node_list.append((cur.val, cur))  # 存放(val, 节点地址)元组元素
            cur = cur.next  # 向后遍历

        # 对node_list按照val进行升序排序
        node_list.sort(key=lambda x: x[0])
        # 最后将排序好的序列串起来
        new_head = node_list[0][1]
        cur = new_head
        for val, node in node_list[1:]:
            cur.next = node
            cur = cur.next

        cur.next = None  # 处理最后一个节点
        return new_head


def test(lst: list):
    sol = Solution()
    rst = sol.sortList(list_to_linked_list(lst))
    print(linked_list_to_list(rst))


if __name__ == '__main__':
    test([4, 2, 1, 3])
    test([-1, 5, 3, 4, 0])
    test([])
