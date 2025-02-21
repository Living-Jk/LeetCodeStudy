# -*- coding: utf-8 -*-
"""
    @Time    : 2/13/25 14:32
    @Author  : Yanjiakang
    @File    : lc11_盛水最多的容器.py
"""

from typing import List


class Solution:
    # 方法一：双指针
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0  # 处理空、只有一个元素的列表

        results = []  # 记录每次计算的结果

        #  设置 left、right 左右指针
        for left in range(0, len(height)):
            # right 初始设置为 left + 1，减少重复计算
            for right in range(left + 1, len(height)):
                area = (right - left) * min(height[left], height[right])  # 计算当前两节点间的水量大小
                results.append(area)  # 插入结果列表

        return max(results)  # 返回最大值即可

    # 方法一：双指针（贪心算法）
    def maxArea2(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # 设置双指针，分别指向首尾
        max_area = 0  # 保存最大水量（结果）

        while left < right:  # 当两指针未相遇时进行循环处理
            # 若left是短板，则计算面积，并移动left指针
            if height[left] < height[right]:
                temp_area = min(height[left], height[right]) * (right - left)  # 计算面积
                max_area = max(temp_area, max_area)  # 保存最大值
                left += 1  # 移动left指针
            # 若 right 是短板，则计算面积，并移动 right 指针
            else:
                temp_area = min(height[left], height[right]) * (right - left)  # 计算面积
                max_area = max(temp_area, max_area)  # 保存最大值
                right -= 1  # 移动 right 指针

        return max_area


def test(lst):
    sol = Solution()
    print(sol.maxArea2(lst))


if __name__ == '__main__':
    test([1, 8, 6, 2, 5, 4, 8, 3, 7])
    test([1, 1])
    test([1])
    test([])
