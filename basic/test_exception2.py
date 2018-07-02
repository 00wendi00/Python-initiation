#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_exception2.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/14
# @Desc  : 异常处理2 .   raise , try exception, try finally


class ShortInputException(Exception):
    '''A user-defined exception class.'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    s = input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
    # Other work can continue as usual here
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException as x:
    print('ShortInputException: The input was of length %d, was expecting at least %d' % (x.length, x.atleast))
else:
    print('No exception was raised.')
