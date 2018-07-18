#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_bubble.py
# @Author: Wade Cheung
# @Date  : 2018/7/8
# @Desc  : 冒泡排序 , 两个for循环加一个if判断 . 时间复杂度为O（n^2）.  注意比较次数


def bubble_sort(lis):
    compareTimes = 0  # 记录比较次数
    exchangeTime = 0  # 记录交换次数
    for m in range(len(lis)):
        for n in range(m):
            compareTimes += 1
            if lis[m] < lis[n]:
                exchangeTime += 1
                lis[m] = lis[m] + lis[n]
                lis[n] = lis[m] - lis[n]
                lis[m] = lis[m] - lis[n]

    print(compareTimes)
    print(exchangeTime)

    return lis


# l = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
l = [20, 30, 40, 90, 50, 10, 60, 70, 80, 100, 110, 5]
print(bubble_sort(l))
