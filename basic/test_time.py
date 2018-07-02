#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_time.py
# @Author: Wade Cheung
# @Date  : 2018/6/21
# @Desc  : 获得当前时间.  str_time, datetime, timestamp的相互转化.


import time
from datetime import datetime

# datetime to str , 获取当前时间str
dt = datetime.now()
str_time = dt.strftime('%Y-%m-%d %H:%M:%S')

# str to datetime
datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')

# str to timestamp
timeArray = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')  # 时间str转换为时间数组 , struct_time . 元组
mytimstamp = time.mktime(timeArray)
print(str(mytimstamp))

# timestamp to str
time_local = time.localtime(mytimstamp)
str_time = time.strftime('%Y-%m-%d %H:%M:%S', time_local)

# 获取当前时间str , 2
time_now = int(time.time())  # 时间戳
time_local = time.localtime(time_now)
str_time = time.strftime('%Y-%m-%d %H:%M:%S', time_local)
