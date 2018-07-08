#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_bubble.py
# @Author: Wade Cheung
# @Date  : 2018/7/8
# @Desc  : 冒泡排序 , 两个for循环加一个if判断


def bubble_sort(lis):
    for m in range(len(lis)):
        for n in range(m):
            if lis[n] < lis[m]:
                lis[m] = lis[m] + lis[n]
                lis[n] = lis[m] - lis[n]
                lis[m] = lis[m] - lis[n]

    return lis


l = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
print(bubble_sort(l))
