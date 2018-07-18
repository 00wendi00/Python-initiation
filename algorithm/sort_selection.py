#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_selection.py
# @Author: Wade Cheung
# @Date  : 2018/7/18
# @Desc  : 选择排序, 每次找出最大数的位置, 将最大数交换到对应位置 --> 比较次数未变, 减少了交换次数


def selection_sort(lis):
    compareTimes = 0  # 记录比较次数
    exchangeTime = 0  # 记录交换次数

    for fileslot in range(len(lis) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fileslot + 1):
            compareTimes += 1

            # 找出最大数的位置
            if lis[location] > lis[positionOfMax]:
                positionOfMax = location

        exchangeTime += 1
        # 将最大数交换到对应位置
        temp = lis[fileslot]
        lis[fileslot] = lis[positionOfMax]
        lis[positionOfMax] = temp

    print(compareTimes)
    print(exchangeTime)


# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
selection_sort(alist)
print(alist)
