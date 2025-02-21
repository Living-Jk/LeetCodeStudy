# -*- coding: utf-8 -*-
"""
    @Time    : 2/14/25 11:24
    @Author  : Yanjiakang
    @File    : lc3_无重复字符的最长子串.py
"""


class Solution:
    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)  # 处理无效输入

        left, right = 0, 0  # 双指针指向不重复子串首尾
        cur = right + 1  # 遍历索引
        result = 0

        while cur < len(s):
            # 如果cur字符不存在于子串中，right指针向后移动，同时继续遍历
            if s[cur] not in s[left:right+1]:
                right += 1
                cur = right + 1
            # 如果存在子串中，则说明遇到了重复字符，结算长度，并向后遍历
            else:
                length = right - left + 1  # 计算子串长度
                result = max(result, length)  # 保存较大结果

                # 双指针向后，同时继续遍历
                left = right = left + 1
                cur = right + 1
        # while循环结束后，仍要进行一次结算，否则会丢失数据（当最后一个子串满足要求）
        else:
            length = right - left + 1  # 计算子串长度
            result = max(result, length)  # 保存较大结果

        return result

    # 优化版本
    def lengthOfLongestSubstring2(self, s: str) -> int:
        left, result = 0, 0  # 左指针、最大长度（结果）
        lookup = set()  # 集合，记录窗口内的字符

        # 右指针遍历字符串
        for right in range(len(s)):
            # 如果当前字符在窗口中，需要不断删除left指向字符，左指针向后遍历，直至将s[right]字符删掉为止
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1

            # 不在窗口中，直接插入集合，继续遍历即可
            lookup.add(s[right])
            result = max(result, right - left + 1)  # 更新最大长度

        return result


def test(s):
    sol = Solution()
    print(sol.lengthOfLongestSubstring2(s))


if __name__ == '__main__':
    test("abcabcbb")
    test("bbbbb")
    test("pwwkew")
    test("au")

