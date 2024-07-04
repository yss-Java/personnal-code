# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '哈哈'
#
# p  = Person('张三',18)
# print(p)   # 哈哈  打印对象时，会自动调用对象的 `__str__` 方法

class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo()  # 执行 `__init__`
obj()  # 执行 `__call__`
