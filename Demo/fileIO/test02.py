#f=open('test.txt','w')
#f=open('test.txt','a+')
#f=open('test.txt','r+')
# f.write('abcdfgr')
# f.write('12346')


# f.write('@@@@@')
# print(f.read())
# f.close()

# f=open('test.txt','w+')
#
# print(f.read())
# f.write('$$$$$$')
# f.close()
f=open('test.txt','a+')
f.seek(0)
print(f.read())
f.write('$$$$$$')
f.close()