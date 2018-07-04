# python_initiation
Systematic learning of basic python knowledge


basic : 根据<简明python教程>一书, 对入门知识和基础句法的练习.
algorithm : 基础数据结构和算法
环境:win10 , python3.5.2

以下为文件说明 :


-------------------- Algorithm --------------------

Fibonacci           斐波拉契列表 .

search_binary       二分查找 : 在有序表中,每次查找并对比low-high范围中的中间元素 . 时间复杂度为O(log2n)

search_insert       插值查找, 二分查找的变体 ：以更快的速度进行缩减

search_fibonacci    斐波拉契查找, 平均性能，要优于二分查找



-------------------- basic--python basic knowledge --------------------

test_start          hello world ~

test_datastruct     数据结构. 列表, 元组, 字典

test_exception      异常处理 , try , exception ~ , else

test_exception2     异常处理2 .  raise , try exception, try finally

test_func           function

test_io             输入~输出~ , file的基本操作.  pickle模块 -- 储存,取储存 -- 将类以二进制的格式存入文件 -- 读取 .

test_io1            输出到控制台 + 输出到文件作为日志保存 --> 同时重定向到控制台和文件

test_loop           控制流 -- 控制语句

test_memory         复制, 浅拷贝, 深拷贝.  不可变对象 -- 见代码详情

test_module         module

test_more           1.特殊方法, 2.单语句块, 3.列表综合, 4.可变参数列表-- *args接收元组列表, **args接收字典 . 实参和形参的写法.  , 5.lambda表达式  6.exec执行语句 , eval执行计算  7.repr函数和反引号

test_object         对象和类 , self, __init__,  类的变量和对象的变量 -- 类属性与实例属性 . 类的私有方法 . 单下划线、双下划线、头尾双下划线说明

test_object1        类与对象的变量 ~    self. 为属性参考, __privatevar修饰的为私有变量

test_object2        继承 , 多态.  多重继承

test_solveprob      遍历文件和文件夹, 并使用zipfile压缩

test_time           获得当前时间.  str_time, datetime, timestamp的相互转化.

test_unitDict       单元测试被测试类, 参考https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140137128705556022982cfd844b38d050add8565dcb9000

test_unitTest       单元测试 : 是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作



-------------------- thread--进程、线程、协程 --------------------
参考https://www.cnblogs.com/aylin/p/5601969.html

test_asyncio        协程asyncio, 只使用一个线程，在一个线程中规定某个代码块执行顺序.   还有gevent, greenlet等第三方包

test_process1       multiprocessing多进程中的共享数据, Value, Array

test_process2       模块multiprocessing.Manager的dict, list . 提供了多种数据类型的共享支持

test_process3       线程池. multiprocessing.Pool , apply, apply_async

test_threading      模块Threading用于提供线程相关的操作. 基本方法 : start, getName, setName, name, is_alive, isAlive, setDaemon, ident, join, run

test_threading1     用threading.Condition实现消费者模型

test_threading2     用queuelib包中的queue.Queue实现消费者模型

test_threading3     使用queuelib包中的queue.Queue实现 线程池

test_threading4     往队列中无限添加任务 : thread, 函数回调, Queue, contextlib.contextmanager