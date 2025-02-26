# -*- coding: utf-8 -*-
"""
    @Time    : 2/25/25 19:09
    @Author  : Yanjiakang
    @File    : lc232-用栈实现队列.py
"""

# 单栈实现
class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)  # 直接尾插即可

    def pop(self) -> int:
        if self.empty():
            return None

        self.stack = self.stack[::-1]  # 倒序排列
        num = self.stack.pop()  # 尾删（队头元素）
        self.stack = self.stack[::-1]  # 再次倒序
        return num

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# 双栈实现
class MyQueue2:

    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)  # 直接尾插即可

    def pop(self) -> int:
        peek = self.peek()
        self.out_stack.pop()
        return peek

    def peek(self) -> int:
        if self.out_stack:
            # 如果out_stack栈不为空，直接返回最后一个元素（out_stack为倒序栈）
            return self.out_stack[-1]
        elif not self.in_stack:
            # out_stack为空，且in_stack也为空，空队列，返回-1
            return -1
        else:
            # out_stack为空，但in_stack还有元素，需要把in_stack倒序放入out_stack，并且返回out_stack的尾部元素
            while self.in_stack:
                pop_num = self.in_stack.pop()
                self.out_stack.append(pop_num)
            return self.out_stack[-1]

    def empty(self) -> bool:
        # 当双栈都为空时，队列为空
        return not self.in_stack and not self.out_stack


if __name__ == '__main__':
    a = []
    b = None
    print(a, b)
    if a:
        print(a)

    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.empty())
