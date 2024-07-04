# 使用迭代器计算列表中元素的平方和
def square_sum(iterable):
    iterator = iter(iterable)
    result = 0

    try:
        while True:
            element = next(iterator)
            result += element ** 2
    except StopIteration:
        pass
    return result


my_list = [1, 2, 3, 4, 5]
total_square_sum = square_sum(my_list)
print(total_square_sum)
