#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_loop.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/11
# @Desc  : 控制流 --  控制语句


print('---------------continue----------------')
while (True):
    s = int(input('Enter something......'))
    if s > 3:
        print(s)
    elif s == 3:
        break
    else:
        continue
    print('string is ', s)
print('Done ! continue')

print('---------------break----------------')
while (True):
    s = input('Enter something......')
    if s == 'quite':
        break
    print('Length of the string is ', len(s))
print('Done ! break')

print('---------------for----------------')
for i in range(1, 5, 2):  # 起+始+步长
    print(i)
else:
    print('Down!')

print('-------------While,if-------------')
number = 32
result = True
while result:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('You guess right!')
        result = False
    elif guess < number:
        print('You are wrong, too small')
    else:
        print('You are wrong, too big')

else:
    print('The While loop is Over ')
print('Down')
