#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_heap.py
# @Author: Wade Cheung
# @Date  : 2018/8/22
# @Desc  : 堆排序, 最大堆

# 堆排序适用于记录数很多的情况

from collections import deque


def element_exchange(numbers, low, high):
    temp = numbers[low]

    # j 是low的左孩子节点
    i = low
    j = 2 * i

    while j <= high:
        # 如果右节点较大，则把j指向右节点
        if j < high and numbers[j] < numbers[j + 1]:
            j = j + 1
        if temp < numbers[j]:
            # 将numbers[j]调整到双亲节点的位置上
            numbers[i] = numbers[j]
            i = j
            j = 2 * i
        else:
            break
    # 被调整节点放入最终位置
    numbers[i] = temp


def top_heap_sort(numbers):
    length = len(numbers) - 1

    # 指定第一个进行调整的元素的下标
    # 它即该无序序列完全二叉树的第一个非叶子节点
    # 它之前的元素均要进行调整
    # cheer up！
    first_exchange_element = length // 2

    # 建立初始堆
    print(first_exchange_element)
    for i in range(first_exchange_element):
        element_exchange(numbers, first_exchange_element - i, length)

    # 将根节点放到最终位置，剩余无序序列继续堆排序
    # length-1 次循环完成堆排序
    for y in range(length - 1):
        temp = numbers[1]
        numbers[1] = numbers[length - y]
        numbers[length - y] = temp
        element_exchange(numbers, 1, length - y - 1)


# 元素的存储必须从1开始
# 涉及到左右节点的定位，和堆排序开始调整节点的定位
# 在下标0处插入0，不参与排序
L = deque([62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50])
L.appendleft(0)
top_heap_sort(L)
print(list(L)[1:])
