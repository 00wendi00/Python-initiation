#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_process3.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 线程池. multiprocessing.Pool , apply, apply_async

from multiprocessing import Pool
import time


def f1(i):
    time.sleep(0.5)
    print(i)
    return i + 100


# apply_async
def f2(i):
    time.sleep(0.5)
    print(i)
    return i + 100  # return 作为回调函数的参数


def f3(arg):
    print('结果: %s' % arg)


if __name__ == "__main__":
    # pool = Pool(5)
    # for i in range(1, 31):
    #     pool.apply(func=f1, args=(i,))    # 结果返回前会一直阻塞

    pool = Pool(5)
    for k in range(1, 31):
        pool.apply_async(func=f2, args=(k,), callback=f3)   # 异步调用 , 适合并发执行.  Callbacks应被立即完成，否则处理结果的线程会被阻塞
    pool.close()
    pool.join()  # 因为被终止的进程需要被父进程调用wait（join等价与wait），否则进程会成为僵尸进程
