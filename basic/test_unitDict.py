#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_unitDict.py
# @Author: Wade Cheung
# @Date  : 2018/6/30
# @Desc  : 被测试类


class Dict(dict):
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
