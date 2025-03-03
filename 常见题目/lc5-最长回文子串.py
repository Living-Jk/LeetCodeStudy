# -*- coding: utf-8 -*-
"""
    @Time    : 2/27/25 17:10
    @Author  : Yanjiakang
    @File    : lc5-最长回文子串.py
"""


def longestPalindrome2(self, s: str) -> int:
    if len(s) <= 1:
        return s  # 处理无效输入

    max_len = 1
    result = ''

    for left in range(len(s)):
        # 反向寻找s[left]是否存在，如果存在，进行下一步操作，如果不存在，直接进行下一次循环
        right = s.rfind(s[left])

        # 没找到，直接下一次循环
        if left >= right or right == -1:
            continue

        # 找到了，对比左右区间的字符串与倒序后的字符串是否相等，相等说明是回文串，计算长度并保留较大值
        temp = s[left:right + 1]
        if temp == temp[::-1] and len(temp) > max_len:
            max_len = len(temp)
            result = temp

    # 返回最长子串
    return result