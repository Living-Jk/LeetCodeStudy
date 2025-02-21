# -*- coding: utf-8 -*-
"""
    @Time    : 2/12/25 11:36
    @Author  : Yanjiakang
    @File    : lc128_最长连续序列.py
"""

from typing import List


class Solution:
    # 方法一：直接排序
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # 处理空列表

        longest_count = 0  # 记录最长序列长度
        current_count = 1  # 记录当前序列长度
        nums.sort()  # 排序

        # 一遍循环搞定
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:  # 若 当前数字 + 1 = 后一个数子，则说明连续，长度+1
                current_count += 1
            elif nums[i] == nums[i + 1]:  # 跳过相等的数字
                continue
            else:  # 这个序列结束
                if current_count > longest_count:  # 更新最长长度
                    longest_count = current_count
                current_count = 1  # 重置current_count，继续找下一个序列
        else:  # for循环结束时做一次判断，看最长长度是否有变化
            if current_count > longest_count:  # 更新最长长度
                longest_count = current_count

        return longest_count

    # 方法二：哈希集合
    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0  # 处理空列表

        longest_count = 0  # 记录最长序列长度
        current_count = 1  # 记录当前序列长度
        nums_set = set(nums)  # 转化为集合，提高查询效率并去重

        # 遍历集合
        for num in nums_set:
            # 如果num-1在集合中，直接跳过
            if num - 1 in nums_set:
                continue

            # 能走到这里，说明当前数值是该序列的起点，向后寻找，直到序列不连续为止
            temp = num
            while temp + 1 in nums_set:  # 向后一直+1寻找连续序列，直到找不到为止
                current_count += 1
                temp += 1

            # 跳出循环后，说明本连续序列已经遍历结束，更新最长长度
            if current_count > longest_count:
                longest_count = current_count

            current_count = 1  # 本序列已经结束，重置current_count

        return longest_count


def test(lst):
    sol = Solution()
    # print(sol.longestConsecutive1(lst))
    print(sol.longestConsecutive2(lst))


if __name__ == '__main__':
    lst1 = [100, 4, 200, 1, 3, 2]
    lst2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    test(lst1)
    test(lst2)
    test([1, 0, -1])
    test([9,1,4,7,3,-1,0,5,8,-1,6])
    test([9,1,-3,2,4,8,3,-1,6,-2,-4,7])

