#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator_01(fun):                              # 第一个装饰器（函数）
    def fun_inner_01():
        print("decorator_01 -> fun_inner_01()")
        fun()                                       # 调用原函数
    return fun_inner_01


def decorator_02(fun):                              # 第二个装饰器（函数）
    def fun_inner_02():
        print("decorator_02 -> fun_inner_02()")
        fun()                                       # 调用原函数
    return fun_inner_02


#
# 多个装饰器装饰函数, 靠近函数的装饰器先执行, 相当于:
#
# test = decorator_01(decorator_02(test))
#
# 即: 先用 @decorator_02 装饰 test() 得到一个新的函数,
#     再用 @decorator_01 装饰上一步得到的新函数。
#
@decorator_01
@decorator_02
def test():
    print("test()")


print(test.__name__)    # 打印被装饰后的函数的名称, 结果为: fun_inner_01

test()                  # 调用被装饰后的函数, 结果为: decorator_01 -> fun_inner_01()
                        #                         decorator_02 -> fun_inner_02()
                        #                         test()
