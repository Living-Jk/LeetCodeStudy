# -*- coding: utf-8 -*-
"""
    @Time    : 2/20/25 11:23
    @Author  : Yanjiakang
    @File    : lc303_区域和检索-数组不可变.py
"""

from typing import List


class NumArray:
    # 方法：前缀和
    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)  # 前缀和数组
        # 计算前缀和
        for i, n in enumerate(nums):
            s[i + 1] = s[i] + n

        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]
