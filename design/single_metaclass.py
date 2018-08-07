#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : single_metaclass.py
# @Author: Wade Cheung
# @Date  : 2018/8/5
# @Desc  : 单例模式--使用元类实现

import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with SingletonType._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)

        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name
