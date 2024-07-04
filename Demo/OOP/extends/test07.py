# 定义基类A
class A:
    def method_A(self):
        print("This is method A")

# 定义中间类B，继承自基类A
class B(A):
    def method_B(self):
        print("This is method B")

# 定义子类C，继承自中间类B
class C(B):
    def method_C(self):
        print("This is method C")
obj = C()
obj.method_C()  # 调用C类的方法
obj.method_B()  # 调用B类的方法
obj.method_A()  # 调用A类的方法
