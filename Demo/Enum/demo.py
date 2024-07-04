#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import enum  # 导入枚举模块


class Color(enum.Enum):  # 定义一个名为 Color 的枚举（继承 enum.Enum）
    red = 1  # 定义枚举元素: name 为 "red", value 为 1
    green = 2
    blue = 3
    red_alias = 1


print(Color.red)  # 引用枚举元素, 输出: Color.red
print(Color["red"])  # 通过 name 引用枚举元素, 输出: Color.red
print(Color(1))  # 通过 value 检索元素（返回最先匹配的元素）, 输出: Color.red

print(type(Color.red))  # 元素的类型为枚举类型 Color, 输出: <enum 'Color'>
print(type(Color))  # 枚举类型的类型为类 enum.EnumMeta, 输出: <class 'enum.EnumMeta'>

print(Color.red.name)  # 输出: "red"
print(Color.red.value)  # 输出: 1

# 枚举元素的 == 和 != 比较的是其 value 值, value 值相等则枚举元素相等
print(Color.red == Color.red_alias)  # 输出: True
print(Color.red != Color.green)  # 输出: True

# 枚举元素的 is 和 is not 比较的是也是其 value 值（相当于 == 和 !=）
print(Color.red is Color.red_alias)  # 输出: True
print(Color.red is not Color.green)  # 输出: True
for c in Color:
    print(c)  # 逐次输出: Color.red
    #          Color.green
    #          Color.blue
for c in Color:
    print(c)  # 逐次输出: Color.red
    #          Color.green
    #          Color.blue
# 遍历 Color.__members__, 迭代变量的值为 name
for name in Color.__members__:
    print(name, Color[name])  # 逐次输出: "red"       Color.red
    #          "green"     Color.green
    #          "blue"      Color.blue
    #          "red_alias" Color.red_alias

# 遍历 Color.__members__.items(), 迭代变量的值为 name, Color
for name, c in Color.__members__.items():
    print(name, c)  # 逐次输出: "red"       Color.red
    #          "green"     Color.green
    #          "blue"      Color.blue
    #          "red_alias" Color.red_alias
