#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_extend.py
# @Author: Wade Cheung
# @Date  : 2018/9/6
# @Desc  : 多继承, 基类的方法名相同时的执行情况


class A:
    def haha(self):
        print('hahaA')


class B1:
    def haha(self):
        print('hahaB1')


class B2(B1):
    def haha(self):
        print('hahaB2')


class C(B2, A):
    def haha(self):
        super().haha()


c = C()
c.haha()
