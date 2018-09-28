#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_gevent1.py
# @Author: Wade Cheung
# @Date  : 2018/9/18
# @Desc  : gevent

# 参考https://blog.csdn.net/sinat_35360663/article/details/78361152

from gevent import monkey
import gevent
import urllib.request

# 有IO时
monkey.patch_all()


def myDownload(url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)  # 执行IO时, gevent自动切换
    data = resp.read()
    print('%d bytes received from %s. ' % (len(data), url))


# gevent.joinall([gevent.spawn(myDownload, 'https://www.baidu.com'),
#                 gevent.spawn(myDownload, 'https://cn.bing.com/'),
#                 gevent.spawn(myDownload, 'https://www.csdn.net/')
#                 ])

glist = []
for i in range(1000):
    g1 = gevent.spawn(myDownload, 'https://www.baidu.com')
    g2 = gevent.spawn(myDownload, 'https://cn.bing.com/')
    g3 = gevent.spawn(myDownload, 'https://www.csdn.net/')
    glist.append(g1)
    glist.append(g2)
    glist.append(g3)

for i in range(len(glist) - 1):
    print(i * 3)
    glist[i].join()
