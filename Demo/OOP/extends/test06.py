class Master():
    def __init__(self):
        self.wugong = '太极'

    def func(self):
        print(f'身怀绝技：{self.wugong}')

class Prentice(Master):
    def __init__(self):
        self.wugong = '闪电五连鞭'

    def func(self):
        print(f'身怀绝技：{self.wugong}')

    def func1(self):
        super().__init__()
        super().func()


zhangsan = Prentice()
zhangsan.func1()  # 身怀绝技：太极
#使用 super() 后面的函数参数列表不需要条件self