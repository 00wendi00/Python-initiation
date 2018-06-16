#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_func.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/12
# @Desc  : function


print('---------------全局变量----------------')


def func(x):
    print('X is ', x)
    x = 2  # global ~
    print('Changed local X to ', x)


x = 50
func(x)
print('X is still ', x)

print('---------------默认参数----------------')


def say(message, times=1):
    print(message * times)


say('Hello')
say('World ', 5)

print('---------------关键参数(命名)----------------')


def funcK(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


funcK(a=20, b=30)

print('---------------return----------------')


def maximum(x, y):
    if x > y:
        return x
    else:
        return y


print(maximum(2, 3))

print('---------------DocStrings----------------')


# 文档字符串 , 首行是大写字母开始,句号结束. 第二行是空行, 第三行开始是详细描述 ~
def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x)  # convert to integers, if possible
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


printMax(3, 5)
print(printMax.__doc__)












