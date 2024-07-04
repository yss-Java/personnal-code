import re


def validate_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


# 示例：验证邮箱地址
email1 = "user@example.com"
email2 = "invalid-email"
print(f"{email1} 是否有效：{validate_email(email1)}")  # 输出：user@example.com 是否有效：True
print(f"{email2} 是否有效：{validate_email(email2)}")  # 输出：invalid-email 是否有效：False
