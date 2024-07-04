names = ['hello', 'good', 'yes']
print(names.__iter__())  # 调用对象的 `__iter__()` 方法
print(iter(names))  # 调用 `iter()` 内置函数


from collections.abc import Iterator
names = ['hello', 'good', 'yes']
print(isinstance(iter(names), Iterator))
