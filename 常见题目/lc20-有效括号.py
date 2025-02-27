# -*- coding: utf-8 -*-
"""
    @Time    : 2/26/25 23:09
    @Author  : Yanjiakang
    @File    : lc20-有效括号.py
"""
from collections import deque


class Solution:
    # 栈
    def isValid(self, s: str) -> bool:
        # 建立括号映射，key为右括号，val为左括号
        map = {')': '(', ']': '[', '}': '{'}
        stack = deque()

        # 遍历字符串
        for ch in s:
            # 如果遇到左括号则入栈
            if ch in map.values():
                stack.append(ch)
            # 如果遇到右括号需要进行判断
            if ch in map.keys():
                # 注意这里要判断stack是否为空，可能存在类似')))'只有右括号的字符串，此时stack为空
                if not stack or stack.pop() != map[ch]:
                    return False  # 如果左右括号不匹配，直接返回False

        # 结束循环后需要检查一下stack是否为空，为空返回True
        return len(stack) == 0
