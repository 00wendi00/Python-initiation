#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_shell.py
# @Author: Wade Cheung
# @Date  : 2018/7/18
# @Desc  : 希尔排序, 将序列分为几个区域来提升插入排序的效率, 时间复杂度为O（n^2）. 注意步长选择


def shell_sort(lis):
    compareTimes = 0  # 记录比较次数
    exchangeTime = 0  # 记录交换次数, 此形容不够准确

    sublistcount = len(lis) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            compareTimes, exchangeTime = gapInsertionSort(lis, startposition, sublistcount, compareTimes, exchangeTime)

        print('After increments of size', sublistcount, 'The list is', lis)

        sublistcount = sublistcount // 2

    print(compareTimes)
    print(exchangeTime)


def gapInsertionSort(lis, start, gap, compareTimes, exchangeTime):
    for i in range(start + gap, len(lis), gap):
        currentvalue = lis[i]
        position = i

        while position >= gap and lis[position - gap] > currentvalue:
            exchangeTime += 1
            compareTimes += 1

            lis[position] = lis[position - gap]
            position = position - gap
        else:
            if position >= gap:
                compareTimes += 1  # 前某个数比currentvalue小时, 也比较了一次, 终止while

        lis[position] = currentvalue

    return compareTimes, exchangeTime


alist = [5, 30, 20, 40, 90, 50, 10, 60, 70, 80, 100, 110]
shell_sort(alist)
print(alist)
