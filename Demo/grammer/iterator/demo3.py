class MyIterator(object):
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


my_it = MyIterator(10)

# 迭代器重写了 `__iter__` 方法，它本身也是一个可迭代对象
for i in my_it:
    print(i)
