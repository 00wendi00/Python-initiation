#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_readwrite.py
# @Author: Wade Cheung
# @Date  : 2018/8/4
# @Desc  : 读写锁的实现 , 读者优先


import threading


class RWLock(object):
    def __init__(self):
        self.rlock = threading.Lock()
        self.wlock = threading.Lock()
        self.reader = 0

    def write_acquire(self):
        self.wlock.acquire()

    def write_release(self):
        self.wlock.release()

    # 在第一个读者到来的时候就要阻止写者
    def read_acquire(self):
        self.rlock.acquire()
        self.reader += 1
        if self.reader == 1:
            self.wlock.acquire()
        self.rlock.release()

    # 最后一个读者离开之后再开放写者
    def read_release(self):
        self.rlock.acquire()
        self.reader -= 1
        if self.reader == 0:
            self.wlock.release()
        self.rlock.release()
