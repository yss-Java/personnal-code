import socket

# 创建面向非连接（TCP）客户端 Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 服务端地址 和 端口
address = ("localhost", 8080)

# 连接服务端
s.connect(address)

# 发送数据 到 服务端
s.sendall("你好 Hello".encode("UTF-8"))

# 阻塞接收服务端发送的数据
data = s.recv(1024)

# 打印 服务端发送的数据
print(data.decode("UTF-8"))

# 关闭 Socket
s.close()
