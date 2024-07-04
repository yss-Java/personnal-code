#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import enum                 # 导入枚举模块


@enum.unique                # 使用 @enum.unique 修饰枚举类型, 如果存在 value 值相同的元素, 运行时将报错
class Color(enum.Enum):     # 定义一个名为 Color 的枚举（继承 enum.Enum）
    red = 1                 # 定义枚举元素: name 为 "red", value 为 1
    green = 2
    blue = 3
