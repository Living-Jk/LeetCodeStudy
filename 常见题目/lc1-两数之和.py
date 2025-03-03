# -*- coding: utf-8 -*-
"""
    @Time    : 2/21/25 16:10
    @Author  : Yanjiakang
    @File    : lc1-两数之和.py
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希集合
        hash_set = set()
        # 循环遍历
        for i in range(len(nums)):
            # 如果target-nums[i]在集合中，直接返回结果
            if target - nums[i] in hash_set:
                return [i, nums.index(target - nums[i])]
            else:
                # 不存在则将nums[i]插入集合
                hash_set.add(nums[i])

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 哈希表
        hash_map = dict()
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [i, hash_map[target - num]]
            else:
                hash_map[num] = i
