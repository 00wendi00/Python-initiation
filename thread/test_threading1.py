#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_threading1.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 用threading.Condition实现消费者模型

# 利用condition变量用锁去通许访问一些共享状态，线程在获取到它想得到的状态前，会反复调用wait()。
# 修改状态的线程在他们状态改变时调用 notify() or notify_all()，用这种方式，线程会尽可能的获取到想要的一个等待者状态。
# 例子： 生产者-消费者模型

import threading
import time


def consumer(cond, name):
    with cond:
        print('%s consumer before wait' % name)
        cond.wait()
        print('%s consumer after wait' % name)


def producer(cond, name):
    with cond:
        print('%s producer before notifyAll' % name)
        cond.notifyAll()
        print('%s producer after notifyAll' % name)


condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition, 'c1',))
c2 = threading.Thread(name='c2', target=consumer, args=(condition, 'c2',))

p = threading.Thread(name='p', target=producer, args=(condition, 'p',))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()
