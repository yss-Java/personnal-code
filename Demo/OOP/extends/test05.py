class Master():
    def __init__(self):
        self.wugong='太极'
    def func(self):
        print(f'身怀绝技:{self.wugong}')
class Prentice(Master):
    def __init__(self):
        self.wugong='闪电五连鞭'
    def func(self):
        print(f'身怀绝技:{self.wugong}')
    def func1(self):
        Master.__init__(self) #调用父类的初始化方法
        Master.func(self)
    def func2(self):
        self.__init__()
        self.func()


zhangsan = Prentice()
zhangsan.func1()
zhangsan.func2()
