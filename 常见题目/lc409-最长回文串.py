# -*- coding: utf-8 -*-
"""
    @Time    : 2/27/25 14:55
    @Author  : Yanjiakang
    @File    : lc409-最长回文串.py
"""
from collections import Counter


class Solution:
    # Counter
    def longestPalindrome(self, s: str) -> int:
        max_len, flag = 0, 0
        hash_map = Counter(s)  # 直接使用Counter来统计次数

        # 遍历hash_map的val，计算结果
        for val in hash_map.values():
            rem = val % 2  # 计算余数
            max_len += val - rem  # 增加长度
            if rem == 1:
                flag = 1  # 更新标志位

        return max_len + flag

    # 哈希表
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_len = 0  # 字符串s有元素，至少都能返回1
        hash_map = {}  # 哈希表，key=字符、val=出现次数
        flag = 0  # 标记，如果存在出现奇数次的字符，则结果需要+1

        # 遍历字符串，完成映射关系
        for ch in s:
            if ch in hash_map:
                hash_map[ch] += 1
            else:
                hash_map[ch] = 1

        # 遍历hash_map的val，计算结果
        for val in hash_map.values():
            rem = val % 2  # 计算余数
            max_len += val - rem  # 增加长度
            if rem == 1:
                flag = 1  # 更新标志位

        return max_len + flag