# -*- coding: utf-8 -*-
"""
    @Time    : 2/10/25 15:09
    @Author  : Yanjiakang
    @File    : lc024_两两交换链表中的节点.py
"""

from typing import Optional
from type.date_structure import ListNode
from common.method import linked_list_to_list, list_to_linked_list


class Solution:
    # 方法一：遍历，每次处理两个节点
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)  # 设置哨兵节点
        prev = dummy_node  # 前节点，保证链表不断
        cur = dummy_node.next  # 通过cur遍历链表

        # 当cur不为空时遍历链表
        while cur is not None:
            left, right = cur, cur.next  # 设置左右节点

            # 当左右节点均不为空时，进行交换操作
            if left is not None and right is not None:
                left.next, right.next = right.next, left
                prev.next = right

            prev = left  # 此时左右节点已经交换，prev应更新为靠右的节点-left
            cur = left.next  # left.next才是下一个需要遍历的节点

        return dummy_node.next


def test(lst: list):
    sol = Solution()
    link_list = list_to_linked_list(lst)
    result = sol.swapPairs(link_list)
    print(linked_list_to_list(result))


if __name__ == '__main__':
    test([1, 2, 3, 4])
    test([])
    test([1])


