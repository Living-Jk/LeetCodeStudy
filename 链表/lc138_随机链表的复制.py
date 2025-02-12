# -*- coding: utf-8 -*-
"""
    @Time    : 2/10/25 16:49
    @Author  : Yanjiakang
    @File    : lc138_随机链表的复制.py
"""

from typing import Optional
from type.date_structure import RandomListNode as Node
from common.method import random_linked_list_to_list, list_to_random_linked_list


class Solution:
    # 方法一：哈希表
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head  # 如果是空链表，直接返回即可

        old_cur = head  # 旧链表迭代指针
        old_node_list = []  # 顺序表，存放旧链表节点
        new_node_list = []  # 顺序表，存放新链表节点
        hash_node = {}  # 哈希表，存放旧链表 {节点地址, 索引}
        index = 0  # 上述要存放的 索引

        # 遍历原链表
        while old_cur is not None:
            old_node_list.append(old_cur)  # 旧链表插入顺序表

            new_node = Node(old_cur.val, None, None)  # 创建新节点, val赋值好
            new_node_list.append(new_node)  # 按顺序插入顺序表
            hash_node[old_cur] = index  # 存放旧链表 {节点地址, 索引}

            # 向后遍历
            index += 1
            old_cur = old_cur.next

        # 遍历顺序表new_node_list，将每个节点的next链接好，形成一个链表
        new_head = new_node_list[0]
        for i in range(0, len(new_node_list) - 1):
            # 最后一个节点next指向null
            if i == len(new_node_list) - 1:
                new_node_list[i].next = None
            # 其他节点，直接指向后一个节点即可
            new_node_list[i].next = new_node_list[i + 1]

        # 同时遍历原链表、新链表，处理新链表每个节点的random指针
        for i in range(0, len(new_node_list)):
            random_node = old_node_list[i].random  # 获取旧链表当前节点的random指针

            if random_node is None:
                new_node_list[i].random = None  # 如果random_node为空，则直接指为空
            else:
                random_index = hash_node[random_node]  # 获取random指针对应的索引
                new_node_list[i].random = new_node_list[random_index]  # 赋值新链表节点的random指针

        return new_head

    '''
    优化一版：
        1. 去掉 old_node_list 和 new_node_list，直接使用 hash_map 存储新旧节点的映射
        2. 用 hash_map.get() 处理 None 值，避免 if 语句，提高代码可读性
        3. 减少遍历次数，一次构建哈希表，一次链接 next 和 random，更高效
    '''
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head  # 处理空链表

        hash_map = {}  # 旧节点 -> 新节点的映射
        cur = head

        # 第一遍遍历：创建新节点，并存入哈希表
        while cur:
            hash_map[cur] = Node(cur.val)  # 创建新节点，并映射旧节点
            cur = cur.next

        # 第二遍遍历：赋值 next 和 random
        cur = head
        while cur:
            hash_map[cur].next = hash_map.get(cur.next)  # 赋值 next（可能为空）
            hash_map[cur].random = hash_map.get(cur.random)  # 赋值 random（可能为空）
            cur = cur.next

        return hash_map[head]  # 返回新链表的头节点

    # 方法二：拼接 + 拆分
    def copyRandomList3(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head  # 处理空链表

        # 复制节点，拼接成为新链表
        cur = head
        while cur:
            temp = Node(cur.val)  # 创建新节点
            temp.next = cur.next  # 链接后节点
            cur.next = temp  # 链接前节点
            cur = temp.next  # 向后遍历，跳过新加的temp节点

        # 构建新链表的random指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next  # 如果cur.random不为空，则执行本逻辑
            cur = cur.next.next

        # 拆分两链表
        prev, cur, result = head, head.next, head.next
        # 当cur.next为空时结束循环（因为此时新连接节点才是最后一个节点）
        while cur.next:
            # 分别改变next指向
            prev.next = prev.next.next
            cur.next = cur.next.next
            # 此时指向已经改变，直接向后走一步即可
            prev = prev.next
            cur = cur.next

        prev.next = None  # 单独处理一下原链表尾节点
        return result


def test(lst: list):
    sol = Solution()
    random_linked_list = list_to_random_linked_list(lst)
    result = sol.copyRandomList(random_linked_list)
    print(random_linked_list_to_list(result))


if __name__ == '__main__':
    lst1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    lst2 = [[1, 1], [2, 1]]
    lst3 = [[3, None], [3, 0], [3, None]]

    test(lst1)
    test(lst2)
    test(lst3)