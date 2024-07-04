class Cat:
    color='black'
    __cid='1'

    def __run(self,speed):
        print('__cid是'+self.__cid+'的猫','以'+speed+'的速度奔跑')
    def run(self,speed):
        self.__run(speed)
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        self.food=food
        print(self.name,'正在吃'+food)
print('color-->',Cat.color)
c=Cat('Tom')
print(c)
print('name-->',c.name)
print('color-->',c.color)
c.run('50')
class PersianCat(Cat):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print(self.name,'正在吃'+food)
class GarfildCat(Cat):
    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print(self.name, '正在以' + speed + '的速度奔跑')
class SingleCat(PersianCat):
    pass
class MultiCat(PersianCat,GarfildCat):
    pass
class SingleCat(PersianCat):
    def eat(self, food ):
        print(self.name, '正在吃'+food, '十分钟后', self.name+'吃饱了')
sc = SingleCat('波斯猫1号')
sc.eat('鱼')
sc=SingleCat("波斯猫1号")
sc.eat('鱼')
mc=MultiCat('波斯加菲猫1号')
mc.eat('鱼')
mc.run('50')



