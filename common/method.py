# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:26
    @Author  : Yanjiakang
    @File    : method.py
"""
from type.date_structure import ListNode


# 将列表转换为 ListNode 链表
def list_to_linked_list(lst):
    if not lst:  # 如果列表为空，返回 None
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 将 ListNode 链表转换为列表
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
