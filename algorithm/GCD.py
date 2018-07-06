#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : GCD.py
# @Author: Wade Cheung
# @Date  : 2018/7/6
# @Desc  : 最小公约数


def gcd(m, n):
    """
    大等于小, 小等于余, 循环
    :param m:
    :param n:
    :return:
    """
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


print(gcd(20, 7))
print(gcd(20, 6))
