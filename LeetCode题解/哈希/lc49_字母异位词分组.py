# -*- coding: utf-8 -*-
"""
    @Time    : 2/11/25 16:15
    @Author  : Yanjiakang
    @File    : lc49_字母异位词分组.py
"""

from typing import List
from collections import defaultdict


class Solution:
    # 方法一：排序
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}  # 创建哈希表
        # 遍历列表，进行处理
        for s in strs:
            key = "".join(sorted(s))  # 字符串排序，作为哈希的kay
            if key in hash_map:
                hash_map[key].append(s)  # 如果key存在，直接尾插
            else:
                hash_map[key] = [s]  # 若key不存在，则需要手动创建一个列表

        return list(hash_map.values())  # hasp_map的values即为需要的分组列表（注意要转化为列表）

    # 方法一优化
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)  # 创建一个默认值为 list 的 defaultdict
        for s in strs:
            key = "".join(sorted(s))
            hash_map[key].append(s)  # 无需考虑key是否存在

        return list(hash_map.values())

    # 方法二：计数
    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)  # 创建一个默认值为 list 的 defaultdict
        for s in strs:
            counts = [0] * 26  # 26位数组，记录26个英文字母的数量
            for ch in s:
                counts[ord(ch) - ord('a')] += 1  # 遍历字符串，记录该字符串所含字母的数量

            # 要把list转化成tuple才能进行哈希，因为字典dict的key必须是不可变数据类型
            hash_map[tuple(counts)].append(s)  # 直接插入哈希表即可

        return list(hash_map.values())


