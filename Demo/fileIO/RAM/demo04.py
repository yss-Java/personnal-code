import json

# # 调用loads方法，传入一个字符串，可以将这个字符串加载成为Python对象
# result = json.loads('["zhangsan", "lisi", "wangwu", "jerry", "henry", "merry", "chris"]')
# print(type(result))  # <class 'list'>


# 以可读方式打开一个文件
file = open('names.txt', 'r')

# 调用load方法，将文件里的内容加载成为一个Python对象
result = json.load(file)

print(result)
file.close()
