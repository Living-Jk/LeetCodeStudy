# -*- coding: utf-8 -*-
"""
    @Time    : 1/24/25 11:34
    @Author  : Yanjiakang
    @File    : lc002_两数相加.py
"""

from typing import Optional
from type.date_structure import ListNode
from common.method import list_to_linked_list, linked_list_to_list


class Solution:

    # 方法2：迭代
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = dummy_node = ListNode(0)  # 创建索引节点 + 哨兵节点
        carry = 0  # 进位值

        # 只要还没遍历完，或者进位值还有数据，就继续循环
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next

            cur_node.next = ListNode(carry % 10)  # 余数作为节点保存
            carry = carry // 10  # 进位值整数10，作为下一次循环的进位值
            cur_node = cur_node.next  # 向后迭代

        return dummy_node.next  # 返回哨兵节点的下一个节点，即为结果链表

    # 方法1：暴力解法 -- 遍历列表，计算出两值，相加后再转化为链表
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 计算两个数字
        num1 = self.linked_list_to_int(l1)
        num2 = self.linked_list_to_int(l2)

        # 再将数字转化为链表
        result = self.int_to_linked_list(num1 + num2)
        return result

    # 把链表数据计算成整数
    def linked_list_to_int(self, lst: Optional[ListNode]):
        index, result = 0, 0
        # 遍历链表
        while lst is not None:
            # 计算结果（可能超过存储范围）
            result += lst.val * (10 ** index)
            index += 1
            # 向后遍历
            lst = lst.next
        return result

    # 将数字转化为链表
    def int_to_linked_list(self, num: int) -> Optional[ListNode]:
        # 数字长度
        num_len = len(str(abs(num)))
        # 索引结点、哨兵节点
        cur_node = dummy_node = ListNode(0)

        # 遍历形成链表，因为头结点已经计算了一次，所以这里少循环一次
        for i in range(num_len):
            cur_val = num % 10
            # 链表尾插
            cur_node.next = ListNode(cur_val)
            cur_node = cur_node.next
            # 迭代num
            num //= 10
        return dummy_node.next


if __name__ == '__main__':
    sol = Solution()

    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]

    # l1 = [0]
    # l2 = [0]

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]

    linked_list1 = list_to_linked_list(l1)
    linked_list2 = list_to_linked_list(l2)

    result = sol.addTwoNumbers2(linked_list1, linked_list2)
    print(linked_list_to_list(result))


