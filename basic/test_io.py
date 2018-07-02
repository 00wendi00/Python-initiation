#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_io.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/14
# @Desc  : 输入~输出~ ,  file的基本操作.  pickle模块 -- 储存,取储存 -- 将类以二进制的格式存入文件, 读取 .
import pickle as p

poem = '''
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

f = open('D:\\data\\test_back\\test.txt', 'wb+')
f.write(str.encode(poem))  # 决定是否有b , open中的b代表二进制
# f.write(poem.encode())    # 决定是否有b , open中的b代表二进制
f.close()

shoplistfile = 'D:\\data\\test_back\\test2'
shoplist = ['apple', 'mango', 'carrot']
f2 = open(shoplistfile, 'rb+')
p.dump(shoplist, f2)
f2.close()

del shoplist
f2 = open(shoplistfile, 'rb+')
storelist = p.load(f2)
print(storelist)
