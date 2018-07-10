#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : BinaryBalancedTree.py
# @Author: Wade Cheung
# @Date  : 2018/7/10
# @Desc  : 平衡二叉树 . BalancedBinaryTree -- AVL


# 参考https://www.cnblogs.com/linxiyue/p/3659448.html?utm_source=tuicool&utm_medium=referral

# 平衡二叉树是第一个引入平衡概念的二叉树。1962年，G.M. Adelson-Velsky 和 E.M. Landis发明了这棵树，所以它又叫AVL树。
# 平衡二叉树要求对于每一个节点来说，它的左右子树的高度之差不能超过1，如果插入或者删除一个节点使得高度之差大于1，
# 就要进行节点之间的旋转，将二叉树重新维持在一个平衡状态。这个方案很好的解决了二叉查找树退化成链表的问题，
# 把插入，查找，删除的时间复杂度最好情况和最坏情况都维持在O(logN)。但是频繁旋转会使插入和删除牺牲掉O(logN)左右的时间，
# 不过相对二叉查找树来说，时间上稳定了很多

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def find(self, key):
        if self.root is None:
            return None
        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if node is None:
            return None
        elif key < node.key:
            return self._find(key, self.left)
        elif key > node.key:
            return self._find(key, self.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(self.root)
        else:
            return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    # 插入操作时, 不平衡有四种情况：
    # 1.对K的左儿子的左子树进行一次插入
    # 2.对K的左儿子的右子树进行一次插入
    # 3.对K的右儿子的左子树进行一次插入
    # 4.对K的右儿子的右子树进行一次插入

    # 1.对K的左儿子的左子树进行一次插入 .  节点向右移
    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height + 1)
        return k1

    # 4.对K的右儿子的右子树进行一次插入 . 节点向左移
    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    # 3.对K的右儿子的左子树进行一次插入
    # 相当于进行了两次单旋转 .  节点先向右移动,再向左移
    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate()

    # 2.对K的左儿子的右子树进行一次插入
    # 相当于进行了两次单旋转 .  节点先向左移动,再向右移
    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    # 插入操作
    def put(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self._put(key, self.root)

    # 插入操作
    def _put(self, key, node):
        if node is None:
            node = Node(key)
        elif key < node.key:
            node.left = self._put(key, node.left)  # 递归
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.key:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)

        elif key > node.key:
            node.right = self._put(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key < node.right.key:
                    node = self.doubleRightRotate(node)
                else:
                    node = self.singleRightRotate(node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    # 删除操作
    def delete(self, key):
        self.root = self.remove(key, self.root)

    # 删除操作
    def remove(self, key, node):
        if node is None:
            raise KeyError('Error, key not in tree')

        # 4.当前节点不是要删除的节点，则对其左子树或者右子树进行递归操作。当前节点的平衡条件可能会被破坏，需要进行平衡操作。
        elif key < node.key:
            node.left = self.remove(key, node.left)  # 递归
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        # 4.当前节点不是要删除的节点，则对其左子树或者右子树进行递归操作。当前节点的平衡条件可能会被破坏，需要进行平衡操作。
        elif key > node.key:
            node.right = self.remove(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        # 3.当前节点为要删除的节点且有左子树右子树:如果右子树高度较高，则从右子树选取最小节点，将其值赋予当前节点，
        # 然后删除右子树的最小节点。如果左子树高度较高，则从左子树选取最大节点，将其值赋予当前节点，然后删除左子树的最大节点。
        # 这样操作当前节点的平衡不会被破坏。
        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.right = self.remove(node.key, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.key = maxNode.key
                node.left = self.remove(node.key, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1

        # 1.当前节点为要删除的节点且是树叶（无子树），直接删除，当前节点（为None）的平衡不受影响。
        # 2.当前节点为要删除的节点且只有一个左儿子或右儿子，用左儿子或右儿子代替当前节点，当前节点的平衡不受影响(或递归到的此层不影响)。
        else:
            if node.right:
                node = node.right
            else:
                node = node.left

        return node
