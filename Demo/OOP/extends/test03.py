class Master1():
    def __init__(self):
        self.wugong = '太极'

    def func(self):
        print(f'身怀绝技：{self.wugong}')

class Master2():
    def __init__(self):
        self.wugong = '闪电五连鞭'

    def func(self):
        print(f'身怀绝技：{self.wugong}')

class Prentice(Master1,Master2):
    def __init__(self):
        self.wugong = '太极+轻功'

    def func(self):
        print(f'身怀绝技：{self.wugong}')

zhangsan = Prentice()
zhangsan.func()  # 身怀绝技：太极+轻功
