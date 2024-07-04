# 方法二：使用函数封装判断素数的逻辑
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_numbers = []  # 存储素数的列表

for num in range(101, 201):  # 遍历101到200之间的所有数字
    if is_prime(num):
        prime_numbers.append(num)

# 输出所有素数
print("101到200之间的素数有以下", len(prime_numbers), "个：")
print(prime_numbers)
