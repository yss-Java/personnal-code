import re

# s = "010-123456789"
# rule = "010-\d*"
# rule_compile = re.compile(rule)  # 返回一个对象
# print(rule_compile)
# s_compile = rule_compile.findall(s)
# print(s_compile)  # 打印compile()返回的对象是什么

# s = "010-123456789"
# rule = "010-\d*"
# rule_compile = re.compile(rule)  # 返回一个对象
# # print(rule_compile)
# s_compile = rule_compile.match(s)
# print(s_compile)  # 打印compile()返回的对象是什么

s = "010-123456789"
rule = "010-\d*"
rule_compile = re.compile(rule)  # 返回一个对象
s_compile = rule_compile.match(s)
print(s_compile.span())  # 用span()处理返回的对象
