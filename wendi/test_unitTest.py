#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_unitTest.py
# @Author: Wade Cheung
# @Date  : 2018/6/30
# @Desc  : 单元测试 : 是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作

import unittest
from wendi.test_unitDict import Dict


# 若不用main , 运行python -m unittest test_unitTest , 也可执行单元测试

# 小结 :
# 1. 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 2. 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 3. 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 4. 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。


# 类名必须以test开头, 继承unittest.TestCase
class TestDict(unittest.TestCase):
    # def setUp(self):
    #     print('开始测试')
    #
    # def tearDown(self):
    #     print('结束测试')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 断言
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    # 通过d['empty']访问不存在的key时，断言会抛出KeyError
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 断言Error
            value = d['empty']

    # 通过d.empty访问不存在的key时，我们期待抛出AttributeError
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):  # 断言Error
            value = d.empty


if __name__ == '__main__':
    unittest.main()
