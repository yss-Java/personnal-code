class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# 使用迭代器
my_iter = MyIterator(5)
for num in my_iter:
    print(num)  # 输出 1 2 3 4 5

