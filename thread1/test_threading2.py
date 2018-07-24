#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_threading2.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 用queuelib包中的queue.Queue实现消费者模型

from queue import Queue
import thread1

message = Queue(10)


def producer(i):
    while True:
        message.put(i)
        print('生产 : %s, 总数: %s' % (i, message.qsize()))


def consumer(i):
    while True:
        msg = message.get()
        print('消费 : %s, 总数: %s' % (msg, message.qsize()))


for k in range(2):
    t = thread1.Thread(target=producer, args=(k,))
    t.start()

for k in range(10):
    t = thread1.Thread(target=consumer, args=(k,))
    t.start()
