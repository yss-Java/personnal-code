import json
file = open('names.txt', 'w')
names = ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']
# file.write(names)  出错，不能直接将列表写入到文件里

# 可以调用 json的dumps方法，传入一个对象参数
result = json.dumps(names)

# dumps 方法得到的结果是一个字符串
print(type(result))  # <class 'str'>

# 可以将字符串写入到文件里
file.write(result)

file.close()
