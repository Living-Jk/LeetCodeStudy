# -*- coding: utf-8 -*-
"""
    @Time    : 3/4/25 11:25
    @Author  : Yanjiakang
    @File    : 最长公共子串.py
"""


class Solution:
    # 动态规划
    def longestCommonSubstring(self, str1: str, str2: str) -> (int, str):
        len1, len2 = len(str1), len(str2)

        # 创建二维dp数组，需要额外添加一行一列，便于处理边界情况
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        max_len, end_pos = 0, 0  # max_len记录最大长度、end_pos记录最长子串的末尾索引

        # 遍历两个字符串
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i - 1] == str2[j - 1]:  # 如果相等，需要更新dp
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:  # 如果出现更大值，更新max_len、end_pos
                        max_len = dp[i][j]
                        end_pos = i
                else:
                    dp[i][j] = 0  # 不连续，直接清零

        return max_len, str1[end_pos - max_len: end_pos]


if __name__ == '__main__':
    sol = Solution()
    max_len, result = sol.longestCommonSubstring('abcde', 'abfce')
    print(f"max_len={max_len}, str={result}")
