#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_memory.py
# @Author: Wade Cheung
# @Date  : 2018/6/22
# @Desc  : 复制, 浅拷贝, 深拷贝.  不可变对象

import copy

# 赋值
print('\n赋值')
list1 = ['abc', 'def', 'ghi']
list2 = list1
print(id(list1), id(list2))

# 浅拷贝
print('\n浅拷贝')
list3 = list(list1)
print(id(list1), id(list3))
for x, y in zip(list1, list3):
    print(id(x), id(y))

# 深拷贝
print('\n深拷贝')
list4 = copy.deepcopy(list1)  # 或使用 list1[:]
print(id(list1), id(list4))
for x, y in zip(list1, list4):
    print(id(x), id(y))
# 此处a和b中元素的id还是一样 :
# 这是因为对于不可变对象，当需要一个新的对象时，python可能会返回已经存在的某个类型和值都一致的对象的引用。
# 而且这种机制并不会影响 a 和 b 的相互独立性，因为当两个元素指向同一个不可变对象时，对其中一个赋值不会影响另外一个。

print('\n深拷贝-- list1和list4 互不影响')
list4[1] = 'wade'
print(id(list4[1]), id(list1[1]))

# 赋值 : 用一个变量给另一个变量赋值 . 实际上是copy的引用. 最后都指向同一处内存.

# 所谓“浅拷贝”，是指创建一个新的对象，其内容是原对象中元素的引用。（拷贝组合对象，不拷贝子对象）
# 常见的浅拷贝有：切片操作、工厂函数、对象的copy()方法、copy模块中的copy函数。

# 所谓“深拷贝”，是指创建一个新的对象，然后递归的拷贝原对象所包含的子对象。深拷贝出来的对象与原对象没有任何关联

# 浅拷贝和深拷贝的不同仅仅是对组合对象来说，所谓的组合对象就是包含了其它对象的对象，
# 如列表，类实例。而对于数字、字符串以及其它“原子”类型，# 没有拷贝一说，产生的都是原对象的引用
