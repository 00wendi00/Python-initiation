#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : HashTable.py
# @Author: Wade Cheung
# @Date  : 2018/7/18
# @Desc  : 数据结构 -- 字典的实现方式.


class HashTable:
    def __init__(self):
        self.size = 11  # initial size for the hash table
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if not self.slots[hashvalue]:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                # nextslot位置上为空, 或slots在nextslot的位置上为key
                while self.slots[nextslot] and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if not self.slots[nextslot]:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while not self.slots[position] and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    # overwrite get() --> index operate
    def __getitem__(self, key):
        return self.get(key)

    # overwrite set() --> index operate
    def __setitem__(self, key, data):
        self.put(key, data)

    # 定位
    def hashfunction(self, key, size):
        return key % size

    # 重新定位 + 1
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
