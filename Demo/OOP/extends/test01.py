class Animal():
    def __init__(self):
        self.info = '动物'

    def func(self):
        print(f'属于{self.info}')

class Cat(Animal):
    pass  # 这里pass是占位符，防止报错

cat = Cat()
cat.func()  # 属于动物
