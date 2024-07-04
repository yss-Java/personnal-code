import socket

# 创建面向非连接（UDP）客户端 Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务端地址 和 端口
address = ("localhost", 8080)

# 发送数据 到 指定地址和端口
s.sendto("你好 Hello".encode("UTF-8"), address)

# 阻塞接收服务端回复的数据, 返回元祖 (数据, 服务端地址)
data, addr = s.recvfrom(1024)

# 打印 服务端地址 和 回复的数据
print("%s: %s" % (addr, data.decode("UTF-8")))

# 关闭 Socket
s.close()
