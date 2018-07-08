#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_quick1.py
# @Author: Wade Cheung
# @Date  : 2018/7/9
# @Desc  : 快速排序, 分治算法1.  优化, 注意while里的一点区别


def quick_sort1(lis, left, right):
    if left < right:
        print(lis)

        base = lis[left]  # 基准数
        m, n = left, right

        while m < n:
            while lis[n] >= base and m < n:
                n -= 1
            lis[m] = lis[n]

            while lis[m] <= base and m < n:
                m += 1
            lis[n] = lis[m]

        lis[m] = base

        quick_sort1(lis, left, m - 1)
        quick_sort1(lis, n + 1, right)

    return lis


l = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
print('结果:', quick_sort1(l, 0, len(l) - 1))
