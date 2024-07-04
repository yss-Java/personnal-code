import time


class TimeSpan:
    def __enter__(self):
        self.end = None
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('耗时：{}毫秒'.format((self.end - self.start)))


class TimeSpan:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('耗时:{}毫秒'.format((self.end - self.start)))


if __name__ == '__main__':
    with TimeSpan() as t:
        for i in range(0, 1000):
            print(i)
