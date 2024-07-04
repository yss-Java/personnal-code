#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

class ShowTime:                     # 创建一个类装饰器

    __fun = None

    def __init__(self, fun):        # 构造器的第二个参数接收被装饰的函数对象
        self.__fun = fun

    def __call__(self):             # 实现 __call__ 方法, 使该类的对象可调用
        start_time = time.time()
        self.__fun()                # 调用原函数
        end_time = time.time()
        print("Call function use time: %f" % (end_time - start_time))


# 用类名当做装饰器去装饰函数, 实际上是把类的构造方法当做了装饰器函数,
# 调用类的构造方法, 创建一个可调用的对象赋值给原函数变量。
#
# 相当于: test = ShowTime(test)
# 装饰完后 test 是 ShowTime 类的一个实例
@ShowTime
def test():
    print("test")
    time.sleep(1)


# 调用被类名装饰后的 test 函数, 实际上调用的是 ShowTime 的实例对象,
# 即调用的是 ShowTime 类的 __call__(...) 方法。
#
# 输出结果: test
#          Call function use time: 1.003948
test()
