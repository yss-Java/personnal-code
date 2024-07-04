# 过滤出正数
numbers = [-5, 3, -2, 9, 0]
positives = [n for n in numbers if n > 0]
print(positives)

# 生成矩阵
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 矩阵转置
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

import random

# 生成10个随机数
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)

# 简洁且可读性高的推导式
squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)  # 输出: [0, 4, 16, 36, 64]

# 复杂且可读性低的推导式
complex_expression = [x ** 2 for x in range(10) if x % 2 == 0 if x > 5]
print(complex_expression)  # 输出: [36, 64]

# 使用推导式处理大数据集，可能会导致内存问题
# large_list = [x ** 2 for x in range(10000000)]  # 占用大量内存

# 使用生成器表达式处理大数据集，节省内存
large_generator = (x ** 2 for x in range(10000000))  # 仅在需要时生成数据
print(next(large_generator))  # 输出: 0

# 推导式中缺乏错误处理机制
numbers = [1, 2, 'three', 4]

try:
    squares = [x ** 2 for x in numbers]
except TypeError as e:
    print(f"Error: {e}")


# 在推导式外进行错误处理
def safe_square(x):
    try:
        return x ** 2
    except TypeError:
        return None


squares = [safe_square(x) for x in numbers]
print(squares)  # 输出: [1, 4, None, 16]

