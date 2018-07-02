#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : search_binary.py
# @Author: Wade Cheung
# @Date  : 2018/7/2
# @Desc  : 二分查找 : 在有序表中,每次查找并对比low-high范围中的中间元素 . 时间复杂度为O(log2n)

def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            print('times: %s' % time)
            return mid

    print('times: %s' % time)
    return False


if __name__ == '__main__':
    LIST = [3, 5, 7, 18, 22, 54, 123, 199, 200, 222, 444]
    result = binary_search(LIST, 222)
    print(result)
