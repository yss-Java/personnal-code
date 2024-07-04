'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''

rabbits = [1, 1]

# 计算兔子总数的月数
months = 24  # 假设计算24个月的兔子总数，你可以根据需要调整月数

# 计算每个月的兔子总数
for i in range(2, months):
    # 新生的兔子数等于前两个月的兔子总数之和
    new_rabbits = rabbits[i - 1] + rabbits[i - 2]
    rabbits.append(new_rabbits)
# 输出每个月的兔子总数
for i, total in enumerate(rabbits, start=1):
    print(f'第{i}个月的兔子总数为：{total}')
