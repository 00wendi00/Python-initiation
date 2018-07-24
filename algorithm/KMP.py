#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : KMP.py
# @Author: Wade Cheung
# @Date  : 2018/7/24
# @Desc  : KMP算法.   移动位数;部分匹配表

# 字符串匹配是计算机的基本任务之一


def pmt(s):
    """
    Partial Math Table -- 部分匹配表
    “部分匹配”的实质是，有时候，字符串头部和尾部会有重复。比如，”ABCDAB”之中有两个”AB”，那么它的”部分匹配值”就是2（”AB”的长度）。
    搜索词移动的时候，第一个”AB”向后移动4位（字符串长度-部分匹配值），就可以来到第二个”AB”的位置。
    :param s:
    :return:
    """
    prefix = [s[:i + 1] for i in range(len(s) - 1)]  # 前缀
    postfic = [s[i + 1:] for i in range(len(s) - 1)]  # 后缀
    intersection = list(set(prefix) & set(postfic))  # 找出部分匹配表str
    if intersection:
        return len(intersection[0])
    return 0


def kmp(big, small):
    i = 0
    while i < len(big) - len(small) + 1:
        match = True
        for j in range(len(small)):
            if big[i + j] != small[j]:
                match = False
                break
        if match:
            print(i)
            return True
        # 移动位数 = 已匹配的字符数 - 对应的部分匹配值
        if j:
            i += j - pmt(small[:j])  # 已经匹配到的small的部分
        else:
            i += 1
    return False


k1 = 'BBC ABCDAB ABCDAAAAAAAAAAAABCDABDE'
k2 = 'ABCDABD'
print(kmp(k1, k2))

print(pmt('cabcdefgab123abc'))
