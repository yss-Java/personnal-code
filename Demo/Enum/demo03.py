#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import enum


@enum.unique
class Color(enum.Enum):
    """
    一个枚举类
    """

    red = 1
    """
    枚举元素 red
    """

    green = 2

    blue = 3

    def fun(self):
        """
        枚举对象的方法, self 表示枚举对象（元素）
        """
        print("Enum:", self.name, "->", self.value)

    @staticmethod
    def static_fun():
        """
        枚举类的静态方法
        """
        print("static_fun")

    @classmethod
    def class_fun(cls):
        """
        枚举类的类方法, cls 表示枚举类型 Color
        """
        print("class_fun:", cls)


Color.red.fun()         # 通过枚举对象（元素）调用对象方法, 输出: Enum: red -> 1
Color.static_fun()      # 通过枚举类型直接调用静态方法, 输出: static_fun
Color.class_fun()       # 通过枚举类型直接调用类方法, 输出: class_fun: <enum 'Color'>
