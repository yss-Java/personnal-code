"""
请求连接: http://httpbin.org/post
"""
import http.client

# 创建于服务器的链接
conn = http.client.HTTPConnection("httpbin.org")

# 发出 post 请求, 请求url为: http://httpbin.org/post
conn.request("POST", "/post", body="name=Tom&age=25")

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



