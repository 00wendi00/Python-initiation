#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Fibonacci.py
# @Author: Wade Cheung
# @Date  : 2018/7/3
# @Desc  : 斐波拉契列表


def fibonacci_create(max_position=0):
    """返回斐波拉契列表

    :param max_position: 最大位数
    :return: 斐波拉契列表
    """
    result = [1, 1]
    while len(result) < max_position:
        result.append(result[-2] + result[-1])

    print(result)
    return result


if __name__ == '__main__':
    fibonacci_create(max_position=50)
