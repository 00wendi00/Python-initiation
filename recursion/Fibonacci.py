#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Fibonacci.py
# @Author: Wade Cheung
# @Date  : 2018/7/13
# @Desc  : 斐波拉契列表 -- 递归实现


def fibonacci_create(max_position=0):
    """返回斐波拉契列表 -- 递归实现

    :param max_position: 最大位数
    :return: 斐波拉契列表
    """
    if max_position in [1, 2]:
        return [1, 1]
    elif max_position > 2:
        return fibonacci_create(max_position - 1) + [
            fibonacci_create(max_position - 1)[-2] + fibonacci_create(max_position - 1)[-1]]

    return [1, 1]


print(fibonacci_create(10))
