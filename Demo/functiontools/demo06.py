# 排序和过滤
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_data = list(filter(lambda x: x % 2 == 0, data))
# sorted_data = sorted(data, key=lambda x: -x)
# print(filtered_data)
# print(sorted_data)

# 日志和权限检查
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log_decorator
def add(a, b):
    return a + b


print(add(3, 4))


# 闭包的变量
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter()
print(counter())  # 输出：1
print(counter())  # 输出：2


# 装饰器的顺序
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()

    return wrapper


def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()

    return wrapper


@decorator1
@decorator2
def greet():
    print("Hello")


greet()

# 匿名函数的限制
# 匿名函数仅限于包含一个表达式的简单函数，复杂逻辑应使用 def 定义函数
# 适合 lambda 的简单函数
simple_func = lambda x: x * x


# 复杂逻辑应使用 def
def complex_func(x):
    if x > 0:
        return x * x
    else:
        return -x
