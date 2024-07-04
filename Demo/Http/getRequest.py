"""
请求连接: http://httpbin.org/get?name=Tom&age=25
"""
import http.client

# 创建于服务器的链接
conn = http.client.HTTPConnection("httpbin.org")

# 发出 get 请求, 请求url为: http://httpbin.org/get?name=Tom&age=25
conn.request("GET", "/get?name=Tom&age=25")

# 获取响应
resp = conn.getresponse()

# 打印响应状态等信息
print(resp.status, resp.reason, resp.version)

# 打印响应头
print(resp.msg)

# 打印响应Body的内容
print(resp.read().decode("utf-8"))

# 关闭连接
conn.close()
