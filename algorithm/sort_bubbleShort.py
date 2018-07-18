#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_bubbleShort.py
# @Author: Wade Cheung
# @Date  : 2018/7/18
# @Desc  : 短冒泡排序, 时间复杂度为O（n^2）, 与sort_bubble比较 --> 减少了比较次数,交换次数未变


def shortBubbleSort(alist):
    exchanges = True  # 是否继续循环的标记
    passnum = len(alist) - 1
    compareTimes = 0  # 记录比较次数
    exchangeTime = 0  # 记录交换次数
    # 当此轮未比较完 & 继续循环(发生了交换)
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            compareTimes += 1

            if alist[i] > alist[i + 1]:
                exchangeTime += 1

                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1

    print(compareTimes)
    print(exchangeTime)


lis = [5, 30, 20, 40, 90, 50, 10, 60, 70, 80, 100, 110]
shortBubbleSort(lis)
print(lis)
