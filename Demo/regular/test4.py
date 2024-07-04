import re

# 使用re.match方法直接匹配
re.match(r'h', 'hello')

# 或者使用re.compile方法生成Pattern对象，再调用Pattern对象的match方法
regex = re.compile(r'h')
regex.match('hello')

re.search(r'l', 'hello')

regex = re.compile(r'l')
regex.search('hello')

regex = re.compile(r'l')
print(regex.findall('hello'))

regex = re.compile(r'l')
regex.finditer('hello')
