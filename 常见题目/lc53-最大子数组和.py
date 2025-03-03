# -*- coding: utf-8 -*-
"""
    @Time    : 2/28/25 14:54
    @Author  : Yanjiakang
    @File    : lc53-最大子数组和.py
"""

from typing import List


class Solution:
    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i]代表以nums[i]结尾的连续子数组最大和
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            # 如果dp[i-1]<0，说明dp[i-1]对dp[i]提供负作用，nums[i]即为连续子数组最大和
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            # 如果dp[i-1]>=0，说明dp[i-1]对dp[i]提供正作用，nums[i] + dp[i-1]为连续子数组最大和
            else:
                dp[i] = nums[i] + dp[i - 1]

        return max(dp)

