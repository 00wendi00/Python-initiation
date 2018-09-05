#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_quick.py
# @Author: Wade Cheung
# @Date  : 2018/7/8
# @Desc  : 快速排序, 分治算法.  平均时间复杂度为O(nlogn)，最糟糕时复杂度为O（n^2）,注意优化


# 1. 选取一个数作为基数, 最左端的值为基数.
# 2. 从后向前搜索,比基数小则调换, 再从前向后搜索,比基数大则调换, 直到两边的index相等
# 3. 重复1,2 直到left不再小于right

# 递归的深度最大为[log2n]+1 , 比较n次, 需要时间为T（n） . 获得的枢轴将数组一分为二，那么各自还需要T（n/2）的时间 = T（n）
# 故时间复杂度为O(nlogn)

# 优化, https://blog.csdn.net/andersen_/article/details/50923493
# 1.基准数 2.基准元素相等的元素放在中间

def quick_sort(lis, left, right):
    if left < right:
        print(lis)

        # 优化, 基准数可以取当前列表的前中后元素的平均值, 防止列表本身有序
        # 或随机取一个
        base = lis[left]  # 基准数
        m, n = left, right

        while m < n:
            while lis[n] >= base and m < n:
                n -= 1
            temp = lis[m]
            lis[m] = lis[n]
            lis[n] = temp

            while lis[m] <= base and m < n:
                m += 1
            temp = lis[n]
            lis[n] = lis[m]
            lis[m] = temp

        # lis[m] = base

        quick_sort(lis, left, m - 1)
        quick_sort(lis, n + 1, right)

    return lis


l = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
print('结果:', quick_sort(l, 0, len(l) - 1))
