# # 打开文件
# f = open('test.txt','rb')
#
# # 文件操作
# print(f.read())
#
# # 关闭文件
# f.close()

# 打开文件
f = open('test.txt','wb')

# 文件操作
f.write(b'zhangsan')

# 关闭文件
f.close()

