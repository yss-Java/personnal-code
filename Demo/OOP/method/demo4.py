# class Person:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# p1 = Person('zhangsan',18)
# p2 = Person('zhangsan',18)
# print(p1 == p2)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # def __ne__(self, other):

    def __lt__(self, other):
        return self.age < other.age

    # def __gt__(self, other):

    def __le__(self, other):
        return self.age <= other.age
    # def __ge__(self, other):


s1 = Student('zhangsan', 18)
s2 = Student('zhangsan', 18)
s3 = Student('lisi', 20)
print(s1 == s2)
print(s1 != s2)
print(s1 > s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 <= s2)
