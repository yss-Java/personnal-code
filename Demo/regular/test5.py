import re

# # 匹配单个数字
# pattern = r'\d'
# string = 'abc 123 def'
# result = re.search(pattern, string)
# if result:
#     print("匹配到数字:", result.group())  # 输出：1
#
# # 匹配多个连续数字
# pattern = r'\d+'
# result = re.findall(pattern, string)
# print("所有数字:", result)  # 输出：['123']
#
# # 查找所有数字的位置和值
# for match in re.finditer(pattern, string):
#     print(f"数字位置：{match.start()}, 数字：{match.group()}")


# # 匹配邮箱地址
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# string = '联系我们：info@example.com 或者 contact@company.co.uk'
# emails = re.findall(pattern, string)
# print("匹配的邮箱地址:", emails)  # 输出：['info@example.com', 'contact@company.co.uk']


# 替换文本中的URL为链接
pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
string = '请访问我们的网站：http://www.example.com 或 https://example.com'
new_string = re.sub(pattern, '<a href="\g<0>">链接</a>', string)
print("替换后的文本:", new_string)
