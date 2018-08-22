#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_decorator1.py
# @Author: Wade Cheung
# @Date  : 2018/8/22
# @Desc  : 装饰器. 注意多个装饰的编译顺序和次数, 执行顺序, 带参装饰器

# 装饰器 : 是用于拓展原来函数功能的一种函数, 返回一个函数 ; 在不用更改原函数的代码的前提下, 给函数增加新的功能
# 使用装饰器的方式即面向切面编程 : 是主要作用 权限控制,插入日志,性能测试, 事务处理, 缓存等

import functools


def dec1(func):
    print("1111")

    # functools.wraps(func) 则可以将原函数对象的指定属性复制给包装函数对象, __module__, __name__, __doc__
    # 具体参考 . https://blog.csdn.net/su92chen/article/details/69568715
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("2222")
        f = func(*args, **kwargs)
        print("3333")
        return f

    return wrapper


def dec2(func):
    print("aaaa")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("bbbb")
        f = func(*args, **kwargs)
        print("cccc")
        return f

    return wrapper


def dec3(text):
    print('kkkk')

    def ptext(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('mmmm')
            print(text)
            print('nnnn')
            return func(*args, **kwargs)

        return wrapper

    return ptext


@dec1
@dec2
@dec3('decorate测试')
def test1():
    print("test1 test1")


@dec1
@dec2
@dec3('decorate测试')
def test2():
    print("test2 test2")


test1()
print('\t')
# test1()
# print('\t')
# test2()
# print('\t')
# print('输出test1的name : ', test1.__name__)
# print('输出test1的dict : ', test1.__dict__)
