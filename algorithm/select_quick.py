#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : select_quick.py
# @Author: Wade Cheung
# @Date  : 2018/8/1
# @Desc  : 快速选择 , topk,找出第K小的数


# 在无序序列中找出第k小的数


def quick_select(lis, left, right, k):
    if left < right:
        print(lis)

        base = lis[left]  # 基准数
        m, n = left, right

        while m < n:
            while lis[n] >= base and m < n:
                n -= 1
            temp = lis[m]
            lis[m] = lis[n]
            lis[n] = temp

            while lis[m] <= base and m < n:
                m += 1
            temp = lis[n]
            lis[n] = lis[m]
            lis[m] = temp

        print(m, right)
        if k - 1 > m:
            return quick_select(lis, n + 1, right, k)
        elif k - 1 < m:
            return quick_select(lis, left, m - 1, k)
        else:
            return lis[k - 1]

    # 此步骤和 k-1比较m的时候配合使用 .
    if left == right:
        return lis[left]


l = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
# [29, 35, 36, 37, 48, 49, 50, 51, 56, 58, 62, 73, 88, 93, 99]
print('结果 : ', quick_select(l, 0, len(l) - 1, 14))
