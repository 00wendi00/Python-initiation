#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Hanoi_tower.py
# @Author: Wade Cheung
# @Date  : 2018/7/13
# @Desc  : 盘杆难题 Tower of Hanoi

# They could only move one disk at a time, and they could never place a larger disk on top of a smaller one

# height -1 的准则 :
# 1. Move a tower of height-1 to an intermediate pole, using the final pole.
# 2. Move the remaining disk to the final pole.
# 3. Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


moveTower(4, "A", "B", "C")
