# -*- coding: utf-8 -*-
"""
    @Time    : 3/4/25 17:03
    @Author  : Yanjiakang
    @File    : lc22-括号生成.py
"""

from typing import List


class Solution:
    # 回溯法
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # 递归函数：path-存储括号的列表；left-左括号数量；right-右括号数量
        def backtrack(path, left, right):
            # 递归终止条件：括号用完（即左右括号数量都为n）
            if left == n and right == n:
                res.append("".join(path))
                return

            # 当 ( < n，直接添加(
            if left < n:
                path.append('(')
                backtrack(path, left + 1, right)
                path.pop()  # 回溯

            # 当 ) < (，添加 )
            if right < left:
                path.append(')')
                backtrack(path, left, right + 1)
                path.pop()

        # 初始递归调用
        backtrack([], 0, 0)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path: str, left: int, right: int):
            # 终止条件：括号已用完
            if left == n and right == n:
                res.append(path)
                return

            # 剪枝优化
            if left < n:  # 只有左括号数量小于 n，才可以加 '('
                backtrack(path + "(", left + 1, right)
            if right < left:  # 只有右括号数量小于左括号数量，才可以加 ')'
                backtrack(path + ")", left, right + 1)

        # 递归调用
        backtrack("", 0, 0)
        return res
