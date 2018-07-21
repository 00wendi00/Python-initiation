#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : colle_chain.py
# @Author: Wade Cheung
# @Date  : 2018/7/22
# @Desc  : 数据结构 -- 单链表的实现 .  append, insert, delete, reverse, get,set


# 1. 注意reverse中两个参数递进
# 2. 注意reverse的多种实现方式
# 3. 注意各种操作下的空链表情况以及_head的指向


class Node:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    def __repr__(self):
        return str(self._data)


class ChainTable:
    def __init__(self):
        self._head = None
        self.length = 0

    # 判断是否为空
    def isEmpty(self):
        return self.length == 0

    # 链表结尾add
    def append(self, item):
        if isinstance(item, Node):
            node = item
        else:
            node = Node(item)

        # 插入操作
        if not self._head:
            self._head = node
        else:
            cu_node = self._head
            while cu_node._next:
                cu_node = cu_node._next
            cu_node._next = node
        self.length += 1

    # 插入数据
    def insert(self, index, data):
        if self.isEmpty():
            print('this chain table is empty')
            return

        if self.length < index or index < 0:
            print('error : out of index')
            return

        in_node = Node(data)
        cu_node = self._head
        if index == 0:
            in_node._next = self._head
            self._head = in_node
        else:
            for i in range(index - 1):
                cu_node = cu_node._next

            # 插入操作
            fo_node = cu_node._next
            cu_node._next = in_node
            in_node._next = fo_node

        self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print('this chain table is empty')
            return

        if self.length - 1 < index or index < 0:
            print('error : out of index')
            return

        if index == 0:
            self._head = self._head._next
        else:
            cu_node = self._head
            for i in range(index - 1):
                cu_node = cu_node._next

            cu_node._next = cu_node._next._next

        self.length -= 1

    def reverse(self):
        if self.isEmpty():
            print('this chain table is empty')
            return

        if not self._head._next:
            return

        p1 = self._head
        p2 = self._head._next
        p1._next = None  # 此步很关键, 不然会循环 1-2-1-2-1.....
        tmp = None
        while p2:
            tmp = p2._next
            p2._next = p1
            p1 = p2
            p2 = tmp

        self._head = p1

    def __repr__(self):
        if self.isEmpty():
            print('this chain table is empty')
            return
        nlist = ""
        node = self._head
        while node:
            nlist += str(node._data) + ' '
            node = node._next
        return nlist

    def __setitem__(self, index, value):
        if self.isEmpty():
            print('this chain table is empty')
            return

        if self.length - 1 < index or index < 0:
            print('error : out of index')
            return

        cu_node = self._head
        for i in range(index):
            cu_node = cu_node._next
        cu_node._data = value

    def __getitem__(self, index):
        if self.isEmpty():
            print('this chain table is empty')
            return

        if self.length - 1 < index or index < 0:
            print('error : out of index')
            return

        cu_node = self._head
        for i in range(index):
            cu_node = cu_node._next
        return cu_node._data


c = ChainTable()
c.append(123)
c.append(456)
c.append(789)
c.append(101112)
c.append(131415)
c.insert(0, 345)
# print(c)
# print(c._head)
# print(c.length)
# c.delete(0)
# print(c)


print(c)
c.reverse()
print(c)
print(c.length)
print(c[0])
c[5] = 555
print(c[5])
