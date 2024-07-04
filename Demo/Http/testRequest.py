import requests

# resp = requests.get("http://httpbin.org/get")
#
# print(resp.status_code)                         # HTTP 状态码
# print(resp.headers)                             # 响应头
# print(resp.cookies)                             # 响应的 cookies
# print(resp.content.decode("utf-8"))             # 响应内容


# resp = requests.post("http://httpbin.org/post", data=b"Hello World")
#
# print(resp.status_code)
# print(resp.content.decode("utf-8"))


file1 = open("aa.txt", "rb")

resp = requests.post("http://httpbin.org/post", data={"key1": "value1"}, files={"file_key1": file1})

print(resp.content.decode("utf-8"))

file1.close()

