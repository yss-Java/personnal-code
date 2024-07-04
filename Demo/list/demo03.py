dict1={'name':'zhangsan','age':18,'gender':'man'}
print(type(dict1))
dict2={}
dict3=dict()
print(dict2)
print(dict3)
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
dict1['tel'] = '1234567890'
print(dict1)
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
del dict1['gender']
print(dict1)

# dict1 = {'name':'zhangsan','age':18,'gender':'man'}
# del dict1['tel']

dict1 = {'name':'zhangsan','age':18,'gender':'man'}
dict1.clear()
print(dict1)

dict1 = {'name':'zhangsan','age':18,'gender':'man'}
dict1['name'] = 'lisi'
print(dict1)
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
print(dict1['name'])
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
print(dict1.get('name'))
print(dict1.get('tel'))
print(dict1.get('tel','0123'))

dict1 = {'name':'zhangsan','age':18,'gender':'man'}
print(dict1.keys())
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
print(dict1.values())
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
print(dict1.items())

dict1 = {'name':'zhangsan','age':18,'gender':'man'}
for key in dict1.keys():
    print(key)
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
for value in dict1.values():
    print(value)
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
for item in dict1.items():
    print(item)
dict1 = {'name':'zhangsan','age':18,'gender':'man'}
for key,value in dict1.items():
    print(f'{key}={value}')
