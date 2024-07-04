import urllib.request

# 创建请求对象
req = urllib.request.Request("http://httpbin.org/get?name=Tom&age=25")

# 设置请求方法
req.method = "GET"
# 添加/覆盖请求头
req.add_header("User-Agent", "Mozilla/5.0")

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
