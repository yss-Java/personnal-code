import datetime
import os

print(os.getcwd())
print(os.listdir('E:/'))
print(os.path.abspath('..'))
os.path.split('E:/tmp.txt')
print(datetime.datetime.utcfromtimestamp(os.path.getctime('../test.txt')))
print(os.path.exists('E:/tmp.txt'))
print(os.path.isdir('E:/'))
print(os.path.isfile('E:/tmp.txt'))
print(os.path.getsize('E:/'))
print(os.system('ping www.baidu.com'))