class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    fib_iter = FibonacciIterator(10)
    for num in fib_iter:
        print(num)
