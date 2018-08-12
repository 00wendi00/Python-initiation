#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : factory_abstract _pattern.py
# @Author: Wade Cheung
# @Date  : 2018/8/13
# @Desc  : 抽象工厂模式


# 提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类
# 抽象工程模式 -- 工厂和产品是一对多的关系. 多个工厂即代表多个产品线.

# 优点: 具体工厂类如MysqlFactory在一个应用中只需要初始化一次. 改动一个具体工厂变得很容易, 只需要改变一个具体工厂就可以改变整合产品配置
#       具体的创建实例过程与客户端分离, 客户端通过他们的抽象接口操纵实例,  产品的具体类名也被具体工厂的实现分离.
# 缺点 : 新增一个具体工厂, 需要增加多个类来实现 .


# 抽象用户类
class User(object):
    def get_user(self):
        pass

    def insert_user(self):
        pass


# 抽象部门类
class Department(object):
    def get_department(self):
        pass

    def insert_department(self):
        pass


# 操作具体User类 -- mysql
class MysqlUser(User):
    def get_user(self):
        print('MysqlUser get User')

    def insert_user(self):
        print('MysqlUser insert User')


# 操作具体Department类-- Mysql
class MysqlDepartment(Department):
    def get_department(self):
        print('MysqlDepartment get department')

    def insert_department(self):
        print('MysqlDepartment insert department')


# 操作具体User类-Orcal
class OracleUser(User):
    def get_user(self):
        print('OracleUser get User')

    def insert_user(self):
        print('OracleUser insert User')


# 操作具体Department类-Oracle
class OracleDepartment(Department):
    def get_department(self):
        print('OracleDepartment get department')

    def insert_department(self):
        print('OracleDepartment insert department')


# 抽象工厂类
class AbstractFactory(object):
    def create_user(self):
        pass

    def create_department(self):
        pass


class MysqlFactory(AbstractFactory):
    def create_user(self):
        return MysqlUser()

    def create_department(self):
        return MysqlDepartment()


class OracleFactory(AbstractFactory):
    def create_user(self):
        return OracleUser()

    def create_department(self):
        return OracleDepartment()


if __name__ == "__main__":
    db = 'Mysql'
    myfactory = object
    if db == 'Mysql':
        myfactory = MysqlFactory()
    elif db == 'Oracle':
        myfactory = OracleFactory()
    else:
        print("不支持的数据库类型")
        exit(0)
    user = myfactory.create_user()
    department = myfactory.create_department()
    user.insert_user()
    user.get_user()
    department.insert_department()
    department.get_department()
