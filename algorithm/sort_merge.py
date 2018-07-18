#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_merge.py
# @Author: Wade Cheung
# @Date  : 2018/7/19
# @Desc  : 归并排序, divide and conquer strategy, 时间复杂度为O(nlogn). split + merge

# divide a list in half logn times, each of which costs n operations


def merge_sort(lis):
    print('Splitting ', lis)
    if len(lis) > 1:
        mid = len(lis) // 2
        lefthalf = lis[:mid]
        righthalf = lis[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        # i+1作为lefthalf的item写进lis的标注, j+1作为righthalf的item写进lis的标识, k作为lis的位置标识
        i, j, k = 0, 0, 0
        # 交替比较, 存入lis
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lis[k] = lefthalf[i]
                i += 1
            else:
                lis[k] = righthalf[j]
                j += 1
            k += 1

        # 剩余lefthalf存入lis
        while i < len(lefthalf):
            lis[k] = lefthalf[i]
            i += 1
            k += 1

        # 剩余righthalf存入lis
        while j < len(righthalf):
            lis[k] = righthalf[j]
            j += 1
            k += 1

    print('Merging ', lis)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
