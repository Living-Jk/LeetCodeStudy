# -*- coding: utf-8 -*-
"""
    @Time    : 2/27/25 17:33
    @Author  : Yanjiakang
    @File    : lc56-合并区间.py
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals  # 处理特殊输入

        intervals.sort()  # 先排序
        result = []  # 存放结果

        start, end = intervals[0][0], intervals[0][1]  # 定义start、end

        # 从第二个区间开始遍历
        for val in intervals[1:]:
            # 如果 end > 当前区间最大值，说明[start, end]已经覆盖当前区域，直接进入下一次遍历
            if end > val[1]:
                continue
            # 如果 end < 当前区间最小值，说明[start, end]无法覆盖当前区域
            elif end < val[0]:
                result.append([start, end])
                start, end = val[0], val[1]
            else:
                # 走到这里，说明 当前区间左边界 < end < 右边界，说明能连上，直接更新end
                end = val[1]

        result.append([start, end])  # 处理最后一组
        return result


