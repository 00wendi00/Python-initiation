#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_object.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/12
# @Desc  : 对象和类 , self, __init__,  类的变量和对象的变量 -- 类属性与实例属性 . 类的私有方法 . 单下划线、双下划线、头尾双下划线说明


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

print('------------类的私有方法------------')


class CalcuCounter:
    __countSecrete = 0
    countPublic = 0

    def count(self):
        self.__countSecrete += 2
        self.countPublic += 1
        print(self.__countSecrete)

    def countPrivate(self):
        return self.__countSecrete


counter = CalcuCounter()
counter.count()
counter.count()
print('public ' + str(counter.countPublic))
print('private ' + str(counter._CalcuCounter__countSecrete))    #对象名._类名__私有属性名 , 访问类的私有变量
print('acquire ' + str(counter.countPrivate()))


# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。