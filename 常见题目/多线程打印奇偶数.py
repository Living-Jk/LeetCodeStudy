# -*- coding: utf-8 -*-
"""
    @Time    : 3/5/25 16:17
    @Author  : Yanjiakang
    @File    : 多线程打印奇偶数.py
"""


import threading


# 打印奇数
def print_odd(max_num):
    for num in range(max_num):
        if num % 2 == 1:
            print(f"odd:{num}")


# 打印偶数
def print_even(max_num):
    for num in range(max_num):
        if num % 2 == 0:
            print(f"odd:{num}")


def main():
    max_num = 20

    # 创建线程
    odd_thread = threading.Thread(target=print_odd, args=(max_num, ))
    even_thread = threading.Thread(target=print_even, args=(max_num, ))

    # 启动线程
    odd_thread.start()
    even_thread.start()

    # 等待线程
    # odd_thread.join()
    # even_thread.join()


if __name__ == '__main__':
    main()
