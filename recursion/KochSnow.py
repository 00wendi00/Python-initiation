#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : KochSnow.py
# @Author: Wade Cheung
# @Date  : 2018/9/17
# @Desc  : 科赫雪花


import turtle


def kohn(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            kohn(size / 3, n - 1)


turtle.speed(0)
turtle.setup(600, 600)
turtle.penup()
turtle.pensize(2)
turtle.goto(-200, 100)
turtle.pendown()
level = 3
kohn(400, level)
turtle.right(120)
kohn(400, level)
turtle.right(120)
kohn(400, level)
turtle.hideturtle()
