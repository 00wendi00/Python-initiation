#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_exception.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/14
# @Desc  : 异常处理 , try , exception ~ , else
import sys

try:
    s = input('Enter something --> ')
except EOFError:
    print('\nWhy did you do an EOF on me?')
    sys.exit() # exit the program
except:
    print('\nSome error/exception occurred.')
    # here, we are not exiting the program
    print('Done')
else:
    print('好的')