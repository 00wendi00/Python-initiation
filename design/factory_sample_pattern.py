#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : factory_sample_pattern.py
# @Author: Wade Cheung
# @Date  : 2018/8/7
# @Desc  : 简单工厂模式


# 工厂模式包涵一个超类。这个超类提供一个抽象化的接口来创建一个特定类型的对象，而不是决定哪个对象可以被创建。

# 当以下情形可以使用工厂模式：
# 1.不知道用户想要创建什么样的对象
# 2.当你想要创建一个可扩展的关联在创建类与支持创建对象的类之间。


# 简单工厂模式 -- 抽象了产品, 在一个工厂类中创建了产品实例.
# 工程方法模式 -- 将工厂也抽象化, 使用时选择一个工厂实例化 --> 产出对应的产品 .
# 抽象工程模式 -- 工厂和产品是一对多的关系. 多个工厂即代表多个产品线.
# 抽象工程模式 : 提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类 -- 即多条产品线的抽象化 .


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
