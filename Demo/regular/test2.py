import re

print(re.search(r'L','hello')) #None

# 不区分大小写，可以匹配到 'l'
print(re.search(r'L', 'hello', re.I))  # <re.Match object; span=(2, 3), match='l'>

# \w+$ 表示匹配以一个或多个字母结尾
# re.M 可以进行多行匹配，每个换行都认为是一个结尾
print(re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)) # ['boy', 'girl', 'man']
# 不使用 re.M 修饰符，只会匹配到最后的 'man'
print(re.findall(r'\w+$', 'i am boy\n you are girl\n he is man')) # ['man']
print(re.search(r'.', '\n')) # None, 因为 '.' 匹配除了换行符以外的所有字符
print(re.search(r'.', '\n', re.S)) # '\n'，匹配到了换行符