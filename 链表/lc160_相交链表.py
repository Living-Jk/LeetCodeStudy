# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:09
    @Author  : Yanjiakang
    @File    : lc160_相交链表.py
"""

from typing import Optional
from type.date_structure import ListNode
from common.method import list_to_linked_list

class Solution:
    # 哈希集合
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 遍历链表A存入集合
        set_A = set()
        headA_tmp = headA
        while headA_tmp != None:
            set_A.add(headA_tmp)
            headA_tmp = headA_tmp.next

        # 遍历B链表
        headB_tmp = headB
        while headB_tmp != None:
            # 当前节点在集合A中，则说明找到了交点
            if headB_tmp in set_A:
                return headB_tmp
            # 没找到就继续像后遍历
            headB_tmp = headB_tmp.next

        # 直到最后都没找到，则说明无交点
        return None

    # 双指针
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # AB两指针分别指向AB链表
        ptr_A = headA
        ptr_B = headB

        # 当AB不相等时，进行遍历
        while ptr_A != ptr_B:
            # A没遍历完，继续遍历A，遍历完了遍历B
            if ptr_A != None:
                ptr_A = ptr_A.next
            else:
                ptr_A = headB

            # 同理
            if ptr_B != None:
                ptr_B = ptr_B.next
            else:
                ptr_B = headA

        # 直到遍历完相遇，此时有2种情况：1.已经找到相交节点； 2.无交点，两指针都为空；（返回任一指针即可）
        return ptr_A

    # 双指针（简化版）
    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr_A, ptr_B = headA, headB
        while ptr_A != ptr_B:
            ptr_A = ptr_A.next if ptr_A else headB
            ptr_B = ptr_B.next if ptr_B else headA
        return ptr_A


if __name__ == '__main__':
    lst1 = [4, 1]
    lst2 = [5, 6, 1]
    lst3 = [8, 4, 5]

    linked_list1 = list_to_linked_list(lst1)
    linked_list2 = list_to_linked_list(lst2)
    linked_list3 = list_to_linked_list(lst3)

    # 制造相交链表
    linked_list1.next.next = linked_list3
    linked_list2.next.next.next = linked_list3

    sol = Solution()
    print(sol.getIntersectionNode(linked_list1, linked_list2).val)

    # 无相交链表
    linked_list4 = list_to_linked_list(lst1)
    linked_list5 = list_to_linked_list(lst2)

    print(sol.getIntersectionNode(linked_list4, linked_list5))

