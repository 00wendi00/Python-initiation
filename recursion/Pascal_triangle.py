#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Pascal_triangle.py
# @Author: Wade Cheung
# @Date  : 2018/7/13
# @Desc  : 帕斯卡三角, 杨辉三角


def Pascal_triangle(high):
    if high is 1:
        return [1]
    elif high is 2:
        return [1, 1]
    elif high > 2:
        lis = [1]
        for i in range(1, high + 1):
            if i not in [1, 2]:
                lis += [Pascal_triangle(high - 1)[i - 3] + Pascal_triangle(high - 1)[i - 2]]
        return lis + [1]


triangle_high = 8
for i in range(1, triangle_high + 1):
    print(Pascal_triangle(i))
