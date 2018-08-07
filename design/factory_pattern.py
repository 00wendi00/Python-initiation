#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : factory_pattern.py
# @Author: Wade Cheung
# @Date  : 2018/8/7
# @Desc  : 工厂模式


# 工厂模式包涵一个超类。这个超类提供一个抽象化的接口来创建一个特定类型的对象，而不是决定哪个对象可以被创建。

# 当以下情形可以使用工厂模式：
# 1.不知道用户想要创建什么样的对象
# 2.当你想要创建一个可扩展的关联在创建类与支持创建对象的类之间。

# 抽象工程模式 -- 把工厂也抽象化了 .
# 抽象工程模式 : 提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类

class Person:
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Male(Person):
    def __init__(self, name):
        print('男name : %s' % name)


class Female(Person):
    def __init__(self, name):
        print('女name : %s' % name)


class PersonFactory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = PersonFactory()
    person = factory.getPerson('Cheung', 'M')
