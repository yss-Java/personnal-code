#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator_fun(name):                # 定一个函数, 该函数返回一个装饰器

    def decorator(fun):                 # 定义一个装饰器
        def inner_fun():
            print(name + ": call inner fun")
            fun()                       # 调用原函数
        return inner_fun

    return decorator                    # 返回装饰器


# 相当于:
#   f = decorator_fun("hello")  调用函数, 返回装饰器
#   test = f(test)              装饰器装饰函数
@decorator_fun("hello")
def test():                     # 定义带参数的函数
    print("test")


print(test.__name__)            # 结果为: inner_fun

test()                          # 调用被装饰后的函数, 结果为: hello: call inner fun
                                #                         test
