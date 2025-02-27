# -*- coding: utf-8 -*-
"""
    @Time    : 2/26/25 15:25
    @Author  : Yanjiakang
    @File    : lc225-用队列实现栈.py
"""
from collections import deque


class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)  # 尾插即可

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


class MyStack2:

    def __init__(self):
        self.queue1 = deque()  # 存储栈内元素
        self.queue2 = deque()  # 辅助入栈

    def push(self, x: int) -> None:
        # 1. 先把queue1队列中的元素插入queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        # 2. 插入新增元素x
        self.queue1.append(x)
        # 3. 再把queue2中的元素依次插入queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1
