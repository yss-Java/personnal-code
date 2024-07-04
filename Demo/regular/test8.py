import re

# # 示例：复杂正则表达式和大数据量性能问题
# text = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus aliquet lectus vitae ligula vehicula auctor.
# Fusce feugiat, dolor eu tempor varius, justo ligula fermentum dui, in vestibulum risus lacus sit amet eros.
# ... (大段文本) ...
# """
#
# # 复杂正则表达式示例
# pattern = r'Lorem.*?amet'
# matches = re.findall(pattern, text)
# print(matches)

import re

# 示例：使用re.findall()获取所有匹配项
text = "apple, banana, cherry"
matches = re.findall(r'\w+', text)
print(matches)  # 输出：['apple', 'banana', 'cherry']

# 示例：使用re.finditer()逐个获取匹配项
iterator = re.finditer(r'\w+', text)
for match in iterator:
    print(match.group())
# 输出：
# apple
# banana
# cherry
