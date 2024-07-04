import re

# 示例：从日志文件中提取错误信息
log_data = """
2023-06-15 14:35: Error - File not found: example.txt
2023-06-15 14:36: Warning - Deprecated function used
2023-06-15 14:37: Error - Database connection failed
"""

# 使用正则表达式提取所有错误信息
pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}: Error - (.+)'
errors = re.findall(pattern, log_data)
print("提取的错误信息：", errors)
# 输出：['File not found: example.txt', 'Database connection failed']
