# class Student:
#     def __init__(self,name,score):
#         print('__init__方法被调用了')
#         self.name=name
#         self.score=score
#     def __del__(self):
#         print('__del__方法被调用了')
#
#
# s = Student("lisi", 77)
# del s
# input("请输入内容")

# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def __str__(self):
#         return '姓名是:{},成绩是{}分'.format(self.name,self.score)
#
# s = Student('lisi',95)
# print(s)   # 姓名是:lisi,成绩是95分


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return 'hello'


class Person:
    def __repr__(self):
        return 'hi'

    def __str__(self):
        return 'good'


s = Student('lisi', 95)
print(s)  # hello

p = Person()
print(p)  # good
