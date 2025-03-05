# -*- coding: utf-8 -*-
"""
    @Time    : 2/27/25 17:10
    @Author  : Yanjiakang
    @File    : lc5-最长回文子串.py
"""


class Solution:
    # 动态规划
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s <= 1:
            return s  # 处理特殊输入

        # 创建二维dp数组，dp[i][j]表示 s[i..j](包含s[i]、s[j])是否为回文串
        dp = [[False] * len_s for _ in range(len_s)]
        max_len, start = 1, 0  # 分别记录最长长度、子串起始位置

        for j in range(len_s):
            for i in range(j + 1):  # i<=j 才合法
                '''
                当s[i]=s[j]时：
                    1. 长度 j-i+1<=2 时，一定是回文子串;
                    2. s[i+1][j-1]是回文串（去头去尾），则s[i..j]是回文串;
                当s[i]!=s[j]时:不可能是回文串
                '''
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if j - i + 1 > max_len:
                        start, max_len = i, j - i + 1
        return s[start: start + max_len]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('babad'))
    print(sol.longestPalindrome('cbbd'))


# def longestPalindrome2(self, s: str) -> int:
#     if len(s) <= 1:
#         return s  # 处理无效输入
#
#     max_len = 1
#     result = ''
#
#     for left in range(len(s)):
#         # 反向寻找s[left]是否存在，如果存在，进行下一步操作，如果不存在，直接进行下一次循环
#         right = s.rfind(s[left])
#
#         # 没找到，直接下一次循环
#         if left >= right or right == -1:
#             continue
#
#         # 找到了，对比左右区间的字符串与倒序后的字符串是否相等，相等说明是回文串，计算长度并保留较大值
#         temp = s[left:right + 1]
#         if temp == temp[::-1] and len(temp) > max_len:
#             max_len = len(temp)
#             result = temp
#
#     # 返回最长子串
#     return result