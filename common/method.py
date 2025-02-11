# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:26
    @Author  : Yanjiakang
    @File    : method.py
"""
from type.date_structure import ListNode, RandomListNode


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


# 将列表转化为 RandomListNode 链表
def list_to_random_linked_list(lst):
    if not lst:  # 如果列表为空，直接返回 None
        return None

    # 第一步：创建所有节点，并存入 nodes 数组
    nodes = [RandomListNode(val) for val, _ in lst]

    # 第二步：设置 next 指针
    for i in range(len(lst) - 1):
        nodes[i].next = nodes[i + 1]

    # 第三步：设置 random 指针
    for i, (_, random_idx) in enumerate(lst):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]

    # 返回链表的头节点
    return nodes[0]


# 将 RandomListNode 链表转化为列表
def random_linked_list_to_list(head):
    if not head:
        return []

    nodes = []  # 存储链表节点的列表
    node_to_index = {}  # 存储节点 -> 索引 映射

    # **第一遍遍历**：存储所有节点及其索引
    cur = head
    index = 0
    while cur:
        nodes.append(cur)
        node_to_index[cur] = index
        cur = cur.next
        index += 1

    # **第二遍遍历**：构造转换后的二维列表
    result = []
    for node in nodes:
        val = node.val
        random_idx = node_to_index[node.random] if node.random else None
        result.append([val, random_idx])

    return result