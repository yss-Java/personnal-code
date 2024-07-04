# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         return self.age + other
#
#     def __sub__(self, other):
#         return self.age - other
#
#     def __mul__(self, other):
#         return self.age * other
#
#     def __truediv__(self, other):
#         return self.age / other
#
#     def __mod__(self, other):
#         return self.age % other
#
#     def __pow__(self, power, modulo=None):
#         return self.age ** power
#
#
# s = Student('zhangsan', 18)
# print(s + 1)  # 19
# print(s - 2)  # 16
# print(s * 2)  # 36
# print(s / 5)  # 3.6
# print(s % 5)  # 3
# print(s ** 2)  # 324

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __int__(self):
        return self.age

    def __float__(self):
        return self.age * 1.0

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.age > 18


s = Student('zhangsan', 18)
print(int(s))
print(float(s))
print(str(s))
print(bool(s))

if s:
    print('hello')
