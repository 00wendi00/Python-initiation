# python_initiation
Systematic learning of basic python knowledge
环境:win10 , python3.5.2


目录 :

## algorithm : 基础数据结构和算法

## basic : 基础

## recursion : 递归

## design : 设计模式

## thread1 : 进程、线程、协程



以下为详细说明 :


## Algorithm

BinaryBalancedTree  平衡二叉树 . BalancedBinaryTree -- AVL

BinarySortTree      二叉查找树 -- 二叉排序数 . BST

BinarySortTree1     二叉树实现 -- List of Lists Representation

Binarytraverse      二叉树的三种遍历方式( 深度优先 ), 先序NLR--preorder, 中序LNR--inorder, 后序LRN--postorder.   递归实现  +  遍历实现

Binarytraverse1     二叉树的遍历方式( 广度优先 )

colle_chain         数据结构 -- 单链表的实现 .  append, insert, delete, reverse, get,set

colle_hash          数据结构 -- 字典的实现方式.

Fibonacci           斐波拉契列表 .

GCD                 最大公约数

KMP                 算法,KMP.   移动位数;部分匹配表

PrimeNumber         查找质数

search_binary       二分查找 : 在有序表中,每次查找并对比low-high范围中的中间元素 . 时间复杂度为O(log2n)

search_insert       插值查找, 二分查找的变体 ：以更快的速度进行缩减

search_fibonacci    斐波拉契查找, 平均性能，要优于二分查找

select_quick        快速选择 , topk,找出第K小的数

sort_bubble         冒泡排序 , 两个for循环加一个if判断 .  时间复杂度为O（n^2）.  注意比较次数

sort_bubbleShort    短冒泡排序, 时间复杂度为O（n^2）, 与sort_bubble比较 --> 减少了比较次数,交换次数未变

sort_heap           堆排序, 最大堆

sort_insertion      插入排序, 取出值,放到合适位置, 时间复杂度为O（n^2）. 与sort_bubble比较 --> 减少了比较次数,交换次数未变

sort_merge          归并排序, divide and conquer strategy, 时间复杂度为O(nlogn). split + merge

sort_quick          快速排序, 分治算法.  平均时间复杂度为O（n×log（n）），最糟糕时复杂度为O（n^2）, 注意优化

sort_quick1         快速排序, 分治算法1.  优化, 注意while里的一点区别

sort_selection      选择排序, 每次找出最大数的位置, 将最大数交换到对应位置, 时间复杂度为O（n^2）. 与sort_bubble比较 --> 比较次数未变, 减少了交换次数

sort_shell          希尔排序, 将序列分为几个区域来提升插入排序的效率, 时间复杂度为O（n^2）. 注意步长选择

test_list           创建list的4个操作, 时间对比 . concatenation, append, comprehension, list range



## basic : 基础

test_decorator1     装饰器. 注意多个装饰的编译顺序和次数, 执行顺序, 带参装饰器

test_decorator2     装饰器 : 类装饰器在类中方法的使用--线程锁

test_extend         多继承, 基类的方法名相同时的执行情况



## recursion : 递归

Fibonacci           斐波拉契列表 -- 递归实现

giveChange          找零钱问题

Hanoi_tower         盘杆难题 Tower of Hanoi

Pascal_triangle     帕斯卡三角, 杨辉三角

Sierpinski          谢尔宾斯基三角形

test_recursion1     递归相加,切片操作,pop() ; 二进制数转化为 n进制数 ; 栈实现递归 ; 字符串反转,字符串截取 ; 判断字符串是否是回文

test_turtle         内嵌的Turtle图形程序模块 . draw Spiral and Tree



## design : 设计模式

builder             建造者模式

factory_sample_pattern      简单工厂模式, 抽象了产品, 在一个工厂类中创建产品实例.

factory_abstract_pattern    抽象工厂模式, 工厂和产品是一对多的关系. 多个工厂即代表多个产品线.

single_class        单例模式--使用类 + @classmethod

single_decorator    单例模式--使用装饰器

single_metaclass    单例模式--使用元类实现

single_module       单例模式--使用模块

single_new          单例模式--使用new



## thread1--进程、线程、协程

参考https://www.cnblogs.com/aylin/p/5601969.html

test_asyncio        协程asyncio, 只使用一个线程，在一个线程中规定某个代码块执行顺序. + 延迟执行    还有gevent, greenlet等第三方包

test_process1       multiprocessing多进程中的共享数据, Value, Array

test_process2       模块multiprocessing.Manager的dict, list . 提供了多种数据类型的共享支持

test_process3       进程池. multiprocessing.Pool , apply, apply_async

test_readwrite      读写锁的实现 , 读者优先

test_threading      模块Threading用于提供线程相关的操作. 基本方法 : start, getName, setName, name, is_alive, isAlive, setDaemon, ident, join, run

test_threading1     用threading.Condition实现消费者模型

test_threading2     用queuelib包中的queue.Queue实现消费者模型

test_threading3     使用queuelib包中的queue.Queue实现 线程池

test_threading4     往队列中无限添加任务 : thread, 函数回调, Queue, contextlib.contextmanager

test_threading5     信号量 Semaphore  , 允许一定数量的线程同时访问数据