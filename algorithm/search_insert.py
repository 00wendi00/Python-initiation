#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : search_insert.py
# @Author: Wade Cheung
# @Date  : 2018/7/3
# @Desc  : 插值查找, 二分查找的变体 ：以更快的速度进行缩减


def insert_search(lis, key):
    low = 0
    high = len(lis) - 1
    times = 0

    while low < high:
        times += 1
        mid = low + int((high - low) * (key - lis[low]) / (lis[high] - lis[low]))   # 核心代码, 非中间位数
        if lis[mid] > key:
            high = mid - 1
        elif lis[mid] < key:
            low = mid + 1
        else:
            print('times: %d' % times)
            return mid

    print('times: %d' % times)
    return False


if __name__ == '__main__':
    LIST = [3, 5, 7, 18, 22, 54, 123, 199, 200, 222, 444]
    result = insert_search(LIST, 222)
    print(result)
