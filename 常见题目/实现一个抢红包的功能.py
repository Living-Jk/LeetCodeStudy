# -*- coding: utf-8 -*-
"""
    @Time    : 3/5/25 16:53
    @Author  : Yanjiakang
    @File    : 实现一个抢红包的功能.py
"""


import random


def distribute_red_packet(total_money, num_people):
    if total_money <= 0 or num_people <= 0:
        return []

    if num_people == 1:
        return [round(total_money, 2)]  # 只有一个人，直接拿走全部金额

    amounts = []  # 结果数组
    remain_money = total_money  # 剩余金额
    remain_people = num_people  # 剩余人数

    for _ in range(num_people - 1):
        # 设置最大分配额为平均数的2倍，避免一个人拿太多
        max_money = (remain_money / remain_people) * 2

        '''
        随机分配金额
            1. random.uniform(0.01, max_money - 0.01)：生成[0.01, max_money - 0.01]区间的随机小数
            2. max_money - 0.01：防止随机生成最大值，导致最后一个人没钱了
            3. round(x, 2)：保留2位小数
        '''
        money = round(random.uniform(0.01, max_money - 0.01), 2)
        amounts.append(money)

        # 更新剩余金额、人数
        remain_money -= money
        remain_people -= 1

    # 最后一个人拿剩余部分的钱
    amounts.append(round(remain_money, 2))
    return amounts


if __name__ == '__main__':
    res = distribute_red_packet(100, 10)
    print(res)
