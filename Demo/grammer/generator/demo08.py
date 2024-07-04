def my_generator(limit):
    current = 0
    while current < limit:
        current += 1
        yield current


# 使用生成器
for num in my_generator(5):
    print(num)  # 输出 1 2 3 4 5

# 使用 iter 和 next
my_list = [1, 2, 3, 4, 5]
iter_obj = iter(my_list)
print(next(iter_obj))  # 输出 1
print(next(iter_obj))  # 输出 2


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# 延迟计算示例
for i in infinite_sequence():
    if i > 5:
        break
    print(i)  # 输出 0 1 2 3 4 5

# def read_large_file(file_path):
#     with open(file_path) as file:
#         for line in file:
#             yield line.strip()
#
# # 逐行读取大文件
# for line in read_large_file('large_file.txt'):
#     print(line)

# import requests
#
# def fetch_data(url):
#     response = requests.get(url, stream=True)
#     for line in response.iter_lines():
#         yield line
#
# # 流式处理网络数据
# for line in fetch_data('http://example.com/largefile'):
#     print(line)

gen = my_generator(3)
for num in gen:
    print(num)  # 输出 1 2 3
for num in gen:
    print(num)  # 不会输出任何内容

iter_obj = iter([1, 2, 3])
try:
    while True:
        print(next(iter_obj))
except StopIteration:
    print("Iteration complete.")

gen_exp = (x ** 2 for x in range(5))
for num in gen_exp:
    print(num)  # 输出 0 1 4 9 16
