# -*- coding: utf-8 -*-
"""
    @Time    : 3/4/25 14:13
    @Author  : Yanjiakang
    @File    : lc1143-最长公共子序列.py
"""


class Solution:
    # 动态规划
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)

        # 创建二维dp数组，dp[i][j]表示text1的前i个字符与text2的前j个字符的最长公共子序列长度（额外增加一行一列，便于处理边界值）
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:  # 如果相等，增加长度即可
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 不等则取前一个状态的最大值（dp[i-1][j] 或 dp[i][j-1]）
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # dp最后一个元素即为最大长度
        return dp[-1][-1]

