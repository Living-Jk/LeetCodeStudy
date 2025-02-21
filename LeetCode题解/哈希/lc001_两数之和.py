# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 11:36
    @Author  : Yanjiakang
    @File    : lc001_两数之和.py
"""

# LeetCode 1.两数之和

from typing import List


class Solution:
    # 解法一：暴力枚举
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 先计算列表长度，便于后续使用
        num_len = len(nums)

        # 外循环从头到尾
        for i in range(0, num_len):
            # 内循环从i + 1开始，避免重复
            for j in range(i + 1, num_len):
                # 如果2个元素之和为tar，即找到目标
                if nums[i] + nums[j] == target:
                    return [i, j]

        # 跳出循环说明找不到
        return None

    # 解法二：哈希表
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 创建哈希表
        hash_table = dict()

        # 循环查找：运用enumerate方法可遍历可迭代对象（如列表、元组或字符串），同时获得索引和值
        for i, num in enumerate(nums):

            # 如果target-num的值存在于哈希表中，则直接返回两下标即可
            if target - num in hash_table:
                return [i, hash_table[target - num]]

            # 如果不存在于哈希表，则将本节点元素插入哈希表，继续循环（数值为key，下标为value）
            hash_table[num] = i


if __name__ == '__main__':
    sol = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = sol.twoSum(nums1, target1)
    print(result1)

    nums2 = [3, 2, 4]
    target2 = 6
    result2 = sol.twoSum(nums2, target2)
    print(result2)

    nums3 = [3, 3]
    target3 = 6
    result3 = sol.twoSum(nums3, target3)
    print(result3)








# 为什么列表直接找不行，因为存在相同值，2-1=1，如果列表有两个1，就会找错【0 1 1 3， 目标值为2】
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, num in enumerate(nums):
#             if target - num in nums:
#                 return [i, nums.index(target - num)]
#         return None



