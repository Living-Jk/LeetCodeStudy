# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:11
    @Author  : Yanjiakang
    @File    : lc234_回文链表.py
"""

from typing import Optional
from type.date_structure import ListNode


class Solution:
    # 方法一：遍历链表形成数组，双指针遍历
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 遍历链表，将数据插入数组
        vals = []
        cur_ptr = head
        while cur_ptr != None:
            vals.append(cur_ptr.val)
            cur_ptr = cur_ptr.next

        # 创建首尾双指针（数组索引）
        fount = 0
        back = len(vals) - 1

        # 两边向中间遍历
        while fount < back:
            # 如果两边值不一样，说明不是回文链表
            if vals[fount] != vals[back]:
                return False
            fount += 1
            back -= 1

        # 遍历结束说明是回文链表
        return True

    # 方法一简化写法
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # 遍历链表，将数据插入数组
        vals = []
        cur_ptr = head
        while cur_ptr != None:
            vals.append(cur_ptr.val)
            cur_ptr = cur_ptr.next

        # 判断正向数组与反向数组是否相同
        return vals == vals[::-1]

    # 方法二：寻找中间节点 + 反转链表
    def isPalindrome3(self, head: Optional[ListNode]) -> bool:
        # 找到链表中间节点
        mid_node = self.middleNode(head)

        # 将后半段链表翻转
        reverse_list = self.reverseList(mid_node)

        # 分别从首尾遍历前后两个链表，看节点元素是否相同
        first_list = head
        second_list = reverse_list
        while second_list != None:
            # 如果元素不一样，说明不是回文链表
            if first_list.val != second_list.val:
                return False
            # 向后遍历
            first_list = first_list.next
            second_list = second_list.next

        # 遍历完说明是回文链表，但我们有素质，先把链表复原
        mid_node.next = self.reverseList(mid_node)
        return True

    # 寻找中间节点
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建快慢双指针
        fast = head
        slow = head

        # 快指针每次走两步、慢指针每次走一步；直到快指针为最后及诶单或者为空
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # 循环结束后，慢指针指向的节点即为中间节点
        return slow

    # 反转链表
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




    # 错误答案，只能跑过部分case
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # 空链表、只有1个节点的链表，默认是回文链表
    #     if head is None or head.next is None:
    #         return True

    #     # 创建集合
    #     s = set()
    #     cur_ptr = head

    #     # 遍历链表
    #     while cur_ptr != None:
    #         # 找到第一个存在集合中的节点，即为后半段的起始节点
    #         if cur_ptr in s:
    #             break
    #         # 将前半段节点加入集合
    #         s.add(cur_ptr)
    #         cur_ptr = cur_ptr.next

    #     # 继续遍历后半段
    #     while cur_ptr != None:
    #         # 如果有节点不在集合中，说明不是回文链表
    #         if cur_ptr not in s:
    #             return False

    #     # 结束遍历走到这里，说明是回文链表
    #     return True



