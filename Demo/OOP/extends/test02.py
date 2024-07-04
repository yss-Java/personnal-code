class Master():
    def __init__(self):
        self.wugong = '太极'

    def func(self):
        print(f'身怀绝技：{self.wugong}')

class Prentice(Master):
    pass

zhangsan = Prentice()
zhangsan.func()  # 身怀绝技：太极
