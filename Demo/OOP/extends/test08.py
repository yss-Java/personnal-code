class Master():
    def __init__(self):
        self.wugong = '太极'
        self.__name = 'lisi'

    def func(self):
        print(f'身怀绝技：{self.wugong}')
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

# class Prentice(Master):
#     def __init__(self):
#         self.wugong = '闪电五连鞭'
#
#     def func(self):
#         print(super().__name)  #3 访问父类的私有权限

# zhangsan = Prentice()
# zhangsan.func()
master = Master()
print(master.get_name())
master.set_name('yssnb')
print(master.get_name())
