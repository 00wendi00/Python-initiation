#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_io1.py
# @Author: Wade Cheung
# @Date  : 2018/6/17
# @Desc  : 输出到控制台 + 输出到文件作为日志保存 --> 输出同时重定向到控制台和文件


import sys


class __redirection__:

    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout

    def write(self, output_stream):
        self.buff += output_stream

    def to_console(self):
        sys.stdout = self.__console__
        print(self.buff)

    def to_file(self, file_path):
        f = open(file_path, 'w')
        sys.stdout = f
        print(self.buff)
        f.close()

    def flush(self):
        self.buff = ''

    def reset(self):
        sys.stdout = self.__console__


if __name__ == "__main__":
    # redirection
    r_obj = __redirection__()
    sys.stdout = r_obj

    # get output stream
    print('hello')
    print('there')

    # redirect to console
    r_obj.to_console()

    # redirect to file
    r_obj.to_file('D:\\data\\test_py\\out.log')

    # flush buffer
    r_obj.flush()

    # reset
    r_obj.reset()
