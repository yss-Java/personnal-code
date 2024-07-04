#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator(fun):             # 定义一个用于打印函数执行时间的装饰器（函数）

    def inner_fun(a, b):        # 在内部函数中定义参数, 参数列表必须要和被装饰的函数的参数列表相同
        print("call inner fun")
        return fun(a, b)        # 调用原函数, 把内部函数接收到的参数传递给原函数, 并返回调用结果

    return inner_fun


@decorator                      # add = decorator(add)
def add(a, b):                  # 定义带参数的函数
    return a + b


print(add.__name__)             # 结果为: inner_fun

s = add(2, 3)                   # 这里调用的实际上是 inner_fun(a, b), 因此会输出: "call inner fun"

print(s)                        # 结果为 5
