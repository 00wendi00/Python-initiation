#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_decorator2.py
# @Author: Wade Cheung
# @Date  : 2018/8/22
# @Desc  : 装饰器 : 类装饰器在类中方法的使用--线程锁

import threading


class ThreadLock(object):
    """
    线程锁装饰器
    """

    def __init__(self):
        self.thread_lock = threading.Lock()

    def __call__(self, func):
        def _call(*args, **kw):
            self.thread_lock.acquire()
            func(*args, **kw)
            self.thread_lock.release()

        return _call


@ThreadLock()
def func():
    print(123)


func()
