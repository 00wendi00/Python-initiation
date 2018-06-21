#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_solveprob.py_base
# @Author: Wade Cheung
# @Date  : 2018/6/12
# @Desc  : 解决实际问题. 遍历文件和文件夹, 并使用zipfile压缩

import os
import time
import zipfile

# print('--------------------备份文件-->zip  +  遍历文件和文件夹---------------------')
# print('--------------------例子---------------------')
# dirstr = 'D:/data/test_back/bb' + time.strftime('%Y%m%d%H%M%S') + '.zip'
# # 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
# azip = zipfile.ZipFile(dirstr, 'w')
# # 必须保证路径存在,将bb件夹（及其下aa.txt）添加到压缩包,压缩算法LZMA
# azip.write('D:/data/statistics', compress_type=zipfile.ZIP_LZMA)
# # 写入一个新文件到压缩包中，data是该文件的具体内容，可以是str或者是byte。
# # 这里是新建一个bb文件夹，其下再新建一个cc.txt,将hello world写入到文本中
# # azip.writestr('D:/data/statistics', data='Hello World', compress_type=zipfile.ZIP_DEFLATED)
# # 关闭资源
# azip.close()

print('--------------------实践----------------------')

dirmystr = 'D:\\data\\statistics'
dirlist = os.listdir(dirmystr)

alllist = []


# 递归--循环调用, 终止条件.   向里没有文件夹的时候, 递归停止.
def doit(parapath):
    dirlist_temp = os.listdir(parapath)
    for k in range(0, len(dirlist_temp)):
        file_str = os.path.join(parapath, dirlist_temp[k])
        alllist.append(file_str)
        if (os.path.isfile(file_str) == False):
            doit(file_str)


doit(dirmystr)
print(alllist)

dirstr = 'D:/data/test_back/' + time.strftime('%Y%m%d%H%M%S') + '.zip'
myzip = zipfile.ZipFile(dirstr, 'a')
for str in alllist:
    # if (os.path.isfile(str)):
    myzip.write(str, compress_type=zipfile.ZIP_DEFLATED)
# else:
#     myzip.write(str, compress_type=zipfile.ZIP_LZMA)
myzip.close()

# dirstr = 'D:/data/test_back/bb' + time.strftime('%Y%m%d%H%M%S') + '.zip'
# # 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
# azip = zipfile.ZipFile(dirstr, 'w')
# # 必须保证路径存在,将bb件夹（及其下aa.txt）添加到压缩包,压缩算法LZMA
# azip.write('D:/data/statistics', compress_type=zipfile.ZIP_LZMA)
# # 写入一个新文件到压缩包中，data是该文件的具体内容，可以是str或者是byte。
# # 这里是新建一个bb文件夹，其下再新建一个cc.txt,将hello world写入到文本中
# # azip.writestr('D:/data/statistics', data='Hello World', compress_type=zipfile.ZIP_DEFLATED)
# # 关闭资源
# azip.close()
