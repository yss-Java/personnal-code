import urllib.request

# 创建请求对象, 有 data 默认为 POST 请求, data 可以是 bytes、bytearray、字节流打开的file对象
req = urllib.request.Request("http://httpbin.org/post", data=b"name=Tom&age=25")

# 发出请求, 返回响应对象 http.client.HTTPResponse
resp = urllib.request.urlopen(req)

# 打印响应状态等信息
print(resp.status, resp.reason, resp.version)
# 打印响应头
print(resp.getheaders())
# 打印响应Body的内容
print(resp.read().decode("utf-8"))

# 关闭响应流
resp.close()
