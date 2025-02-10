# -*- coding: utf-8 -*-
"""
    @Time    : 1/26/25 11:39
    @Author  : Yanjiakang
    @File    : lc019_删除链表的第N个结点.py
"""

from typing import Optional
from type.date_structure import ListNode
from common.method import list_to_linked_list, linked_list_to_list


class Solution:
    # 方法1：遍历，找到倒数第n个结点，然后再找到它的前一个结点，改变前一个结点的next指向，即删除了结点
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp, list_len = head, 0
        # 遍历链表，计算节点个数
        while temp is not None:
            list_len += 1
            temp = temp.next

        dummy_node = ListNode(0)  # 哨兵节点
        dummy_node.next = head

        cur_node, prev_node,  = head, dummy_node  # 当前节点初始化为head节点、前节点初始化为哨兵节点
        next_node = cur_node.next  # 后节点，初始化为当前节点的下一个节点

        # 有长度之后，遍历链表，找到倒数第n个结点 + 前后结点，改变指向即可
        for _ in range(list_len - n):
            # 整体向后遍历即可
            prev_node = cur_node
            cur_node = cur_node.next
            next_node = cur_node.next

        # 结束循环后，目前三个结点已经都找到，改变指向即可实现删除
        prev_node.next = next_node
        return dummy_node.next

    # 方法2：双指针：快指针比慢指针领先n步，然后同时遍历，遍历到最后一个节点时，慢指针指向即为倒数第n+1个结点，改变指向即可
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)  # 设置哨兵节点
        fast = slow = dummy_node  # 设置快慢指针，均指向哨兵节点

        # 快指针比慢指针先走n步
        for _ in range(n):
            fast = fast.next
        # 然后同时向后遍历，直到找到最后一个节点（node.next == null）
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # 循环结束后slow指针指向即为倒数第n+1个结点，改变指向即可完成删除逻辑
        slow.next = slow.next.next

        return dummy_node.next  # 返回哨兵指针.next，而不是head，因为head可能是被删除节点


if __name__ == '__main__':
    sol = Solution()

    lst = [1, 2, 3, 4, 5]
    # lst = [1]
    # lst = [1, 2]
    link_list = list_to_linked_list(lst)

    result = sol.removeNthFromEnd(link_list, 2)
    # result = sol.removeNthFromEnd2(link_list, 1)
    print(linked_list_to_list(result))


