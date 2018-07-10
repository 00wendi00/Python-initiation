#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_recursion1.py
# @Author: Wade Cheung
# @Date  : 2018/7/10
# @Desc  : 递归相加,切片操作,pop() ; 二进制数转化为 n进制数 ; 栈实现递归 ; 字符串反转,字符串截取 ; 判断字符串是否是回文


# 递归相加
from pythonds3.basic.stack import Stack


def addlist1(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + addlist1(numlist[1:])


# 递归相加
def addlist2(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist.pop() + addlist2(numlist)


# 二进制数转化为 n进制数
def toStr1(n, base):
    print(n)
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr1(n // base, base) + convertString[n % base]


# 栈实现递归
rStack = Stack()


def toStr2(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.is_empty():
        res = res + str(rStack.pop())
    return res


# 字符串反转,字符串截取
def reverseStr(str1, str0):
    if len(str1) < len(str0):
        str1 += str0[-1 - len(str1)]
        return reverseStr(str1, str0)
    else:
        return str1


# 判断字符串是否是回文
def palindrome(str0, n):
    if n <= len(str0) / 2:
        if str0[n] == str0[-n - 1]:
            return palindrome(str0, n + 1)
        else:
            return False
    else:
        return True


# print(addlist1(([1, 3, 5, 7, 9])))
# print(addlist2(([1, 3, 5, 7, 9])))
# print(toStr1(1024, 2))
print(toStr2(1453, 16))
# print(reverseStr('', 'abcdefg'))
# print(palindrome('abcba', 0))
