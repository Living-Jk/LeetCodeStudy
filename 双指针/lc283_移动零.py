# -*- coding: utf-8 -*-
"""
    @Time    : 1/23/25 12:13
    @Author  : Yanjiakang
    @File    : lc283_移动零.py
"""

from typing import List


# 方法一：双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        nums_len = len(nums)

        # 使用右指针遍历列表
        while right < nums_len:
            # 当右指针为非0数字时，进行交换
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                # 交换完成后，左指针向后移动
                left += 1
            # 右指针要保证每次都向后迭代
            right += 1

    # 方法二：直接赋值
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 遍历索引
        index = 0
        nums_len = len(nums)

        # 遍历列表
        for i in range(nums_len):
            # 当前节点为非0数字，直接赋值并迭代，否则直接跳过
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        # 结束循环后，非0数字都已处理完成，只需要在最后补几个0
        # 【0的数量 = 列表长度 - index】index即为目前已处理的数量
        for i in range(index, nums_len):
            nums[i] = 0

    # 直接掉包，删除0后尾插
    def moveZeroes3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0

        # 先统计0的个数
        count = nums.count(0)

        # 遍历列表，要把0的数量排除，否则会陷入死循环
        while index < len(nums) - count:
            # 如果当前节点为0，则直接删除，并且尾插一个0（索引index不能递增，因为可能下一个元素还是0）
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            # 当当前节点不再是0时，索引递增向后遍历
            if nums[index] != 0:
                index += 1


if __name__ == '__main__':
    sol = Solution()

    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)

    nums2 = [0]
    sol.moveZeroes(nums2)
    print(nums2)


