#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_coins.py
# @Author: Wade Cheung
# @Date  : 2018/7/13
# @Desc  : 找零钱问题


def giveChange(smallMoneyList, money):
    """
    找零钱问题
    :param smallMoneyList: 币额列表
    :param money: 找零总数
    :return:
    """
    if money > 0:
        for f in smallMoneyList:
            if round(money, 1) >= f:
                print(money, f)     # 找零的过程.  此处显示浮点数会略小, 故用round()保留一位小数.
                return giveChange(smallMoneyList, round(money, 1) % round(f, 1)) + round(money, 1) // round(f, 1)
        return 0
    else:
        return 0


print(giveChange([50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1], 66.9))
