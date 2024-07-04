import csv

# 以写入方式打开一个csv文件
file = open("test.csv", 'w')

# 调用writer方法，传入csv文件对象，得到的结果是一个CSVWriter对象
writer = csv.writer(file)

# 调用CSVWriter对象的writerow方法，一行行地写入数据
writer.writerow(['name', 'age', 'score'])

# 还可以调用writerows方法，一次性写入多行数据

writer.writerows([['zhangsan', '18', '98'], ['lisi', '20', '99'], ['wangwu', '17', '90'], ['jerry', '19', '95']])
file.close()
