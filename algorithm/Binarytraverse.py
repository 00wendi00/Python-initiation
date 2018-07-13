#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Binarytraverse.py
# @Author: Wade Cheung
# @Date  : 2018/7/13
# @Desc  : 二叉树的三种遍历方式, 先序NLR, 中序LNR, 后序LRN.   递归实现  +  遍历实现

from algorithm.BinarySortTree import BinarySortTree


# 先序遍历NLR
def node_left_right(node):
    if node:
        return [node.data] + node_left_right(node.left) + node_left_right(node.right)
    else:
        return []


# 中序遍历LNR
def left_node_right(bst):
    l = []
    stack = []
    node = bst._root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        l.append(node.data)
        node = node.right

    return l


# 后序遍历LRN
def left_right_node(node):
    if node:
        return left_right_node(node.left) + left_right_node(node.right) + [node.data]
    else:
        return []


# 将列表insert进binary
# lis = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
lis = [4, 2, 1, 5, 3]
bs_tree = BinarySortTree()
for i in lis:
    bs_tree.insert(i)

for i in bs_tree:
    print(i, end=" ")

print('\n')

print(node_left_right(bs_tree._root), '先序\n')

print(left_node_right(bs_tree), '中序\n')

print(left_right_node(bs_tree._root), '后序\n')