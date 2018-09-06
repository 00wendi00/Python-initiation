#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_extend.py
# @Author: Wade Cheung
# @Date  : 2018/9/6
# @Desc  : 多继承, 基类的方法名相同时的执行情况 -- MRO列表


# 属性与方法的遍历 : MRO列表-- 所有基类的线性顺序列表 ,
# C3线性化算法来实现 : 子类先于父类被检查, 多个父类根据顺序,

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
