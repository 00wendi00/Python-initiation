#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Wade Cheung
# @Date  : 2018/8/5
# @Desc  :


## 使用模块
# from singleton.single_module import mySingleton
#
# print(mySingleton)

## 使用类
# from singleton.single_class import Singleton
#
# Singleton.instance()

# 使用new
# from singleton.single_new import Singleton
#
# s = Singleton()

from singleton.single_metaclass import Foo
obj1 = Foo('name')
obj2 = Foo('name')
print(obj1, obj2)

