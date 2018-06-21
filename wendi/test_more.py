#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_more.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/14
# @Desc  :  更多内容 : 1.特殊方法, 2.单语句块, 3.列表综合,
# 4.可变参数列表-- *args接收元组列表, **args接收字典 . 实参和形参的写法.
# 5.lambda表达式
# 6.exec执行语句 ,  eval执行计算
# 7.repr函数和反引号
import os

listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)


# 定义的时候 * 的作用 将位置实参 装配成元组，** 的作用 将关键字实参 装配成字典
def test3(x, y, z):
    print(x, y, z)


x1 = [1, 2, 3]
x2 = ('q', 'w', 'e')
y = {'x': 1, 'y': 2, 'z': 3}
# 实参的写法.
test3(*x1)
test3(*x2)
test3(**y)


def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


powersum(2, 4, 5)


def make_repeater(n):
    return lambda s: s * n


twice = make_repeater(2)

print('test_start.py'.join(twice('word')))
print(twice(5))

exec('print("Hello World")')
eval('2*3')

mylist = ['it', 'item']
assert len(mylist) >= 1
mylist.pop()
print(mylist)

k = []
k.append('item')
repr(k)  # repr函数和反引号用来获取对象的可打印的表示形式。可以通过定义类的__repr__方法来控制你的对象在被repr函数调用的时候返回的内容
print(k)
print(os.sep)
