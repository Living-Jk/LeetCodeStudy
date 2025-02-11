# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:13
    @Author  : Yanjiakang
    @File    : lc876_寻找链表中间节点.py
"""

from typing import Optional
from type.date_structure import ListNode
from common.method import list_to_linked_list


class Solution:
    # 方法1：遍历链表，形成数组
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建数组
        new_node_list = []

        # 遍历链表，将每个节点存入数组
        cur = head
        while cur != None:
            new_node_list.append(cur)
            cur = cur.next

        # 通过下标直接返回中间节点
        index = len(new_node_list) // 2
        return new_node_list[index]

    # 方法2：快慢指针
    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建快慢双指针
        fast = head
        slow = head

        # 快指针每次走两步、慢指针每次走一步；直到快指针为最后及诶单或者为空
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # 循环结束后，慢指针指向的节点即为中间节点
        return slow


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5]
    linked_list = list_to_linked_list(lst1)

    sol = Solution()
    result = sol.middleNode(linked_list)

    print(result.val)

    lst2 = [1, 2, 3, 4, 5, 6]
    linked_list2 = list_to_linked_list(lst2)

    sol = Solution()
    result = sol.middleNode(linked_list2)

    print(result.val)
