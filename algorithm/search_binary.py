#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : search_binary.py
# @Author: Wade Cheung
# @Date  : 2018/7/2
# @Desc  : 二分查找 : 在有序表中,每次查找并对比low-high范围中的中间元素 . 时间复杂度为O(log2n)


def binary_search(lis, key):
    """二分查找的mid运算是加法与除法，插值查找则是复杂的四则运算，而斐波那契查找只是最简单的加减运算。
    在海量数据的查找中，这种细微的差别可能会影响最终的查找效率。
    因此，三种有序表的查找方法本质上是分割点的选择不同，各有优劣，应根据实际情况进行选择

    :param lis:
    :param key:
    :return:
    """
    low = 0
    high = len(lis) - 1
    times = 0
    while low < high:
        times += 1
        mid = int((low + high) / 2)
        print(low, high, lis[mid])
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            print('times: %s' % times)
            return mid

    print('times: %s' % times)
    return False


if __name__ == '__main__':
    LIST = [3, 5, 7, 18, 22, 54, 123, 199, 200, 222, 444]
    result = binary_search(LIST, 222)
    print(result)
