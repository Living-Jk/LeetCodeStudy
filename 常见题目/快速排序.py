# -*- coding: utf-8 -*-
"""
    @Time    : 2/27/25 14:17
    @Author  : Yanjiakang
    @File    : 快速排序.py
"""


'''
思路：快速排序是一种分治算法，通过选择一个基准（pivot），将数组划分为小于基准、等于基准、大于基准的三部分，递归地对前后两个部分进行排序，最终达到整体有序。
'''


def quick_sort(lst):
    # 结束递归条件：如果长度<=1，直接返回当前序列
    if len(lst) <= 1:
        return lst

    # 选择基准值，这里采取三数取中（防止极端情况）
    pivot = sorted([lst[0], lst[len(lst) // 2], lst[-1]])[1]

    # 每次分三个区间，大、小、等于，不断通过递归对区间进行排序，直到最后
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    # 递归排序左半部分和右半部分，并组合最终排序结果
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)  # 输出: [1, 1, 2, 3, 6, 8, 10]
