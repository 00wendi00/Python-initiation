#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : single_class.py
# @Author: Wade Cheung
# @Date  : 2018/8/5
# @Desc  : 单例模式--使用类 + @classmethod


# classmethod 是类对象与函数的结合。
# 可以使用类和类的实例调用，但是都是将类作为隐含参数传递过去。
# 使用类来调用 classmethod 可以避免将类实例化的开销。

import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance
