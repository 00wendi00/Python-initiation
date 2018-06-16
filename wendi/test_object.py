#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_object.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/12
# @Desc  : 对象和类 , self, __init__,  类的变量和对象的变量 -- 类属性与实例属性


class Person:
    pass  # An empty block


p = Person()
print(p)


class Person1:
    def sayHi(self):
        print('Hello, how are you?')


p1 = Person1()
p1.sayHi()


class Person2:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Hello, my name is', self.name)


p2 = Person2('Swaroop')
p2.sayHi()
