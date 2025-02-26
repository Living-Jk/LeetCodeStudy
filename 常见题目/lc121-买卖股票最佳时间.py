# -*- coding: utf-8 -*-
"""
    @Time    : 2/21/25 16:47
    @Author  : Yanjiakang
    @File    : lc121-买卖股票最佳时间.py
"""
from typing import List


class Solution:
    # 暴力解法（超时）
    def maxProfit(self, prices: List[int]) -> int:
        # 如果prices为空 or 只有一个元素，返回0
        if len(prices) <= 1:
            return 0

        max_profit = 0  # 记录最大利润

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit

    # 稍微优化一下，当prices[j] > 当prices[i]的时候在计算，减少计算次数（仍然超时）
    def maxProfit(self, prices: List[int]) -> int:
        # 如果prices为空 or 只有一个元素，返回0
        if len(prices) <= 1:
            return 0

        max_profit = 0  # 记录最大利润

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)

        return max_profit

    # 贪心
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = prices[0], 0  # cost为花费（最低价格为花费）、profit为利润，取最大值
        for price in prices:
            cost = min(cost, price)  # cost取最小值
            profit = max(profit, price - cost)  # 计算利润，并取最大值
        return profit

