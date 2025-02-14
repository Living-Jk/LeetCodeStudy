# -*- coding: utf-8 -*-
"""
    @Time    : 2/13/25 15:58
    @Author  : Yanjiakang
    @File    : lc15_三数之和.py
"""

from typing import List


class Solution:
    # 方法一：双指针（暴力循环）
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []  # 处理元素个数<3的列表

        result = []  # 存放结果
        # 三重循环进行遍历
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):

                    # 找到三数之和为0的三个下标
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp_list = sorted([nums[i], nums[j], nums[k]])  # 形成子列表并排序
                        if temp_list not in result:  # 判断 temp_list 是否存在于结果集 result 中，因为我们已经排好序，所以直接判断即可
                            result.append(temp_list)

        return result

    # 优化版本，排序+双指针
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []  # 处理无效输入

        nums.sort()  # 排序
        result = []  # 存放结果

        # 使用i从头遍历数组nums
        for i in range(len(nums)):
            # i从头遍历，指向的永远是最小的数字，如果此时nums[i]>0，说明不可能再有三数之和==0，因此直接返回result，减少遍历
            if nums[i] > 0:
                return result
            # 如果下一个数字与当前数字相同，直接跳过，因为必定得到的是相同解，减少遍历
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 设置双指针left、right分别指向[i+1, len(nums)-1]
            left, right = i + 1, len(nums) - 1
            # 逐渐向中间逼近
            while left < right:
                # 找到三数之和为0的三个数字
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])  # 插入结果列表
                    # 同时left、right双指针要同时向中间逼近，并且要过滤重复数字，避免重复计算
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 注意：要先过滤重复数字，再向中间逼近（如果先逼近，大概率过滤的就不是当前数字了）
                    left, right = left + 1, right - 1

                # 如果三数之和>0，说明需要一个更小的数字，所以右指针right向左移动
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                # 如果三数之和<0，说明需要一个更大的数字，所以左指针left向左移动
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        return result


def test(lst):
    sol = Solution()
    # print(sol.threeSum(lst))
    print(sol.threeSum2(lst))


if __name__ == '__main__':
    test([-1, 0, 1, 2, -1, -4])
    test([0, 1, 1])
    test([0, 0, 0])
    test([-2, 0, 1, 1, 2])
