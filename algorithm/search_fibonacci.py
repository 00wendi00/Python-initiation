#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : search_fibonacci.py
# @Author: Wade Cheung
# @Date  : 2018/7/3
# @Desc  : 斐波拉契查找

from algorithm.Fibonacci import fibonacci_create


def fibonacci_search(lis, key):
    """斐波拉契查找, 平均性能，要优于二分查找。但是在最坏情况下，比如这里如果key为1，则始终处于左侧半区查找，此时其效率要低于二分查找

    :param lis:
    :param key:
    :return:
    """
    fib = fibonacci_create(100)

    low = 0
    high = len(lis) - 1

    # 为了使得查找表满足斐波那契特性，在表的最后添加几个同样的值
    # 这个值是原查找表的最后那个元素的值
    # 添加的个数由fib[k]-i-1决定
    k = 0
    while high > fib[k] - 1:
        k += 1
    print(k)

    i = high
    while fib[k] - 1 > i:
        lis.append(lis[high])
        i += 1
    print(lis)

    times = 0
    while low <= high:
        times += 1
        # 为了防止fib列表下标溢出
        if k < 2:
            mid = low
        else:
            mid = low + fib[k - 1] - 1

        print('low=%s, mid=%s, high=%s' % (low, mid, high))

        if key < lis[mid]:
            high = mid - 1
            k -= 1
        elif key > lis[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                print('times: %s' % times)
                return mid
            else:
                print('times: %s' % times)
                return high

    print('times: %s' % times)
    return False


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = fibonacci_search(LIST, 222)
    print(result)
