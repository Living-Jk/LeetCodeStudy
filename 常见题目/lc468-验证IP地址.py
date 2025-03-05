# -*- coding: utf-8 -*-
"""
    @Time    : 3/5/25 15:03
    @Author  : Yanjiakang
    @File    : lc468-验证IP地址.py
"""


class Solution:

    def isIPv4(self, queryIP: str) -> bool:
        ip_list = queryIP.split('.')

        if len(ip_list) != 4:  # 如果不是4部分组成，直接返回false
            return False

        for ip in ip_list:
            # 如果每部分数字小于0 or 大于255 or 大于0但含有前导零，直接返回False
            if len(ip) < 1 or len(ip) > 3 or ip < '0' or ip > '255' or (ip > '0' and ip.startswith('0')):
                return False
        return True

    def isIPv6(self, queryIP: str) -> bool:
        ip_list = queryIP.split(':')

        if len(ip_list) != 8:
            return False

        for ip in ip_list:
            if len(ip) > 4 or len(ip) < 1:
                return False
            for s in ip:
                if s not in "01234567789ABCDEFabcdef":
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return "IPv4"
        elif self.isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"


if __name__ == '__main__':
    sol = Solution()
    print(sol.validIPAddress("172.16.254.1"))
    print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(sol.validIPAddress("256.256.256.256"))