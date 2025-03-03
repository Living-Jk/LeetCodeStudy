# -*- coding: utf-8 -*-
"""
    @Time    : 2/28/25 10:39
    @Author  : Yanjiakang
    @File    : lc54-螺旋矩阵.py
"""

from typing import List


class Solution:
    # 4个指针螺旋循环
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []  # 处理特殊输入

        left, right = 0, len(matrix[0]) - 1  # 左右指针
        up, down = 0, len(matrix) - 1  # 上下指针
        result = []

        while left <= right and up <= down:
            # 打印当前第一行
            for i in range(left, right + 1):
                if up <= down:
                    result.append(matrix[up][i])
            up += 1

            # 打印当前最后一列
            for j in range(up, down + 1):
                if left <= right:
                    result.append(matrix[j][right])
            right -= 1

            # 打印当前最后一行
            for i in range(right, left - 1, -1):
                if up <= down:
                    result.append(matrix[down][i])
            down -= 1

            # 打印当前第一列
            for j in range(down, up - 1, -1):
                if left <= right:
                    result.append(matrix[j][left])
            left += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))