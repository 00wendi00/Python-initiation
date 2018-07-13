#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : PrimeNumber.py
# @Author: Wade Cheung
# @Date  : 2018/7/13
# @Desc  : 查找质数


def finPrime(n):
    num = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num.append(i)
    return num


print(finPrime(200))
