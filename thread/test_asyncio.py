#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_asyncio.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 协程asyncio, 只使用一个线程，在一个线程中规定某个代码块执行顺序.   还有gevent, greenlet等第三方包

# 对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态）
# 适用场景: 当程序中存在大量不需要CPU的操作时（IO），适用于协程

import asyncio


async def cor1():
    print('COR1 start')
    await cor2()
    print("COR1 end")


async def cor2():
    print("COR2")


loop = asyncio.get_event_loop()  # 启动默认的event loop . 协程执行的控制点
loop.run_until_complete()  # 阻塞执行 -- 直到所有的异步函数执行完成
loop.close()
