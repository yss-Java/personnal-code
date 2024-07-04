# import re
# result1 = re.match(r'H','Hello')
# result2 = re.match(r'e','Hello')
# print(result1.group(0)) # 'H' 匹配到的元素
# print(result1.span()) # (0,1) 匹配到的元素所在位置
# print(result2)  # None

# import re
# result1 = re.search(r'He','Hello')
# result2 = re.search(r'lo','Hello')
#
# print(result1.group(0))  # He
# print(result1.span()) # (0,2)
# print(result2.group(0)) # lo
# print(result2.span()) # (3,5)
#

# import re
# result1 = re.search(r'天气','今天天气不错哟')
# result2 = re.match(r'天气','今天天气不错哟')
# print(result1)  # <re.Match object; span=(2, 4), match='天气'>
# print(result2) # None

import re

ret = re.findall(r'\d+', 'he23ll34')
print(ret)  # ['23', '34']
ret = re.match(r'\d+', 'he23ll34')
print(ret)  # None match只匹配开头，所以匹配到
ret = re.search(r'\d+', 'he23ll34')
print(ret)  # <re.Match object; span=(2, 4), match='23'> search 只能匹配到一个数字
ret = re.findall(r'\w+@(qq|126|163)\.com', '123@qq.com;aa@163.com;bb@126.com')
print(ret)  # ['qq', '163', '126']  只匹配到了分组里的内容
ret = re.findall(r'\w+@(qq|126|163)(\.com)', '123@qq.com;aa@163.com;bb@126.com')
print(ret)  # [('qq', '.com'), ('163', '.com'), ('126', '.com')]
ret = re.findall(r'\w+@(?:qq|126|163)\.com', '123@qq.com;aa@163.com;bb@126.com')
print(ret)  # ['123@qq.com', 'aa@163.com', 'bb@126.com']
ret = re.finditer(r'\d+','he23ll34')  # 得到的结果是一个可迭代对象
for x in ret: # 遍历 ret 取出里面的每一项匹配
    print(x.group(), x.span()) # 匹配对象里的group保存了匹配的结果
