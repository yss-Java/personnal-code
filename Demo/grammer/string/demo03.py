import re
# s = "abcabcacc" #原字符串
# l = re.sub("abc","ddd",s)   #通过sub()处理过的字符串
# print(l)
# s = "abcabcacc" #原字符串
# l = re.subn("abc","ddd",s)   #通过sub()处理过的字符串
# print(l)
s = "abcabcacc"
l = re.split("b",s)
print(l)
