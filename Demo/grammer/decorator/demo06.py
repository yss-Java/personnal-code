#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student:
    __score = 0

    @property                   # 使用 @property 装饰方法, 使 score 变为类的一个可读属性,
    def score(self):            # 被 @property 装饰后的 score 对象会有若干可作为"装饰器"属性,
        return self.__score     # 例如 @score.setter 装饰器用于装饰其他函数使其变为可写属性。

    @score.setter               # 使用被 @property 装饰后的 score 的一个属性（装饰器）@score.setter 装饰函数,
    def score(self, value):     # 使 score 变为一个可写属性, 第2个参数接收写入操作等号右边的值。
        if value < 0:           # 在 setter 方法内可以检查传入值的合法性
            value = 0
        elif value > 100:
            value = 100
        self.__score = value


stu = Student()

# 读取 stu.score 的值实际上会调用 Student 类中的 score(self) 方法
# 相当于 s = stu.score()
s = stu.score

# 给 stu.score 写入值实际上会调用 Student 类中的 score(self, value) 方法
# 相当于 stu.score(50)
stu.score = 50

