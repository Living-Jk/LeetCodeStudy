# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 11:42
    @Author  : Yanjiakang
    @File    : lc021_合并两个有序链表.py
"""

# LeetCode 21.合并两个有序链表

from typing import Optional
from type.date_structure import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # return list1 if list2 is None else list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # 初始化变量，cur1、cur2为两个列表的遍历索引；new_head为新列表的头结点;cur_node为新链表索引，表示当前节点
        cur1, cur2 = list1, list2
        new_head = cur_node = None

        # 区分第一个节点是从哪个链表开始
        if list1.val <= list2.val:
            new_head = cur_node = list1
            cur1 = list1.next
        else:
            new_head = cur_node = list2
            cur2 = list2.next

        # 当两个链表都未遍历完时，进行循环遍历比较
        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                cur_node.next = cur1
                # 向后遍历
                cur1 = cur1.next
            else:
                cur_node.next = cur2
                # 向后遍历
                cur2 = cur2.next

            # 无论如何当前节点都要向后遍历
            cur_node = cur_node.next

        # 结束循环说明有一个链表已完成遍历，我们需要把另一个链表接到后面即可
        if cur1 is None:
            cur_node.next = cur2
        else:
            cur_node.next = cur1

        return new_head


# 辅助函数：将 Python 列表转换为 ListNode 链表
def list_to_linked_list(lst):
    if not lst:  # 如果列表为空，返回 None
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 辅助函数：将 ListNode 链表转换为 Python 列表
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


list1 = [1, 2, 4]
list2 = [1, 3, 5]

# 转换为链表
linked_list1 = list_to_linked_list(list1)
linked_list2 = list_to_linked_list(list2)

# 合并链表
solution = Solution()
result = solution.mergeTwoLists(linked_list1, linked_list2)

print(linked_list_to_list(result))  # 输出: [1, 1, 2, 3, 4, 5]


