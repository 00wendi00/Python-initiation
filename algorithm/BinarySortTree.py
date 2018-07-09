#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : BinarySortTree.py
# @Author: Wade Cheung
# @Date  : 2018/7/4
# @Desc  : 二叉查找树 -- 二叉排序数 . BST

# 二叉树或为空, 或满足如下性质
# 若左子树不为空, 则左子树上所有节点的值均小于它的根结构的值
# 若右子树不为空, 则右子树上所有节点的值均大于它的根结构的值
# 它的左右子树也都是二叉排序树

class BSTNode:
    """
    定义二叉树节点类
    """

    def __init__(self, data, left=None, right=None):
        """
        初始化
        :param data: 节点存储的数据
        :param left: 节点左子树
        :param right: 节点右子树
        """
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree:
    """
    基于BSTNode类的二叉排序树, 维护一个跟节点指针
    """

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        """
        关键码检索
        :param key: 关键码
        :return: 查询节点或None
        """
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry:
                bt = bt.left
            elif key > entry:
                bt = bt.right
            else:
                return entry
        return None

    def insert(self, key):
        """
        插入操作
        :param key: 关键码
        :return: 布尔值
        """
        bt = self._root
        if not bt:
            self._root = BSTNode(key)
            return

        while True:
            entry = bt.data
            if key < entry:
                if bt.left is None:
                    bt.left = BSTNode(key)
                    return
                bt = bt.left
            elif key > entry:
                if bt.right is None:
                    bt.right = BSTNode(key)
                    return
                bt = bt.right
            else:
                bt.data = key
                return

    def delete(self, key):
        p, q = None, self._root
        if not q:
            print('空树!')
            return

        # 找到要删除的节点, q为引用, 而p是q的父节点或者None(q为根节点时)
        while q and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if not q:
                return

        # 如果q没有左子树
        if not q.left:
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return

        # 查找节点q的左子树的最右节点，将q的右子树链接为该节点的右子树
        # 该方法可能会增大树的深度，效率并不算高。可以设计其它的方法。
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def __iter__(self):
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.data
            node = node.right


if __name__ == '__main__':
    lis = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
    bs_tree = BinarySortTree()
    for i in range(len(lis)):
        bs_tree.insert(lis[i])
    bs_tree.delete(58)
    for i in bs_tree:
        print(i, end=" ")

    print('\n')
    bs_tree.insert(93)
    for i in bs_tree:
        print(i, end=" ")
