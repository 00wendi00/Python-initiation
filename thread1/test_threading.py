#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_threading.py
# @Author: Wade Cheung
# @Date  : 2018/7/3
# @Desc  : 模块Threading用于提供线程相关的操作

# 基本方法 : start, getName, setName, name, is_alive, isAlive, setDaemon, ident, join, run

import thread1
import time


def worker(num):
    print('start...')
    time.sleep(num)
    print('sleep time : %ss' % num)


globals_num = 0
lock = thread1.RLock()


# RLock允许在同一线程中被多次acquire。而Lock却不允许, 若出现则产生死锁
# 如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐
def fun_locl():
    lock.acquire()
    global globals_num
    globals_num += 1
    time.sleep(1)
    print(globals_num)
    lock.release()


def fun_lock_exe():
    t = thread1.Thread(target=fun_locl)
    t.start()


def event_do(event):
    print('start...')
    event.wait()
    print('execute')


# 事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，
# 如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
def event_do_exe():
    event_obj = thread1.Event()  # Flag默认为False ,阻塞
    for i in range(10):
        t = thread1.Thread(target=event_do, args=(event_obj,))
        t.start()
    event_obj.clear()  # 将“Flag”设置为False
    inp = input('input:')
    if inp == 'true':
        event_obj.set()  # 将“Flag”设置为True


if __name__ == '__main__':
    # worker(2)
    # fun_lock_exe()
    event_do_exe()
