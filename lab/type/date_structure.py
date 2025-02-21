# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:26
    @Author  : Yanjiakang
    @File    : date_structure.py
"""


# 链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RandomListNode:
    def __init__(self, x: int, next: 'RandomListNode' = None, random: 'RandomListNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random
