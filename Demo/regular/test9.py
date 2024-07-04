import re

# 示例：贪婪匹配和非贪婪匹配的区别
text = "<html><head><title>Title</title></head><body>Body</body></html>"

# 贪婪匹配示例
pattern_greedy = r'<.*>'
match_greedy = re.search(pattern_greedy, text)
print("贪婪匹配结果:", match_greedy.group())

# 非贪婪匹配示例
pattern_non_greedy = r'<.*?>'
match_non_greedy = re.search(pattern_non_greedy, text)
print("非贪婪匹配结果:", match_non_greedy.group())
