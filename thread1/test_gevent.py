#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_gevent.py
# @Author: Wade Cheung
# @Date  : 2018/9/18
# @Desc  : gevent


import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
