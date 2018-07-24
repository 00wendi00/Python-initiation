#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_threading3.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 使用queuelib包中的queue.Queue实现 线程池


import thread1
import time
from queue import Queue


class Threadingpool():
    def __init__(self, max_num=10):
        self.queue = Queue(max_num)
        for i in range(max_num):
            self.queue.put(thread1.Thread)

    def getthreading(self):
        return self.queue.get()

    def addthreading(self):
        self.queue.put(thread1.Thread)
        print('放入线程池')


def func(p, i):
    time.sleep(i)
    print(i)
    p.addthreading()


if __name__ == '__main__':
    p = Threadingpool()
    for i in range(0, 15, 2):
        thread = p.getthreading()
        t = thread1.Thread(target=func, args=(p, i))
        t.start()
