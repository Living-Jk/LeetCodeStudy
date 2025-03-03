# -*- coding: utf-8 -*-
"""
    @Time    : 2/28/25 14:25
    @Author  : Yanjiakang
    @File    : lc3-无重复最长子串.py
"""


class Solution:
    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len = 0, 0
        lookup = set()

        for right in range(len(s)):
            # 当遇到重复字符时，删除left指针指向的元素，并且left指针向后移动
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1

            # 插入窗口, 计算长度
            lookup.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
