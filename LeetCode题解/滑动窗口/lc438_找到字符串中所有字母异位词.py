# -*- coding: utf-8 -*-
"""
    @Time    : 2/14/25 14:36
    @Author  : Yanjiakang
    @File    : lc438_找到字符串中所有字母异位词.py
"""

from typing import List


class Solution:
    # 滑动窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        left, result = 0, []  # 左指针、记录结果列表
        len_p = len(p)  # 目标子串p的长度
        p = sorted(p)  # 把p进行排序，方便比较

        # 使用右指针right遍历字符串
        for right in range(len(s)):

            if right - left + 1 < len_p:
                continue  # 窗口内子串长度<目标子串长度，直接进行下一次循环，增加窗口内子串长度
            elif right - left + 1 > len_p:
                left += 1  # 窗口内子串长度>目标子串长度，左指针向后移动，减少窗口内子串长度
            else:
                # 窗口内子串长度==目标子串长度，判断窗口内子串是否为目标子串的异位词
                if sorted(s[left:right + 1]) == p:
                    result.append(left)
                left += 1

        return result

    # 不排序，用数组比较
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)  # s、p字符串长度
        if len_s < len_p:
            return []  # 如果字符串长度 < 目标子串长度，直接返回空即可

        # 因为字符串中只包含小写字母，可采用26位数组代表子串中所含字母以及对应个数
        p_count = [0] * 26
        s_count = [0] * 26
        # 分别初始化p_count、s_count，s_count初始化为len_p长度的子串
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        for i in range(len_p):
            s_count[ord(s[i]) - ord('a')] += 1

        result = []  # 记录结果列表

        # 使用右指针right遍历字符串，因为窗口已经包含了len_p长度的子串，所以从len_p开始
        for right in range(len_p, len_s):
            if s_count == p_count:  # 若相等，插入窗口左端索引
                result.append(right - len_p)
            # 进窗口：右端字符加入
            s_count[ord(s[right]) - ord('a')] += 1
            # 出窗口：左端字符移除
            s_count[ord(s[right - len_p]) - ord('a')] -= 1

        # 处理最后一个窗口
        if s_count == p_count:
            result.append(len_s - len_p)

        return result


def test(s, p):
    sol = Solution()
    print(sol.findAnagrams2(s, p))


if __name__ == '__main__':
    test("cbaebabacd", "abc")
    test("abab", "ab")
