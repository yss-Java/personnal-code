# fn = lambda a, b: a + b
# result = fn(10, 20)
# print(result)
#print(lambda a,b:a+b)
fn=lambda :100
print(fn())
fn=lambda a,b :f'a={a},b={b}'
print(fn(10,20))

fn=lambda a,b:f'a={a},b={b}'
print(fn(b=200,a=100))

# 使用默认参数
fn = lambda a,b,c=100 : a+b+c
print(fn(100,50))  # 250
# 取消使用默认参数
fn = lambda a,b,c=100 : a+b+c
print(fn(100,50,200))  # 350

fn = lambda *args : args
print(fn(10,20,30))

fn = lambda **args : args
print(fn(name = 'zhangsan',age = 18,gender = 'man'))

fn=lambda a,b:a if a>b else b
print(fn(10,20))