#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_datastruct.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/12
# @Desc  : 数据结构. 列表, 元组, 字典


shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')
shoplist.append('rice')
shoplist.sort()
del shoplist[1]
print(shoplist)

zoo = ('wolf', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
print(zoo)

new_zoo = ('monkey', 'dolphin', zoo)
print(new_zoo)
print(new_zoo[2][1])

age = 22
name = 'Swaroop'
print('%s is %d years old' % (name, age))  # %s表示字符串, %d表示整数
print('Why is %s playing with that python?' % name)

ab = {'Swaroop': 'swaroopch@byteofpython.info',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

print('\n\n\n' + ab['Larry'])

del ab['Spammer']
ab.pop('Larry')
ab.update({'Matsumoto': '123321123'})
for name, address in ab.items():
    print(name, address)

shoplist = ['apple', 'mango', 'carrot', 'banana']
print('Item 0 to 3 is', shoplist[0:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -2 is', shoplist[0:-2])
print('Item start to end is', shoplist[:])

# !/usr/bin/python
# Filename: reference.py_base
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist  # mylist is just another name pointing to the same object!
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object
print('Copy by making a full slice')
mylist = shoplist[:]  # make a copy by doing a full slice
del mylist[0]  # remove first item
print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that now the two lists are different


print('-------------------字符串操作----------------------')
# startswith, in, find(''), join
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
