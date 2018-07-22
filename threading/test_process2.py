#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_process2.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 模块multiprocessing.Manager的dict, list . 提供了多种数据类型的共享支持

# manager提供list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue,
# Value and Array类型的支持
# Server process manager比 shared memory 更灵活，因为它可以支持任意的对象类型。
# 另外，一个单独的manager可以通过进程在网络上不同的计算机之间共享，不过比shared memory要慢

from multiprocessing import Process, Manager


def f(d, l):
    d["name"] = "wade cheung"
    d["age"] = 24
    d["Job"] = "pythoner"
    l.reverse()


if __name__ == "__main__":
    with Manager() as man:
        dd = man.dict()
        ll = man.list(range(10))

        p1 = Process(target=f, args=(dd, ll))
        p2 = Process(target=f, args=(dd, ll))
        p3 = Process(target=f, args=(dd, ll))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()

        print(dd)
        print(ll)
