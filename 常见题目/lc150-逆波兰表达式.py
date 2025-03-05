# -*- coding: utf-8 -*-
"""
    @Time    : 3/5/25 11:21
    @Author  : Yanjiakang
    @File    : lc150-逆波兰表达式.py
"""

from typing import List


class Solution:
    # 栈
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # 遍历tokens，遇到数字入栈，遇到操作符取出栈顶两元素进行运算再入栈
        for ch in tokens:
            # 若是操作符，则取出操作数进行运算再入栈（注意顺序：先取出的是右操作数）
            if ch in '+-*/':
                right, left = stack.pop(), stack.pop()  # 取操作数

                # 运算后入栈
                if ch == '+': stack.append(left + right)
                elif ch == '-': stack.append(left - right)
                elif ch == '*': stack.append(left * right)
                # elif ch == '/': stack.append(left // right)  # 不能用整除【向下取整】
                elif ch == '/': stack.append(int(left / right))  # 先除后转换【只截取小数部分】

            else:
                stack.append(int(ch))

        return stack[-1]

    def evalRPN2(self, tokens: List[str]) -> int:
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        stack = []
        for ch in tokens:
            if ch in op:
                right, left = stack.pop(), stack.pop()
                stack.append(op[ch](left, right))
            else:
                stack.append(int(ch))
        return stack[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))