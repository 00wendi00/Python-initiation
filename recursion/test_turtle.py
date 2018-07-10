#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_turtle.py
# @Author: Wade Cheung
# @Date  : 2018/7/11
# @Desc  : 内嵌的Turtle图形程序模块 . Spiral and Tree

import turtle


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 10)


def exe1():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    drawSpiral(myTurtle, 100)
    myWin.exitonclick()


def drawTree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        drawTree(branchLen - 15, t)
        t.left(40)
        drawTree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)


def exe2():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    drawTree(75, t)
    myWin.exitonclick()


exe1()  # draw Spiral
exe2()  # draw Tree
