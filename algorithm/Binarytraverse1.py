#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Binarytraverse1.py
# @Author: Wade Cheung
# @Date  : 2018/7/31
# @Desc  : 二叉树的遍历方式( 广度优先 )


from algorithm.BinarySortTree import BinarySortTree


def test1(node):
    l = []
    queue = [node]
    while queue:
        node = queue[0]
        l.append(node.data)
        del queue[0]

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return l


lis = [4, 2, 1, 5, 7, 9, 6, 3]
bs_tree = BinarySortTree()
for i in lis:
    bs_tree.insert(i)

for i in bs_tree:
    print(i, end=" ")

print('\n')

print(test1(bs_tree._root))
