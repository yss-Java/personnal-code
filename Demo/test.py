id='001'

name="张三"
skill='''
唱歌
跳舞
'''
skill="""
唱歌
跳舞
"""
print('Hello Python')

# name=input()
# print('Hi',name)

if True:
    print(True)
else:
    print(False)

a=128
b=1024
c=512
d=a+ \
  b- \
  c
arr={
    a,
    b,
    c
}
#我是单行注释
'''
我是单行注释
我是单行注释
'''

str='Python'
for s in str:
    if s=='o':
        #break
        continue
    print(s)

sum=0
m=10
while m>0:
    sum=sum+m
    m=m-1
print(sum)

if True:
    pass

import math

print(math.sqrt(1024))
import random

print(random.random())

print(random.uniform(1, 10))

s='Python'
#访问第一个字符P
print(s[0])

print(s[1:3])
print(s[:3])
print(s[3:])

s='A'
print(ord(s))
print(chr(65))

s1='Hello'
s2='Pyhton'
print('s1+s2-->',s1+s2)
print('s1*2-->',s1*2)
print('s1[0]-->',s1[0])
print('\\r-->',R'r')
print('Hello %s'%'Python')
print('{0} {1}'.format('Hello','Python'))

str='Python'
print('str[0] str[-6]=',str[0],str[-6])

print('str[5] str[-1] =', str[5], str[-1])


str = 'Python'
print(str[:3])
print(str[3:])
print(str[:])


str1 = 'Python'
str2 = 'Python'
print('str1 + str2 --> ',str1 + str2)


str = 'Python'
print('2 * str --> ',2 * str)

str = 'Python'
print('on'in str)


str = 'dbcae'
print('len -->', len(str))
print('max -->', max(str))
print('sorted -->', sorted(str))

l=[1024,0.5,'python']
print('l[0] -->', l[0])
print('l[1:] -->', l[1:])



# 修改列表中第二个元素
l[1] = 5
# 向列表中添加新元素
l.append('Hello')
print('l[1] -->', l[1])
print('l -->', l)
del l[1]
print('l -->', l)


l = ['d', 'b', 'a', 'f', 'd']
print("l.count('d') -->", l.count('d'))


l = ['d', 'b', 'a', 'f', 'd']
print("l.index('d') -->", l.index('d'))
l.remove('d')
print("l -->", l)

l.sort()
print('l -->', l)
lc = l.copy()
print('lc -->', lc)

t= (1024, 0.5, 'Python')
print('t[0] -->', t[0])
print('t[1:] -->', t[1:])

t = (1024, 0.5, 'Python', 'Hello')
print('t -->', t)
# del t
# print('t -->', t)
print('len(t) -->', len(t))

t = ('d', 'b', 'a', 'f', 'd')
print('max(t) -->', max(t))
print('min(t) -->', min(t))

l = ['d', 'b', 'a', 'f', 'd']
t = tuple(l)
print('t -->', t)



d = {'name':'小明', 'age':'18'}

# 使用 dict 函数
# 方式一
l = [('name', '小明'), ('age', 18)]
d = dict(l)
# 方式二
d = dict(name='小明', age='18')

# 空字典
d = dict()
d = {}

d = dict(name='小明', age='18')
print(d['name'])
print(d.get('name'))
d['age']='20'
print(d['age'])

d.clear()
print(d)
d = dict(name='小明', age='18')
print(len(d))


s = {'a', 'b', 'c'}

# 使用 set 函数
s = set(['a', 'b', 'c'])

# 空集合
s = set()

s = {'a', 'a', 'b', 'c', 'c'}
print(s)

s = {'a', 'b', 'c'}
s.add('d')
print(s)
s.update('e')
print(s)
s.add('a')
print(s)
s.remove('c')
print(s)
s.clear()
print(s)
s = {'a', 'b', 'c'}
print(len(s))