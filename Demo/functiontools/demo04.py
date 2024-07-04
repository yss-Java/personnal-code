# def sum_add(a,b):
#     return abs(a) + abs(b)  # abd函数返回数字的绝对值
#
# print(sum_add(-10,20))

# def sum_add(a,b,f):
#     return f(a)+f(b)
# print(sum_add(1.25,2.85,round))
# # 返回列表中每个元素的平方
# def func(x):
#     return x**2
# list1=[1,2,3,4,5]
# print(list(map(func,list1)))
# print(list(map((lambda x:x**2),list1)))


# 使用reduce方法需要导入functools模块
import functools
def func(x,y):
    return x+y
list1=[1,2,3,4,5]
print(functools.reduce(func,list1))
print(functools.reduce((lambda x,y:x+y),list1))

def func(x):
    return x%2==0
list1=[i for i in range(1,11)]
print(list(filter(func,list1)))
print(list(filter((lambda x:x%2==0),list1)))