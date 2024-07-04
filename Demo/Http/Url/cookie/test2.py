import ssl
import urllib.request
import http.cookiejar

# 默认的 HTTPS上下文 使用 不校验的上下文
ssl._create_default_https_context = ssl._create_unverified_context

# 创建 MozillaCookieJar 对象, 指定 Cookie 文件路径
cookieJar = http.cookiejar.MozillaCookieJar("cookies.txt")

# 从文件中加载 Cookie
cookieJar.load()

# 创建请求
req = urllib.request.Request("https://www.baidu.com")

# 从 CookieJar 中查找符合 req 请求的 Cookie 并添加到请求头中
cookieJar.add_cookie_header(req)

# 可以打印查看被添加的 Cookie
print(req.header_items())

# 打开请求, 获取响应
resp = urllib.request.urlopen(req)

# 输出响应内容
# print(resp.read().decode("utf-8"))

# 从响应中提取 Cookie 并保存到 CookieJar 中
cookieJar.extract_cookies(resp, req)

# 把内存中的 Cookie 保存到文件中
cookieJar.save()

# 关闭响应
resp.close()
