#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : single_decorator.py
# @Author: Wade Cheung
# @Date  : 2018/8/5
# @Desc  : 单例模式--使用装饰器


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
