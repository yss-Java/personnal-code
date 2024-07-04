from io import StringIO

# 创建一个StringIO对象
f = StringIO()
# 可以像操作文件一样，将字符串写入到内存中
f.write('hello\r\n')
f.write('good')
# 需要调用getvalue()方法才能获取到写入到内存中的数据
print(f.getvalue())

f.close()
