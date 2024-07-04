import json

class MyEncode(json.JSONEncoder):
    def default(self, o):
        # return {"name":o.name,"age":o.age}
        return o.__dict__

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+'正在吃东西')

p1 = Person('zhangsan', 18)

# 自定义对象想要转换成为json字符串，需要给这个自定义对象指定JSONEncoder
result = json.dumps(p1, cls=MyEncode)
print(result)  # {"name": "zhangsan", "age": 18}

# 调用loads方法将对象加载成为一个对象以后，得到的结果是一个字典
p = json.loads(result)
print(type(p))
