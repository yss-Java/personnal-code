try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

class Demo(object):
    def __init__(self,n):
        self.n=n
        self.current=0
    def __iter__(self):
        pass


demo = Demo(10)

print(isinstance(demo,Iterable))

for d in demo:
    print(d)
