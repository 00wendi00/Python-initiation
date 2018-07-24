#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_process1.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : multiprocessing多进程中的共享数据, Value, Array

from multiprocessing import Array, Value, Process


def func(a, b):
    a.value = 3.333333333333333333
    for i in range(len(b)):
        b[i] = -b[i]


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(11))

    c = Process(target=func, args=(num, arr))
    d = Process(target=func, args=(num, arr))
    e = Process(target=func, args=(num, arr))
    c.start()
    d.start()
    e.start()
    c.join()
    d.join()
    e.join()

    for i in arr:
        print(i)

    print(num.value)
