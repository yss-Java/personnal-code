message = (1,2,3,'zhangsan',13.14)
print(type(message))
message=(1)
print(type(message))
message=(1,)
print(type(message))
# message = (1,2,3,'zhangsan',13.14)
# message[0] = 8
# print(message)
message = (1,2,3,'zhangsan',13.14)
message = (8,2,3,'zhangsan',13.14)
print(message)
message = (1,2,3,'zhangsan',13.14,['lisi','wangwu'])
message[5][0] = 'zhaoliu'
print(message)
message = (1,2,3,'zhangsan',13.14)
print(message.index('zhangsan'))  # 3
message = (1,2,3,'zhangsan',13.14)
print(message.count('zhangsan'))  # 1
print(message.count('lisi'))  # 0
message = (1,2,3,'zhangsan',13.14)
print(len(message))  # 5




