add = lambda x, y: x + y
print(add(3, 5))


# 高阶函数是指将函数作为参数传递或返回函数的函数

def apply_func(func, value):
    return func(value)


result = apply_func(lambda x: x * x, 10)
print(result)


# 装饰器
# 装饰器用于在不修改原函数的情况下扩展其功能

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# 闭包
# 闭包是指函数定义在另一个函数的内部，并且引用了外部函数的变量

def outer_function(text):
    def inner_function():
        print(text)

    return inner_function


closure = outer_function('Hello wolrd!')
closure()


# 函数注解
# 函数注解用于提供函数参数和返回值的元数据

def greet(name: str) -> str:
    return 'Hello,' + name


print(greet('Alice'))
print(greet.__annotations__)
