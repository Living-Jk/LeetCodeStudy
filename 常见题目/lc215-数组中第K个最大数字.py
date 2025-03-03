# -*- coding: utf-8 -*-
"""
    @Time    : 2/27/25 17:12
    @Author  : Yanjiakang
    @File    : lc215-数组中第K个最大数字.py
"""
from typing import List


class Solution:
    # 直接用内置函数排序
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[k-1]

    # 快排
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        sorted_nusm = self.quickSort(nums)
        return sorted_nusm[-k]

    def quickSort(self, nums: List[int]) -> List[int]:
        # 递归停止条件
        if len(nums) <= 1:
            return nums

        # 选择基准值（三数取中法）
        pivot = sorted([nums[0], nums[len(nums) // 2], nums[-1]])[1]

        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        return self.quickSort(left) + middle + self.quickSort(right)
