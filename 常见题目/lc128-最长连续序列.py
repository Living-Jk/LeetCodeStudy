# -*- coding: utf-8 -*-
"""
    @Time    : 2/28/25 16:26
    @Author  : Yanjiakang
    @File    : lc128-最长连续序列.py
"""

from typing import List


class Solution:
    # 方法二：哈希集合
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)  # 集合
        max_len, cur_len = 0, 0

        for num in nums_set:
            # 如果num-1在集合中，说明num不是连续序列的最小值，直接跳过即可
            if num - 1 in nums_set:
                continue

            # 找到当前连续序列最小值，开始向后查找
            while num in nums_set:
                cur_len += 1
                num += 1

            max_len = max(max_len, cur_len)
            cur_len = 0

        return max_len


