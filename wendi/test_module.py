#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_module.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/12
# @Desc  :  模块

import os
import sys
# from sys import argv
# from sys import *
# import ~

print('-------------import module-------------')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')


print(dir(sys))



