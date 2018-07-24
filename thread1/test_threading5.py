#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_threading5.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 信号量 Semaphore  , 允许一定数量的线程同时访问数据

# 互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，
# 比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去

import time
import thread1


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread1: %s\n' % n)
    semaphore.release()


if __name__ == '__main__':
    num = 0
    semaphore = thread1.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = thread1.Thread(target=run, args=(i,))
        t.start()

while thread1.active_count() != 1:
    pass
else:
    print('------all threads done------')
    print(num)
