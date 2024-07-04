#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import enum

# 定义一个枚举类型
# 第 1 个字符串参数表示枚举类型名称（等号左边的 Color 仅为变量名称, 可以是任意合法标识符）
# 第 2 个元组参数表示所有枚举元素的名称(name), 其中元素的 value 值默认为从 1 开始的整数
Color = enum.Enum("Color", ("red", "green", "blue"))

# 遍历
for c in Color:
    print(c, ":", c.name, "->", c.value)  # 输出: Color.red : red -> 1
    #      Color.green : green -> 2
    #      Color.blue : blue -> 3

print(Color.red)  # 输出: Color.red
print(Color["red"])  # 输出: Color.red
print(Color(1))  # 输出: Color.red

print(type(Color.red))  # 输出: <enum 'Color'>

print(Color)  # 输出: <enum 'Color'>
print(type(Color))  # 输出: <class 'enum.EnumMeta'>
