class Animal():
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):  # 重写父类方法来实现多态
        print('喵喵喵')

class Dog(Animal):
    def speak(self):  # 同样重写父类方法，实现多态
        print('汪汪汪')

cat = Cat()
dog = Dog()
cat.speak()  # 喵喵喵
dog.speak()  # 汪汪汪
