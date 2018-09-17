#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_yieldfrom.py
# @Author: Wade Cheung
# @Date  : 2018/9/17
# @Desc  : yield from


# https://www.cnblogs.com/gqtcgq/p/8126124.html
def test():
    i = 1
    while i < 4:
        n = yield i
        print(n)
        if i == 3:
            return 100
        i += 1


def itertest():
    val = yield from test()
    print(val)


t = itertest()
t.send(None)
j = 0
while j < 3:
    j += 1
    try:
        t.send(j)
    except StopIteration as e:
        print('异常了')
