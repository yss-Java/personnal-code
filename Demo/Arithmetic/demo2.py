# 判断101-200之间有多少个素数，并输出所有素数。

'''
这个方法使用两个嵌套循环来检查每个数字是否为素数。
对于每个数字，它会检查从2到该数字本身之间是否有除了1和它自身以外的因子。
如果没有其他因子，那么它就是素数。
'''

prime_numbers = []  # 存储素数的列表

for num in range(101, 201):
    is_prime = True  # 假设当前数字是素数

    # 判断是否为素数
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # 如果有处1和自身以外的因子
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

# 输出所有素数
print("101到200之间的素数有以下", len(prime_numbers), "个：")
print(prime_numbers)
