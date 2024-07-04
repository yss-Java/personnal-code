# 以字典的 name值 作为排序的标准
list1 = [
    {'name':'zhangsan','age':18,'gender':'man'},
    {'name':'lisi','age':20,'gender':'woman'},
    {'name':'wangwu','age':28,'gender':'man'}
]

# list1.sort(key = lambda x:x['name'],reverse = False)
# for i in list1:
#     print(i)
list1.sort(key=lambda x:x['age'],reverse=False)
for i in list1:
    print(i)
