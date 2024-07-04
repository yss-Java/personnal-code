class Person():
    name = 'zhangsan'


person1 = Person()
person2=Person()
Person.name='yssnb'
print(person1.name)  # 通过实例对象来访问类属性  zhangsan
print(Person.name)  # 通过类对象来访问类属性  zhangsan
person1.name='lisi'
print(person1.name)
print(person2.name)
person2.name='wangwu'
print(person1.name)
print(person2.name)
# 类的实例记录的某项数据始终保持一致时，则定义类属性。
# 实例属性要求每个对象为其单独开辟一份内存空间来记录数据，而类属性为全类所共有，仅占用一份内存，更加节省内存空间。