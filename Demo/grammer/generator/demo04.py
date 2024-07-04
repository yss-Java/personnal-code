class FibIterator(object):
    """斐波那契数列迭代器"""

    def __int__(self, n):
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.current = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self

    def fib(n):
        current = 0
        num1, num2 = 0, 1
        while current < n:
            yield num1
            num1, num2 = num2, num1 + num2
            current += 1
        return "done"