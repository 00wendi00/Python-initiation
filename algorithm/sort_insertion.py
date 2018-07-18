#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_insertion.py
# @Author: Wade Cheung
# @Date  : 2018/7/18
# @Desc  : 插入排序, 取出值,放到合适位置, 时间复杂度为O（n^2）. 与sort_bubble比较 --> 减少了比较次数,交换次数未变


def insertion_sort(lis):
    compareTimes = 0  # 记录比较次数
    exchangeTime = 0  # 记录交换次数, 此形容不够准确

    for index in range(1, len(lis)):
        currentvalue = lis[index]  # 先把index位置的值拿出来
        position = index

        # 当此轮未比较完 & 前一个比currentvalue大
        while position > 0 and lis[position - 1] > currentvalue:
            exchangeTime += 1
            compareTimes += 1

            lis[position] = lis[position - 1]  # 值往后移
            position = position - 1  # 再往前面一个找
        else:
            if position > 0:
                compareTimes += 1  # 前某个数比currentvalue小时, 也比较了一次, 终止while

        lis[position] = currentvalue  # 将取出来的放入合适位置

    print(compareTimes)
    print(exchangeTime)


alist = [5, 30, 20, 40, 90, 50, 10, 60, 70, 80, 100, 110]
insertion_sort(alist)
print(alist)
