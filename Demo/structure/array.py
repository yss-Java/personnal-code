# # 创建一个整数数组
# arr = [1, 2, 3, 4, 5]
#
# # 访问数组元素
# print(arr[0])  # 输出：1


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)
