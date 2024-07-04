# 生成平方数列表
squares = [x ** 2 for x in range(10)]
print(squares)

# 生成唯一平方数集合
unique_squares = {x ** 2 for x in range(10)}
print(unique_squares)

# 生成数值及其平方的字典
square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

unique_letters = {char.upper() for char in 'hello world' if char.isalpha()}
print(unique_letters)

cubes = {x: x ** 3 for x in range(10)}
print(cubes)

