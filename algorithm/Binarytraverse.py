#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Binarytraverse.py
# @Author: Wade Cheung
# @Date  : 2018/7/13
# @Desc  : 二叉树的三种遍历方式( 深度优先 ), 先序NLR--preorder, 中序LNR--inorder, 后序LRN--postorder.   递归实现  +  遍历实现

from algorithm.BinarySortTree import BinarySortTree


# 先序遍历NLR
def node_left_right1(node):
    if node:
        return [node.data] + node_left_right1(node.left) + node_left_right1(node.right)
    else:
        return []


# 先序遍历NLR
def node_left_right2(node):
    l = []
    stack = []
    while stack or node:
        while node:
            l.append(node.data)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right

    return l


# 中序遍历LNR
def left_node_right1(node):
    if node:
        return left_node_right1(node.left) + [node.data] + left_node_right1(node.right)
    else:
        return []


# 中序遍历LNR
def left_node_right2(node):
    l = []
    stack = []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        l.append(node.data)
        node = node.right

    return l


# 后序遍历LRN
def left_right_node1(node):
    if node:
        return left_right_node1(node.left) + left_right_node1(node.right) + [node.data]
    else:
        return []


# 后序遍历LRN , 最后reverse
def left_right_node2(node):
    l = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        l.append(node.data)
    l.reverse()   # append 的实际顺序为中右左 . 翻转为左右中.
    return l


# 将列表insert进binary
# lis = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
lis = [4, 2, 1, 5, 3]
bs_tree = BinarySortTree()
for i in lis:
    bs_tree.insert(i)

for i in bs_tree:
    print(i, end=" ")

print('\n')

print(node_left_right1(bs_tree._root), '先序1\n')
print(node_left_right2(bs_tree._root), '先序2\n')

print(left_node_right1(bs_tree._root), '中序1\n')
print(left_node_right2(bs_tree._root), '中序2\n')

print(left_right_node1(bs_tree._root), '后序1\n')
print(left_right_node2(bs_tree._root), '后序2\n')
