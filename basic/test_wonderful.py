#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_wonderful.py
# @Author: Wade Cheung
# @Date  : 2018/9/6
# @Desc  : 查看结果.  generator--yield, try-except-else-finally


def generator():
    print('aaa')
    yield 'bbb'
    print('ccc')


def func(g):
    try:
        print('start')
        i = next(g)
        print(i)
    except Exception:
        print('error')
    else:
        print('ok')
    finally:
        print('end')


g = generator()
func(g)
func(g)

# 结果 :
# start
# aaa
# bbb
# ok
# end
# start
# ccc
# error
# end
