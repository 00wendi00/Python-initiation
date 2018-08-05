#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : single_new.py
# @Author: Wade Cheung
# @Date  : 2018/8/5
# @Desc  : 单例模式--使用new


import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = object.__new__(cls)

        return Singleton._instance
