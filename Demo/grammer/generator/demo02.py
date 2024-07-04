# 使用生成器计算列表中元素的平方和
def square_generator(iterable):
    for element in iterable:
        yield element ** 2


my_list = [1, 2, 3, 4, 5]
squared_values = square_generator(my_list)

# 使用for循环获取生成器的值并计算平方和
total_square_sum = sum(squared_values)
print(total_square_sum)
